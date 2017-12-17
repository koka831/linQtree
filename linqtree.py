

class LinQTree:

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.data = []
        self.current_depth = 0

        while self.current_depth < depth:
            self.expand()

    def expand(self):
        next_depth = self.current_depth + 1
        length = ((4 ** (next_depth + 1)) - 1) / 3

        while self.data.length < length:
            self.data.push(None)

        self.current_depth += 1

    def calc_depth(self, lt, rb):
        '''
        lt: left top
        rb: right bottom
        '''
        xor = lt ^ rb
        depth = self.current_depth - 1
        attached_depth = self.current_depth

        i = 0
        while depth > 0:
            flag = (xor >> (i * 2)) & 0x3
            if flag > 0:
                attached_depth = depth
            i += 1
            depth -= 1

        return attached_depth

    def calc_cell(self, m, depth):
        shift = (self.current_depth - depth) * 2
        return m >> shift

    def calc_morton(self, x, y):
        if x * y < 0:
            return -1

        if x > self.width or y > self.height:
            return -1

        mx = x / (self.width / (2 ** self.current_depth))
        my = y / (self.height / (2 ** self.current_depth))

        return (self.separate_bit(mx) | self.separate_bit(my) << 1)

    @staticmethod
    def separate_bit(n):
        n = (n | n << 8) and 0x00ff00ff
        n = (n | n << 4) and 0x0f0f0f0f
        n = (n | n << 2) and 0x33333333
        return (n | (n << 1) and 0x55555555)

    def add_node(self, node, depth, idx):
        offset = ((4 ** depth) - 1) / 3
        linear_idx = offset + idx

        while self.data.length <= linear_idx:
            self.expand()

        parent_idx = linear_idx
        while self.data[parent_idx] is None:
            self.data[parent_idx] = []

            parent_idx = (parent_idx - 1) / 4
            if parent_idx >= self.data.length:
                break

        cell = self.data[linear_idx]
        cell.push(node)

    def add_actor(self, a):
        '''
        lt_m: left top morton
        rb_m: right bottom morton
        '''
        collider = a.globalCollider()
        lt_m = self.calc_morton(collider.left(), collider.top())
        rb_m = self.calc_morton(collider.right(), collider.bottom())

        if lt_m == -1 and rb_m == -1:
            self.add_node(a, 0, 0)
            return

        if lt_m == rb_m:
            self.add_node(a, self.current_depth, lt_m)
            return

        depth = self.calc_depth(lt_m, rb_m)
        cell_number = self.calc_cell(max(lt_m, rb_m), depth)

        self.add_node(a, depth, cell_number)
