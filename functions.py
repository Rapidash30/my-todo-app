def show(list):
    """Prints each item in the task list int the format - 'index+1' . 'list[index]' """
    for x in range(len(list)):
        print(f"{x + 1}. {list[x]}", end="")

def read(text_file="todos.txt"):
    """Reads todos.txt and returns the content as a list, line-wise."""
    with open(text_file, "r") as file:
        rd = file.readlines()
    return rd

def write(contents, text_file="todos.txt"):
    """Writes each item in list 'content' line-wise in todos.txt."""
    with open(text_file, "w") as file:
        file.writelines(contents)


