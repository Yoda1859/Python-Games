""" Turtle in Pygame

We really miss the turtle module from Python's standard library. It was a great
way to introduce programming, so let's make something similar in PyGame, using
objects. 

This program is for assignment 3 and 4

Assignment 3:

1. Read and run the program `01_Tom_the_Turtle.py` in this lession directory.
2. Create a derived class from the `Turtle` class that adds some new behavior.
   Add a function `right` that turns the turtle to the right. ( Bonus, use the
   `left` function to implement the `right` function )
3. In your derived class, add a new variable `color` and a way to set it. Use
   that color to set the color of the turtle's line
4. Add a `pen_up` and `pen_down` function that will raise and lower the pen.

Assignment 4:

1. Create a function ( not a method, the function should not be part of a class) 
   in your `01_Tom_the_Turtle` program that takes a Turtle object and prints
   out the x and y position of the turtle.
2. Show that your function works by creating a turtle, moving it around, and
   then calling your function, for both the base `Turtle` class and your derived
   class.

"""
import math
import pygame

def event_loop():
    """Wait until user closes the window"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

class Turtle:
    def __init__(self, screen, x: int, y: int):
        self.x = x
        self.y = y
        self.screen = screen
        self.angle = 0  # Angle in degrees, starting facing right
        self.color = 'black'

    def forward(self, distance):
        # Calculate new position based on current angle
        radian_angle = math.radians(self.angle)

        start_x = self.x  # Save the starting position
        start_y = self.y

        # Calculate the new position displacement
        dx = math.cos(radian_angle) * distance
        dy = math.sin(radian_angle) * distance

        # Update the turtle's position
        self.x += dx
        self.y -= dy

        # Draw line to the new position
        pygame.draw.line(self.screen, self.color, (start_x, start_y), (self.x, self.y), 2)

    def left(self, angle):
        # Turn left by adjusting the angle counterclockwise
        self.angle = (self.angle + angle) % 360

    def pencolor(self, color):
        self.color = color

    def pen_up(self, distance):
        radian_angle = math.radians(self.angle)
        dx = math.cos(radian_angle) * distance
        dy = math.sin(radian_angle) * distance
        self.x += dx
        self.y -= dy

    def print_location(self):
        print(self.y, self.x)

class Little_Turtle(Turtle):
    def __init__(self, screen, x: int, y: int):
        self.x = x
        self.y = y
        self.screen = screen
        self.angle = 0  # Angle in degrees, starting facing right
        self.color = 'black'

    def right(self, angle):
        self.angle = (self.angle - angle) % 360

# Main loop

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Turtle Style Drawing")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 120, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
pink = (255, 120, 120)

screen.fill(white)
turtle = Turtle(screen, screen.get_width() // 2, screen.get_height() // 2)  # Start at the center of the screen
little_turtle = Little_Turtle(screen, screen.get_width() // 2, screen.get_height() // 2)  # Start at the center of the screen

# Draw a square using turtle-style commands
for _ in range(120):
    little_turtle.pencolor('orange')
    little_turtle.forward(25)
    little_turtle.left(22)
    little_turtle.right(3)
    little_turtle.pencolor('yellow')
    little_turtle.forward(100)
    little_turtle.left(90)
    little_turtle.right(3)
    little_turtle.pencolor('red')
    little_turtle.forward(50)
    little_turtle.left(45)
    little_turtle.right(3)

little_turtle.print_location()

# Display the drawing
pygame.display.flip()

# Wait to quit
event_loop()

# Quit Pygame
pygame.quit()
