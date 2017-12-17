

class Actor:

    def __init__(self, collider=None):
        self.x = 0
        self.y = 0
        self.collider = collider

    def update(self, data):
        pass

    def render(self, ctx):
        pass

    def hit(self, other):
        pass

    def globalCollider(self):
        return self.collider.translate(self.x, self.y)
