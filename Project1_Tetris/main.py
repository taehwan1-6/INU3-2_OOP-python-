from Block import *
from TetrisApp import *
import pygame


# Define some colors
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_GRAY = (128, 128, 128)
C_ORANGE = (255, 165, 0)
C_CYAN = (0, 255, 255)


if __name__ == '__main__':
    # STEP1: INITIALIZATION -------------------------------------------------------------------------------------------#
    # Initialize the game engine
    pygame.init()

    # Set screen
    screen_size = (500, 600)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Tetris")

    # Set tetris-game
    tetris_game = TetrisApp(20, 10)

    # STEP2: RUN-GAME -------------------------------------------------------------------------------------------------#
    done = False
    clock = pygame.time.Clock()
    fps = 20
    counter = 0

    key_pressing_down = False
    while not done:
        # Update counter
        counter += 1
        if counter > 100000:
            counter = 0

        # Add a new-block
        if tetris_game.block is None:
            tetris_game.set_new_block()

        if counter % (fps // tetris_game.level // 2) == 0 or key_pressing_down:
            if not tetris_game.is_game_over:
                tetris_game.move_down()

        # Handle keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When close window
                done = True
            if event.type == pygame.KEYDOWN:  # Occurs when the keyboard is pressed and released
                if event.key == pygame.K_UP:  # Up-arrow key
                    tetris_game.rotate()
                if event.key == pygame.K_DOWN:  # Down-arrow key
                    key_pressing_down = True
                if event.key == pygame.K_LEFT:  # Left-arrow key
                    tetris_game.move_side(-1)
                if event.key == pygame.K_RIGHT:  # Right-arrow key
                    tetris_game.move_side(1)
                if event.key == pygame.K_SPACE:  # Space key
                    tetris_game.move_straight_down()
                if event.key == pygame.K_ESCAPE:  # Esc key
                    tetris_game.__init__(20, 10)  # Reset tetris_game

        if event.type == pygame.KEYUP:  # Occurs when the keyboard is pressed
            if event.key == pygame.K_DOWN:  # Down-arrow key
                key_pressing_down = False

        # STEP3: DRAW -------------------------------------------------------------------------------------------------#
        screen.fill(C_BLACK)  # Fill the screen with black-color

        # Draw background
        for i in range(tetris_game.height):
            for j in range(tetris_game.width):
                # Draw grid-lines
                tetris_game_grid = [tetris_game.screen_x + tetris_game.zoom * j,
                                    tetris_game.screen_y + tetris_game.zoom * i,
                                    tetris_game.zoom, tetris_game.zoom]
                pygame.draw.rect(screen, C_GRAY, tetris_game_grid, 1)

                # Draw blocks
                if tetris_game.field[i][j] > 0:
                    tetris_game_block_static = [tetris_game.screen_x + tetris_game.zoom * j + 1,
                                                tetris_game.screen_y + tetris_game.zoom * i + 1,
                                                tetris_game.zoom - 2, tetris_game.zoom - 1]
                    pygame.draw.rect(screen, block_colors[tetris_game.field[i][j]], tetris_game_block_static)

        # Draw moving block
        if tetris_game.block is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in tetris_game.block.get_image():
                        tetris_game_block_dynamic = [tetris_game.screen_x + tetris_game.zoom * (j + tetris_game.block.x) + 1,
                                                     tetris_game.screen_y + tetris_game.zoom * (i + tetris_game.block.y) + 1,
                                                     tetris_game.zoom - 2, tetris_game.zoom - 2]
                        pygame.draw.rect(screen, block_colors[tetris_game.block.idx_color], tetris_game_block_dynamic)

        font1 = pygame.font.SysFont('Calibri', 25, True, False)
        font2 = pygame.font.SysFont('Calibri', 65, True, False)
        text_score = font1.render("Score: " + str(tetris_game.score), True, C_WHITE)
        text_game_over1 = font2.render("Game Over", True, C_ORANGE)
        text_game_over2 = font2.render("Press ESC", True, C_CYAN)

        screen.blit(text_score, [screen_size[0] - 100, 0])
        if tetris_game.is_game_over:
            screen.blit(text_game_over1, [100, 200])
            screen.blit(text_game_over2, [100, 265])

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
