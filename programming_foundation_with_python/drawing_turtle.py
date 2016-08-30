# drawing squares

import turtle
def setup():
	myTurtle= turtle.Turtle()
	myTurtle.shape('turtle')
	myTurtle.shapesize(2,2)
	myTurtle.color('blue')
	myTurtle.speed(10)
	return myTurtle

def draw_turtle(myTurtle):
	for i in range(4):
		myTurtle.forward(100)
		myTurtle.right(120)
		myTurtle.left(20)
		++i

	return myTurtle

window = turtle.Screen()
window.setup(width=750, height=500, startx=590, starty=300)


thisGuy = setup()
for i in range (40):
	draw_turtle(thisGuy)
	thisGuy.right(5)

turtle.getscreen()._root.mainloop()