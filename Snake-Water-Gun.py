import speech_recognition as sr
import pyttsx3 as speak
import random

Gwen = speak.init()

voices = Gwen.getProperty("voices")
volume = Gwen.getProperty("volume")
rate = Gwen.getProperty("rate")

Gwen.setProperty("voice",voices[1].id)
Gwen.setProperty("volume",1)
Gwen.setProperty("rate",200)

Gwen.say("Okay Lets Play. Choose Snake, Water or Gun")
Gwen.runAndWait()

print("Give your choice: ")
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.record(source, duration=5)
    player = r.recognize_google(audio)
    
    trials = ["snake","water","gun"]
    Computer = random.choice(trials)
    
    if Computer == "snake":
        if player == "snake":
            print("That is a DRAW!")
            Gwen.say("This is a Draw")
            Gwen.runAndWait()
        
        if player == "water":
            print("COMPUTER WINS!")
            Gwen.say("Computer Wins")
            Gwen.runAndWait()
        
        if player == "gun":
            print("YOU WIN!")
            Gwen.say("You Win")
            Gwen.runAndWait()
    
    if Computer == "water":
        
        if player == "water":
            print("That is a DRAW!")
            Gwen.say("This is a Draw")
            Gwen.runAndWait()
        
        if player == "gun":
            print("COMPUTER WINS!")
            Gwen.say("Computer Wins")
            Gwen.runAndWait()
        
        if player == "snake":
            print("YOU WIN!")
            Gwen.say("You Win")
            Gwen.runAndWait()
    
    if Computer == "gun":
        
        if player == "gun":
            print("That is a DRAW!")
            Gwen.say("This is a Draw")
            Gwen.runAndWait()
        
        if player == "snake":
            print("COMPUTER WINS!")
            Gwen.say("Computer Wins")
            Gwen.runAndWait()
        
        if player == "water":
            print("YOU WIN!")
            Gwen.say("You Win")
            Gwen.runAndWait()
    