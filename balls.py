import pygame
import numpy as np
from Ball import Ball
# Initialize Pygame
pygame.init()
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls")

# Create a list of balls
balls = [Ball(screen, np.random.randint(200,800 ,2), np.random.randint(-2,2,2),10) for _ in range(1, 1000)]


# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update balls
    for ball in balls:
        ball.update(np.array([9.8,0]))

    # Draw everything
    screen.fill((255, 255, 255))
    for ball in balls:
        ball.draw()
    pygame.display.flip()

    # Limit frames per second
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
