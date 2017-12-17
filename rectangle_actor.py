from collider import RectangleCollider
from actor import Actor
import random


class RGB(object):

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class RectangleActor(Actor):

    def __init__(self, x, y, width, height):
        super(collider=RectangleCollider(0, 0, width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = RGB(0, 0, 0)

        self.vx = random.random() * 10 - 5
        self.vy = random.random() * 10 - 5

    def update(self, info):
        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > info.world.width:
            self.vx = -self.vx

        if self.y < 0 or self.y > info.world.height:
            self.vy = -self.vy

    def render(self, ctx):
        ctx.fill_style = self.color
        ctx.fill_rect(self.x, self.y, self.width, self.height)

    def hit(self, other):
        self.color = RGB(255, 0, 0)
