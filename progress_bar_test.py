import sys
import shutil # copy file
import os # handle search path
import Tkinter as tk # Create alias for Tkinter
import tkMessageBox, tkFileDialog, tkSimpleDialog, ttk
import fnmatch # to search file recursively
import random # Select random songs from a list
import time


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

    # Create cancel button on the right of the progress bar. If clicked, the root window is closed
    #cancel_button = tk.Button(frame, text="Cancel", fg="black", command=root.destroy)
    cancel_button = tk.Button(frame, text="Cancel", fg="black", command=exit)
    cancel_button.pack(side=tk.RIGHT )

    # Locate position of the progress bar within the window
    pb_hd.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    pb_hd.start(1)

    # Launch Tkinter
    root.mainloop()

# I would use this function for the copying of the mp3 file
# Since Tkinter uses the main thread, I cannot run the window and perform
# my copying of file in the same time on the same thread.
# I need to use queue system (https://stackoverflow.com/questions/15323574/how-to-connect-a-progress-bar-to-a-function)

# Class which inherits attributes from tk.Tk (parent)
class progress_bar_class(tk.Tk):
    def __init__(self):
        self.myframe = ttk.Frame(self)
        self.myframe.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

        # Title of the window
        self.myframe.winfo_toplevel().title("Please wait")

        # Create progress bar window and make horizontal, inderteminate, and with length 200 pixels
        self.pb_hd = ttk.Progressbar(self.myframe, orient='horizontal', mode='indeterminate', length=200)

        # Create cancel button on the right of the progress bar. If clicked, the root window is closed
        cancel_button = tk.Button(frame, text="Cancel", fg="black", command=exit)
        cancel_button.pack(side=tk.RIGHT )


            
def progress_bar_determinate(max_value):
    # Create root window (master widget)
    root = tk.Tk()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

    # Title of the window
    frame.winfo_toplevel().title("Please wait")

    # Create progress bar window and make horizontal, inderteminate, and with length 200 pixels
    pb_hd = ttk.Progressbar(frame, orient='horizontal', mode='determinate', length=200, maximum=max_value)

    # Create cancel button on the right of the progress bar. If clicked, the root window is closed
    #cancel_button = tk.Button(frame, text="Cancel", fg="black", command=root.destroy)
    cancel_button = tk.Button(frame, text="Cancel", fg="black", command=exit)
    cancel_button.pack(side=tk.RIGHT )

    # Locate position of the progress bar within the window
    pb_hd.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

    #pb_hd["maximum"]=(max_value)

    def progress(currentValue):
        pb_hd["value"]=currentValue

    #currentValue=0
    #pb_hd["value"]=currentValue

    for i in range(max_value+1):
        #pb_hd.after(10, progress(currentValue))
        pb_hd["value"]=i # Go quicker than using the progress function (check doc https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.step)
        pb_hd.update() # Force an update of the GUI
        #currentValue += 1
        time.sleep(1)
        
    # Destroy the root once the loop is over    
    root.destroy()
    
    # Launch Tkinter
    root.mainloop()
    

if __name__ == "__main__":
    progress_bar_determinate(5)
    #progress_bar()
