# fatAlbert.py

import turtle
import random
import time
import math
import os

#Setting up the window and background
window = turtle.Screen()
window.bgpic("backgroundA.gif")
os.system("afplay music.mp3&")
#The music continues even when you exit the game
#window.bgcolor("lightblue")
turtle.setup(1000,1000)
window.tracer(4)
score = 0
window.title("Sweet Albert: Help him get candy! By Reena Sarkar and Amanda Chen")

#Naming all of our turtles (characters and candies)
mom = turtle.Turtle()
mom.ht()
mom.penup()
turtle.addshape("pal.gif")
mom.shape("pal.gif")

dad = turtle.Turtle()
dad.ht()
dad.penup()
turtle.addshape("dad.gif")
dad.shape("dad.gif")

sis = turtle.Turtle()
sis.ht()
sis.penup()
turtle.addshape("sis.gif")
sis.shape("sis.gif")

bro = turtle.Turtle()
bro.ht()
bro.penup()
turtle.addshape("bro.gif")
bro.shape("bro.gif")

grandpa = turtle.Turtle()
grandpa.ht()
grandpa.penup()
turtle.addshape("dude.gif")
grandpa.shape("dude.gif")

grandma = turtle.Turtle()
grandma.ht()
grandma.penup()
turtle.addshape("grandma.gif")
grandma.shape("grandma.gif")

coach = turtle.Turtle()
coach.ht()
coach.penup()
turtle.addshape("coach.gif")
coach.shape("coach.gif")

aunt = turtle.Turtle()
aunt.ht()
aunt.penup()
turtle.addshape("aunt.gif")
aunt.shape("aunt.gif")

bae = turtle.Turtle()
bae.ht()
bae.penup()
turtle.addshape("bae.gif")
bae.shape("bae.gif")

man = turtle.Turtle()
man.ht()
man.penup()
turtle.addshape("man.gif")
man.shape("man.gif")

uncle = turtle.Turtle()
uncle.ht()
uncle.penup()
turtle.addshape("uncle.gif")
uncle.shape("uncle.gif")

dude = turtle.Turtle()
dude.ht()
dude.penup()
turtle.addshape("dude.gif")
dude.shape("dude.gif")

friendA = turtle.Turtle()
friendA.ht()
friendA.penup()
turtle.addshape("sis.gif")
friendA.shape("sis.gif")

friendB = turtle.Turtle()
friendB.ht()
friendB.penup()
turtle.addshape("uncle.gif")
friendB.shape("uncle.gif")

friendC = turtle.Turtle()
friendC.ht()
friendC.penup()
turtle.addshape("man.gif")
friendC.shape("man.gif")

friendD = turtle.Turtle()
friendD.ht()
friendD.penup()
turtle.addshape("bae.gif")
friendD.shape("bae.gif")

aunt = turtle.Turtle()
aunt.ht()
aunt.penup()
turtle.addshape("aunt.gif")
aunt.shape("aunt.gif")

friendE = turtle.Turtle()
friendE.ht()
friendE.penup()
turtle.addshape("bae.gif")
friendE.shape("bae.gif")

friendF = turtle.Turtle()
friendF.ht()
friendF.penup()
turtle.addshape("man.gif")
friendF.shape("man.gif")

friendG = turtle.Turtle()
friendG.ht()
friendG.penup()
turtle.addshape("uncle.gif")
friendG.shape("uncle.gif")

friendH = turtle.Turtle()
friendH.ht()
friendH.penup()
turtle.addshape("sis.gif")
friendH.shape("sis.gif")

candyA = turtle.Turtle()
candyA.ht()
candyA.penup()
turtle.addshape("candyA.gif")
candyA.shape("candyA.gif")

candyB = turtle.Turtle()
candyB.ht()
candyB.penup()
candyB.color("yellow")
turtle.addshape("candyC.gif")
candyB.shape("candyC.gif")

candyC = turtle.Turtle()
candyC.ht()
candyC.penup()
turtle.addshape("candyC.gif")
candyC.shape("candyC.gif")

candyD = turtle.Turtle()
candyD.ht()
candyD.penup()
turtle.addshape("candyA.gif")
candyD.shape("candyA.gif")

candyE = turtle.Turtle()
candyE.ht()
candyE.penup()
turtle.addshape("candyA.gif")
candyE.shape("candyA.gif")

albert = turtle.Turtle()
albert.goto(0,0)
albert.left(90)
albert.penup()
albert.speed(30)
turtle.addshape("albert.gif")
albert.shape("albert.gif")

myPen = turtle.Turtle()
myPen.penup()
myPen.color("white")
myPen.hideturtle()
myPen.goto(350,370)

#Define functions
def turnleft():
        albert.speed(30)
        albert.goto(albert.xcor()-10,albert.ycor())

def turnright():
        albert.speed(30)
        albert.goto(albert.xcor()+10, albert.ycor())
      
def forward():
        albert.forward(10)

def backward():
        albert.backward(10)

def distance(x1, x2, y1, y2): #Distance formula to help with detecting collisions
     distance1 = ((x2-x1)**2+(y2-y1)**2)**0.5
     return distance1

def hideTurtles(): #Hide all turtles after game is over
        myPen.undo()
        myPen.ht()
        os.system("afplay collision.mp3&")
        global score
        score = 0
        done = True
        while done == True:
            window.bgpic("gameover.gif") #Displays "Game over"
            mom.hideturtle()
            dad.hideturtle()
            sis.hideturtle()
            bro.hideturtle()
            grandpa.hideturtle()
            grandma.hideturtle()
            coach.hideturtle()
            aunt.hideturtle()
            bae.hideturtle()
            man.hideturtle()
            uncle.hideturtle()
            dude.hideturtle()
            friendA.hideturtle()
            friendB.hideturtle()
            friendC.hideturtle()
            friendD.hideturtle()
            friendE.hideturtle()
            friendF.hideturtle()
            friendG.hideturtle()
            friendH.hideturtle()
            candyA.hideturtle()
            candyB.hideturtle()
            candyC.hideturtle()
            candyD.hideturtle()
            candyE.hideturtle()
            if (albert.xcor() >= 300 and albert.xcor() <= 500) and (albert.ycor() >= 300 and albert.ycor() <= 500):
                done = False
                print("You've restarted your game!")
                mom.reset()
                aunt.reset()
                bae.reset()
                bro.reset()
                coach.reset()
                dude.reset()
                grandma.reset()
                man.reset()
                sis.reset()
                friendA.reset()
                friendB.reset()
                friendC.reset()
                friendD.reset()
                friendE.reset()
                friendF.reset()
                friendG.reset()
                friendH.reset()
                candyA.reset()
                candyB.reset()
                candyC.reset()
                candyD.reset()
                candyE.reset()
                mom.penup()
                dad.penup()
                aunt.penup()
                bae.penup()
                bro.penup()
                coach.penup()
                dude.penup()
                grandma.penup()
                man.penup()
                sis.penup()
                friendA.penup()
                friendB.penup()
                friendC.penup()
                friendD.penup()
                friendE.penup()
                friendF.penup()
                friendG.penup()
                friendH.penup()
                candyA.penup()
                candyB.penup()
                candyC.penup()
                candyD.penup()
                candyE.penup()
                window.bgpic("background.gif")
                myPen.ht()
                myPen.undo()
                main()
                        

score = 0
#Start the event loop where the program "listens" for key presses.
def movement():
                        
        momRightOrLeft = random.randrange(0,2)
        dadRightOrLeft = random.randrange(0,2)
        auntRightOrLeft = random.randrange(0,2)
        baeRightOrLeft = random.randrange(0,2)
        broRightOrLeft = random.randrange(0,2)
        coachRightOrLeft = random.randrange(0,2)
        dudeRightOrLeft = random.randrange(0,2)
        grandmaRightOrLeft = random.randrange(0,2)
        manRightOrLeft = random.randrange(0,2)
        sisRightOrLeft = random.randrange(0,2)
        uncleRightOrLeft = random.randrange(0,2)

        friendAForBack = random.randrange(0,2)
        friendBForBack = random.randrange(0,2)
        friendCForBack = random.randrange(0,2)
        friendDForBack = random.randrange(0,2)
        friendEForBack = random.randrange(0,2)
        friendFForBack = random.randrange(0,2)
        friendGForBack = random.randrange(0,2)
        friendHForBack = random.randrange(0,2)

        candyAForBack = random.randrange(0,2)
        candyBForBack = random.randrange(0,2)
        candyCForBack = random.randrange(0,2)
        candyDRightOrLeft = random.randrange(0,2)
        candyERightOrLeft = random.randrange(0,2)

        momForward = random.randrange(6,10)
        dadForward = random.randrange(6,10)
        auntForward = random.randrange(6,10)
        baeForward = random.randrange(6,10)
        broForward = random.randrange(6,10)
        coachForward = random.randrange(6,10)
        dudeForward = random.randrange(6,10)
        grandmaForward = random.randrange(6,10)
        manForward = random.randrange(6,10)
        sisForward = random.randrange(6,10)
        uncleForward = random.randrange(6,10)

        friendAForward = random.randrange(6,10)
        friendBForward = random.randrange(6,10)
        friendCForward = random.randrange(6,10)
        friendDForward = random.randrange(6,10)
        friendEForward = random.randrange(6,10)
        friendFForward = random.randrange(6,10)
        friendGForward = random.randrange(6,10)
        friendHForward = random.randrange(6,10)

        candyAForward = random.randrange(6,10)
        candyBForward = random.randrange(6,10)
        candyCForward = random.randrange(6,10)
        candyDForward = random.randrange(6,10)
        candyEForward = random.randrange(6,10)
        
        momYcor = random.randrange(-440,440)
        dadYcor = random.randrange(-440,440)
        auntYcor = random.randrange(-440,440)
        baeYcor = random.randrange(-440,440)
        broYcor = random.randrange(-440,440)
        coachYcor = random.randrange(-440,440)
        dudeYcor = random.randrange(-440,440)
        grandmaYcor = random.randrange(-440,440)
        manYcor = random.randrange(-440,440)
        sisYcor = random.randrange(-440,440)
        uncleYcor = random.randrange(-440,440)

        friendAXcor = random.randrange(-440,440)
        friendBXcor = random.randrange(-440,440)
        friendCXcor = random.randrange(-440,440)
        friendDXcor = random.randrange(-440,440)
        friendEXcor = random.randrange(-440,440)
        friendFXcor = random.randrange(-440,440)
        friendGXcor = random.randrange(-440,440)
        friendHXcor = random.randrange(-440,440)

        candyAXcor = random.randrange(-440,440)
        candyBXcor = random.randrange(-440,440)
        candyCXcor = random.randrange(-440,440)
        candyDYcor = random.randrange(-440,440)
        candyEYcor = random.randrange(-440,440)

        if momRightOrLeft == 0: #Starts on the right
                momXcor = 500
                mom.left(180)
        elif momRightOrLeft == 1: #Starts on the left
                momXcor = -500
        if dadRightOrLeft == 0: #Starts on the right
                dadXcor = 500
                dad.left(180)
        elif dadRightOrLeft == 1: #Starts on the left
                dadXcor = -500
        if auntRightOrLeft == 0: #Starts on the right
                auntXcor = 500
                aunt.left(180)
        elif auntRightOrLeft == 1: #Starts on the left
                auntXcor = -500
        if baeRightOrLeft == 0: #Starts on the right
                baeXcor = 500
                bae.left(180)
        elif baeRightOrLeft == 1: #Starts on the left
                baeXcor = -500
        if broRightOrLeft == 0: #Starts on the right
                broXcor = 500
                bro.left(180)
        elif broRightOrLeft == 1: #Starts on the left
                broXcor = -500
        if coachRightOrLeft == 0: #Starts on the right
                coachXcor = 500
                coach.left(180)
        elif coachRightOrLeft == 1: #Starts on the left
                coachXcor = -500
        if dudeRightOrLeft == 0: #Starts on the right
                dudeXcor = 500
                dude.left(180)
        elif dudeRightOrLeft == 1: #Starts on the left
                dudeXcor = -500
        if grandmaRightOrLeft == 0: #Starts on the right
                grandmaXcor = 500
                grandma.left(180)
        elif grandmaRightOrLeft == 1: #Starts on the left
                grandmaXcor = -500
        if manRightOrLeft == 0: #Starts on the right
                manXcor = 500
                man.left(180)
        elif manRightOrLeft == 1: #Starts on the left
                manXcor = -500
        if sisRightOrLeft == 0: #Starts on the right
                sisXcor = 500
                sis.left(180)
        elif sisRightOrLeft == 1: #Starts on the left
                sisXcor = -500

        if friendAForBack == 0: #Starts on the top
                friendAYcor = 500
                friendA.right(90)
        elif friendAForBack == 1: #Starts on the bottom
                friendAYcor = -500
                friendA.left(90)
        if friendBForBack == 0: #Starts on the top
                friendBYcor = 500
                friendB.right(90)
        elif friendBForBack == 1: #Starts on the bottom
                friendBYcor = -500
                friendB.left(90)
        if friendCForBack == 0: #Starts on the top
                friendCYcor = 500
                friendC.right(90)
        elif friendCForBack == 1: #Starts on the bottom
                friendCYcor = -500
                friendC.left(90)
        if friendDForBack == 0: #Starts on the top
                friendDYcor = 500
                friendD.right(90)
        elif friendDForBack == 1: #Starts on the bottom
                friendDYcor = -500
                friendD.left(90)
        if friendEForBack == 0: #Starts on the top
                friendEYcor = 500
                friendE.right(90)
        elif friendEForBack == 1: #Starts on the bottom
                friendEYcor = -500
                friendE.left(90)
        if friendFForBack == 0: #Starts on the top
                friendFYcor = 500
                friendF.right(90)
        elif friendFForBack == 1: #Starts on the bottom
                friendFYcor = -500
                friendF.left(90)
        if friendGForBack == 0: #Starts on the top
                friendGYcor = 500
                friendG.right(90)
        elif friendGForBack == 1: #Starts on the bottom
                friendGYcor = -500
                friendG.left(90)
        if friendHForBack == 0: #Starts on the top
                friendHYcor = 500
                friendH.right(90)
        elif friendHForBack == 1: #Starts on the bottom
                friendHYcor = -500
                friendH.left(90)

        if candyAForBack == 0: #Starts on the top
                candyAYcor = 500
                candyA.right(90)
        elif candyAForBack == 1: #Starts on the bottom
                candyAYcor = -500
                candyA.left(90)
        if candyBForBack == 0: #Starts on the top
                candyBYcor = 500
                candyB.right(90)
        elif candyBForBack == 1: #Starts on the bottom
                candyBYcor = -500
                candyB.left(90)
        if candyCForBack == 0: #Starts on the top
                candyCYcor = 500
                candyC.right(90)
        elif candyCForBack == 1: #Starts on the bottom
                candyCYcor = -500
                candyC.left(90)

        if candyDRightOrLeft == 0: #Starts on the right
                candyDXcor = 500
                candyD.left(180)
        elif candyDRightOrLeft == 1: #Starts on the left
                candyDXcor = -500
        if candyERightOrLeft == 0: #Starts on the right
                candyEXcor = 500
                candyE.left(180)
        elif candyERightOrLeft == 1: #Starts on the left
                candyEXcor = -500
        
        
        mom.speed(200)
        mom.goto(momXcor, momYcor)
        mom.st()
        dad.speed(200)
        dad.goto(dadXcor, dadYcor)
        dad.st()
        aunt.speed(200)
        aunt.goto(auntXcor, auntYcor)
        aunt.st()
        bae.speed(200)
        bae.goto(baeXcor, baeYcor)
        bae.st()
        bro.speed(200)
        bro.goto(broXcor, broYcor)
        bro.st()
        coach.speed(200)
        coach.goto(coachXcor, coachYcor)
        coach.st()
        dude.speed(200)
        dude.goto(dudeXcor, dudeYcor)
        dude.st()
        grandma.speed(200)
        grandma.goto(grandmaXcor, grandmaYcor)
        grandma.st()
        man.speed(200)
        man.goto(manXcor, manYcor)
        man.st()
        sis.speed(200)
        sis.goto(sisXcor, sisYcor)
        sis.st()

        friendA.speed(200)
        friendA.goto(friendAXcor, friendAYcor)
        friendA.st()
        friendB.speed(200)
        friendB.goto(friendBXcor, friendBYcor)
        friendB.st()
        friendC.speed(200)
        friendC.goto(friendCXcor, friendCYcor)
        friendC.st()
        friendD.speed(200)
        friendD.goto(friendDXcor, friendDYcor)
        friendD.st()
        
        friendE.speed(200)
        friendE.goto(friendEXcor, friendEYcor)
        friendE.st()
        friendF.speed(200)
        friendF.goto(friendFXcor, friendFYcor)
        friendF.st()
        friendG.speed(200)
        friendG.goto(friendGXcor, friendGYcor)
        friendG.st()
        friendH.speed(200)
        friendH.goto(friendHXcor, friendHYcor)
        friendH.st()

        candyA.speed(200)
        candyA.goto(candyAXcor, candyAYcor)
        candyA.st()
        candyB.speed(200)
        candyB.goto(candyBXcor, candyBYcor)
        candyB.st()
        candyC.speed(200)
        candyC.goto(candyCXcor, candyCYcor)
        candyC.st()
        candyD.speed(200)
        candyD.goto(candyDXcor, candyDYcor)
        candyD.st()
        candyE.speed(200)
        candyE.goto(candyEXcor, candyEYcor)
        candyE.st()

        momDistance = 0
        dadDistance = 0
        auntDistance = 0
        baeDistance = 0
        broDistance = 0
        coachDistance = 0
        dudeDistance = 0
        grandmaDistance = 0
        manDistance = 0
        sisDistance = 0

        friendADistance = 0
        friendBDistance = 0
        friendCDistance = 0
        friendDDistance = 0
        friendEDistance = 0
        friendFDistance = 0
        friendGDistance = 0
        friendHDistance = 0


        candyADistance = 0
        candyBDistance = 0
        candyCDistance = 0
        candyDDistance = 0
        candyEDistance = 0

        done = False
        
        while done == False:
                x = albert.xcor()
                y = albert.ycor()

                        # Collisions with the characters = game over
                if distance(x, mom.xcor(), y, mom.ycor()) <= 8 and mom.isvisible() == True:
                        hideTurtles()
                if distance(x, dad.xcor(), y, dad.ycor()) <= 8  and dad.isvisible() == True:
                        hideTurtles()
                if distance(x, sis.xcor(), y, sis.ycor()) <= 8  and sis.isvisible() == True:
                        hideTurtles()
                if distance(x, bro.xcor(), y, bro.ycor()) <= 8  and bro.isvisible() == True:
                        hideTurtles()
                if distance(x, grandpa.xcor(), y, grandpa.ycor()) <= 8 and grandpa.isvisible() == True:
                        hideTurtles()
                if distance(x, grandma.xcor(), y, grandma.ycor()) <= 8 and grandma.isvisible() == True:
                        hideTurtles()
                if distance(x, coach.xcor(), y, coach.ycor()) <= 8 and coach.isvisible() == True:
                        hideTurtles()
                if distance(x, aunt.xcor(), y, aunt.ycor()) <= 8 and aunt.isvisible() == True:
                        hideTurtles()
                if distance(x, bae.xcor(), y, bae.ycor()) <= 8 and bae.isvisible() == True:
                        hideTurtles()
                if distance(x, man.xcor(), y, man.ycor()) <= 8 and man.isvisible() == True:
                        hideTurtles()
                if distance(x, uncle.xcor(), y, uncle.ycor()) <= 8 and uncle.isvisible() == True:
                        hideTurtles()
                if distance(x, dude.xcor(), y, dude.ycor()) <= 8 and dude.isvisible() == True:
                        hideTurtles()
                if distance(x, friendA.xcor(), y, friendA.ycor()) <= 8 and friendA.isvisible() == True:
                        hideTurtles()
                if distance(x, friendB.xcor(), y, friendB.ycor()) <= 8 and friendB.isvisible() == True:
                        hideTurtles()
                if distance(x, friendC.xcor(), y, friendC.ycor()) <= 8 and friendC.isvisible() == True:
                        hideTurtles()
                if distance(x, friendD.xcor(), y, friendD.ycor()) <= 8 and friendD.isvisible() == True:
                        hideTurtles()
                if distance(x, friendE.xcor(), y, friendE.ycor()) <= 8 and friendE.isvisible() == True:
                        hideTurtles()
                if distance(x, friendF.xcor(), y, friendF.ycor()) <= 8 and friendF.isvisible() == True:
                        hideTurtles()
                if distance(x, friendG.xcor(), y, friendG.ycor()) <= 8 and friendG.isvisible() == True:
                        hideTurtles()
                if distance(x, friendH.xcor(), y, friendH.ycor()) <= 8 and friendH.isvisible() == True:
                        hideTurtles()

                # Collisions with the sweets = gain a point for each candy scored
                randomSpot = random.randrange(-440,440)
                global score
                if distance(x, candyA.xcor(), y, candyA.ycor()) <= 8 and candyA.isvisible() == True:
                        #print ("candyA")
                        myPen.undo()
                        candyA.hideturtle()
                        score += 1
                        candyA.goto(randomSpot, randomSpot)
                        candyA.showturtle()
                        os.system("afplay doodoo.mp3&")
                        myPen.goto(350,370)
                        myPen.write("Score: " + str(score), align="left", font=("Arial", 30, "normal"))

                if distance(x, candyB.xcor(), y, candyB.ycor()) <= 8 and candyB.isvisible() == True:
                        #print ("candyB")
                        myPen.undo()
                        candyB.hideturtle()
                        score += 1
                        candyB.goto(randomSpot, randomSpot)
                        candyB.showturtle()
                        os.system("afplay doodoo.mp3&")
                        myPen.goto(350,370)
                        myPen.write("Score: " + str(score), align="left", font=("Arial", 30, "normal"))

                if distance(x, candyC.xcor(), y, candyC.ycor()) <= 8 and candyC.isvisible() == True:
                        #print ("candyC")
                        myPen.undo()
                        candyC.hideturtle()
                        score += 1
                        myPen.goto(350,370)
                        myPen.write("Score: " + str(score), align="left", font=("Arial", 30, "normal"))
                        candyC.goto(randomSpot, randomSpot)
                        candyC.showturtle()
                        os.system("afplay doodoo.mp3&")

                if distance(x, candyD.xcor(), y, candyD.ycor()) <= 8 and candyD.isvisible() == True:
                        #print ("candyD")
                        myPen.undo()
                        candyD.hideturtle()
                        score += 1
                        myPen.goto(350,370)
                        myPen.write("Score: " + str(score), align="left", font=("Arial", 30, "normal"))
                        candyD.goto(randomSpot, randomSpot)
                        candyD.showturtle()
                        os.system("afplay doodoo.mp3&")

                if distance(x, candyE.xcor(), y, candyE.ycor()) <= 8 and candyE.isvisible() == True:
                        #print ("candyE")
                        myPen.undo()
                        candyE.hideturtle()
                        score += 1
                        candyE.goto(-500,500)
                        candyE.showturtle()
                        os.system("afplay doodoo.mp3&")
                        myPen.goto(350,370)
                        myPen.write("Score: " + str(score), align="left", font=("Arial", 30, "normal"))
                        
                if momDistance <= 1000:
                        mom.forward(momForward)
                        momDistance += momForward
                else:
                        mom.ht()
                if dadDistance <= 1000:
                        dad.forward(dadForward)
                        dadDistance += dadForward
                else:
                        dad.ht()
                if auntDistance <= 1000:
                        aunt.forward(auntForward)
                        auntDistance += auntForward
                else:
                        aunt.ht() 
                if baeDistance <= 1000:
                        bae.forward(baeForward)
                        baeDistance += baeForward
                else:
                        bae.ht()
                if broDistance <= 1000:
                        bro.forward(broForward)
                        broDistance += broForward 
                else:
                        bro.ht()
                if coachDistance <= 1000:
                        coach.forward(coachForward)
                        coachDistance += coachForward
                else:
                        coach.ht()
                if dudeDistance <= 1000:
                        dude.forward(dudeForward)
                        dudeDistance += dudeForward
                else:
                        dude.ht()
                if grandmaDistance <= 1000:
                        grandma.forward(grandmaForward)
                        grandmaDistance += grandmaForward
                else:
                        grandma.ht()
                if manDistance <= 1000:
                        man.forward(manForward)
                        manDistance += manForward 
                else:
                        man.ht()
                if sisDistance <= 1000:
                        sis.forward(sisForward)
                        sisDistance += sisForward
                else:
                        sis.ht()
                if friendADistance <= 1000:
                        friendA.forward(friendAForward)
                        friendADistance += friendAForward
                else:
                        friendA.ht()
                if friendBDistance <= 1000:
                        friendB.forward(friendBForward)
                        friendBDistance += friendBForward
                else:
                        friendB.ht()
                if friendCDistance <= 1000:
                        friendC.forward(friendCForward)
                        friendCDistance += friendCForward
                else:
                        friendC.ht()
                if friendDDistance <= 1000:
                        friendD.forward(friendDForward)
                        friendDDistance += friendDForward
                else:
                        friendD.ht()
                if friendEDistance <= 1000:
                        friendE.forward(friendEForward)
                        friendEDistance += friendEForward
                else:
                        friendE.ht()
                if friendFDistance <= 1000:
                        friendF.forward(friendFForward)
                        friendFDistance += friendFForward
                else:
                        friendF.ht()
                if friendGDistance <= 1000:
                        friendG.forward(friendGForward)
                        friendGDistance += friendGForward
                else:
                        friendG.ht()
                if friendHDistance <= 1000:
                        friendH.forward(friendHForward)
                        friendHDistance += friendHForward
                else:
                        friendH.ht()

                if candyADistance <= 1000:
                        candyA.forward(candyAForward)
                        candyADistance += candyAForward
                else:
                        candyA.ht()
                if candyBDistance <= 1000:
                        candyB.forward(candyBForward)
                        candyBDistance += candyBForward
                else:
                        candyB.ht()
                if candyCDistance <= 1000:
                        candyC.forward(candyCForward)
                        candyCDistance += candyCForward
                else:
                        candyC.ht()
                if candyDDistance <= 1000:
                        candyD.forward(candyDForward)
                        candyDDistance += candyDForward
                else:
                        candyD.ht()
                if candyEDistance <= 1000:
                        candyE.forward(candyEForward)
                        candyEDistance += candyEForward
                else:
                        candyE.ht()

                if momDistance > 1000 and dadDistance > 1000 and \
                auntDistance > 1000 and baeDistance > 1000 and \
                broDistance > 1000 and coachDistance > 1000 and \
                dudeDistance > 1000 and grandmaDistance > 1000 and \
                manDistance > 1000 and sisDistance > 1000 and \
                friendADistance > 1000 and friendBDistance > 1000 and \
                friendCDistance > 1000 and friendDDistance > 1000 and \
                friendEDistance > 1000 and \
                friendFDistance > 1000 and friendGDistance > 1000 and \
                friendHDistance > 1000:
                        done = True

                        mom.reset()
                        mom.ht()
                        dad.reset()
                        dad.ht()
                        aunt.reset()
                        aunt.ht()
                        bae.reset()
                        bae.ht()
                        bro.reset()
                        bro.ht()
                        coach.reset()
                        coach.ht()
                        dude.reset()
                        dude.ht()
                        grandma.reset()
                        grandma.ht()
                        man.reset()
                        man.ht()
                        sis.reset()
                        sis.ht()
                        friendA.reset()
                        friendA.ht()
                        friendB.reset()
                        friendB.ht()
                        friendC.reset()
                        friendC.ht()
                        friendD.reset()
                        friendD.ht()
                        friendE.reset()
                        friendE.ht()
                        friendF.reset()
                        friendF.ht()
                        friendG.reset()
                        friendG.ht()
                        friendH.reset()
                        friendH.ht()
                        candyA.reset()
                        candyA.ht()
                        candyB.reset()
                        candyB.ht()
                        candyC.reset()
                        candyC.ht()
                        candyD.reset()
                        candyD.ht()
                        candyE.reset()
                        candyE.ht()
                        mom.penup()
                        dad.penup()
                        aunt.penup()
                        bae.penup()
                        bro.penup()
                        coach.penup()
                        dude.penup()
                        grandma.penup()
                        man.penup()
                        sis.penup()
                        friendA.penup()
                        friendB.penup()
                        friendC.penup()
                        friendD.penup()
                        friendE.penup()
                        friendF.penup()
                        friendG.penup()
                        friendH.penup()
                        candyA.penup()
                        candyB.penup()
                        candyC.penup()
                        candyD.penup()
                        candyE.penup()

                        
def main():
    window.bgpic("background.gif")
    done = False
    while done == False:
            movement()

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(forward, "Up")
turtle.onkey(backward, "Down")
turtle.onkey(main, "a")

#main()

while True:
        albert.forward(0) #Draw turtle, but not so that it moves.



