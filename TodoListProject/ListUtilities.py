"""Utilities for the TodoList project."""

import os

"""Method for returning a list"""
def get_todo_list(list_name):
    """Function to open a file"""
    entry = find_todo_list(list_name)
    if entry:
        True # place holder because not having anything in the if statement breaks it
        # examples to read or print from our file    with open(entry, 'r') as ourList:
        # examples to read or print from our file        lines = ourList.readlines()
        # examples to read or print from our file        for line in lines:
        # examples to read or print from our file            print(line)
    else:
        print("No list found. Try again later.")


"""Find the list."""
def find_todo_list(list_name):  # refactor to be a find_file
    cwd = os.getcwd()
    # print(cwd)
    for entry in os.scandir(path="./featherDuster/"):  #os.scandir(path=cwd):
        # print(entry)
        if entry.is_file():
            if list_name == entry.name:
                print("true")
                return entry
            # print("No such list was found.")
            # return False


"""Method for saving a list."""
# def save_todo_list(list_name):
# how are we going to handle files that already exist?

"""Method to add edits to a list."""
# def update_todo_list(list_name):


"""Method to delete a list."""
# def del_todo_list(list_name):


"""Method to make a new list."""
# def create_todo_list(list_name):


"""Dunno about this yet."""
# def change_type_todo_list(list_name):
