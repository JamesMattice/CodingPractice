import os

LIST_PATH = "./featherDuster/"


class TodoListFileIO:

    def __init__(self, name='.txt'):
        if not name.endswith('.txt'):
            name += '.txt'
        self.filename = name
        # self.items = items

    def add_todo_element_to_file(self, item):
        with open((LIST_PATH + self.filename), 'a') as f:
            f.write(item + '\n')

    def remove_todo_element_from_file(self, item):
        with open((LIST_PATH + self.filename), 'r+') as f:
            data = f.readlines()
            f.seek(0, 0)
            for line in data:
                # print(line)
                if line.strip("\n") != item:
                    f.write(line)
            f.truncate()

    def get_todo_element_from_file(self, item):
        with open((LIST_PATH + self.filename), 'r') as f:
            data = f.readlines()
            for line in data:
                if line.strip("\n") == item:
                    # print(line)
                    return line
                else:
                    return print("Item does not exist.")

    def create_new_todo_list(self, name='.txt'):
        if name == '.txt':
            i = 1
            if os.path.exists(LIST_PATH + 'newList.txt'):
                # iterate through the files in the directory, incrementing for the numbered suffix
                while os.path.exists(LIST_PATH + 'newList%s.txt' % i):
                    print('its cycling through the while %s' % i)
                    i += 1
                name = 'newList%s.txt' % i
            else:
                name = 'newList.txt'
        if not name.endswith('.txt'):
            name += '.txt'
        self.filename = name
        file = open((LIST_PATH + name), 'a+')
        file.close()
        return self

    def rename_list_file(self, new_name, save_dir=LIST_PATH):
        for filename in os.listdir(save_dir):
            if filename == self.filename:
                if not new_name.endswith('.txt'):
                    new_name.join('.txt')
                # rename will fail if the chosen name already exists, allow user to choose to overwrite, use a new name, or cancel
                if new_name in os.listdir(save_dir):
                    self.naming_conflict(new_name)
                    #self.rename_list_file(self, new_name) make a recursive call once the naming_conflict logic has been added
                    return
                try:
                    os.rename(save_dir + filename, save_dir + new_name)
                    self.filename = new_name
                except FileExistsError:
                    print("The rename attempt failed because a file with that name already exists")
                    #

    def naming_conflict(self, new_name):
        print("i should be popping up a GUI window")

    #a placeholder for handling deleting all of the tasks in a list and their associations
    #def delete_list(self, list_name):
    #    return

