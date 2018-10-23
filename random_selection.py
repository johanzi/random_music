#!/usr/bin/env python

from Tkinter import *
from tkSimpleDialog import askstring
import Tkinter, tkMessageBox, Tkconstants, tkFileDialog, os
import Tkinter as tk


## Layout pseudocode

# Ask to user directory containing music and output directory

# Function requiring directory to user
# Variable 'dir' created to personalize the GUI text
def get_dirname(dir):
    # withdraw allows to remove the default root window displayed by Tk
    Tk().withdraw()
    dirname = tkFileDialog.askdirectory(initialdir=os.getcwd(),title='Please select '+dir)
    if len(dirname) > 0:
        print ("You chose %s" % dirname)
        return dirname
    else: 
        dirname = os.getcwd()
        print ("\nNo directory selected - initializing with %s \n" % os.getcwd())
        return dirname 


#dir = "directory containing music"
#dir_input = get_dirname(dir)

#dir = "destination directory"
#dir_output = get_dirname(dir)


while True:

    try:
        # Ask for the number of songs requested
        root = tk.Tk()
        # show askstring dialog without the Tkinter window
        root.withdraw()
        # Get value and check if integer
        nb_song = int(askstring("Number of songs", ""))
    except ValueError:
        tkMessageBox.showerror("Error message", "Value provided is not an integer")
    else:
        # Value given is an integer
        break
   

# Check if number given is an integer

# Find mp3 in directory and select a random

# Get a random selection of x files within the search results

# Copy these files into the output directory

