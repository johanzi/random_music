import sys
import time
import shutil # copy files
import os # handle search path
import fnmatch # to search file recursively

# Make Tkinter working on python2 and 3
try:
    #import Tkinter as tk
    #from ttk import *
    from Tkinter import *
    from ttk import *
    import tkFileDialog as filedialog
except ImportError:
    #import tkinter as tk
    #from tkinter.ttk import *
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import filedialog


class random_music():
    
    def __init__(self, root):
        # A frame is a widget that displays just as a simple rectangle.
        # Frames are primarily used as a container for other widgets,
        # which are under the control of a geometry manager such as grid.
        # I can define the size using padding option
        self.frame = Frame(root, padding=20)
        
        # This line seems optional
        self.root = root
        
        # Name of the main Window
        self.root.title("Random music")
        
        # Choose to use either 'pack' or 'grid' mode to arrange widget in the frame
        self.frame.grid()

        # Create a menu bar with the label "Menu" and submenus "Help" and "Quit"
        self.menubar = Menu(root)
        self.root['menu'] = self.menubar

        # Create submenus (need to be done first)
        self.menu_file = Menu(self.menubar)
        self.menu_file.add_command(label="Quit", command=self.quit)
        self.menu_file.add_command(label="Help", command=self.display_help)

        # Give label to menu name
        self.menubar.add_cascade(menu=self.menu_file, label='Menu')
        

        # Create buttons to select the directories

        # Create Tkinter variable, call the corresponding constructor
        # Check http://effbot.org/tkinterbook/variable.htm
        # These variables will be assigned with set() in browse_button function
        
        folder_input = StringVar()

        # Create text before the button
        lbl0 = Label(master=self.root, text="Choose input directory")
        lbl0.grid(row=0, column=0)

        self.folder_input = StringVar(self.root)
        
        lbl1 = Label(master=self.root, textvariable=folder_input)
        lbl1.grid(row=0, column=2)

        # Do not put () beside browse_button
        browse_button_input = Button(text="Browse", command=self.browse_button)
        browse_button_input.grid(row=0, column=1)

        #folder_input = StringVar()
        
        # Create text before the button
        lbl2 = Label(master=self.root, text="Choose output directory")
        lbl2.grid(row=1, column=0)

        folder_output = StringVar()
        lbl3 = Label(master=self.root, textvariable=folder_input)
        lbl3.grid(row=1, column=2)

        browse_button_output = Button(text="Browse", command=self.browse_button)
        browse_button_output.grid(row=1, column=1)


    def browse_button(self, root):

        global folder_input
        
        filename = filedialog.askdirectory(initialdir=os.getcwd(), title='Please select directory')
        folder_input.set(filename)
       

    def display_help(self):
      pass
    
    def quit(self):
        self.frame.quit()   


# Build the app in the main loop
if __name__ == "__main__":
    root = Tk()
    app = random_music(root)
    root.mainloop()
