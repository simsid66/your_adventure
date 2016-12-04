name = input("What's your name? ")
print ("hello" +" " + name + ". Welcome to The Meal, a python text adventure.")
print ("Your game begins here.")
choice1= input("You wake up. You can hear the whoosh of the Winds blowing against the shelter. What do you do? a)go out b)stay inside (a/b)")
goout = choice1
if goout ==("a"):
 print ("You go out, worried about the effect of the Winds. Your worries soon go away, as you burn to death in the acidic gas.{ENDING 1}")
 print ("restart this applet to continue.")
elif goout ==("b"):
 print ("You stay inside, as it is the safest thing to do. The winds could kill you.")
 print ("The sounds soon stop, and you decide to venture out. The food isn't going to gather itself, is it?")
 choice2= input("You find: a) a package of cup noodles b) a meal-ready-to-eat package (a/b)")
 youfind1 = choice2
 if youfind1 ==("a"):
     print ("The cup noodles are useless to you: you need hot water to eat them. You toss them away.")
     print ("You keep walking.")
     print ("The thirty-minute sun begins to dawn. You sigh, and realize that you won't be eating anything today, like most days. You return to your shelter.")
     choice3= input("You decide to: a) go to sleep b) stare at the wall (a/b)")
     decide1 = choice3
     if decide1 ==("a"):
         print("(MUSEUM, 1000 years later) Specimen " + name + " was found buried under a sort of makeshift shelter. He died in his sleep, as a result of starvation. {ENDING 3}")

     if decide1 ==("b"):
         print("(MUSEUM, 1000 years later) Specimen " + name + " was found buried under a sort of makeshift shelter. He died in agony awake, as a result of starvation. {ENDING 4}")

   
 elif youfind1 ==("b"):
     print ("You are glad. You finally found food.")
     choice4= input("The thirty minute sun begins to dawn. You decide to: a)stay out b)go back to your shelter and eat the MRE (a/b)")
     decide2 = choice4
     if decide2==("a"):
         print (" You stay out, conscious that the Winds are blowing. You are not conscious of this very long, as the acidic gas burns you to death.")
         print ("(MUSEUM, 1000 years later) Specimen " + name + " was found on the open ground. He died in agony awake, as a result of starvation. He clutched some kind of package in his hand. {ENDING 2}")
     elif decide2==("b"):
         print ("You go back to your shelter and eat. This is your first good meal in days. You fall asleep, content. {ENDING 1}")
         
 
 
else:
 print("bad syntax")

