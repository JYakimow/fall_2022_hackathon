from tkinter import *

from tkinter import ttk



def printtoScreen(args=[]):
	print(args)


top = Tk()
top.geometry("400x250")
L1 = Label(top, text="ID:")
L1.pack()
E1 = Text(top, width=20,height=1)

E1.insert(END, "Enter ID")
E1.pack()


top.geometry("700x350")
L2 = Label(top, text="Passcode:")
L2.pack()
E2 = Text(top, width=20,height=1)

E2.insert(END, "Enter Passcode")
E2.pack()

L3 = Label(top )
L3.pack()




B = ttk.Button(top, text ="Confirm", command=lambda: print(E1.get(1.0, "end-1c"),E2.get(1.0, "end-1c")) )
B.pack( ipadx=10, ipady = 5)




top.mainloop()


"""
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

"""
