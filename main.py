###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import random
import turtle

tim = turtle.Turtle()
tim.pensize(15)

turtle.colormode(255)

tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140,
                                                                                                                30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
def print_row():
    for _ in range(10):
        tim.pencolor(random.choice(color_list))
        tim.forward(1)
        tim.penup()
        tim.forward(30)
        tim.pendown()
        tim.pencolor(random.choice(color_list))
        tim.forward(1)
        tim.penup()


def comeback():
    tim.back(320)
    tim.rt(90)
    tim.forward(30)
    tim.lt(90)
    tim.pendown()


def print_all():
    for _ in range(10):
        print_row()
        comeback()

print_all()

turtle.exitonclick()