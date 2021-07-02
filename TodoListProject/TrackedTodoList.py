"""Creating a subclass of TodoList"""
import BaseTodoList
import datetime

class TrackedList(BaseTodoList):


    def __init__(self):
        BaseTodoList.SuperBasicTodoList.__init__(self)
        # self.contents.append(number_of_completions, max_completions, last_completed)
        self.contents.extend([0, -1, datetime.datetime.max])

    def get_number_of_completions(self):
        return self.contents[4] # This is horrible, find a better solution

    def set_number_of_completions(self, num):
        try:
            if num >= 0:
                if num <= self.get_max_completions() or self.get_max_completions() == -1:
                    self.contents[4] = num
        except ValueError:
            print("Number is either negative or greater than your max completions.")

    def get_max_completions(self):
        return self.contents[5]

    def set_max_completions(self, num):
        self.contents[5] = num

    def get_last_completed(self):
        return self.contents[6]

    def set_last_completed(self, completion_time):
        self.contents[6] = completion_time



    # Update number of completions
    # Update last completed date
    # Something to happen when number of completions hits max