#Project: Code <-- Shows the code for the project            Name of code: The Barney Star

import turtle #Brings in a turtle, turtles create the design.
turtle.colormode(255) #Brings in 255 shades of red, blue, and green for the turtle to use.
bob = turtle.Turtle() #bob is a variable for the turtle.
from myFunction import * #Imports all functions from the file "myFunction".
bob.speed(0) #Increases the speed of the turtle "bob".
turtle.bgcolor("black") #Changes the background color of the design.

pi3t(bob) #pi3t is the name of the function being used (pi3t means "project idea 3 testing").






#Project: Function <--Shows function for the code within the file "myFunction"

#def pi3t(i3):   <-- Defines function (pi3t) and gives variable (i3)
#    angle = 135 <-- sets angles (a variable) to 135
#    distance = 43 <-- sets distance (a variable) to 43

#    for times in range(255): <-- make the code below loop 255 times
#        c = (times * 1,0,times * 1) <-- made c as a variable for purple 
#        i3.color(c) <-- sets the variable turtle (i3) color to c (or purple)
#        i3.left(angle)   <-- tells i3 to turn left 'angle' degrees (or 135 degrees) 
#        i3.circle(times * 10) <-- i3 creates a circle 10 times each time the code repeats
#        i3.forward(distance) <-- tells i3 to move forward 'distance' times (or 43 times)

#    for times in range(127): <-- makes the code below loop 127 times
#        c = (0,times * 2,times * 1) <-- made c as a variable for green
#        i3.color(c) <-- sets the turtle (i3) to c (green)
#        i3.left(angle) <-- tells the turtle (i3) to turn left 'angle' (or 135 degrees)  
#        i3.circle(times * 10) <-- i3 creates a circle 10 times each time the code repeats
#        i3.forward(distance) <-- tells i3 to move forward 'distance' times (or 43 times)
