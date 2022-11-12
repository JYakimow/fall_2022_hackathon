from tkinter import *

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

def openFrame1():
    frame1 = Tk()  
    frame1.geometry("400x250") 
   
    # the label for username
    frame1_user_id = Label(frame1, text = "Employee ID").place(x = 35, y = 60) 
   
    # the label for user_password 
    frame1_user_pin = Label(frame1, text = "Pin").place(x = 80, y = 100) 
   
    frame1_submit_button = Button(frame1, text = "Login").place(x = 140, y = 130)
    quit_button = Button(frame1, text = "Login").place(x = 140, y = 130)
   
    user_name_input_area = Entry(frame1, width = 30).place(x = 110, y = 60) 
   
    user_password_entry_area = Entry(frame1, width = 30).place(x = 110, y = 100) 
     
    frame1.mainloop()