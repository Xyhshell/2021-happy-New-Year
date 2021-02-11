#!/usr/bin/python
# -*- coding:utf-8 -*-
# @File   : 2021_demo.py
# @Time   : 2021/2/11 15:00

import turtle
import numpy
import os


print(os.getcwd())
file_path = os.getcwd()

turtle.speed(0.001)
turtle.color('red', 'red')


def conan(matrix, width, height):
    turtle.tracer(500)
    turtle.speed(0)
    turtle.pensize(2)
    turtle.delay(0)
    x = -width / 2
    y = height / 2
    for row in matrix:
        for element in row:
            if element == 1:
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.goto(x + 2, y)
            if x == width / 2:
                x = -width / 2
                y -= 1
            x += 1
    turtle.hideturtle()


def conan2(matrix, width, height):
    turtle.tracer(100)
    turtle.speed(0)
    turtle.pensize(2)
    turtle.delay(0)
    x = -width / 2
    y = height / 2
    for row in matrix:
        for element in row:
            if element == 1:
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.goto(x + 2, y)
            if x == width / 2:
                x = -width / 2
                y -= 1
            x += 1
    turtle.hideturtle()


def frame():
    turtle.speed(0)
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-450, 300)
    turtle.pendown()
    turtle.forward(900)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(900)
    turtle.right(90)
    turtle.forward(600)
    turtle.penup()
    turtle.goto(-450 - 15, 300 + 10)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(900 + 30)
    turtle.right(90)
    turtle.forward(600 + 20)
    turtle.right(90)
    turtle.forward(900 + 30)
    turtle.right(90)
    turtle.forward(600 + 20)


c1 = numpy.load(file_path + r"/img2.npy")
c = numpy.load(file_path + r"/img3.npy")


turtle.setup(960, 700, 450, 200)
turtle.title(" Hello 2021 & This is demo & goodbye 2020 ")
frame()

turtle.penup()
turtle.goto(-465, 320)
turtle.pendown()
turtle.write("辛丑牛年 新春快乐！", align="left", font=("楷体", 18, "bold"))

conan2(c1, 261, 193)
conan(c, 840, 525)

turtle.speed(0)

turtle.penup()
turtle.goto(465, -335)
turtle.pendown()
turtle.write("Painting By JINGMO", align="right", font=("OCR A Std", 10, "bold"))
turtle.exitonclick()


