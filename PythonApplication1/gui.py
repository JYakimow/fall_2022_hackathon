import tkinter as tk


def createWindow1():
    #This creates the window
    window = tk.Tk()
    #Adds label to window
    label = tk.Label(
        text="Name:",
        foreground="orange",
        background="black",
        width=50,
        height=10
     )
    
    entry = tk.Entry(
        width=30,
    )

    button = tk.Button(
        text="Click me!",
        width=20,
        height=5,
        bg="white",
        fg="black",
        command = closeWindow
        )
    #This adds the stuff to the window, I think
    label.pack()
    entry.pack()
    button.pack()
    


    #This makes the window have to wait until it is closed to close.
    window.mainloop()

   # name = entry.get()
    #print(name)


    print("This worked, at least.")

def closeWindow():
    global username
    username = entry.get()
    window.destroy()
