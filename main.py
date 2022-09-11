import colorgram as cg
import turtle as t
import random


def extract_colors(image_name):
    """Extracts the most common non-background colors from a .jpg image"""

    hirst_colors = cg.extract(image_name, 20)
    color_list = []
    for item in hirst_colors:
        color = item.rgb
        r = color.r
        g = color.g
        b = color.b
        if item.proportion < 0.5:
            color_list.append((r, g, b))
    return color_list


color_list = extract_colors("hirst.jpg")

t.colormode(255)
screen = t.Screen()
screen.screensize(800, 800)
print(screen.canvwidth)
print(screen.canvheight)


def hirst(scr, dot_radius, x_dots, y_dots, colors):
    """Generates a """
    painter = t.Turtle()
    painter.hideturtle()
    painter.speed("fastest")
    painter.penup()
    painter.pensize(dot_radius * 2)
    painter.setposition(-scr.canvwidth / 2, -scr.canvheight / 2)
    x_spacing = scr.canvwidth / x_dots
    y_spacing = scr.canvheight / y_dots

    def paint_row():
        for n in range(0, x_dots):
            painter.dot(dot_radius * 2, random.choice(colors))
            painter.forward(x_spacing)

    for n in range(0, y_dots):
        paint_row()
        painter.setx(-scr.canvwidth / 2)
        painter.sety(painter.ycor() + y_spacing)


hirst(screen, 14, 16, 16, color_list)
screen.exitonclick()
