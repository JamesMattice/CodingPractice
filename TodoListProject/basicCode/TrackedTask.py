"""Creating a subclass of TodoList"""
from SuperBasicTask import SuperBasicTask
import datetime


class TrackedTask(SuperBasicTask):

    number_of_completions = ""
    max_completions = ""
    last_completed = datetime
    next_completion = datetime

    def __init__(self):
        SuperBasicTask.__init__(self)
        # self.contents.append(number_of_completions, max_completions, last_completed)
        #self.contents.extend([0, -1, datetime.datetime.max])
        self.number_of_completions = 0
        self.max_completions = -1
        self.last_completed = datetime.datetime.max
        self.next_completion = datetime.datetime.max  # Might be changing soon

    #create a string representation of this class
    def __repr__(self):
        contents = SuperBasicTask.__repr__(self)
        contents = contents + ", " + str(self.number_of_completions) + ", " + str(self.max_completions) + ", " + str(self.last_completed)
        return contents

    def get_number_of_completions(self):
        return self.number_of_completions  # This is horrible, find a better solution

    def set_number_of_completions(self, num):
        if num >= 0:
            if num <= self.get_max_completions() or self.get_max_completions() == -1:
                self.number_of_completions = num
            else:
                # raise ValueError("Number is greater than max completions.")
                print("Number is greater than max completions.")
        else:
            # raise ValueError("Number is less than zero.")
            print("Number is less than zero.")

    def get_max_completions(self):
        return self.max_completions

    def set_max_completions(self, num):
        self.max_completions = num

    def get_last_completed(self):
        return self.last_completed

    def set_last_completed(self, completion_time):
        self.last_completed = completion_time

    def get_next_completion(self):
        return self.next_completion

    def set_next_completion(self, time_object):  # datetime object
        self.next_completion = time_object

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
        # Todo add check for Timezone config if needed
        self.set_last_completed(datetime.datetime.now())
        if self.is_repeatable():
            self.update_date_of_next()
        if self.get_number_of_completions() == self.get_max_completions():
            self.set_status(self.status_tuple[len(self.status_tuple)-1])
    # Update number of completions
    # Update last completed date
    # Something to happen when number of completions hits max