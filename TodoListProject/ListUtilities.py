"""Utilities for the TodoList project."""

import os


"""Method for opening or returning a list"""
def get_todo_list(list_name):

    """Function to open a file"""
    if find_todo_list(list_name):
        open("list_name", "w")
    else:
        print("No list found. Try again later.")

"""Find the list."""
def find_todo_list(list_name):

    for list_name in os.scandir(os.pardir()):
        if list_name.is_file():
            print('File: ' + list_name.path)
            return True
        else:
            print("No such list was found.")
            return False


"""Method for saving a list."""
def save_todo_list(list_name):


"""Method to add edits to a list."""
def update_todo_list(list_name):


"""Method to delete a list."""
def del_todo_list(list_name):


"""Method to make a new list."""
def create_todo_list(list_name):

"""Dunno about this yet."""
def change_type_todo_list(list_name):