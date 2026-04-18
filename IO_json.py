import json

def read_json(file_path:str = 'dummy_users.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path: str = 'dummy_users.json', data: dict = None):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        return True # Return True if the write operation was successful
    

def append_json(file_path: str = 'dummy_users.json', new_data: dict = None):
    # Reading old data
    with open(file_path, 'r') as file:
        data = json.load(file)

    # appending new data to old data
    data.append(new_data)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        return True # Return True if the append operation was successful
    

def delete_json(file_path: str = 'dummy_users.json'):
    with open(file_path, 'w') as file:
        json.dump([], file, indent=4)
        return True # Return True if the delete operation was successful
    

        