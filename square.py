import turtle

def draw_circle():
    print("printing circle")
    #time.sleep(10)
    
    cir = turtle.Turtle()
    cir.speed(2)
    cir.shape("turtle")
    cir.color("green")
    
    cir.circle(100)

    
def draw_square():
    print("printing square")
    #time.sleep(10)

    moves = 0
    countsq = 0
    angle = 10
    sqTr = turtle.Turtle()
    sqTr.speed(10)
    sqTr.shape("turtle")
    sqTr.color("green")
    
    while countsq < 360/10:
        while moves < 4:
            sqTr.forward(100)
            sqTr.right(90)
            moves = moves + 1
        countsq = countsq + 1
        #print("Square number: " + repr(countsq))
        moves = 0
        sqTr.right(angle)
        
            


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    #draw_circle()
    draw_square()

    window.exitonclick()

    
draw_shapes()
