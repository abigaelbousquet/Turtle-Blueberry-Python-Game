######
# This program will generate a game where the user can use their mouse, arrow keys, and their "g" key to move
# blueberries to a turtle in order to "feed" it. Successfully feeding the blueberries to the turtle will
# increase their score by 1 each time.
#####
# the blueberries image named blueberries.gif is from clipart-library.com
# the turtle image named turtle.gif is from clipartbay.com
#####

# import statements
import turtle as trtl
import random as rand

# import images
turtle_image = "turtle.gif"
berry_image = "blueberries.gif"

# set up screen
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

# add shapes to program
wn.addshape(turtle_image)
wn.addshape(berry_image)

# set up turtle
turtle = trtl.Turtle()
turtle.hideturtle()
turtle.penup()
turtle.goto(-250, 0)
turtle.shape(turtle_image)
turtle.showturtle()

# set up directions writer turtle
directions_writer = trtl.Turtle()
directions_writer.hideturtle()
directions_writer.penup()
directions_writer.goto(-400, 250)
directions_writer.pendown()
directions_writer.color("black")

# set up score writer turtle
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-400, -250)
score_writer.pendown()

# variables
score = 0 # initial score

# lists
berries = []
bb_x_values = []
bb_y_values = []

##### FUNCTIONS #####
def print_directions():
  directions_writer.write("Click on a blueberry to select it. (It may take several tries to get the right berry to respond.)" + "\n" + "Use your arrow keys to change its direction, as well as the 'g' key to move it forward." + "\n" + "Move the blueberries to the turtle's mouth to feed it and earn points!", font=("Arial", 15))

def update_score(new_score):
  score_writer.clear()
  score_writer.write(("Score: " + str(score)), font=("Arial", 20, "bold"))

def new_berry(x, y):
  # create the new berry and send it to its random coordinates
  berry = trtl.Turtle()
  berry.shape(berry_image)
  berry.penup()
  berry.goto(x, y)
  berry.setheading(-180) # set initial heading facing the turtle

  # add newly created berry and its x and y values to the corresponding lists
  berries.append(berry)
  bb_x_values.append(x)
  bb_y_values.append(y)

# remove berry & its x/y coordinates from the corresponding lists once it reaches the turtle's mouth 
def remove_berry():
  berries[active_berry_index].hideturtle() # make berry disappear from screen
  berries.pop(active_berry_index)
  bb_x_values.pop(active_berry_index)
  bb_y_values.pop(active_berry_index)

# respond to arrow keys being pressed
def up_pressed():
  berries[active_berry_index].setheading(90)

def down_pressed():
  berries[active_berry_index].setheading(-90)

def right_pressed():
  berries[active_berry_index].setheading(0)

def left_pressed():
  berries[active_berry_index].setheading(180)

# respond to "g" key being pressed
def move_berry():
  berries[active_berry_index].forward(10)
  x_position_abs_dif = abs(-200 + (berries[active_berry_index].xcor()))
  y_position_abs_dif = abs(0 - (berries[active_berry_index].ycor()))
  if ((x_position_abs_dif <= 410) and (x_position_abs_dif >= 390)) and (y_position_abs_dif <= 10):
    global score
    score = score + 1
    update_score(score)
    remove_berry()

# figure out which berry turtle should be the active berry based on the user's click
def berry_clicked(x, y):
  global active_berry_index
  index = 0 # start index at 0 to start at beginning of berries list

  for i in berries:
    if abs(x - (bb_x_values[index]) <= 5) and abs(y - (bb_y_values[index]) <= 5):
      active_berry_index = index

    # update index variable for next iteration
    index = index + 1

##### FUNCTION CALLS #####
print_directions()
update_score(score)

# create the 5 blueberries at random locations
for i in range(0, 5):
  global new_x
  new_x = rand.randint(-200, 400)
  global new_y
  new_y = rand.randint(-200, 200)

  new_berry(new_x, new_y)

# call the berry_clicked function when the user clicks the screen (hopefully clicking a berry)
wn.onscreenclick(berry_clicked)

# listen for & respond to key presses
wn.onkeypress(up_pressed, "Up")
wn.onkeypress(down_pressed, "Down")
wn.onkeypress(right_pressed, "Right")
wn.onkeypress(left_pressed, "Left")
wn.onkeypress(move_berry, "g")

wn.listen()


wn.mainloop()
