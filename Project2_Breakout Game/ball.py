# BREAKOUT GAME: BALL

import pygame
import random

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    # This class represents a car
    # It derives from the "Sprite" class in Pygame

    def __init__(self, color, size_ball, vel_range):
        self.width_ball = size_ball[0]
        self.height_ball = size_ball[1]
        self.vmin = vel_range[0]
        self.vmax = vel_range[1]

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the background color
        self.image = pygame.Surface([self.width_ball, self.height_ball])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (rectangle)
        pygame.draw.rect(self.image, color, [0, 0, self.width_ball, self.height_ball])

        self.velocity = [random.randint(1, self.vmax), random.randint(1, self.vmax)]

        # Get rectangle object from the image
        self.rect = self.image.get_rect()

    def set_pose(self, x, y):
        # Set position (x, y)
        self.rect.x = x
        self.rect.y = y

    def get_pose(self):
        # Return position (x, y)
        return [self.rect.x, self.rect.y]

    def update(self):
        # Overriding update() in pygame.sprite.Sprite
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def update_reverse(self):
        self.rect.x -= self.velocity[0]
        self.rect.y -= self.velocity[1]

    def reverse_vel_x(self):
        # Reverse velocity (x)
        self.velocity[0] = -self.velocity[0]

    def reverse_vel_y(self):
        # Reverse velocity (y)
        self.velocity[1] = -self.velocity[1]

    def update_vel_bounce(self):
        # Update velocity after bouncing
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(self.vmin, self.vmax)
        if self.velocity[1] == 0:
            self.velocity[1] = 1
