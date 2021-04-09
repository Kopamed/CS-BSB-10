import random
import sys
#import pyinputplus as pyip

def Eightball():
    #why_does = "this_not_work"
    return random.choice(["yes","no", "windows 10 bad", "maybe", "i dont know", "ask again", "probably"])

while True:
    what = input("What would you like to do?\n[1] 8ball\n[2] quit\n>")
    if what == "2":
        print("quit")
        break

    elif what == "1":
        print(Eightball())
    else:
        print("Select a nimber from the menu")
    #i = input("Press [ENTER] to confirm")
    #sys.clear()
