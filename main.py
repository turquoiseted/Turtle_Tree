# Challenge using turtle to create a tree using recursion #
import turtle
import random


def draw_trunk(tree_turtle):
    tree_turtle.back(10)
    for x in range(2):
        tree_turtle.pensize(10 - x*2)
        tree_turtle.left(90)
        tree_turtle.forward(15 - x*2)
        tree_turtle.back(30 - x*4)
        tree_turtle.forward(15 - x*2)
        tree_turtle.right(90)
        tree_turtle.forward(5)

    tree_turtle.pensize(20)
    tree_turtle.forward(10)

    tree_turtle.pensize(18)
    tree_turtle.forward(30)

    tree_turtle.pensize(14)
    tree_turtle.forward(60)
    tree_turtle.pensize(10)
    tree_turtle.forward(20)

    tree_turtle.pensize(8)
    tree_turtle.forward(120)


def curve_branch(tree_turtle, length):
    full_length = length
    while full_length > 0:
        test = random.randint(0, 1)
        if test == 0:
            tree_turtle.right(2)
        else:
            tree_turtle.left(2)
        tree_turtle.forward(10)
        full_length -= 10


def draw_tree(tree_turtle):

    # Start tree at the bottom of the screen
    tree_turtle.penup()
    tree_turtle.setpos(0, -240)
    tree_turtle.pendown()
    # Set turtle facing upwards
    tree_turtle.left(90)

    draw_trunk(tree_turtle)

    draw_branches(100, 7, tree_turtle)
    # Stop window from closing
    turtle.done()


def draw_branches(length, depth, tree_turtle):
    if depth == 0:
        # Define leaf colour
        red = random.randint(30, 150)
        green = random.randint(170, 230)
        blue = random.randint(30, 150)

        tree_turtle.color("black", (red, green, blue))
        tree_turtle.begin_fill()
        circle_size = random.randint(5,10)
        tree_turtle.circle(circle_size)
        tree_turtle.end_fill()

    else:
        depth -= 1
        tree_turtle.pensize(depth)
        branches = random.randint(0,1)

        # Take current position and angle
        position = tree_turtle.pos()
        angle = tree_turtle.heading()

        # branch left
        tree_turtle.left(40)
        curve_branch(tree_turtle, length)
        draw_branches(length*(2/3), depth, tree_turtle)

        tree_turtle.penup()
        tree_turtle.setpos(position)
        tree_turtle.setheading(angle)
        tree_turtle.pendown()

        if branches == 1:
            # branch forward
            tree_turtle.pensize(depth)
            curve_branch(tree_turtle, length)
            draw_branches(length*(2/3), depth, tree_turtle)

            tree_turtle.penup()
            tree_turtle.setpos(position)
            tree_turtle.setheading(angle)
            tree_turtle.pendown()

        # branch right
        tree_turtle.pensize(depth)
        tree_turtle.right(40)
        curve_branch(tree_turtle, length)
        draw_branches(length*(2/3), depth, tree_turtle)


my_turtle = turtle.Turtle()
my_turtle.speed(0)
turtle.colormode(255)
draw_tree(my_turtle)
