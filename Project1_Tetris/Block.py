import random

# Colors of block
block_colors = [(0, 0, 0), (120, 37, 179), (100, 179, 179), (80, 34, 22), (80, 134, 22), (180, 34, 22), (180, 34, 122)]


# Block class
class Block:
    x = 0  # x-position
    y = 0  # y-position

    idx_rotation = 0  # rotation-index
    idx_color = 0  # color-index

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.idx_color = random.randint(1, len(block_colors) - 1)  # Set block color

    def get_image(self):
        pass

    def rotate(self):
        pass


# I-shape block class
class IBlock(Block):
    block_images = [[1, 5, 9, 13], [4, 5, 6, 7]]

    def __init__(self, x, y):
        Block.__init__(self, x, y)

    def get_image(self):
        return self.block_images[self.idx_rotation]

    def rotate(self):
        self.idx_rotation = (self.idx_rotation + 1) % len(self.block_images)


# Z-shape block class
class ZBlock(Block):
    block_images = [[4, 5, 9, 10], [2, 6, 5, 9]]

    def __init__(self, x, y):
        Block.__init__(self, x, y)

    def get_image(self):
        return self.block_images[self.idx_rotation]

    def rotate(self):
        self.idx_rotation = (self.idx_rotation + 1) % len(self.block_images)


# S-shape block class
class SBlock(Block):
    block_images = [[6, 7, 9, 10], [1, 5, 6, 10]]

    def __init__(self, x, y):
        Block.__init__(self, x, y)

    def get_image(self):
        return self.block_images[self.idx_rotation]

    def rotate(self):
        self.idx_rotation = (self.idx_rotation + 1) % len(self.block_images)


# L-shape block class
class LBlock(Block):
    block_images = [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]]

    def __init__(self, x, y):
        Block.__init__(self, x, y)

    def get_image(self):
        return self.block_images[self.idx_rotation]

    def rotate(self):
        self.idx_rotation = (self.idx_rotation + 1) % len(self.block_images)


# J-shape block class
class JBlock(Block):
    block_images = [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]]

    def __init__(self, x, y):
        Block.__init__(self, x, y)

    def get_image(self):
        return self.block_images[self.idx_rotation]

    def rotate(self):
        self.idx_rotation = (self.idx_rotation + 1) % len(self.block_images)


# T-shape block class
class TBlock(Block):
    block_images = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]

    def __init__(self, x, y):
        Block.__init__(self, x, y)

    def get_image(self):
        return self.block_images[self.idx_rotation]

    def rotate(self):
        self.idx_rotation = (self.idx_rotation + 1) % len(self.block_images)


# O-shape block class
class OBlock(Block):
    block_images = [[1, 2, 5, 6]]

    def __init__(self, x, y):
        Block.__init__(self, x, y)

    def get_image(self):
        return self.block_images[self.idx_rotation]

    def rotate(self):
        self.idx_rotation = (self.idx_rotation + 1) % len(self.block_images)
