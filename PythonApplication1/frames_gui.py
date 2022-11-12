from tkinter import *

import debug

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
    id_var = Tk.StringVar.get()
    in_var = Tk.StringVar()

    def login():
        employee_id = id_var.StringVar.get()
        employee_pin = pin_var.StringVar.get()

        #debug.output("Employee ID: ", employee_id)
        #debug.output("Employee PIN: ", employee_pin)

        employee_id = ""
        employee_id = ""

    frame1 = Tk()  
    frame1.geometry("400x250") 
   
    # the label for username
    frame1_user_id = Label(frame1, text = "Employee ID").place(x = 35, y = 60) 
   
    # the label for user_password 
    frame1_user_pin = Label(frame1, text = "Pin").place(x = 80, y = 100) 
   
    frame1_user_name_input_area = Entry(frame1, textvariable = id_var, width = 30).place(x = 110, y = 60) 
    frame1_user_password_entry_area = Entry(frame1, textvariable = pin_var, width = 30).place(x = 110, y = 100) 

    frame1_submit_button = Button(frame1, text = "Login", command = login()).place(x = 140, y = 130)
    frame1_quit_button = Button(frame1, text = "Quit").place(x = 200, y = 130)

    frame1.mainloop()

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