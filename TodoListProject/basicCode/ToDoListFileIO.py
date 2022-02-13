from pathlib import Path
import ProjectDefinitions



class TodoListFileIO:

    # LIST_PATH = "./featherDuster/"

    def __init__(self, name='newList.txt'):
        if not name.endswith('.txt'):
            name += '.txt'
        self.filename = name
        self.save_dir = ProjectDefinitions.ROOT_DIR
        self.save_dir = self.save_dir.joinpath('featherDuster')
        self.target_file = self.save_dir.joinpath(self.filename)
        self.LIST_PATH = self.save_dir.__str__() + '/'
        #print('before joinpath ' + ProjectDefinitions.ROOT_DIR.__str__())
        #self.save_dir = ProjectDefinitions.ROOT_DIR
        #self.save_dir = self.save_dir.joinpath('featherDuster')
        #print("the fucking save dir " + self.save_dir.__str__())
        # self.items = items

    def add_todo_element_to_file(self, item):
        #with open((self.LIST_PATH + self.filename), 'a') as f:
        with Path.open(self.target_file, 'a') as f:
            f.write(item.__str__() + '\n')

    def remove_todo_element_from_file(self, item):
        with Path.open(self.target_file, 'r+') as f:
            data = f.readlines()
            f.seek(0, 0)
            for line in data:
                # print(line)
                if line.strip("\n") != item:
                    f.write(line)
            f.truncate()

    def get_todo_element_from_file(self, item):
        with Path.open(self.target_file, 'r') as f:
            data = f.readlines()
            for line in data:
                if line.strip("\n") == item:
                    # print(line)
                    return line
                else:
                    return print("Item does not exist.")

    def create_new_todo_list(self, name=None):
        print(self.save_dir)
        if name is None:
            i = 1
            if Path.exists(self.save_dir.joinpath('newList.txt')):
                # iterate through the files in the directory, incrementing for the numbered suffix
                while Path.exists(self.save_dir.joinpath('newList%s.txt' % i)):
                    # print('its cycling through the while %s' % i)
                    i += 1
                name = 'newList%s.txt' % i
                print(name)
            else:
                name = 'newList.txt'
        elif not name.endswith('.txt'):
            name += '.txt'
        #self.filename = name
        self.target_file = self.save_dir.joinpath(name)
        self.filename = name
        file = Path.open(self.target_file, 'a+')
        file.close()
        return self

    def rename_list_file(self, new_name, save_dir_param=None):
        if save_dir_param is None:
            save_dir_param = self.save_dir
        for filename in Path.iterdir(save_dir_param):
            print("the rename dir is " + save_dir_param.__str__())
            print(new_name)
            print(filename)
            if filename == self.filename:
                if not new_name.endswith('.txt'):
                    new_name.join('.txt')
                # rename will fail if the chosen name already exists, allow user to choose to overwrite, use a new name, or cancel
                if new_name in Path.iterdir(save_dir_param):
                    self.naming_conflict(new_name)
                    #self.rename_list_file(self, new_name) make a recursive call once the naming_conflict logic has been added
                    return
                try:
                    Path.rename(Path.joinpath(save_dir_param, filename), Path.joinpath(save_dir_param, new_name))
                    self.filename = new_name
                except FileExistsError:
                    print("The rename attempt failed because a file with that name already exists")
                    #

    def naming_conflict(self, new_name):
        print("i should be popping up a GUI window")

    #a placeholder for handling deleting all of the tasks in a list and their associations
    #def delete_list(self, list_name):
    #    return

