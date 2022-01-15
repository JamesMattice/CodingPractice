"""Create a subclass of TrackedTask"""
from TrackedTask import TrackedTask
import datetime


class TimedTask(TrackedTask):

    fastest_time = datetime.time(23, 59, 59)  # Could make empty if there is a check for number_of_completions
    average_time = datetime.time()  # Do I need to state these if I'm stating them in the __init__?
    previous_time = datetime.time()
    time_elapsed = datetime.time()
    time_remaining = datetime.time()
    total_time_elapsed = datetime.time()

    def __init__(self):
        TrackedTask.__init__(self)
        self.fastest_time = datetime.time(23, 59, 59)
        self.average_time = datetime.time()  # Might have to use timedelta to do this
        self.previous_time = datetime.time()
        self.time_elapsed = datetime.time()
        self.time_remaining = datetime.time()
        self.start_time = datetime.datetime.min
        self.total_time_elapsed = datetime.time()
        self.previously_paused = False

    def get_fastest_time(self):
        return self.fastest_time

    def set_fastest_time(self, time_object):
        self.fastest_time = time_object

    def get_average_time(self):
        return self.average_time

    def set_average_time(self, time_object):
        completions = self.get_number_of_completions()
        if completions == 0:
            self.average_time = time_object
        else:
            self.average_time = (self.average_time * completions + time_object) / (completions + 1)

    def get_previous_time(self):
        return self.previous_time

    def set_previous_time(self, time_object):
        self.previous_time = time_object

    def get_total_time_elapsed(self):
        return self.total_time_elapsed

    def set_total_time_elapsed(self, time_object):
        if self.previously_paused:
            self.total_time_elapsed += time_object
        else:
            self.total_time_elapsed = time_object
            self.previously_paused = True

    def start_task(self):
        # self.start_time = datetime.datetime.now().time()
        self.start_time = datetime.datetime.now()

    def calculate_time_elapsed(self):
        current_time = datetime.datetime.now()
        self.time_elapsed = current_time - self.start_time
        # Reworked to not have to use datetime.combine

    def calculate_time_remaining(self):
        current_time = datetime.datetime.now()
        self.time_remaining = self.next_completion - current_time

    def end_task(self):
        end_time = datetime.datetime.now()
        duration = end_time - self.start_time
        if self.previously_paused:
            duration += self.total_time_elapsed
        if duration < self.fastest_time:  # Shortened to duration instead of duration.time() in order to account for day
            self.set_fastest_time(duration)
        self.set_previous_time(duration)
        self.set_average_time(duration)
        self.complete_task()

    def pause_task(self):
        self.status = self.status_tuple[2]
        self.calculate_time_elapsed()
        self.set_total_time_elapsed(self.time_elapsed)



