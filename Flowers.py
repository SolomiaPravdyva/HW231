import turtle
from random import randint, choice

class Stem:
    def __init__(self, length, color):
        self.length = length
        self.color = color
    def draw(self, t):
        t.color(self.color)
        t.width(3)
        t.forward(self.length)
class Leaf:
    def __init__(self, size):
        self.size = size
        self.color = "green"
    def draw(self, t):
        t.color(self.color)
        t.begin_fill()
        for _ in range(2):
            t.circle(self.size, 60)
            t.left(120)
        t.end_fill()
class Petals:
    def __init__(self, radius):
        self.radius = radius
        self.color = "red"
    def set_color(self, color):
        self.color = color
    def draw(self, t):
        t.color(self.color)
        for _ in range(8):
            t.begin_fill()
            t.circle(self.radius, 60)
            t.left(120)
            t.circle(self.radius, 60)
            t.left(120)
            t.end_fill()
            t.left(45)
class Flower:
    def __init__(self, stem_len, petal_radius, leaf_size, color, angle):
        self.stem = Stem(stem_len, "green")
        self.leaf = Leaf(leaf_size)
        self.petals = Petals(petal_radius)
        self.petals.set_color(color)
        self.stem_len = stem_len
        self.angle = angle
    def draw(self, t):
        t.setheading(self.angle)
        self.stem.draw(t)
        t.penup()
        t.backward(self.stem_len * 0.5)
        t.pendown()
        t.left(60)
        self.leaf.draw(t)
        t.right(60)
        t.penup()
        t.forward(self.stem_len * 0.5)
        t.pendown()
        self.petals.draw(t)
        t.penup()
        t.backward(self.stem_len)
        t.pendown()

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
colors = ["red", "salmon", "hot pink", "purple", "dark magenta",
          "gold", "navy", "turquoise", "sky blue", "seashell",
          "blue violet", "brown", "indigo", "moccasin"]
CENTER_X=0
CENTER_Y= -200
t.penup()
t.goto(CENTER_X, CENTER_Y)
t.setheading(90)
t.pendown()
for i in range(10):
    angle = randint(60, 120)
    flower = Flower(
        stem_len=randint(120, 180),
        petal_radius=randint(35, 60),
        leaf_size=25,
        color=choice(colors),
        angle=angle
    )
    flower.draw(t)
turtle.done()