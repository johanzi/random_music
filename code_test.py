
import sys
import time
import shutil # copy files
import os # handle search path

# Make Tkinter working on python2 and 3
try:
    #import Tkinter as tk
    #from ttk import *
    from Tkinter import *
    from ttk import *
except ImportError:
    #import tkinter as tk
    #from tkinter.ttk import *
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import filedialog

import fnmatch # to search file recursively
import random # Select random songs from a list
import threading # Allow to run tkinter and copy files in the same time (progress bar implementation)
import queue



class random_music():
    def __init__(self, root):

        # A frame is a widget that displays just as a simple rectangle.
        # Frames are primarily used as a container for other widgets,
        # which are under the control of a geometry manager such as grid.
        # I can define the size using padding option
        self.frame = Frame(root, padding=2000)

        # Choose to use either 'pack' or 'grid' mode to arrange widget in the frame
        self.frame.grid()

        self.root = root

        self.notebook = Notebook(root)

        # Create a menu bar with the label "Menu" and submenus "Help" and "Quit"
        menubar = Menu(root)
        root['menu'] = menubar

        # Create submenus (need to be done first)
        menu_file = Menu(menubar)
        menu_file.add_command(label="Quit", command=self.quit)
        menu_file.add_command(label="Help", command=self.display_help)

        # Give label to menu name
        menubar.add_cascade(menu=menu_file, label='Menu')
        

        # Create buttons to select the directories

        def browse_button():
            # Allow user to select a directory and store it in global var
            # called folder_path (can be then used outside of the function)
            global folder_path
            # The title will appear in the pop up window when selecting directory
            filename = filedialog.askdirectory(initialdir=os.getcwd(), title='Please select directory')
            folder_path.set(filename)
            print(filename)

        # Create Tkinter variable, call the corresponding constructor
        # Check http://effbot.org/tkinterbook/variable.htm
        # These variables will be assigned with set() in browse_button function
        #folder_input = StringVar()
        #lbl1 = Label(master=root, textvariable=folder_input)
        #lbl1.grid(row=0, column=1)

        #folder_output = StringVar()
        #lbl2 = Label(master=root, textvariable=folder_output)
        #lbl2.grid(row=0, column=1)

        folder_path = StringVar()

        lbl1 = Label(master=root,textvariable=folder_path)
        lbl1.grid(row=0, column=1)

        browse_button_input = Button(text="Browse", command=browse_button)
        browse_button_input.grid(row=0, column=0)

        #browse_button_input = Button(text="Browse output directory", command=browse_button)
        #browse_button_input.grid(row=1, column=0)
        




        
        

        
    def display_help():
        pass

    # Somehow does not work while it works in script all_widgets.py
    def quit(self):
        self.frame.quit()
        
       


# Build the app in the main loop
if __name__ == "__main__":
    root = Tk()
    app = random_music(root)
    root.mainloop()
