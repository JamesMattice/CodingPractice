"""It's the main file of the TodoList project"""
import TrackedTask
import TodoListFileManipulation
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
    my_list = TodoListFileManipulation.TodoList("aList")
    for task in sample_list:
        my_list.add_item(task.__repr__())


if __name__ == "__main__":
    main()
