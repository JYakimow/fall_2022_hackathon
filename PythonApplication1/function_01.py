from datetime import datetime

def temp():
    global now
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

     #Run when "Clock in" pressed"
     #Run when "Clock out" is pressed

    



def resetVal():
    a = ""
    b = ""
    return a, b



def clockIn(ClockIn):
    global start_time
    start_time = ((int)(now.strftime("%H")) * 60) + (int)(now.strftime("%M"))
    return start_time


def clockOut(ClockOut):
    global end_time
    end_time = ((int)(now.strftime("%H")) * 60) + (int)(now.strftime("%M"))
    return end_time

def calculateTimeWorked(start_time, end_time):
    timeWorked = end_time - start_time
    return timeWorked