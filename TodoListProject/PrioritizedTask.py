# put in control logic for different ways to prioritize a task here...
import collections


class PrioritizedTasks:

    # what i want is a way to have a key/pair to a sortable list? of tasks
    # PRIORITY_LEVEL = ['Highest', 'High', 'Medium', 'Low', 'Lowest']
    PRIORITY_LEVELS = {'Highest': ['a thing', 'another thing'], 'High': [], 'Medium': [], 'Low': ["and this is low"], 'Lowest': []}

    # can these variables be in the init, or should they be local for the class?
    def __init__(self):
        priority_levels = {'Highest': ['a thing', 'another thing'], 'High': [], 'Medium': [], 'Low': ["and this is low"], 'Lowest': []}
        # sorted_tasks = collections.OrderedDict()

    def setup_something(self):
        # this should sort the list in descending priority
        descending_priority = collections.OrderedDict(sorted(self.PRIORITY_LEVELS.items(), key=lambda t: t[0]))
        for level in descending_priority.keys():
            curr_priority_level_tasks = descending_priority.get(level)
            print(level, curr_priority_level_tasks)
            for task in curr_priority_level_tasks:
                print("Its in the task loop")


