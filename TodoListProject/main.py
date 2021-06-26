"""It's the main file of the TodoList project"""


def main():
    #from ListUtilities import del_todo_list
    #del_todo_list("list2.txt")
    #"""Load the TodoList project"""
    from BaseTodoList import TodoList
    x = TodoList("list3")
    x.remove_item("Hello")
    from InProgressListDev import SuperBasicTodoList
    basic_list = SuperBasicTodoList()
    x.add_item(str(basic_list.contents))

if __name__ == "__main__":
    main()
