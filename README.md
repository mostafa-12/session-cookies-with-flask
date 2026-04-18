# Session Cookies with Flask

A beginner-friendly Flask project that demonstrates login, logout, route protection, and user registration using cookie-based session tracking.

## What this project does

- Lets a user register with name, email, and password.
- Lets a user log in with email and password.
- Creates a unique session ID after successful login.
- Stores the session ID in a browser cookie.
- Protects dashboard and logout routes so only logged-in users can access them.
- Reads and writes users from a JSON file as a simple data store.

## Tech stack

- Python 3
- Flask
- Jinja2 templates
- Bootstrap 5 (CDN)
- JSON file storage (no database)

## Project structure

- app.py: Main Flask application, routes, auth flow, in-memory session store.
- IO_json.py: Utility functions for reading/writing/appending JSON user data.
- dummy_users.json: Sample users used as data storage.
- templates/base.html: Shared layout and theme.
- templates/login.html: Login page.
- templates/register.html: Registration page.
- templates/dashboard.html: Protected dashboard that lists users.

## Quick start

1. Clone or download the repository.
2. Create and activate a virtual environment.
3. Install Flask.
4. Run the app.
5. Open the local URL printed in the terminal.

Example commands:

    python -m venv .venv
    source .venv/bin/activate
    pip install flask
    python app.py

## Core concepts demonstrated

## 1) HTTP basics

- HTTP is stateless. Each request is independent.
- The app uses cookies to connect one request to a logged-in state.
- Login and register use POST requests because they submit form data.
- Dashboard uses GET request because it reads and shows data.
- Redirects are used after login, register, and logout to move user to the next page.

## 2) Cookies

- After login success, the server creates a session ID (UUID).
- The session ID is sent to the browser using Set-Cookie.
- Browser sends this cookie back on future requests.
- On logout, the cookie is deleted.

What to notice in this project:

- response.set_cookie("session_id", session_id)
- response.delete_cookie("session_id")

## 3) Session management

- The app stores session IDs in a Python dictionary named session_store.
- Key is the session ID, value is user email.
- If request cookie session_id exists in session_store, user is considered authorized.
- A custom decorator login_required blocks protected routes.

## 4) Request lifecycle in Flask

- before_request checks auth status and stores it in g.authorized.
- context_processor injects authorized into all templates.
- Templates show different navigation links based on auth state.

## 5) Template rendering with Jinja2

- base.html provides common page layout and style.
- Other pages extend base.html.
- Dashboard loops through users passed from backend and renders rows.

## 6) Simple persistence with JSON

- User records are stored in dummy_users.json.
- IO_json.py provides helper functions:
- read_json
- write_json
- append_json
- delete_json

## Learning path: how to learn sessions, cookies, and HTTP from this project

1. Start with app.py route flow
- Read login route.
- Understand where credentials are checked.
- Follow what happens when login succeeds.

2. Trace cookie behavior
- Find where cookie is set after login.
- Find where cookie is read on each request.
- Find where cookie is deleted on logout.

3. Trace session behavior
- Follow how session_store is written on login.
- Follow how login_required checks session_store.
- Follow how session is removed on logout.

4. Trace HTTP methods and redirects
- Compare GET and POST handlers.
- Observe redirects after form submission.
- Open browser dev tools and inspect status codes and headers.

5. Inspect template auth rendering
- In base.html, check how authorized controls navbar links.
- Verify dashboard is only reachable when logged in.

6. Practice by making small changes
- Add a profile route protected by login_required.
- Add created_at timestamp for sessions.
- Expire sessions after a timeout.
- Show current logged-in user on dashboard.
- Add validation for duplicate email on register.

## Security notes for real projects

This project is intentionally simple for learning. For production, improve the following:

- Do not store plain-text passwords. Use hashing.
- Do not keep sessions only in memory (lost on restart).
- Use secure cookie flags: HttpOnly, Secure, SameSite.
- Use Flask session or server-side session storage (Redis or database).
- Add CSRF protection for forms.
- Add input validation and stricter error handling.

## Suggested next steps

1. Replace JSON storage with SQLite and SQLAlchemy.
2. Hash passwords with Werkzeug security helpers.
3. Move session storage to Flask-Session.
4. Add unit tests for login and protected routes.
5. Add environment variables for secret keys.
