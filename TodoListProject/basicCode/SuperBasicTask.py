# Ability to view/get items from list
#LIST_PATH = "./featherDuster/"

import datetime


class SuperBasicTask: # Currently, is actually a single task, not a TodoList

    task_name = ""
    date_of_next = datetime
    frequency_tuple = ("once", "hourly", "daily", "weekly", "fortnight",
                       "monthly", "quarterly", "yearly", "infinite")
    __frequency_dict = {"once": datetime, "hourly": datetime.timedelta(hours=1), "daily": datetime.timedelta(days=1),
                        "weekly": datetime.timedelta(weeks=1), "fortnight": datetime.timedelta(weeks=2),
                        "monthly": datetime.timedelta(weeks=4), "quarterly": datetime.timedelta(weeks=16),
                        "yearly": datetime.timedelta(weeks=52), "infinite": datetime.datetime.max}
    status_tuple = ("to be completed", "active task", "partially completed", "done")

    # why the hell do you have contents to hold member variables of self?, just have the name and date as variables and call them through self.<x>
    def __init__(self):
        self.task_name = "new task"
        self.date_of_next = datetime.datetime.max
        self.frequency = self.frequency_tuple[0]
        self.status = self.status_tuple[0]

        # self.contents = [name, date_of_next, frequency_of_repetition]
        # self.contents = ["new task", datetime.datetime.max, self.frequency[0],
                         #self.status[0]]

    def __repr__(self):
        contents = self.task_name + ", " + str(self.date_of_next) + ", " + self.frequency + ", " + self.status
        return contents

    def get_task_name(self):
        return self.task_name

    def set_task_name(self, name):
        self.task_name = name

    def get_date_of_next(self):
        return self.date_of_next

    def set_date_of_next(self, next_date):
        if next_date is datetime.datetime:
            self.date_of_next = next_date
        else:
            print("Invalid date entered, no change made")

    def calculate_date_of_next(self):
        if (self.frequency is not 'once' or 'infinite') and (self.date_of_next != datetime.datetime.max):
            return self.date_of_next + self.__frequency_dict[self.frequency]
        else:
            return self.date_of_next

    def update_date_of_next(self, time_from=None):
        if time_from is datetime.datetime:
            self.set_date_of_next(time_from + self.calculate_date_of_next())
        self.set_date_of_next(self.calculate_date_of_next())

    def get_frequency(self):
        return self.frequency

    # requires an integer parameter for frequency
    def set_frequency(self, freq):
        if freq in self.frequency_tuple:
            #this works by setting the value of frequency from the index of the base frequency array
            self.frequency = freq
        else:
            self.frequency = self.frequency_tuple[0]
            assert "The frequency was invalid and defaulted to none"

    def get_status(self):
        return self.status

    # requires an integer parameter for status
    # if we wanted to allow the string, you would just check in self.status instead of the range(len...))
    def set_status(self, stat):
        if stat in self.status_tuple:
            # this works by setting the value of status from the index of the base status array
            self.status = stat
        else:
            self.status = self.status_tuple[0]
            assert "The status was invalid and defaulted to none"

    # Check to see if task is repeatable.
    def is_repeatable(self):
        if self.frequency != "once":
            return True
        else:
            return False

    # Grayham figure out how to do KVP with datetime -- possibly completed
