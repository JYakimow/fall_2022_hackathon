import tkinter as tk




def createWindow1():
     

    def closeWindow():
       # username = userNameEntry.get()
        #window.destroy()
        print(userNameEntry.get())

    #This creates the window
    window = tk.Tk()
    #Adds label to window
    userNameLabel = tk.Label(
        text="Name:",
        foreground="orange",
        background="black",
        width=50,
        height=5
     )
    passwordLabel = tk.Label(
        text="Password:",
        foreground="orange",
        background="black",
        width=50,
        height=5
     )
    
    userNameEntry = tk.Entry(
        width=30,
    )

    passwordEntry = tk.Entry(
        width=30,
    )

    button = tk.Button(
        text="Click me!",
        width=20,
        height=5,
        bg="white",
        fg="black",
        command = closeWindow()
        )
    #This adds the stuff to the window, I think
    userNameLabel.pack()
    userNameEntry.pack()
    passwordLabel.pack()
    passwordEntry.pack()
    button.pack()
    


    #This makes the window have to wait until it is closed to close.
    window.mainloop()
    print(userNameEntry.get())


   # name = entry.get()
    #print(name)


    print("This worked, at least.")


