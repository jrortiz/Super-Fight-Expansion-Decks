import sys
import random
import tkinter as tk
from tkinter import *



class Application(tk.Frame):

    def helloCallBack(self):
        tk.messagebox.showinfo("Hello Python", "Hello World")

        
    def startBlueDeck(self):
        self.text.get(self,"test", "test?")
        print("Entering Blue Deck")

    def startPurpleDeck(self):
        print("Entering Purple Deck")
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
            #self.text = tk.Text(self)
            #self.text.pack()
            
            self.Button = tk.Button(self)
            self.Button["text"] = "Hello"
            self.Button["command"] = self.helloCallBack
            self.Button.pack()

            
            self.blueDeck = tk.Button(self)
            self.blueDeck["text"] = "Blue Deck"
            self.blueDeck["command"] = self.startBlueDeck
            self.blueDeck.pack(side="top")

            self.purpleDeck = tk.Button(self)
            self.purpleDeck["text"] = "Purple Deck"
            self.purpleDeck["command"] = self.startPurpleDeck
            self.purpleDeck.pack()


            self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)

            self.QUIT.pack(side="bottom")







root = tk.Tk()
app = Application(master=root)
app.mainloop()


##
##def getLocation():
##    locations = ['Ocean', 'Moon', 'Smash Bros']
##    print(locations[random.randint(0,len(locations)-1)] + "\n")
##
##
##def runDeck():
##    gameOnFlag = True
##    while gameOnFlag:
##        n=input("Enter for a Location or Q/q to quit:")
##        if n.strip() == 'Q' or n.strip() == 'q':
##            gameOnFlag = False
##        elif not n:
##            getLocation()
##
##
###top.mainloop()
##print("Welcome to the Blue Deck")
##runDeck()
##print("Thanks for using the Blue Deck")
##    
##
##
