#!/usr/bin/env python


from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, os

# import os, random, sys, Tkinter

## Layout pseudocode

# Ask to user directory containing music


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

# Require 
dir = "directory containing music"
#dir_input = get_dirname(dir)

# It will appear very quick if I don't use the stop function of os, here just for testing
# print 'dir_input is '+dir_input

# Ask output directory
# Require 
dir = "destination directory"
#dir_output = get_dirname(dir)



# Ask for the number of songs requested
# Still searching for an easy snippet from the web
# x = get_song_number()
# print x

root = Tk()
Button(root, text="Press here", command=hello).pack()
root.mainloop()


# Check if number given is an integer

# Find mp3 in directory and select a random

# Get a random selection of x files within the search results

# Copy these files into the output directory

