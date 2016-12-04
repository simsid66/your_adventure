name = input("What's your name? ")
print ("hello" +" " + name + ". Welcome to Your Adventure, a python text adventure.")
print ("Your game begins here.")
choice1= input("You wake up. You can hear the whoosh of the Winds blowing against the shelter. What do you do? (go out/stay inside)")
goout = choice1
if goout ==("go out"):
 print ("You go out, worried about the effect of the Winds. Your worries soon go away, as you burn to death in the acidic gas.")
elif goout ==("stay inside"):
 print ("You stay inside, as it is the safest thing to do. The winds could kill you.")
else:
 print("bad syntax")

