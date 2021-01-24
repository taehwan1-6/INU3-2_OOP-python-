# BREAKOUT GAME: MAIN

import pygame
import time

from paddle import Paddle
from ball import Ball
from brick import Brick

# Define colors
WHITE = (255, 255, 255)
DARKSLATE_GRAY = (47, 79, 79)
CYAN = (0, 255, 255)
CRIMSON = (220, 20, 60)
CORAL = (255, 127, 80)
KHAKI = (255, 255, 0)


def set_initial_bricks(bricks, size_brick):
    # Display initial brick
    for i in range(7):
        brick = Brick(CRIMSON, size_brick)
        brick.set_pose(60 + i * 100, 60)
        sprite_paddle_ball.add(brick)
        bricks.add(brick)
    for i in range(7):
        brick = Brick(CORAL, size_brick)
        brick.set_pose(60 + i * 100, 100)
        sprite_paddle_ball.add(brick)
        bricks.add(brick)
    for i in range(7):
        brick = Brick(KHAKI, size_brick)
        brick.set_pose(60 + i * 100, 140)
        sprite_paddle_ball.add(brick)
        bricks.add(brick)

    return bricks


if __name__ == "__main__":
    pygame.init()  # Initiate pygame engine

    score, lives = 0, 3

    # Set size
    size_screen = (800, 600)
    size_paddle = (100, 10)
    size_ball = (10, 10)
    size_brick = (80, 30)

    # Set velocity range (ball)
    vel_range = (-5.0, 5.0)
    vel_move = 5.0

    # Create a new window
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption("Breakout Game")

    # Create the Paddle
    paddle = Paddle(CYAN, size_paddle, size_screen)
    paddle.set_pose(320, 560)

    # Create the ball sprite
    ball = Ball(WHITE, size_ball, vel_range)
    ball.set_pose(350, 180)

    # Sprite-list for paddle & ball
    sprite_paddle_ball = pygame.sprite.Group()
    sprite_paddle_ball.add(paddle)
    sprite_paddle_ball.add(ball)

    # Sprite-list for brick
    sprite_brick = pygame.sprite.Group()
    sprite_brick = set_initial_bricks(sprite_brick, size_brick)

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # RUN LOOP --------------------------------------------------------------------------------------------------------#
    # Run program until the user exit the game (e.g. clicks the close button)
    run_loop = True
    game_state = 0  # 1: game-over, 2: complete-game
    start_time = time.time()  # Start to record time
    time_hour, time_minute, time_second = 0, 0, 0
    while run_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                run_loop = False  # Flag that we exit the program

        if game_state == 0:
            # Moving the paddle with the arrow keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.move_left(vel_move)
            if keys[pygame.K_RIGHT]:
                paddle.move_right(vel_move)
            sprite_paddle_ball.update()

            # Check whether the ball is bouncing against any of the 4 walls
            # Write code here!

            if ball.rect.x <= 0:
                ball.reverse_vel_x()
            elif ball.rect.x >= 790:
                ball.reverse_vel_x()
            elif ball.rect.y <= 40:
                ball.reverse_vel_y()
            elif ball.rect.y >= 590:
                ball.reverse_vel_y()
                lives -= 1
                if lives == 0:
                    game_state = 1

            # Detect collisions between the ball and the paddles
            if pygame.sprite.collide_mask(ball, paddle):
                ball.update_reverse()
                ball.update_vel_bounce()

            # Check collision
            brick_collision_list = pygame.sprite.spritecollide(ball, sprite_brick, False)
            for brick in brick_collision_list:
                ball.update_vel_bounce()
                brick.kill()
                score += 1
                if len(sprite_brick) == 0:
                    # Stop the Game
                    game_state = 2
                    print("SUCCESS")

        # Check how much time passes
        # Write code here!
        
        if game_state == 0:
            time_second = time.time() - start_time
            time_minute, time_second = divmod(time_second, 60)
            time_hour, time_minute = divmod(time_minute, 60)
        else:
            pass

        # SCREEN ------------------------------------------------------------------------------------------------------#
        # Clear the screen
        screen.fill(DARKSLATE_GRAY)
        pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
        pygame.draw.line(screen, WHITE, [0, 42], [800, 42], 2)

        # Display lives & scores & time
        # Write code here!
    
        font = pygame.font.Font(None, 34)
        str_lives = "Lives: {0}".format(lives)
        text_lives = font.render(str_lives, 1, WHITE)
        screen.blit(text_lives, (20, 10))

        font = pygame.font.Font(None, 34)
        str_score = "Score: {0}".format(score)
        text_score = font.render(str_score, 1, WHITE)
        screen.blit(text_score, (350, 10))

        font = pygame.font.Font(None, 34)
        str_time = "Time: %0d:%02d:%02d" % (time_hour,time_minute,time_second)
        text_time = font.render(str_time, 1, WHITE)
        screen.blit(text_time, (600,10))

        if game_state == 1:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250, 300))

        if game_state == 2:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (180, 300))

        # Draw sprites
        sprite_paddle_ball.draw(screen)

        # Update display
        pygame.display.flip()

        # Limit the clock-speed
        clock.tick(60)

    # Quit pygame
pygame.quit()
