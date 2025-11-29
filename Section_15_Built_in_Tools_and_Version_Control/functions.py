FILEPATH = 'files/todos.txt'

def get_todos(filepath=FILEPATH):
    """Function incharge of getting all of the value inside the todo list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """This function write todos in the file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)