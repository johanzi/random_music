import sys
import os # handle search path

# Check if script run with Python3
if sys.version_info[0] < 3:
    print("This script must be using Python 3")
    os.system("pause")

import shutil # copy files
import tkinter as tk # Create alias for Tkinter
from tkinter import messagebox, filedialog, simpledialog # Import from tkinter needed modules
import fnmatch # to search file recursively
import random # Select random songs from a list

# Check if user has tqdm installed
try:
    from tqdm import tqdm # Get terminal progress bar
except ImportError:
    print("tqdm module is not installed, do without it")
    print("If progress bar wished, do 'pip install tqdm --user' and rerun the script")
    pass

# Function requiring directory to user
# Variable 'dir' created to personalize the GUI text
def get_dirname(dir):
    # withdraw removes the default root window displayed by Tk
    tk.Tk().withdraw()
    dirname = tk.filedialog.askdirectory(initialdir=os.getcwd(), title='Please select '+ dir)
    # Exit in case user clicks 'cancel'
    if dirname:
        return dirname
    else:
        sys.exit()

# The output directory should not be contain within the input directory
# otherwise conflict of same file copied at the sane place will happen

# Ask for the number of songs requested
# Check if number given is an integer
def get_nb_song():
    # Remove default Tk window
    tk.Tk().withdraw()
    # Get value and check if integer (first argument is the name of the window, second is
    # the message near the entry box)
    nb_song = tk.simpledialog.askstring("", "Number of songs")
    # Exit if user clicks 'cancel'
    if not nb_song:
        sys.exit()
    # Check if variable is an integer
    try:
        nb_song = int(nb_song)
    except ValueError:
        tk.messagebox.showerror(title="Error message", message="Value provided is not an integer")
        sys.exit()
    # If variable is an integer, return it
    return nb_song


# Find mp3 in directory and select a random
# This step may take time in large directory.
# TODO: time length of the code for large folders
def find_mp3(dir_input):
    matches = []

    # If module tqdm exists, use it to assess progress, otherwise
    # do without it
    if 'tqdm' in sys.modules:
        range_files = tqdm(os.walk(dir_input), unit="files", ascii=True, desc="Total number files found")
    else:
        range_files = os.walk(dir_input)
    
    for root, dirnames, filenames in range_files:
        for filename in fnmatch.filter(filenames, '*.mp3'):
            matches.append(os.path.join(root, filename))
    if len(matches) == 0:
        tk.messagebox.showerror(title="Error message", message="No mp3 files were found in "+dir_input)
        sys.exit()
    else:
        return matches


# Get a random selection of x files within the search results
def select_random(list_song, nb_song):
    if len(list_song) < nb_song:
        nb_song = len(list_song)
    sub_list = random.sample(list_song, nb_song)
    return sub_list

# Copy these files into the output directory
# Check if file with same name is already present, it yes, add suffix
def copy_files(sub_list, dir_output):

    # If module tqdm exists, use it to assess progress, otherwise
    # do without it
    if 'tqdm' in sys.modules:
        range_files = tqdm(sub_list, total=len(sub_list), unit="files", ascii=True, desc="mp3 files copied")
    else:
        range_files = sub_list
    
    for i in range_files:
        # Check if file name exists in dir_output
        file_name = os.path.basename(i)
        file_name = os.path.join(dir_output, file_name)

        if not os.path.exists(file_name):
            shutil.copy(i, dir_output)

        else:
            # Initialize the suffix
            ii = 1
            # While loop until the name of the file is unique
            while True:
                file_name = os.path.basename(i)
                file_name = os.path.splitext(file_name)[0]
                file_name = os.path.join(dir_output, file_name + "_" + str(ii) + ".mp3")
                if not os.path.exists(file_name):
                    shutil.copy(i, file_name)
                    break
                ii += 1
    
def main():
    # Get the two directories from user

    dir_input = get_dirname("directory containing music")
    #dir_input = "C:/Users/iblis/Documents/test_music"

    dir_output = get_dirname("destination directory")
    #dir_output = "C:/Users/iblis/Documents/output_dir_music"

    # Test if dir_input and dir_output are different
    if dir_input == dir_output:
        tk.messagebox.showerror(title="Error", message="Chosen source and destination directories are identical, please choose different directories")
        sys.exit()

    nb_song = get_nb_song()
    #nb_song = int(5)

    # Get list of mp3 files in dir_input
    list_song = find_mp3(dir_input)

    if nb_song == None:
        sys.exit()

    # Get a sublist of the selection
    sub_list = select_random(list_song, nb_song)

    # Copy element of the sublist in output directory
    copy_files(sub_list, dir_output)


if __name__ == "__main__":
    main()
    sys.exit()

