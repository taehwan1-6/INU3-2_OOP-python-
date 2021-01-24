# BREAKOUT GAME: BRICK

import pygame

BLACK = (0, 0, 0)


class Brick(pygame.sprite.Sprite):
    # This class represents a brick
    # It inherits the "Sprite" class in Pygame

    def __init__(self, color, size_brick):
        self.width_brick = size_brick[0]
        self.height_brick = size_brick[1]

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the background color
        self.image = pygame.Surface([self.width_brick, self.height_brick])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the brick (rectangle)
        pygame.draw.rect(self.image, color, [0, 0, self.width_brick, self.height_brick])

        # Get rectangle object from the image
        self.rect = self.image.get_rect()

    def set_pose(self, x, y):
        # Set position (x, y)
        self.rect.x = x
        self.rect.y = y
