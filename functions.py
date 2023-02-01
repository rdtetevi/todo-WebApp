FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items.
    :param filepath: path of the file
    :return: todo list items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items.
    :param todos_arg: todos argument
    :param filepath: file path
    :return: list to-do items
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
