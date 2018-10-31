import Tkinter              # Python 2
import ttk


# https://github.com/lbgists/ttk-progressbar-example.py/blob/master/ttk-progressbar-example.py

def main():

    root = Tkinter.Tk()

    ft = ttk.Frame()
    #fb = ttk.Frame()

    ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
    #fb.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)

    pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')

    pb_hd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
    pb_hd.start(50)

    root.mainloop()


if __name__ == '__main__':
    main()
