
import turtle

pen = turtle.Turtle()
pen.hideturtle()
window = turtle.Screen()
window.setup(width = 800, height = 1000, startx = 550, starty = 0)
pen.speed(0)


def Grid():
    pen.pensize(2.5)
    #Writing the Title
    pen.color("black")
    pen.penup()
    pen.goto(0,300)
    pen.pendown()
    pen.write("Connect 4", align = "center", font=(("Arial"),30, "bold", "underline"))
    pen.penup()
    pen.goto(355,-330)
    pen.pendown()
    pen.color("#99a7b2")
    pen.write("By Richard Burgin", align = "left",font=(("Calibri"), 11,"bold"))
    pen.color("black")
    pen.penup()
    pen.goto(-350,270)
    pen.pendown()

    #Writing the Column numbers
    for i in range(0,7):
        pen.goto(-300+(i*100),270)
        pen.write(i+1, align = "left", font=(("Arial"),10, "bold"))
        
    #Drawing the Grid
    for i in range(0,8):
        pen.goto(-350+(i*100),270)
        pen.goto(-350+(i*100),-330)
        pen.goto(-350+(i*100),270)
    for i in range(0,6):
        pen.goto(350,-330+(i*100))
        pen.goto(-350,-330+(i*100))
        pen.goto(350,-330+(i*100))

def Turns(turn):
    pen.pensize(20)
    pen.color("white")
    for i in range(0,2):
        pen.penup()
        pen.goto(150-(i*300),300)
        pen.pendown()
        if i == 0:
            pen.goto(150-(i*300)+125,300)
        else:
            pen.goto(150-(i*300)-125,300)
    #Turn Title Statment
    if turn == "X" :
        pen.color("Red")
    else:
        pen.color("Blue")
    pen.pensize(2.5)
    for i in range(0,2):
        pen.penup()
        pen.goto(150-(i*300),290)
        pen.pendown()
        if i == 0:
            if turn == "X" :
                pen.write("RED's Turn", align = "left", font=(("Arial"),15, "bold"))
            else:
                pen.write("BLUE's Turn", align = "left", font=(("Arial"),15, "bold"))
            
        else:
            if turn == "X" :
                pen.write("RED's Turn", align = "right", font=(("Arial"),15, "bold"))
            else:
                pen.write("BLUE's Turn", align = "right", font=(("Arial"),15, "bold"))  

def Move(cooX,cooY):
    pen.pensize(95)
    pen.penup()
    #Translating the coordinates and Plotting the point
    if cooX < 4:
        if cooX == 2:
            pen.goto(-200,220-(cooY*100))
            pen.pendown()
            pen.goto(-201,220-(cooY*100))
        else:
            pen.goto(0-(1/cooX)*300,220-(cooY*100))
            pen.pendown()
            pen.goto((0-(1/cooX)*300)+1,220-(cooY*100))
    elif cooX > 4:
        pen.goto(0+(cooX-4)*100,220-(cooY*100))
        pen.pendown()
        pen.goto((0+(cooX-4)*100)+1,220-(cooY*100))
    else:
        pen.goto(0,220-(cooY*100))
        pen.pendown()
        pen.goto(1,220-(cooY*100))

def win(player):
    pen.pensize(90)
    pen.color("white")
    pen.penup()
    pen.goto(-250,330)
    pen.pendown()
    pen.goto(250,330)
    pen.penup()
    pen.goto(0,300)
    if player == "BLUE":           
        pen.color("Blue")
        pen.write("BLUE WINS!!", align = "center", font=(("Arial"),50, "bold"))
    elif player == "RED":
        pen.color("Red")
        pen.write("RED WINS!!", align = "center", font=(("Arial"),50, "bold"))
    else:
        pen.color("black")
        pen.write("NOBODY WINS!!", align = "center", font=(("Arial"),50, "bold"))

        
    
    
