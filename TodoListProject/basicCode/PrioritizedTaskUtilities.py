# put in control logic for different ways to prioritize a task here...

class PrioritizedTaskUtilities:

    def test_priority_order(self):
        # this should sort the list in descending priority
        descending_priority = self.priority_levels
        for level in descending_priority.keys():
            curr_priority_level_tasks = descending_priority.get(level)
            # print(level, curr_priority_level_tasks)
            # for task in curr_priority_level_tasks:
            print("descending priority " + curr_priority_level_tasks.__str__())
        # This is a working way to sort from lowest to highest (feel like its probably inefficient)
        ascending_priority = dict(reversed(list(self.priority_levels.items())))
        for level in ascending_priority.keys():
            curr_priority_level_tasks = ascending_priority.get(level)
            print("ascending priority " + curr_priority_level_tasks.__str__())
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

    #implement greater than and less than functionality
    def sort_priority_list_by(self, some_list, some_enum, some_level='none'):
        if some_enum in self.available_sorts:
            # need some way to call the different ways to sort by priority that we want
            if some_enum == 'ascending':
                self.order_by_ascending_priority(some_list)
            elif some_enum == 'descending':
                self.order_by_descending_priority(some_list)
            elif some_enum == 'greater_than_level':
                print("this sort is not implemented yet")
            elif some_enum == 'less_than_level':
                print("this sort is not implemented yet")
        else:
            print("this was an invalid sort option")

    # currently the default order I think
    def order_by_descending_priority(self, input_list):
        the_input = list(input_list)
        first_category = the_input.pop(0)
        if first_category == 'Lowest':
            input_list.sort(reverse=True)
        elif first_category == "Highest":
            print('already in descending order')
        # add error or try catch
        else:
            print("not in a recognized priority order")
        return input_list

    def order_by_ascending_priority(self, input_list):
        the_input = list(input_list)
        first_category = the_input.pop(0)
        if first_category == 'Lowest':
            print('already in ascending order')
            return input_list
        elif first_category == "Highest":
            input_list.sort(reverse=True)
        # should do a try/catch here probably, same with descending
        else:
            print("not in a recognized priority order")
        return input_list

