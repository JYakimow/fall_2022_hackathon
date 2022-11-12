#import libraries
import tkinter as tk

#import other files
import functionality
import frame1_gui
import gui

def doSomething():
	print("do something")

def main():
	print("hello world")
	print("Timothy has made it into the project!")
	print("I'm here - Rhianna")

	
	functionality.functionality_hello()
	doSomething()
	


	gui.createWindow1()
	



	#frame2_gui.openWindow()
	frame1_gui.openFrame1()
	

if __name__ == "__main__":
	main()