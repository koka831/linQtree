

class Detector:

    def detect_collision(self, a1, a2):
        c1 = a1.globalCollider()
        c2 = a2.globalCollider()

        if c1.type == 'rectangle' and c2.type == 'rectangle':
            return self.detect_rectangle_collision(c1, c2)

    def detect_rectangle_collision(c1, c2):
        horizontal = c1.left < c2.right and c2.left < c1.right
        vertical = c2.top < c1.bottom and c1.top < c2.bottom
        return horizontal and vertical
