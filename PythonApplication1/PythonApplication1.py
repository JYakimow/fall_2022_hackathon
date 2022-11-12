#import libraries
import tkinter as tk

#import other files
import functionality
import gui

window = tk.Tk()

def doSomething():
	print("do something")

def main():
	print("hello world")
	print("Timothy has made it into the project!")
	print("I'm here - Rhianna")

	functionality.functionality_hello()
	doSomething()
	


	gui.workingFunction()
	


if __name__ == "__main__":
	main()