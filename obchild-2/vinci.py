import turtle 
import sys
import time

class start:
    def __init__(obj, color="black"):
        obj.t = turtle.Turtle()
        obj.screen = turtle.Screen()
        obj.screen.tracer(0, 0)
        turtle.bgcolor(color)
    def paint(obj, x, y):
        obj.t.penup()
        obj.t.goto(x, y)
        obj.t.pendown()
        obj.t.circle(1)
        obj.screen.update()
    def vector(obj, x, y):
        obj.t.goto(x, y)
        obj.screen.update()
    def end(obj):
        obj.screen.update()
        obj.t.done()
        sys.exit()
    def end_time(obj, t):
        obj.screen.update()
        obj.t.done()
        time.sleep(t)
        sys.exit()
    def exit(obj):
        sys.exit()
    def polygon(obj, n_sides, size):
        angle = 360 / n_sides
        for i in range(n_sides):
            obj.t.forward(size)
            obj.t.right(angle)
            obj.screen.update()
    def clean(obj):
        obj.t.clean()
        obj.screen.update()
    def wait(obj, t):
        time.sleep(t)
    def circle(obj, size):
        obj.t.circle(size)
        obj.screen.update()
    def pencil(obj, size):
        obj.t.pensize(size)
        obj.screen.update()
    def color(obj, color):
        obj.t.pencolor(color)
        obj.screen.update()
    def rt(obj, data):
        obj.t.right(data)
        obj.screen.update()
    def lt(obj, data):
        obj.t.left(data)
        obj.screen.update()
    def fw(obj, data):
        obj.t.forward(data)
        obj.screen.update()
    def bw(obj, data):
        obj.t.back(data)
        obj.screen.update()
    def add(obj, data):
        obj.t.clone(data)
        obj.screen.update()
    def color_time(obj, color_a="black", color_b="black", color_c="black", t=1):
        try:
            obj.t.pencolor(color_a)
            time.sleep(t)
            obj.t.pencolor(color_b)
            time.sleep(t)
            obj.t.pencolor(color_c)
            obj.screen.update()
        except TypeError as error:
            print(f"TypeError -> {error}")
    def color_equal(obj, condition_1, condition_2, color_true, color_false):
        try:
            if condition_1 == condition_2:
                obj.t.pencolor(color_true)
            else:
                obj.t.pencolor(color_false)
            obj.screen.update()
        except TypeError as t:
            print(t)
    def color_less(obj, value1, value2, color_true, color_false):
        try:
            if value1 < value2:
                obj.t.pencolor(color_true)
            else:
                obj.t.pencolor(color_false)
            obj.screen.update()
        except TypeError as e:
            print(e)
    def color_great(obj, value1, value2, true, false):
        try:
            if value1 > value2:
                obj.t.pencolor(true)
            else:
                obj.t.pencolor(false)
            obj.screen.update()
        except TypeError as e:
            print(e)
        
