# Challenge using turtle to create a tree using recursion #
import turtle
# import random


def draw_tree(tree_turtle):
    tree_turtle.penup()
    tree_turtle.setpos(0, -200)
    tree_turtle.pendown()
    tree_turtle.left(90)
    tree_turtle.forward(200)
    draw_branches(100, 5, tree_turtle)
    # Stop window from closing
    turtle.done()


def draw_branches(length, depth, tree_turtle):
    if depth == 0:
        pass
    else:
        depth -= 1
        position = tree_turtle.pos()
        angle = tree_turtle.heading()
        tree_turtle.left(60)
        tree_turtle.forward(length)
        draw_branches(length/2, depth, tree_turtle)

        tree_turtle.penup()
        tree_turtle.setpos(position)
        tree_turtle.setheading(angle)
        tree_turtle.pendown()

        tree_turtle.right(60)
        tree_turtle.forward(length)
        draw_branches(length/2, depth, tree_turtle)


my_turtle = turtle.Turtle()
draw_tree(my_turtle)
