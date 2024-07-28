# Python program for creating a Chess Board using Turtle
import turtle

# setting the Screen in order to work on it
scr = turtle.Screen()

# Defining the instance of Turtle
ttl = turtle.Turtle()


# method for drawing each of the squares
def draw():
    # for loop used to draw the squares
    for i in range(4):
        ttl.forward(35)
        ttl.left(90)

    ttl.forward(35)

    # Main driving Code


if __name__ == "__main__":

    # setting the Screen in order to work on it
    scr.setup(500, 500)

    # setting the turtle's drawing speed
    ttl.speed(0)

    # Using a for loops for making the entire board
    for j in range(8):

        # not to draw condition
        ttl.up()

        # setting the position of every row of the chess board
        ttl.setpos(-150, 35 * j)

        # condition for being ready to draw
        ttl.down()

        # for loop for the rows
        for k in range(8):

            # conditions for choosing the alternative color for every box
            if (j + k) % 2 == 0:
                clr = 'black'

            else:
                clr = 'white'

                # filling the box with the given color
            ttl.fillcolor(clr)

            # starting to fill the color
            ttl.begin_fill()

            # calling the draw method
            draw()
            # stopping to fill the color
            ttl.end_fill()

            # hiding the turtle
    ttl.hideturtle()
    turtle.done()
