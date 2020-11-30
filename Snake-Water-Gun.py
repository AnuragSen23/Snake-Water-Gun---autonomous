import pyttsx3 as speak
import random

Gwen = speak.init()

voices = Gwen.getProperty("voices")
volume = Gwen.getProperty("volume")
rate = Gwen.getProperty("rate")

Gwen.setProperty("voice",voices[1].id)
Gwen.setProperty("volume",1)
Gwen.setProperty("rate",200)

Gwen.say("How Many times you want to play this game?")
Gwen.runAndWait()
N = input("Enter your number of chances: ")


Gwen.say("Okay Lets Play. Choose Snake, Water or Gun")
Gwen.runAndWait()

a=0
b=0
c=0
for i in range(int(N)):

    player = input("Enter your Choice: ")

   
    trials = ["snake","water","gun"]
    Computer = random.choice(trials)

    Gwen.say("Computer chose " + Computer)
    Gwen.runAndWait()

    a = "This is a Draw"
    b = "Computer Wins"
    c = "You Win"

try:
    if Computer == "snake":
        if player == "snake":
            print(a)
            Gwen.say(a)
            Gwen.runAndWait()
            
        if player == "water":
            print(b)
            Gwen.say(b)
            Gwen.runAndWait()
            
        if player == "gun":
            print(c)
            Gwen.say(c)
            Gwen.runAndWait()
                    
    elif Computer == "water":
        if player == "water":
            print(a)
            Gwen.say(a)
            Gwen.runAndWait()
        
        if player == "gun":
            print(b)
            Gwen.say(b)
            Gwen.runAndWait()
        
        if player == "snake":
            print(c)
            Gwen.say(c)
            Gwen.runAndWait()
    
    else:
        
        if player == "gun":
            print(a)
            Gwen.say(a)
            Gwen.runAndWait()
        
        if player == "snake":
            print(b)
            Gwen.say(b)
            Gwen.runAndWait()
        
        if player == "water":
            print(c)
            Gwen.say(c)
            Gwen.runAndWait()
