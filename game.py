import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Screen configuration
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)

# Dreadnought configuration
DREADNOUGHT_COLOR = (255, 255, 255)
DREADNOUGHT_SIZE = 50
SPEED = 0.01

# Searchlight configuration
SEARCHLIGHT_COLOR = (255, 255, 0, 50)  # Reduce alpha value for more transparency, increase alpha value for less transparency
SEARCHLIGHT_RADIUS = 150  # Update to make the searchlight larger or smaller


# Main game loop
def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Dreadnought Game')

    dreadnought_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

    while True:
        screen.fill(BACKGROUND_COLOR)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and dreadnought_position[1] > 0:
            dreadnought_position[1] -= SPEED
        if keys[pygame.K_s] and dreadnought_position[1] < SCREEN_HEIGHT - DREADNOUGHT_SIZE:
            dreadnought_position[1] += SPEED
        if keys[pygame.K_a] and dreadnought_position[0] > 0:
            dreadnought_position[0] -= SPEED
        if keys[pygame.K_d] and dreadnought_position[0] < SCREEN_WIDTH - DREADNOUGHT_SIZE:
            dreadnought_position[0] += SPEED

        # Drawing the dreadnought
        pygame.draw.rect(screen, DREADNOUGHT_COLOR, (*dreadnought_position, DREADNOUGHT_SIZE, DREADNOUGHT_SIZE))

        # Drawing the searchlight
        dx = mouse_x - dreadnought_position[0]
        dy = mouse_y - dreadnought_position[1]
        angle = math.atan2(dy, dx)
        cone_angle = math.pi / 4  # Adjust this value to change the cone's size
        left_angle = angle - cone_angle / 2
        right_angle = angle + cone_angle / 2
        points = [
            (dreadnought_position[0] + DREADNOUGHT_SIZE // 2, dreadnought_position[1] + DREADNOUGHT_SIZE // 2),
            (dreadnought_position[0] + math.cos(left_angle) * SEARCHLIGHT_RADIUS + DREADNOUGHT_SIZE // 2, 
             dreadnought_position[1] + math.sin(left_angle) * SEARCHLIGHT_RADIUS + DREADNOUGHT_SIZE // 2),
            (dreadnought_position[0] + math.cos(right_angle) * SEARCHLIGHT_RADIUS + DREADNOUGHT_SIZE // 2, 
             dreadnought_position[1] + math.sin(right_angle) * SEARCHLIGHT_RADIUS + DREADNOUGHT_SIZE // 2)
        ]
        pygame.draw.polygon(screen, SEARCHLIGHT_COLOR, points)

        # Update the display
        pygame.display.flip()

# Run the game loop
game_loop()