"""It's the main file of the TodoList project"""


def main():
    #from ListUtilities import del_todo_list
    #del_todo_list("list2.txt")
    #"""Load the TodoList project"""
    # from BaseTodoList import SuperBasicTodoList
    import TrackedTodoList
    basic_list = TrackedTodoList.TrackedList()
    basic_list.set_max_completions(1)
    basic_list.complete_task()
    basic_list.complete_task()
    print(basic_list.get_number_of_completions())

if __name__ == "__main__":
    main()
