"""It's the main file of the TodoList project"""


def main():
    from ListUtilities import del_todo_list
    del_todo_list("list2.txt")
    """Load the TodoList project"""


if __name__ == "__main__":
    main()
