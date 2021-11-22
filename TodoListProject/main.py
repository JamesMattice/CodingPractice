"""It's the main file of the TodoList project"""
from basicCode import TrackedTask, ToDoListFileIO


#from gtts import gTTS
#from playsound import playsound
#import pyttsx3


#def main():
#    text_val = "Hello there.  General kenobi"
#    language = 'en'
#    sound_obj = gTTS(text=text_val, lang=language, slow=False)
#    sound_obj.save("example.mp3")
#    playsound("example.mp3")


def main():
    # from ListUtilities import del_todo_list
    # del_todo_list("list2.txt")
    # """Load the TodoList project"""
    # from BaseTodoList import SuperBasicTodoList
    #print("trying the priority thingy")
    #prio_task = PrioritizedTask.PrioritizedTasks()
    #prio_task.get_priority('Highest')
    #prio_task.test_priority_order()
    sample_list = []
    print("hello")
    basic_task = TrackedTask.TrackedTask()
    basic_task.set_task_name("sleep")
    basic_task.set_frequency("daily")
    basic_task.set_max_completions(1)
    basic_task.complete_task()
    sample_list.append(basic_task)
    print(basic_task.get_frequency())
    another_task = TrackedTask.TrackedTask()
    another_task.set_task_name("more sleep")
    another_task.set_status("completed")
    print(another_task.get_status())
    print(another_task.get_frequency())
    print(basic_task.get_number_of_completions())
    sample_list.append(another_task)
    my_list = ToDoListFileIO.TodoList("aList")
    for task in sample_list:
        my_list.add_todo_element_to_file(task.__repr__())
    a_new_list = ToDoListFileIO.TodoList().create_new_todo_list("it should work")
    for task in sample_list:
        a_new_list.add_todo_element_to_file(task.__repr__())
    a_new_list.rename_list_file("it_was_renamed")

if __name__ == "__main__":
    main()
