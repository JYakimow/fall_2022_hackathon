import tkinter as tk


def workingFunction():
    #This creates the window
    window = tk.Tk()
    #Adds label to window
    label = tk.Label(text="Python rocks!")
    #This adds label to the window, I think
    label.pack()
    #This makes the window have to wait until it is closed to close.
    window.mainloop()

    print("This worked, at least.")

