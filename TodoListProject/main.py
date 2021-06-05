"""It's the main file of the TodoList project"""


def main():
    from TodoListProject.ListUtilities import get_todo_list
    get_todo_list("list1.txt")
    """Load the TodoList project"""


if __name__ == "__main__":
    main()
