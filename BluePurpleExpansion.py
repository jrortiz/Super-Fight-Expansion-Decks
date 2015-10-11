import sys
import random
import tkinter as tk
from tkinter import *


#global variables because I'm having trouble with the deletion/lines and calling both decks at the same time.
purpleCards = ["ZOMBIES!!!","A Bomb's ticking down!", "Save the falling babies!", "A Damsel in Distress",
                    "A Bachelor in Distress", "Save Obama!", "Your hero is naked"]
blueCards = ["Ocean", "China", "Disney Land", "Earth's Moon", "Atillan"]

welcomeMessage = '''Welcome to the Blue Deck and Purple Deck program for SuperFight.
This deck allows you to use the Blue Deck and Purple Deck along with your
SuperFight game!
Blue Deck button will give you a location.
Purple Deck button will give you a situation.'''

class Application(tk.Frame):


    def infoCallBack(self):
        #This will print information about the Program.
        tk.messagebox.showinfo("INFO", '''Superfight is a hilarious card game based on fights between characters with superpowers and super problems.
Check it out at: http://www.superfightgame.com/
This is an independent project that I have created to save me money on the Blue and Purple Deck.
Written by Jeremy Ortiz \n''' + "="*86 + welcomeMessage)

        
    def callBlueDeck(self):
        #This will take a card from the blue deck
        self.text.configure(state="normal")
        self.text.delete('1.0', END)
        self.text.insert(END,"Blue card: " + blueCards[random.randrange(0,len(blueCards),1)] + "\n")
        self.text.configure(state="disabled")

    def callPurpleDeck(self):
        #This will take a card from the purple deck
    
        self.text.configure(state="normal")
        self.text.delete('1.0', END)
        self.text.insert(END,"PurpleCard: " + purpleCards[random.randrange(0,len(purpleCards),1)] + "\n")
        self.text.configure(state="disabled")

    def callBothDecks(self):
        self.text.configure(state="normal")
        self.text.delete('1.0', END)
        self.text.insert(END,"Blue card: " + blueCards[random.randrange(0,len(blueCards),1)] + "\n")
        self.text.insert(END,"PurpleCard: " + purpleCards[random.randrange(0,len(purpleCards),1)] + "\n")
        self.text.configure(state="disabled")

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):

            #Textbox that will print out the cards taken from the deck
            self.text = tk.Text(self)
            self.text.pack()
            self.text.insert(END,welcomeMessage)
            self.text.configure(state="disabled")
            self.text.insert(END,"test")

            #Blue Deck button widget
            self.blueDeck = tk.Button(self, fg="blue")
            self.blueDeck["text"] = "Blue Deck"
            self.blueDeck["command"] = self.callBlueDeck
            self.text.insert(END, "="*80)
            self.blueDeck.pack(side="top")

            #Purple Deck button widget
            self.purpleDeck = tk.Button(self, fg="purple")
            self.purpleDeck["text"] = "Purple Deck"
            self.purpleDeck["command"] = self.callPurpleDeck
            self.text.insert(END, "="*80)
            self.purpleDeck.pack()

            #Purple Deck button widget
            self.purpleDeck = tk.Button(self)
            self.purpleDeck["text"] = "Purple and Blue Deck"
            self.purpleDeck["command"] = self.callBothDecks
            self.text.insert(END, "="*80)
            self.purpleDeck.pack()
            
            #Info Button Widget
            self.Button = tk.Button(self)
            self.Button["text"] = "INFO"
            self.Button["command"] = self.infoCallBack
            self.Button.pack()

            #Quit button widget
            self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
            self.QUIT.pack(side="bottom")







root = tk.Tk()
root.wm_title("SuperFight Blue and Purple Deck")
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
