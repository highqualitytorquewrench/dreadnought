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
DREADNOUGHT_LENGTH = 80  # Adjusted to create a more elongated shape
DREADNOUGHT_WIDTH = 30
SPEED = 0.01

# Searchlight configuration
SEARCHLIGHT_COLOR = (255, 255, 0, 50)  # Adjusted alpha value for more transparency (smaller is more transparent)
SEARCHLIGHT_RADIUS = 150
cone_angle = math.pi / 4  # Adjust cone angle (smaller is bigger)

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
        if keys[pygame.K_s] and dreadnought_position[1] < SCREEN_HEIGHT - DREADNOUGHT_WIDTH:
            dreadnought_position[1] += SPEED
        if keys[pygame.K_a] and dreadnought_position[0] > 0:
            dreadnought_position[0] -= SPEED
        if keys[pygame.K_d] and dreadnought_position[0] < SCREEN_WIDTH - DREADNOUGHT_LENGTH:
            dreadnought_position[0] += SPEED

        # Drawing the dreadnought
        dreadnought = pygame.Surface((DREADNOUGHT_LENGTH, DREADNOUGHT_WIDTH), pygame.SRCALPHA)  # Semi-transparent surface
        pygame.draw.polygon(dreadnought, DREADNOUGHT_COLOR, [(0, DREADNOUGHT_WIDTH // 2), (DREADNOUGHT_LENGTH // 2, 0), 
                                                            (DREADNOUGHT_LENGTH, DREADNOUGHT_WIDTH // 2), 
                                                            (DREADNOUGHT_LENGTH // 2, DREADNOUGHT_WIDTH)])
        screen.blit(dreadnought, dreadnought_position)

        # Drawing the searchlight
        dx = mouse_x - dreadnought_position[0]
        dy = mouse_y - dreadnought_position[1]
        angle = math.atan2(dy, dx)
        left_angle = angle - cone_angle / 2
        right_angle = angle + cone_angle / 2
        points = [
            (dreadnought_position[0] + DREADNOUGHT_LENGTH // 2, dreadnought_position[1] + DREADNOUGHT_WIDTH // 2),
            (dreadnought_position[0] + math.cos(left_angle) * SEARCHLIGHT_RADIUS + DREADNOUGHT_LENGTH // 2, 
             dreadnought_position[1] + math.sin(left_angle) * SEARCHLIGHT_RADIUS + DREADNOUGHT_WIDTH // 2),
            (dreadnought_position[0] + math.cos(right_angle) * SEARCHLIGHT_RADIUS + DREADNOUGHT_LENGTH // 2, 
             dreadnought_position[1] + math.sin(right_angle) * SEARCHLIGHT_RADIUS + DREADNOUGHT_WIDTH // 2)
        ]
        pygame.draw.polygon(screen, SEARCHLIGHT_COLOR, points)

        # Update the display
        pygame.display.flip()

# Run the game loop
game_loop()
