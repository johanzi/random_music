import shutil # copy file
import os # handle search path
import Tkinter as tk # Create alias for Tkinter
import tkMessageBox, tkFileDialog, tkSimpleDialog
import fnmatch # to search file recursively
import random # Select random songs from a list

# This script runs on Python2.7


## Layout pseudocode

# Ask to user directory containing music and output directory

# Function requiring directory to user
# Variable 'dir' created to personalize the GUI text
def get_dirname(dir):
    # withdraw removes the default root window displayed by Tk
    tk.Tk().withdraw()
    dirname = tkFileDialog.askdirectory(initialdir=os.getcwd(), title='Please select '+dir)
    if len(dirname) > 0:
        print ("You chose %s" % dirname)
        return dirname
    else: 
        dirname = os.getcwd()
        print ("\nNo directory selected - initializing with %s \n" % os.getcwd())
        return dirname 

# The output directory should not be contain within the input directory
# otherwise conflict of same file copied at the sane place will happen



# Ask for the number of songs requested
# Check if number given is an integer
def get_nb_song():
    while True:
        try:
            # Remove default Tk window
            tk.Tk().withdraw()
            # Get value and check if integer
            nb_song = int(tkSimpleDialog.askstring("Number of songs", ""))
        except ValueError:
            tkMessageBox.showerror("Error message", "Value provided is not an integer")
        else:
            # Value given is an integer
            break
    return nb_song


# Find mp3 in directory and select a random

def find_mp3(dir_input):
    matches = []
    for root, dirnames, filenames in os.walk(dir_input):
        for filename in fnmatch.filter(filenames, '*.mp3'):
            matches.append(os.path.join(root, filename))
    if len(matches) == 0:
        tkMessageBox.showerror("Error message", "No mp3 files were found in "+dir_input) 
    else:
        return matches


# Get a random selection of x files within the search results
def select_random(list_song, nb_song):
    if len(list_song) < nb_song:
        nb_song = len(list_song)
    sub_list = random.sample(list_song, nb_song)
    return sub_list



# Copy these files into the output directory

def copy_files(sub_list, dir_output):
    for i in sub_list:
        print 'shutil.copy('+i+', '+dir_output+')'
        shutil.copy(i, dir_output)


dir_input = get_dirname("directory containing music")

dir_output = get_dirname("destination directory")

list_song = find_mp3(dir_input)

nb_song = get_nb_song()

sub_list = select_random(list_song, nb_song)
#print sub_list

copy_files(sub_list, dir_output)
