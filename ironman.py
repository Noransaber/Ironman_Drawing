#Import turtul
import turtle
face_one = [
  [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),(-40, -20), (0, -20)],

  [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),(40, 120), (0, 120)]
]

face_two = [
  [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),(-80, -230), (-64, -210), (0, -210)],
  
  [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),(100, -46), (50, -40), (40, -30), (0, -30)]
]

face_three = [
  [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),(0, -250)],
  
  [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),(0,-220)]
]
#start using tutle, hide tutle
turtle.hideturtle()

#Change the background color
turtle.bgcolor('#ba161e')

#Determin the width and height of the screen
turtle.setup(500, 600)

#Start point
face_one_start = (0, 120)
face_two_start = (0, -30)
face_three_start = (0, -220)

#Spead
turtle.speed(1)

#Function to draw
def draw_face(face_list, start_point):
  #Move the pen up
  turtle.penup()
  #move the pen to the point where we will start drawing
  turtle.goto(start_point)
  #Set the pen down
  turtle.pendown()
  #The pen color
  turtle.color('#fab104', '#fab104')
  #Start drwaing
  turtle.begin_fill()

  for i in range(len(face_list[0])):
    x, y = face_list[0][i]
    turtle.goto(x, y)

  for i in range(len(face_list[1])):
    x, y = face_list[1][i]
    turtle.goto(x, y)
  turtle.end_fill()
  

#calling the function
draw_face(face_one, face_one_start)
draw_face(face_two, face_two_start)
draw_face(face_three, face_three_start)