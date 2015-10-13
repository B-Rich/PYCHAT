#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

enteringID = False
sessionID = "DEFAULT"

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent): 
        Tkinter.Tk.__init__(self,parent) #Tkinter.Tk constructor
        self.parent = parent #references to parent parameter
        self.initialize()
        self.geometry("500x55+500+250")

    def initialize(self): #initailizes program; Creates all GUI elements separate of the logic of the program
        self.grid() #Grid System Used to place widgets

        #Text Entry Widget
        self.entryVariable = Tkinter.StringVar() 
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        #Adds text box to grid under this column and row. 
        #Sticky='EW' refers to the widget sticking to East and West of the cell
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entry.bind("<FocusIn>", self.OnBoxEntered)
        self.entryVariable.set("Enter text here.")

        #Button Widgets
        buttonClick = Tkinter.Button(self,text="Session ID", command=self.OnButtonClick, cursor="pointinghand")
        buttonClick.grid(column=1,row=0)

        buttonQuit = Tkinter.Button(self, text="Exit", command=self.quit, cursor="poof")
        buttonQuit.grid(column=1,row=1)

        #Label Widget
        self.labelVariable = Tkinter.StringVar() #Creates variable/label
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue") #Colors and anchors the label
        label.grid(column=0,row=1,columnspan=1,sticky='EW')
        self.labelVariable.set("Hello!") #Sets the text of the label

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False) #Allows for horizontal, but not vertical resizing of label and text entry
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set() #Automatically focuses on the entry box when the button is hit
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self): #Event when Button is clicked
        global enteringID
        self.labelVariable.set("Enter a Session ID")
        enteringID = True
        self.entryVariable.set("")
        self.entry.focus_set() #Sets focus on Entry
        self.entry.selection_range(0, Tkinter.END) #Highlights existing text

    def OnPressEnter(self,event): #User hits enter button [i.e sends text]
        global enteringID
        global sessionID
        userInput = self.entryVariable.get()

        if sessionID != "DEFAULT" and userInput == "save" or userInput == "Save":
            kernel.saveBrain("bot_brain.brn")

        elif sessionID == "DEFAULT" and userInput == "save" or userInput == "Save":
            self.labelVariable.set("Sorry, you cannot save anything, as you are not signed in.")

        elif enteringID == False:
            self.labelVariable.set(kernel.respond(userInput, sessionID))
            self.entryVariable.set("") 
            self.entry.focus_set()
            self.entry.selection_range(0, Tkinter.END)

        else:
            enteringID = False
            sessionID = userInput
            sessionData = kernel.getSessionData(sessionID)
            print sessionData
            self.labelVariable.set("Your ID is" + sessionID + ". Enter text to begin Chat. Save to save data.")
            self.entryVariable.set("") 
            self.entry.focus_set()
            self.entry.selection_range(0, Tkinter.END)

    def OnBoxEntered(self,event): #When User enters text box, the text is deleted
        self.entryVariable.set("")


if __name__ == "__main__": #Executed when program is run from command-line
    app = simpleapp_tk(None)
    app.title('Chat Bot') #Window Title
    app.mainloop() 