"""
This program creates a flower design using the turtle module in python.
"""



import turtle
def square(turtle_name, length):
	"""This is just for practice, creates a square"""
	for i in range(4):
		turtle_name.forward(length)
		turtle_name.left(90)

def polygon(turtle_name, n, length):
	"""This creates a polygon"""
	angle=360/n
	for i in range(n):
		turtle_name.forward(length)
		turtle_name.left(angle)

def circle(turtle_name, r):
	"""Next logical step is to practice creating a cirlcle"""
	circum = 2*3.14159*r
	n = int(circum / 3) + 3
	length = circum / n
	polygon(turtle_name,n,length)


def arc(turtle_name, r, angle, color):
	"""A very important function uses the logic learnt in circle function"""
	arc_length = 2 * 3.14159 * r * (angle/360)
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = angle / n

	turtle_name.color('black', color)
	turtle_name.begin_fill()
	
	for i in range(n):
		turtle_name.forward(step_length)
		turtle_name.left(step_angle)
	
	turtle_name.end_fill()

def petal(turtle_name, r, angle, color):
	"""Create a single petal"""
	for i in range(2):
		arc(turtle_name, r, angle, color)
		turtle_name.left(180-angle)

def flower(turtle_name, n, r, angle, color):
	"""Create a flower design using n number of petals"""
	for i in range(n):
		petal(turtle_name, r, angle, color)
		turtle_name.left(360/n)

def stick(turtle_name, angle):
	"""Added this feature using the petal logic only. Can be improved to look more like a stick"""
	turtle_name.left(270)
	arc(turtle_name, 1000, angle, 'brown')
	turtle_name.left(180-angle)
	arc(turtle_name, 1000, angle, 'brown')




color1 = 'red' #inner color
color2 = 'yellow' #outer color

my_turtle = turtle.Turtle()


#Test polygon
#my_turtle2 = turtle.Turtle()
#polygon(my_turtle2, 6, 50)


#Test Square
#my_turtle3 = turtle.Turtle()
#square(my_turtle3, 100)


#Test circle
#my_turtle4 = turtle.Turtle()
#circle(my_turtle4, 100)

#Test arc
#my_turtle5 = turtle.Turtle()
#arc(my_turtle5, 100, 90)

#Test Petal
#my_turtle6 = turtle.Turtle()
#petal(my_turtle6, 300, 45)






#The following will create a normal sized flower design with stick
stick(my_turtle, 20)
flower(my_turtle, 9, 150, 45, color2)
flower(my_turtle, 9, 100, 45, color1)


#The following will create a huge flower with 50 petals in yellow followed by 50 smaller petals in red
#flower(my_turtle, 50, 1000, 20, color2)
#flower(my_turtle, 50, 750, 20, color1)



turtle.mainloop()


