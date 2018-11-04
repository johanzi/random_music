# Random music selector

## Function

If you find time consuming the transfer of mp3 music files from your desktop computer to your mp3 player and you would like a quick selection of random songs for the day, this program is for you. This python script allows to select a defined number of mp3 files in a random and recursive manner and transfer them on the selected output directory. The program use the built-in tkinter library to offer a GUI. It requires python3 to be installed on your computer and to click on the script file.

## Usage

This script is compatible with Python3.

Double-click on the script file or launch it directly from a terminal such as:


´´´
python random_music.py

´´´

A window should pop up and prompt you to choose the directory containing your music.
A second window will ask you to choose the directory in which the files will be transfered.
The third and last window will ask how many mp3 files you want to transfer. Click OK and wait.

*NB: In Windows or Linux, check that Python3 executable is used to run the script*

## Options

### Progress bar (terminal only)

If you want to assess the progress of the work, the module [tqdm](https://github.com/tqdm/tqdm) is implemented in the script but is facultative. If you want to get its function, install it with pip. Note that the progress bars only appear in the terminal (nothing will be displayed if the script is launched by double-clicking on it).

```
pip install tqdm --user
```

When the script will be search for mp3 files, a progress bar will appear in the terminal and indicate the total number of files screened and then the number of mp3 files being copied to the destination directory

```
$ python random_music.py
Total number files found: 270files [00:00, 2472.52files/s]
mp3 files copied: 100%|##########| 15/15 [00:03<00:00,  3.29files/s]

```


### Progress bar (GUI with tkinter)
I started implementing the progress bar in tkinter to have it as a popup window but I still need to deal with the threading process. You can give a try on this [brancj](https://github.com/johanzi/random_music/tree/implement_progress_bar)


# TODO

* Check if script runs on Linux and Mac OS X
* Implement tkinter progress bar (indeterminate when searching for mp3 files and determinate when copying mp3 files)


# Authors
* **Johan Zicola** - [johanzi](https://github.com/johanzi)

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

