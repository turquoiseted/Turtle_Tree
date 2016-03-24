# Challenge using turtle to create a tree using recursion #
import turtle
# import random


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
        pass
    else:

        depth -= 1

        tree_turtle.pensize(depth)
        position = tree_turtle.pos()
        angle = tree_turtle.heading()
        tree_turtle.left(40)
        tree_turtle.forward(length)
        draw_branches(length*(2/3), depth, tree_turtle)

        tree_turtle.penup()
        tree_turtle.setpos(position)
        tree_turtle.setheading(angle)
        tree_turtle.pendown()

        tree_turtle.pensize(depth)
        tree_turtle.right(40)
        tree_turtle.forward(length)
        draw_branches(length*(2/3), depth, tree_turtle)


my_turtle = turtle.Turtle()
draw_tree(my_turtle)
