import sys
import shutil # copy file
import os # handle search path
import Tkinter as tk # Create alias for Tkinter
import tkMessageBox, tkFileDialog, tkSimpleDialog, ttk
import fnmatch # to search file recursively
import random # Select random songs from a list

# This script runs on Python2.7


# Function requiring directory to user
# Variable 'dir' created to personalize the GUI text
def get_dirname(dir):
    # withdraw removes the default root window displayed by Tk
    tk.Tk().withdraw()
    dirname = tkFileDialog.askdirectory(initialdir=os.getcwd(), title='Please select '+dir)
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
    # Get value and check if integer
    nb_song = tkSimpleDialog.askstring("", "Number of songs")
    # Exit if user clicks 'cancel'
    if not nb_song:
        sys.exit()
    # Check if variable is an integer
    try:
        nb_song = int(nb_song)
    except ValueError:
        tkMessageBox.showerror("Error message", "Value provided is not an integer")
        sys.exit()
    # If variable is an integer, return it
    return nb_song


# Find mp3 in directory and select a random
# This step may take time in large directory.
# TODO: time length of the code for large folders
def find_mp3(dir_input):
    matches = []
    for root, dirnames, filenames in os.walk(dir_input):
        for filename in fnmatch.filter(filenames, '*.mp3'):
            matches.append(os.path.join(root, filename))
    if len(matches) == 0:
        tkMessageBox.showerror("Error message", "No mp3 files were found in "+dir_input) 
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
    for i in sub_list:
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

    root.mainloop()
    
    
# Loading progress
# Check doc https://docs.python.org/3/library/tkinter.ttk.html
# https://github.com/lbgists/ttk-progressbar-example.py/blob/master/ttk-progressbar-example.py
def progress_bar():
    # Create root window (master widget)
    root = tk.Tk()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

    # Title of the window
    frame.winfo_toplevel().title("Please wait")

    # Create progress bar window and make horizontal, inderteminate, and with length 200 pixels
    pb_hd = ttk.Progressbar(frame, orient='horizontal', mode='indeterminate', length=200)

    # Create cancel button on the right of the progress bar. If clicked, the program is killed
    cancel_button = tk.Button(frame, text="Cancel", fg="black", command=exit)
    cancel_button.pack(side=tk.RIGHT )

    # Locate position of the progress bar within the window
    pb_hd.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    pb_hd.start(1)

    # Launch Tkinter
    root.mainloop()


def main():
    # Get the two directories from user
    
    dir_input = get_dirname("directory containing music")
    #dir_input = "C:/Users/iblis/Documents/test_music"
    
    dir_output = get_dirname("destination directory")
    #dir_output = "C:/Users/iblis/Documents/output_dir_music"

    # Test if dir_input and dir_output are different
    if dir_input == dir_output:
        tkMessageBox.showerror("Chosen source and destination directories are identical, please choose different directories") 
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
    sys.exit(main())

