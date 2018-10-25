import sys
import shutil # copy file
import os # handle search path
import Tkinter as tk # Create alias for Tkinter
import tkMessageBox, tkFileDialog, tkSimpleDialog, ttk
import fnmatch # to search file recursively
import random # Select random songs from a list

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
def progress_bar_determinate():
    # Create root window (master widget)
    root = tk.Tk()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

    # Title of the window
    frame.winfo_toplevel().title("Please wait")

    # Create progress bar window and make horizontal, inderteminate, and with length 200 pixels
    pb_hd = ttk.Progressbar(frame, orient='horizontal', mode='determinate', length=200)

    # Create cancel button on the right of the progress bar. If clicked, the root window is closed
    #cancel_button = tk.Button(frame, text="Cancel", fg="black", command=root.destroy)
    cancel_button = tk.Button(frame, text="Cancel", fg="black", command=exit)
    cancel_button.pack(side=tk.RIGHT )

    # Locate position of the progress bar within the window
    pb_hd.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

    pb_hd["maximum"]=(100)

    def progress(currentValue):
        pb_hd["value"]=currentValue
    
    currentValue=0
    pb_hd["value"]=currentValue
    for i in range(100):
        pb_hd.after(10, progress(currentValue))
        #pb_hd.update() # Force an update of the GUI
        currentValue += 1


    

    # Launch Tkinter
    root.mainloop()

progress_bar_determinate()

#progress_bar()
