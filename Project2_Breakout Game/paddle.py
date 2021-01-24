# BREAKOUT GAME: PADDLE

import pygame

BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    # This class represents a paddle
    # It inherits the "Sprite" class in Pygame

    def __init__(self, color, size_paddle, size_screen):
        self.width_paddle = size_paddle[0]
        self.height_paddle = size_paddle[1]
        self.width_screen = size_screen[0]
        self.height_screen = size_screen[1]

        self.xmin = 0
        self.xmax = self.width_screen - self.width_paddle

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the background color
        self.image = pygame.Surface([self.width_paddle, self.height_paddle])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (rectangle)
        pygame.draw.rect(self.image, color, [0, 0, self.width_paddle, self.height_paddle])

        # Get rectangle object from the image
        self.rect = self.image.get_rect()

    def set_pose(self, x, y):
        # Set position (x, y)
        self.rect.x = x
        self.rect.y = y

    def move_left(self, pmove):
        # Move the paddle left
        # Write code here!
        if self.rect.x == self.xmin:
            pass
        else:
            self.rect.x -= pmove
        pass


    def move_right(self, pmove):
        # Move the paddle right
        # Write code here!
        if self.rect.x == self.xmax:
            pass
        else:
            self.rect.x += pmove
        pass
