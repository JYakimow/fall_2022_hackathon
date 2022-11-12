#import libraries
import tkinter as tk

#import other files
import functionality
import frames_gui
import gui

def doSomething():
	print("do something")

def main():
	print("hello world")
	print("Timothy has made it into the project!")
	print("I'm here - Rhianna")

	functionality.functionality_hello()
	doSomething()
	
	#gui.createWindow1()

	#frames_gui.openWindow()
	#frames_gui.openFrame1()
	frames_gui.openFrame2()
	

if __name__ == "__main__":
	main()