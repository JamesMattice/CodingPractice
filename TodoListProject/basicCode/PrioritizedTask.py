# put in control logic for different ways to prioritize a task here...
import TrackedTask, TimedTask


class PrioritizedTasks:

    priority_levels = {'Highest': [], 'High': [], 'Medium': [], 'Low': [], 'Lowest': []}
    available_sorts = ('ascending', 'descending', 'greater_than_level', 'less_than_level')

    # can these variables be in the init, or should they be local for the class?
    def __init__(self):
        self.priority_levels = {'Highest': ['a thing', 'another thing'], 'High': ['a high thing'], 'Medium': ['a medium thing'], 'Low': ["and this is low"], 'Lowest': ['the lowest thing']}
        self.sorted_tasks = dict

    def test_priority_order(self):
        # this should sort the list in descending priority
        print(self.priority_levels)
        descending_priority = self.priority_levels
        for level in descending_priority.keys():
            curr_priority_level_tasks = descending_priority.get(level)
            # print(level, curr_priority_level_tasks)
            for task in curr_priority_level_tasks:
                print("descending priority " + task)
        # This is a working way to sort from lowest to highest (feel like its probably inefficient)
        ascending_priority = dict(reversed(list(self.priority_levels.items())))
        for level in ascending_priority.keys():
            curr_priority_level_tasks = ascending_priority.get(level)
            # print(level, curr_priority_level_tasks)
            for task in curr_priority_level_tasks:
                print("ascending priority " + task)
        above_list = self.get_tasks_above_priority("Low", descending_priority)
        print(above_list)
        print(ascending_priority)

    # returns a list that has removed all values with priorities above the desired level
    def get_tasks_above_priority(self, desired_level, input_list):
        my_prio_list = input_list
        if desired_level in self.priority_levels.keys():
            level_reached = False
            for level in my_prio_list:
                if desired_level == level:
                    level_reached = True
                if level_reached:
                    my_prio_list[level] = []
        return my_prio_list

    # returns a list that has removed all values with priorities below the desired level
    def get_tasks_below_priority(self, desired_level, input_list):
        my_prio_list = input_list
        if desired_level in self.priority_levels.keys():
            level_reached = False
            for level in my_prio_list:
                if not level_reached:
                    my_prio_list[level] = []
                if desired_level == level:
                    level_reached = True
        return my_prio_list

    def make_prioritized_list(self, existing_list):
        if isinstance(existing_list, self.__class__):
            return existing_list

    def sort_list_by(self, some_list, some_enum):
        if some_enum in self.available_sorts:
            # need some way to call the different ways to sort by priority that we want
            print('hey')

    def get_priority_level(self, level):
        if level in self.priority_levels.keys():
            return self.priority_levels.get(level)
        else:
            print("invalid priority level for get_priority function")

    def add_prioritized_task(self, task, level):
        if level in self.priority_levels.keys():
            self.priority_levels.__setitem__(level, task)
            #print(self.priority_levels[1])



