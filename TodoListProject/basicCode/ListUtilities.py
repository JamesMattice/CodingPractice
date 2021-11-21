"""Utilities for the TodoList project."""

import os

LIST_PATH = "../featherDuster/"

"""Method for returning a list"""

def get_todo_list(list_name):

    """Function to open a file"""
    cwd = os.getcwd()
    # print(cwd)
    for entry in os.scandir(path="../featherDuster/"):  # os.scandir(path=cwd):
        # print(entry)
        if entry.is_file():
            if list_name == entry.name:
                print("true")
                return entry
            # print("No such list was found.")
            # return False


"""Find the list."""

def find_todo_list(list_name):  # refactor to be a find_file

    entry = get_todo_list(list_name)
    if entry:
        return True  # place holder because not having anything in the if statement breaks it
        # examples to read or print from our file    with open(entry, 'r') as ourList:
        # examples to read or print from our file        lines = ourList.readlines()
        # examples to read or print from our file        for line in lines:
        # examples to read or print from our file            print(line)
    else:
        print("No list found. Try again later.") # Do we need to prompt user?
        return False


"""Method for saving a list."""

# def save_todo_list(list_name):
# how are we going to handle files that already exist?


"""Method to add edits to a list."""

# def update_todo_list(list_name):


"""Method to delete a list."""

def del_todo_list(list_name):

    """Remove file."""
    delete_prompt = input("Are you sure you want to delete %s? (yes/no)" % list_name)
    if delete_prompt.lower() == "yes" or "y":
        os.remove(LIST_PATH + list_name)


"""Method to make a new list."""

def create_todo_list():

    """Prompt user for list name."""
    list_name = input("Please enter a name for the list:") + ".txt"

    """Check to see if list exists."""
    if find_todo_list(list_name): # This logic needs to be reworked. Probably.
        print("That list name is already in use.")
        try_again = input("Would you like to try a different name? (yes/no)")
        if try_again.lower() == "yes" or "y":
            create_todo_list()
    else:
        with open((LIST_PATH + list_name), 'x') as temp_list:
            temp_list.close() # Maybe redundant


"""Dunno about this yet."""

# def change_type_todo_list(list_name):


