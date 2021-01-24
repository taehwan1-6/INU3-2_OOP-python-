from Block import *


class TetrisApp:
    level = 2
    score = 0
    is_game_over = False
    field = []
    height = 0
    width = 0
    screen_x = 120
    screen_y = 100
    zoom = 20

    block = None
    num_block_type = 7  # Number of block type

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.is_game_over = False

        # Set field (screen)
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)


    def set_new_block(self):
        type = random.randint(0, self.num_block_type - 1)  # Set block type
        if type == 0:
            self.block = IBlock(3, 0)
        elif type == 1:
            self.block = ZBlock(3, 0)
        elif type == 2:
            self.block = SBlock(3, 0)
        elif type == 3:
            self.block = LBlock(3, 0)
        elif type == 4:
            self.block = JBlock(3, 0)
        elif type == 5:
            self.block = TBlock(3, 0)
        elif type == 6:
            self.block = OBlock(3, 0)

    def check_intersection(self):
        intersection = False
        # Write code here!
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.get_image():
                    if (j + self.block.x < 0) or (j + self.block.x > self.width-1):
                        intersection = True
                        return intersection
                    if (i + self.block.y < 0) or (i + self.block.y > self.height-1):
                        intersection = True
                        return intersection
                    if self.field[i + self.block.y][j + self.block.x] > 0:
                        intersection = True
                        return intersection

        return intersection

    def delete_lines(self):
        lines = 0
        # Write code here!
        for i in range(self.height):
            counts = 0
            for j in range(self.width):
                if self.field[i][j] > 0:
                    counts = counts + 1
            if counts == 10:
                lines = lines + 1
                del self.field[i]
                new_line = []
                for k in range(self.width):
                    new_line.append(0)
                self.field.insert(0, new_line)

        self.score += lines

    def move_straight_down(self):
        # Write code here!
        while True:
            self.block.y = self.block.y + 1
            if self.check_intersection():
                self.block.y = self.block.y - 1
                break

        self.check_condition()

    def move_down(self):
        self.block.y += 1
        if self.check_intersection():
            self.block.y -= 1
            self.check_condition()

    def check_condition(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.get_image():
                    self.field[i + self.block.y][j + self.block.x] = self.block.idx_color

        self.delete_lines()
        self.set_new_block()
        if self.check_intersection():
            self.is_game_over = True

    def move_side(self, dx):
        old_x = self.block.x
        self.block.x += dx
        if self.check_intersection():
            self.block.x = old_x

    def rotate(self):
        # Write code here!
        self.block.rotate()
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.get_image():
                    if (j + self.block.x < 0) or (j + self.block.x > self.width-1):
                        self.block.idx_rotation = self.block.idx_rotation + (-1)
                        return
                    if (i + self.block.y < 0) or (i + self.block.y > self.height-1):
                        self.block.idx_rotation = self.block.idx_rotation + (-1)
                        return
                    if self.field[i + self.block.y][j + self.block.x] > 0:
                        self.block.idx_rotation = self.block.idx_rotation + (-1)
                        return
        pass