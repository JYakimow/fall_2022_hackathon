from tkinter import *

import debug
import DATA
from tkinter import ttk

import function_01

#test
def openWindow():
    # declare the window
    window = Tk()
    # set window title
    window.title("Python GUI App")
    # set window width and height
    window.configure(width=500, height=300)
    # set window background color
    window.configure(bg='lightgray')
    #open window
    window.mainloop()

#frame1 
def openFrame1():
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

        def getLogin():

            if(DATA.checkCredentials((int)(E1.get(1.0, "end-1c")) ,(int)(E2.get(1.0, "end-1c")) ) == 1):
                openFrame2()
                print("1")
            else: 
                print(0)



        B = ttk.Button(top, text ="Confirm", command=lambda: getLogin() )
        B.pack( ipadx=10, ipady = 5)
        B.place(relx=.44, rely=.3, anchor="center")

        QuitButton = ttk.Button(top, text ="Quit", command=top.destroy)
        QuitButton.pack( ipadx=10, ipady = 5 )
        QuitButton.place(relx=.56, rely=.3, anchor="center")

        top.mainloop()

def openFrame2():
    frame2 = Tk()  
    frame2.geometry("400x250") 
    frame2.title("Frame 2")
   
    # the label for username
    #frame1_user_id = Label(frame1, text = "Employee ID").place(x = 35, y = 60) 
   
    # the label for user_password 
    #frame1_user_pin = Label(frame1, text = "Pin").place(x = 80, y = 100) 
   
    #frame1_user_name_input_area = Entry(frame1, width = 30).place(x = 110, y = 60) 
    #frame1_user_password_entry_area = Entry(frame1, width = 30).place(x = 110, y = 100) 

    frame2_label = Label(frame2, text = "Hello Employee #").place(x = 145, y = 15) 

    frame2_clock_in_button = Button(frame2, text = "Clock In", height= 4, width=10).place(x = 100, y = 40)
    frame2_clock_out_button = Button(frame2, text = "Clock Out", height= 4, width=10).place(x = 200, y = 40)

    frame2_30min_break_button = Button(frame2, text = "30 Minute \n Break", height= 4, width=10).place(x = 100, y = 130)
    frame2_15min_break_button = Button(frame2, text = "15 Minute \n Break", height= 4, width=10).place(x = 200, y = 130)

    frame2.mainloop()