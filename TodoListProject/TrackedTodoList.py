"""Creating a subclass of TodoList"""
from BaseTodoList import SuperBasicTodoList
import datetime


class TrackedList(SuperBasicTodoList):

    def __init__(self):
        SuperBasicTodoList.__init__(self)
        # self.contents.append(number_of_completions, max_completions, last_completed)
        self.contents.extend([0, -1, datetime.datetime.max])

    def get_number_of_completions(self):
        return self.contents[4]  # This is horrible, find a better solution

    def set_number_of_completions(self, num):
        if num >= 0:
            if num <= self.get_max_completions() or self.get_max_completions() == -1:
                self.contents[4] = num
            else:
                # raise ValueError("Number is greater than max completions.")
                print("Number is greater than max completions.")
        else:
            # raise ValueError("Number is less than zero.")
            print("Number is less than zero.")

    def get_max_completions(self):
        return self.contents[5]

    def set_max_completions(self, num):
        self.contents[5] = num

    def get_last_completed(self):
        return self.contents[6]

    def set_last_completed(self, completion_time):
        self.contents[6] = completion_time

    # When base list updated, add task parameter to replace contents call
    # def complete_task(self):
        # if self.status == "done":
            # return print("Task has been previously completed.")
        # curr_completions = self.get_number_of_completions()
        # curr_completions += 1
        # print("Current completions: ", curr_completions)
        # self.set_number_of_completions(curr_completions)
        # print("Number of completions: ", self.get_number_of_completions())
    def complete_task(self):
        self.set_number_of_completions(self.get_number_of_completions() + 1)

    # Update number of completions
    # Update last completed date
    # Something to happen when number of completions hits max