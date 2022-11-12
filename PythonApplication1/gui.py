from tkinter import *

from tkinter import ttk

import DATA

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
B.place(relx=.44, rely=.3, anchor="center")

QuitButton = ttk.Button(top, text ="Quit", command=top.destroy)
QuitButton.pack( ipadx=10, ipady = 5 )
QuitButton.place(relx=.56, rely=.3, anchor="center")


top.mainloop()
