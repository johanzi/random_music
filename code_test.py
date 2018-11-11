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
    import tkMessageBox as messagebox
    
except ImportError:
    #import tkinter as tk
    #from tkinter.ttk import *
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import filedialog, messagebox


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


        ################# MENU ##########################
        
        # Create a menu bar with the label "Menu" and submenus "Help" and "Quit"
        self.menubar = Menu(self.root)
        self.root['menu'] = self.menubar

        # Create submenus (need to be done first)
        self.menu_file = Menu(self.menubar)
        self.menu_file.add_command(label="Quit", command=self.quit)
        self.menu_file.add_command(label="Help", command=self.display_help)

        # Give label to menu name
        self.menubar.add_cascade(menu=self.menu_file, label='Menu')

        
        ################# INPUT AND OUTPUT DIRECTORIES ##########################
        
        # Create buttons to select the directories

        # Create Tkinter variable, call the corresponding constructor
        # Check http://effbot.org/tkinterbook/variable.htm
        # These variables will be assigned with set() in browse_button function
        self.folder_input = StringVar()

        # Create text before the button
        lbl0 = Label(master=self.root, text="Choose input directory")
        lbl0.grid(row=0, column=0)

        lbl1 = Label(master=self.root, textvariable=self.folder_input)
        lbl1.grid(row=0, column=2)

        # Do not put () beside browse_button unless it is used with lambda
        # Note that if no argument are needed for browse_button, I could use command=self.browse_button
        # However, if I need to provide an argument, I need to use lambda:
        # 2 functions can be given in lambda by using []
        browse_button_input = Button(text="Browse", command=lambda: [self.browse_button(self.folder_input), self.check_directories()])
        browse_button_input.grid(row=0, column=1)

        # Initialize folder_output variable
        self.folder_output = StringVar()
        
        # Create text before the button
        lbl2 = Label(master=self.root, text="Choose output directory")
        lbl2.grid(row=1, column=0)

        lbl3 = Label(master=self.root, textvariable=self.folder_output)
        lbl3.grid(row=1, column=2)

        browse_button_output = Button(text="Browse", command=lambda:[self.browse_button(self.folder_output), self.check_directories()])
        browse_button_output.grid(row=1, column=1)


        ################# NUMBER OF SONGS ##########################

        self.nb_songs = 0
        self.entered_number = 0
        
        #self.nb_songs = IntVar()
        
        # Create label
        self.label_nb_songs = Label(self.root, text="Number of songs:")
        self.label_nb_songs.grid(row=2, column=0)
        
        # Create entry pannel abnd use a validate command
        # to verify that then entry is an integer
        # check http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/entry-validation.html
        vcmd = self.root.register(self.validate) # we have to wrap the command
        self.entry = Entry(self.root, validate="key", validatecommand=(vcmd, '%P'))
        self.entry.grid(row=2, column=1)
        
        # Add OK button
        self.add_button = Button(self.root, text="OK", command=self.update)
        self.add_button.grid(row=2, column=2)
        
        ################## LAUNCH FUNCTIONS ###########################

        # All the inputs are there, now we can use the different functions needed

        
        #list_song = find_mp3(dir_input)
        

        
    def browse_button(self, folder):
        """
        ask directory interface which assigns user choice to the argument 'folder'
        which should be already initialized with 'self.folder - StringVar()'
        """
        filename = filedialog.askdirectory(initialdir=os.getcwd(), title='Please select directory')
        folder.set(filename)


    # Still in development
    def check_directories(self):
        # Check if output and input directories are different (does not work if not called in the GUI)
        if self.folder_input.get() and self.folder_output.get():

            if self.folder_input.get() == self.folder_output.get():
                messagebox.showerror("Error message", "Input and output directories are similar, change one path")



    
    def validate(self, new_text):
        """
        Test if user input is an integer
        """
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            self.entered_number > 0
            return True
        except ValueError:
            return False

    def update(self):
        self.nb_songs += self.entered_number
        #self.nb_songs.set(self.nb_songs)
        print("Number of song:"+str(self.nb_songs))



    def find_mp3(self, dir_input):
        matches = []
        for root, dirnames, filenames in os.walk(dir_input):
            for filename in fnmatch.filter(filenames, '*.mp3'):
                matches.append(os.path.join(root, filename))
        if len(matches) == 0:
            messagebox.showerror("Error message", "No mp3 files were found in "+dir_input)
            sys.exit()
        else:
            return matches
        

    def display_help(self):
        print(self.folder_input.get())
        print(self.folder_output.get())
        messagebox.showinfo("Help window", "a Tk MessageBox")

    
    def quit(self):
        self.frame.quit()   


# Build the app in the main loop
if __name__ == "__main__":
    root = Tk()
    app = random_music(root)
    root.mainloop()
