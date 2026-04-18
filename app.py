from flask import Flask, render_template, request, redirect, url_for, flash, g
import uuid
import random
from functools import wraps
import IO_json


session_store = {

}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secret key'
@app.context_processor
def inject_user():
    session_id = request.cookies.get('session_id')
    authorized = session_id in session_store
    return dict(authorized=authorized)

@app.before_request
def before_request():
    session_id = request.cookies.get('session_id')
    g.authorized = session_id in session_store
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_id = request.cookies.get("session_id")
        if not session_id in session_store:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function




@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard():
    data = IO_json.read_json()
    return render_template('dashboard.html', data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.authorized:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = IO_json.read_json()
        user = next((user for user in users if user['email'] == email and user['password'] == password), None)
        if user:
            session_id = str(uuid.uuid4())
            session_store[session_id] = user['email']
            response = redirect(url_for('dashboard'))
            response.set_cookie('session_id', session_id)
            flash('Login successful!', 'success')
            
            return response
        else:
            flash('Invalid email or password. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.authorized:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        data = {
            "id": str(random.randint(9,100)),
            "username": name,
            "email": email,
            "password": password
        }
        IO_json.append_json(new_data= data)
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session_id =request.cookies.get('session_id')
    session_store.pop(session_id, None)
    flash('You have been logged out.', 'info')
    response = redirect(url_for('login'))
    response.delete_cookie('session_id')
    return response

if __name__ == '__main__':
    app.run(debug=True)