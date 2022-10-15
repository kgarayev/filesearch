# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

from pathlib import Path
import os, os.path

# establish the default path which is the current directory
default_path = Path.cwd()
current_path = default_path
chosen_files = []

# choose a path if you know the directory exactly
def choose_path():

    global default_path, current_path

    # understand if the user knows the exact path
    answer = input('\nDo you want to choose a path? [Y/N]: ')

    # keep asking for the correct input until it is received
    while True:
        if answer == 'N':
            print('\nThe current directory path is used as a default.')
            path = Path.cwd()
            break
        elif answer == 'Y':
            while True:
                home_dir = Path.cwd().home()
                path = default_path.home().joinpath(input(f'\nEnter the path after the home directory {home_dir}/'))
                print(path)
                if path.exists():
                    break
                else:
                    print('\nThe path doesn''t exist. Try again.')
            break
    current_path = path
    print(current_path)
    return current_path
    
# lists all folders in the given path (optional) or current directory (default)
def choose_folder():

    global current_path
    print(current_path)

    # create a list and have a dummy entry as the 0th variable
    folders = ['empty']

    print('\nThese are all your folders in the directory: \n')

    # iterate through all the files in the directory
    for item in current_path.iterdir():
        # print the files that are folders (directories)
        if item.is_dir():
            # add the folder path into the list and print the index and the names of the folders
            folders.append(item)
            print(folders.index(item), item.name)

    #print(folders)

    while True:
        folder_number = int(input('\nChoose a folder number: '))
        if folder_number >= len(folders):
            continue
        break
    
    current_path = folders[folder_number]
    
    return current_path

def question():
    global default_path
    global current_path
    choose_path()
    current_path = choose_folder()

    while True:
        answer = input('\nWould you like to open another folder in the current directory? [Y/N] ')
        if answer=='N':
            print(f'You are currently in: {current_path}')
            break
        elif answer=='Y':
            current_path = choose_folder()
            continue
        else:
            print('Type the correct answer.')
            continue

    return current_path


def search(path):

    global chosen_files

    for root, dirs, files in os.walk(path):
        print(root)
        for file in files:
            if os.path.splitext(file)[1]=='.py':
                chosen_files.append(os.path.join(root, file))
                print(file)
    
    return chosen_files



search(Path('c:/Users/kenan/Desktop/codingnomads'))
print(chosen_files)