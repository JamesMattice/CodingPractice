import TrackedTask
import TimedTask


class PrioritizedTask:

    priority_levels = {'Highest': [], 'High': [], 'Medium': [], 'Low': [], 'Lowest': []}
    available_sorts = ('ascending', 'descending', 'greater_than_level', 'less_than_level')
    current_order = ('in_ascending_order', 'in_descending_order')

    def __init__(self, existing_list=None):
        self.priority_levels = {'Highest': [], 'High': [], 'Medium': [], 'Low': [], 'Lowest': []}
        #self.priority_levels = {'Highest': ['a thing', 'another thing'], 'High': ['a high thing'], 'Medium': ['a medium thing'], 'Low': ["and this is low"],'Lowest': ['the lowest thing']}
        self.sorted_tasks = dict

        if existing_list is not None:
            if isinstance(existing_list, list):
                for item in existing_list:
                    self.add_prioritized_task(item, 'Medium')

    def make_prioritized_list(self, existing_list):
        if isinstance(existing_list, self.__class__):
            return existing_list
        else:
            for item in existing_list:
                self.add_prioritized_task(item, 'Medium')
            return self

    def add_prioritized_task(self, task, level):
        if level in self.priority_levels.keys():
            self.priority_levels[level].append(task)

    def get_priority_level(self, level):
        if level in self.priority_levels.keys():
            return self.priority_levels.get(level)
        else:
            print("invalid priority level for get_priority function")
