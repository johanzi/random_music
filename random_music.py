import shutil # copy files
import os # handle search paths
import fnmatch # search files recursively
import random # Get random elements from song list
import threading
import time

# Make Tkinter working on python2 and 3
try:
    from Tkinter import *
    from ttk import *
    import tkFileDialog as filedialog
    import tkMessageBox as messagebox
    
except ImportError:
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import filedialog, messagebox


class Progress():
    """ threaded progress bar for tkinter gui """
    def __init__(self, root, row, column, columnspan):
        self.maximum = 100
        self.interval = 10
        self.progressbar = Progressbar(root, orient=HORIZONTAL,
                                           mode="indeterminate",
                                           maximum=self.maximum,
                                           value=0)
        
        self.progressbar.grid(row=row, column=column,
                              columnspan=columnspan, sticky="we")
        
        
        # progress bar is first define as determinate since 
        # a little chunk of green is visible it mode 'indeterminate'
        # is chosen
        self.progressbar.configure(mode="determinate", value=0)
        
        self.thread = threading.Thread()
        
        # Progress bar should be empty at first
        
        #self.thread.__init__(target=self.progressbar.start(self.interval), args=())
        self.thread.start()

    def pb_stop(self):
        """ stops the progress bar """
        if not self.thread.isAlive():
            VALUE = self.progressbar["value"]
            self.progressbar.stop()
            self.progressbar["value"] = VALUE

    def pb_start(self):
        """ starts the progress bar """
        if not self.thread.isAlive():
            VALUE = self.progressbar["value"]
            self.progressbar.configure(mode="indeterminate",
                                       maximum=self.maximum,
                                       value=VALUE)
            #self.progressbar.start(self.interval)
            self.progressbar.start()
            
    def pb_complete(self):
        """ stops the progress bar and fills it """
        if not self.thread.isAlive():
            self.progressbar.stop()
            self.progressbar.configure(mode="determinate",
                                       maximum=self.maximum,
                                       value=self.maximum)
        
    def print_statement(self):
        messagebox.showinfo("Thread is running")


class random_music():
    
    def __init__(self, root):
        # A frame is a widget that displays just as a simple rectangle.
        # Frames are primarily used as a container for other widgets,
        # which are under the control of a geometry manager such as grid.
        # I can define the size using padding option
        self.frame = Frame(root, padding=50)
        
        # This line seems optional (in condition that root is called as root in other methods)
        self.root = root
        
        # Name of the main Window
        self.root.title("Random music")
        
        # Choose to use either 'pack' or 'grid' mode to arrange widget in the frame
        self.frame.grid()


        ############################### MENU #######################################
        
        # Create a menu bar with the label "Menu" and submenus "Help" and "Quit"
        self.menubar = Menu(self.root)
        self.root['menu'] = self.menubar
        
        # Create submenus (need to be done first)
        self.menu_file = Menu(self.menubar)
        self.menu_file.add_command(label="Help", command=self.display_help)
        self.menu_file.add_command(label="Quit", command=self.quit)
        
        # Give label to menu name
        self.menubar.add_cascade(menu=self.menu_file, label='Menu')
       
        ###################### INPUT AND OUTPUT DIRECTORIES ##########################
        
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

        
        ######################## NUMBER OF SONGS ##########################

        self.nb_songs = 0
        self.entered_number = 0
        
        # Create label
        self.label_nb_songs = Label(self.root, text="Number of songs:")
        self.label_nb_songs.grid(row=2, column=0)
        
        # Create entry pannel abnd use a validate command
        # to verify that then entry is an integer
        # check http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/entry-validation.html
        # TOFIX: when only digit is entered (no paths), the error message of 'no mp3 files are found'
        # is displayed. Try to handle this to display an appropriate error message
        
        vcmd = self.root.register(self.validate) # we have to wrap the command
        self.entry = Entry(self.root, validate="key", validatecommand=(vcmd, '%P'))
        self.entry.grid(row=2, column=1)
        
          
        # Add OK button to validate input song number and launch 'main'
        self.add_button = Button(self.root, text="OK", command=lambda:[self.prog_bar.pb_start(), self.update(), threading.Thread(target=self.main).start()])
        self.add_button.grid(row=2, column=2)
        
        # All the inputs are there, now we can use the different functions needed
        
        ##################### PROGRESS BAR ###########################
        
        # Add a progress bar on the main GUI window
        self.prog_bar = Progress(root, row=3, column=0, columnspan=3)
        
        ################## LAUNCH FUNCTIONS ###########################

        # TODO: implement progress bars for the searching (indeterminate) and 
        # the copying (determinate) step. There will probably need of threading for this
        
    def main(self):
  
        """
        This method calls all methods needed after the user provided 3 valid
        arguments (input_dir, output_dir, and nb_songs)
        """
        #prog_bar.pb_start()
        
        # Get list of songs of the input directory
        self.list_songs = self.find_mp3(self.folder_input.get())

        # Check if there is a least one song in the directory, return 
        # error message if not
        if self.nb_songs == None:
            sys.exit(messagebox.showerror("Help window", "a Tk MessageBox"))
        
        # Get the return of select_random wich is tuple of 2 items
        # The nb_songs variable is updated to the true number of songs found 
        # in case user gave more songs than the input directory actuall contains
        tuple = self.select_random(self.list_songs, self.nb_songs)
        self.sub_list = tuple[0]
        self.nb_songs = tuple[1]
        
        # Copy the mp3 files to output directory
        self.copy_files(self.sub_list, self.folder_output.get())
        
        # Make progress bar appear as complete
        self.prog_bar.pb_complete()
                
        # Display info message after copying
        messagebox.showinfo("Information window", str(self.nb_songs)+" mp3 files were successfully copied into "+str(self.folder_output.get()))
        
        # Reassign nb_songs to 0 so the user can redo a copy operation with a new value
        self.nb_songs = 0
        
        
        
  
    def browse_button(self, folder):
        """
        ask directory interface which assigns user choice to the argument 'folder'
        which should be already initialized with 'self.folder - StringVar()'
        """
        filename = filedialog.askdirectory(initialdir=os.getcwd(), title='Please select directory')
        folder.set(filename)


    def check_directories(self):
        """
        Check if output and input directories are different (does not work if not called in the GUI)
        """
        if self.folder_input.get() and self.folder_output.get():
            if self.folder_input.get() == self.folder_output.get():
                messagebox.showerror("Error message", "Input and output directories are similar, change one path")
  
  
    def validate(self, new_text):
        """
        Allow user to enter an integer only
        """
        
        # This if statement is needed otherwise one cannot erase the first digit entered in the window
        if not new_text:
            return True

        # Allow only integer entry
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False


    def update(self):
        """
        Update values of nb_songs by the user input
        """
        if not self.entered_number:
            messagebox.showerror("Error message", "No number of songs indicated")
        else:
            self.nb_songs += self.entered_number

        
    def find_mp3(self, dir_input):
        """
        Get recursively all mp3 files contained in the input_directory
        and returns a list
        """
        matches = []
        for root, dirnames, filenames in os.walk(dir_input):
            for filename in fnmatch.filter(filenames, '*.mp3'):
                matches.append(os.path.join(root, filename))
        if len(matches) == 0:
            messagebox.showerror("Error message", "No mp3 files were found in "+dir_input)
        else:
            return matches


    def select_random(self, list_songs, nb_songs):
        """
        Select randomly nb_songs mp3 files from list list_songs
        Return a tuple with the files selected and the actual
        number of songs (corrected nb_songs) in case value of input
        is superior to the actual number of mp3 files in the input
        directory
        """
        if len(list_songs) < nb_songs:
            nb_songs = len(list_songs)
        
        sub_list = random.sample(list_songs, nb_songs)
        
        return sub_list, nb_songs


    # Copy these files into the output directory
    # Check if file with same name is already present, it yes, add suffix
    def copy_files(self, sub_list, dir_output):
        """
        Copy the selected mp3 files into dir_output. If dir_output
        already contains a file, the file is renamed by adding a number 
        suffix and this suffix is incremented as long as the file does 
        not get a unique name.
        """
        for i in sub_list:
            # Check if file name exists in dir_output
            file_name = os.path.basename(i)
            file_name = os.path.join(dir_output, file_name)
            
            
            time.sleep(1)
            
            
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


    def display_help(self):
        """
        Display help window from the menu
        """
        messagebox.showinfo("Help window", "This software allows you to copy a random set of a chosen number of mp3 files from an input directory (e.g. hard disk) to an output directory (e.g. mp3 player). The software will search for all mp3 files in the input directory and all subdirectories, then select the number of files chosen by the user to copy into the output directory.\n\nAuthor: Johan Zicola")

    
    def quit(self):
        """
        Quit the application
        """
        self.frame.quit()   

        



# Build the app in the main loop
if __name__ == "__main__":
    root = Tk()
    app = random_music(root)
    root.mainloop()
