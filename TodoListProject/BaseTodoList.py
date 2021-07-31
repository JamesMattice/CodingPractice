# Ability to view/get items from list
#LIST_PATH = "./featherDuster/"

import datetime


class SuperBasicTodoList: # Currently, is actually a single task, not a TodoList

    frequency = ("once", "hourly", "daily", "weekly", "fortnight",
                 "monthly", "quarterly", "yearly", "infinite")

    status = ("to be completed", "active task", "partially completed", "done")

    def __init__(self):
        # self.contents = [name, date_of_next, frequency_of_repetition]
        self.contents = ["new task", datetime.datetime.max, self.frequency[0],
                         self.status[0]]

    def get_contents(self):
        return self.contents

    def get_task_name(self):
        return self.contents[0]

    def set_task_name(self, name):
        self.contents[0] = name

    def get_date_of_next(self):
        return self.contents[1]

    def set_date_of_next(self, next_date):
        if next_date is datetime.datetime:
            self.contents[1] = next_date
        else:
            print("Invalid date entered, no change made")

    def get_frequency(self):
        return self.contents[2]

    # requires an integer parameter for frequency
    def set_frequency(self, freq):
        if freq in range(len(self.frequency)):
            self.contents[2] = self.frequency[freq] # This is horrible, but works
        else:
            self.contents[2] = 0
            assert "The frequency was invalid and defaulted to none"

    # requires an integer parameter for status
    # if we wanted to allow the string, you would just check in self.status instead of the range(len...))
    def set_status(self, stat):
        if stat in range(len(self.status)):
            self.contents[3] = self.status[stat]
        else:
            self.contents[3] = 0
            assert "The status was invalid and defaulted to none"

    # Check to see if task is repeatable.
    def is_repeatable(self):
        if self.contents[2] != "once":
            return True
        else:
            return False


    # James figure out Python switch statement
    # Grayham figure out how to do KVP with datetime
