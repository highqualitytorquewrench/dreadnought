import pygame
import sys

# Initialize pygame
pygame.init()

# Screen configuration
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)

# Dreadnought configuration
DREADNOUGHT_COLOR = (255, 255, 255)
DREADNOUGHT_SIZE = 50
SPEED = 0.01  # Adjust the speed of the dreadnought's movement

# Main game loop
def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Dreadnought Game')

    dreadnought_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

    while True:
        screen.fill(BACKGROUND_COLOR)

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

        # Update the display
        pygame.display.flip()

# Run the game loop
game_loop()
