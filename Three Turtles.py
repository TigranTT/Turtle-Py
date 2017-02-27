import turtle

def draw_quad(some_turtle):
    for i in range (0,4):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("lightblue")

    art=turtle.Turtle()
    art.color("yellow")
    art.speed(15)
    for i in range (0,72):
        draw_quad(art)
        art.right(5)

def draw_square():
    window=turtle.Screen()
    window.bgcolor("lightblue")
    
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.shapesize(1,1,2)
    brad.color("blue","yellow")
    brad.speed(15)
    
    i=0
    while (i<90):
        brad.forward(200)
        brad.right(90)
        brad.right(5)
        i+=1

    bob=turtle.Turtle()
    bob.shape("arrow")
    bob.shapesize(1,2)
    bob.color("red","yellow")
    bob.speed(15)
    bob.left(300)

    i=0
    while(i<90):
        bob.right(120)
        bob.forward(241)
        bob.right(5)
        i+=1
    
    bond=turtle.Turtle()
    bond.shape("circle")
    bond.color("darkgreen","yellow")
    bond.speed(15)
    i=0
    while(i<90):
        bond.circle(141)
        bond.right(5)
        i+=1

    window.exitonclick()



draw_art()
draw_square()
