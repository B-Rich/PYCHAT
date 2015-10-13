#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import random
learningMode = False
learnQuestion = ""
memorize = False
greetings = ['hola', 'hello', 'hi','hey!','Hello','Hi']
questions = ['How are you?','How are you doing?']
responses = ['Okay','I am fine']
validations = ['yes','yeah','yea','no','No','Nah','nah']
verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]
memory = {"question": "1", "answer": "2"}

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent): 

        Tkinter.Tk.__init__(self,parent) #Tkinter.Tk constructor
        self.parent = parent #references to parent parameter
        self.geometry("500x55+500+250")
        self.initialize()

    def initialize(self): #initailizes program; Creates all GUI elements separate of the logic of the program
        self.grid() #Grid System Used to place widgets

        #Text Entry Widget
        self.entryVariable = Tkinter.StringVar() 
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        #Adds text box to grid under this column and row. 
        #Sticky='EW' refers to the widget sticking to East and West of the cell
        self.entry.bind("<Return>", self.messageSent) #Binds the Return key to the entry
        self.entry.bind("<FocusIn>", self.OnBoxEntered) #Binds clicking the text box to the text box
        self.entryVariable.set("Enter text here.")

        #Button Widgets
        buttonClick = Tkinter.Button(self,text="Language Builder", command=self.buttonClick, cursor="pointinghand")
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
      
        self.entry.selection_range(0, Tkinter.END)

    def messageSent(self, event): #Event when Enter is clicked
        global learningMode
        global learnQuestion
        userInput = ""
        if learningMode == False:
            #self.labelVariable.set( random.choice(questions) ) #Sets label to text
            userInput = (self.entryVariable.get()).lower()
            print userInput
        elif len(learnQuestion) != 0:
            response = self.entryVariable.get()
            memory[learnQuestion] = response
            self.labelVariable.set( "Another Question? (or click Language Builder again)" )
            learnQuestion = ""
        else:
            learnQuestion = (self.entryVariable.get()).lower()
            self.labelVariable.set( "And an appropriate response?" )

        
        if len(userInput) != 0:
            chatResponse = ""
            for i in memory:
                if userInput == i:
                    chatResponse = memory[i]
            if chatResponse == "":
                userReversed = userInput[::-1]
                if userReversed[0] == "?":
                    print "This is a Question!"
                    if userInput[0:2] == "are":
                        
                    elif userInput[0:2] == "how":
                    elif userInput[0:2] == "who":
                    elif userInput[0:2] == "why":
                    elif userInput[0:3] == "what":
                    else:

                else:
                    print "This is not a Question!"
            else:
                self.labelVariable.set(chatResponse)

        self.entryVariable.set("") #Empties Text Box
        self.entry.focus_set() #Sets focus on Entry
        self.entry.selection_range(0, Tkinter.END) #Highlights existing text

    def buttonClick (self):
        global learningMode
        if learningMode == False:
            learningMode = True
            print "Language Builder Engaged"
            self.labelVariable.set( "Enter a Question." )
        elif learningMode == True:
            learningMode = False
            print "Language Builder Disengaged"
            self.labelVariable.set( "Hello Again" )

        self.entryVariable.set("") 
        self.entry.focus_set() 
        self.entry.selection_range(0, Tkinter.END) 


    def OnBoxEntered(self,event): #When User enters text box, the text is deleted
        self.entryVariable.set("")

if __name__ == "__main__": #Executed when program is run from command-line
    app = simpleapp_tk(None)
    app.title('Chat Bot') #Window Title
    app.mainloop() 