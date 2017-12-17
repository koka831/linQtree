

class Collider():

    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y


class RectangleCollider(Collider):

    def __init__(self, x, y, width, height):
        super('rectangle', x, y)
        self.width = width
        self.height = height

    def translate(self, dx, dy):
        return RectangleCollider(self.x + dx, self.y + dy, self.width, self.height)

    def top(self):
        return self.y

    def bottom(self):
        return self.y + self.height

    def left(self):
        return self.x

    def right(self):
        return self.x + self.width
