import turtle
t = turtle.Turtle()



t.hideturtle()
t.color('black', 'coral')
t.begin_fill()

for _ in range(4):
  t.forward(200) 
  t.left(90) 
t.end_fill()



t.up()
t.goto(-125, 0)
t.down()




t.color('black', 'chartreuse')
t.begin_fill()


t.forward(120) 
t.left(90) 
t.forward(90) 
t.left(90) 
t.forward(120)
t.left(90) 
t.forward(90)   
t.left(90) 
t.end_fill()




t.up()
t.goto(0, -95)      
t.down()


t.color('black', 'white')
t.begin_fill()

t.forward(200) 
t.left(90) 
t.forward(90)
t.left(90)
t.forward(200)
t.left(90) 
t.forward(90)

t.end_fill()


t.up()
t.goto(-125, 305)      
t.down()


t.color('black', 'white')
t.begin_fill()

t.forward(210) 
t.left(90) 
t.forward(120)
t.left(90) 
t.forward(210)
t.left(90) 
t.forward(120)

t.end_fill()

t.up()
t.goto(360, 305)      
t.down()

t.color('black', 'MediumPurple')
t.begin_fill()

t.forward(360) 
t.left(90) 
t.forward(100)
t.left(90) 
t.forward(360)
t.left(90) 
t.forward(100)

t.end_fill()

t.up()
t.goto(360, -95)      
t.down()

t.color('black', 'chartreuse')
t.begin_fill()

t.forward(295) 
t.left(90) 
t.forward(155)
t.left(90) 
t.forward(295)
t.left(90) 
t.forward(155)

t.end_fill()

t.up()
t.goto(-125, -95)      
t.down()

t.color('black', 'MediumPurple')
t.begin_fill()

t.forward(120) 
t.left(90) 
t.forward(90)
t.left(90) 
t.forward(120)
t.left(90)
t.forward(90)

t.end_fill()








turtle.exitonclick()
