import turtle

def test():

    t = turtle.Turtle()
    t.shape("turtle",)
    t.color("yellow")
    t.speed(20)
    t.begin_fill()
    
    moves = 0

    while moves < 36: #y 36 ??
        t.forward(200)
        t.left(170)
      
        moves = moves + 1
    t.end_fill()
    draw_circle()
    t.up()
    t.goto(100,-50)
    t.down()
    t.right(90)
    t.color("green")
    t.forward(200)
    
    

    
    
def draw_circle():
    tc = turtle.Turtle()
    tc.shape("turtle",)
    tc.color("brown")
    tc.speed(20)
    tc.begin_fill()
    tc.up()
    tc.goto(100,10)
    tc.down()
   
    movesc = 0
    while movesc < 360/10:
        tc.forward(2)
        tc.right(10)
        movesc = movesc + 1
    tc.end_fill()
    




    
def draw_shapes():
    window = turtle.Screen()
    #window.bgcolor("red")

    test()

    window.exitonclick()


draw_shapes()
