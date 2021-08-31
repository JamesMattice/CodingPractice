"""Create a subclass of TrackedTask"""
from TrackedTodoTask import TrackedTask
import datetime


class TimerTask(TrackedTask):

    fastest_time = datetime.time(24, 60, 60)  # Could make empty if there is a check for number_of_completions
    average_time = datetime.time()  # Do I need to state these if I'm stating them in the __init__?
    previous_time = datetime.time()
    time_elapsed = datetime.time()
    time_remaining = datetime.time()

    def __init__(self):
        TrackedTask.__init__(self)
        self.fastest_time = datetime.time(24, 60, 60)
        self.average_time = datetime.time()  # Might have to use timedelta to do this
        self.previous_time = datetime.time()
        self.time_elapsed = datetime.time()
        self.time_remaining = datetime.time()
        self.start_time = datetime.datetime.min

    def get_fastest_time(self):
        return self.fastest_time

    def set_fastest_time(self, time_object):
        self.fastest_time = time_object

    def get_average_time(self):
        return self.average_time

    # def set_average_time(self, time_object):
        # Come Back to this. Don't know if datetime allows you to simply divide a .time object

    def get_previous_time(self):
        return self.previous_time

    def set_previous_time(self, time_object):
        self.previous_time = time_object

    def start_task(self):
        # self.start_time = datetime.datetime.now().time()
        self.start_time = datetime.datetime.now()

    def calculate_time_elapsed(self):
        current_time = datetime.datetime.now()
        self.time_elapsed = current_time - self.start_time
        # Reworked to not have to use datetime.combine

    # def calculate_time_remaining(self):
        # Need to implement next_completion in TrackedTask.py first
        # current_time = datetime.datetime.now()
        # self.time_remaining = self.next_completion - current_time

    def end_task(self):
        end_time = datetime.datetime.now()
        duration = end_time - self.start_time
        if duration.time() < self.fastest_time:
            self.set_fastest_time(duration.time())
        self.set_previous_time(duration.time())
        # self.set_average_time(duration.time())
