#!/usr/bin/env python


from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, os

# import os, random, sys, Tkinter

## Layout pseudocode

# Ask to user directory containing music


def get_dirname():
    Tk().withdraw()
    dirname = tkFileDialog.askdirectory(initialdir=os.getcwd(),title='Please select a directory containing your music')
    if len(dirname) > 0:
        print ("You chose %s" % dirname)
        return dirname
    else: 
        dirname = os.getcwd()
        print ("\nNo directory selected - initializing with %s \n" % os.getcwd())
        return dirname 


get_dirname()


# Check if directory exist (not needed if done with tinker)

# Ask output directory

# Ask for the number of songs requested

# Check if number given is an integer

# Find mp3 in directory and select a random

# Get a random selection of x files within the search results

# Copy these files into the output directory

