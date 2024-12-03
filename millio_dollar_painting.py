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

import turtle as turtle_model
import random

turtle_model.colormode(255)
tin =turtle_model.Turtle()
tin.speed("fastest")
tin.penup()
color_list = [(243, 243, 245), (244, 240, 232), (244, 237, 242), (236, 243, 240), (214, 154, 105), (49, 96, 139), (163, 80, 45), (223, 209, 107), (17, 36, 59), (185, 163, 25), (120, 163, 202), (56, 30, 18), (126, 68, 94), (210, 91, 69), (43, 128, 70), (193, 140, 160), (162, 20, 10), (125, 181, 156), (58, 28, 40), (129, 26, 42), (19, 52, 43), (194, 91, 113), (48, 170, 98), (39, 62, 97), (27, 91, 52), (235, 162, 187), (108, 118, 172), (225, 206, 2), (6, 88, 108), (227, 179, 170)]
tin.hideturtle()

tin.setheading(225)
tin.forward(300)
tin.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tin.dot(20, random.choice(color_list))
    tin.forward(50)

    if dot_count % 10 == 0:
        tin.setheading(90)
        tin.forward(50)
        tin.setheading(180)
        tin.forward(500)
        tin.setheading(0)




screen = turtle_model.Screen()
screen.exitonclick()
