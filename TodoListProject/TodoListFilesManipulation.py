"""Base class for Todo lists"""

# Name
# Ability to add to the list
# Ability to remove items from the list
# Ability to view/get items from list

LIST_PATH = "./featherDuster/"


class TodoList:

    def __init__(self, name):
        self.filename = name + ".txt"
        # self.items = items

    def add_item(self, item):
        with open((LIST_PATH + self.filename), 'a') as f:
            f.write(item + '\n')

    def remove_item(self, item):
        with open((LIST_PATH + self.filename), 'r+') as f:
            data = f.readlines()
            f.seek(0, 0)
            for line in data:
                # print(line)
                if line.strip("\n") != item:
                    f.write(line)
            f.truncate()

    def get_item(self, item):
        with open((LIST_PATH + self.filename), 'r') as f:
            data = f.readlines()
            for line in data:
                if line.strip("\n") == item:
                    # print(line)
                    return line
                else:
                    return print("Item does not exist.")
