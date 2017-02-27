import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor("lightblue")
    
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.shapesize(2,2,4)
    brad.color("blue","yellow")
    brad.speed(3)
    
    i=1
    while (i<3):
        brad.forward(200)
        brad.right(90)
        i+=1
    brad.forward(400)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(400)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(400)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(45)
    brad.forward(283)
    brad.right(90)
    brad.forward(283)
    brad.right(90)
    brad.forward(283)
    brad.right(90)
    brad.forward(283)
    brad.right(180)
    brad.forward(141.5)
    brad.circle(141.5)
    
    

    window.exitonclick()

draw_square()
