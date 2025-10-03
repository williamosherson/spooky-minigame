import numpy as np 
import pygame
from Ball import Ball
from Character import Character 
from NewBall import NewBall


# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character")

# Create a Character object
character = Character(screen,20,"metal.mp3","metalog.mp3")
ball = Ball(screen, np.random.randint(200, 600, 2), np.random.randint(-2, 2, 2), 20)

# Counter variables
counter = 0
font = pygame.font.Font(None, 36)  # Font for counter

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                character.moving_up = True
            elif event.key == pygame.K_s:
                character.moving_down = True
            elif event.key == pygame.K_a:
                character.moving_left = True
            elif event.key == pygame.K_d:
                character.moving_right = True
            if event.key == pygame.K_t:
                character.playSound()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                character.moving_up = False
            elif event.key == pygame.K_s:
                character.moving_down = False
            elif event.key == pygame.K_a:
                character.moving_left = False
            elif event.key == pygame.K_d:
                character.moving_right = False


    if character.position[0] < 0:
        character.position[0] = screen_width
    elif character.position[0] > screen_width:
        character.position[0] = 0
    if character.position[1] < 0:
        character.position[1] = screen_height
    elif character.position[1] > screen_height:
        character.position[1] = 0

    # Clear the screen
    screen.fill((248, 248, 248))
    
    # Check distance between character and ball
    displacement = character.position - ball.position
    distance = np.linalg.norm(displacement)

    if distance < character.radius + ball.radius:  # If they are touching or overlapping
        ball.position = np.array([float(np.random.randint(0,screen_width)),float(np.random.randint(0,screen_height))])   # Reset ball position
        ball.velocity = np.random.rand(2)       # Reset ball velocity
        counter += 1                               # Increment counter
    
    # Draw the character
    character.draw(1000/(counter+1))
    
    # Draw the ball
    ball.draw()
    ball.update(displacement,counter)
    
    # Update character position
    character.updatePosition(counter+1)
        
    # Display the counter
    counter_text = font.render("Counter: " + str(counter), True, (0, 0, 0))
    screen.blit(counter_text, (screen_width // 2 - counter_text.get_width() // 2, 20))
        # Play sound when mouth closes
    
    # Update the display
    pygame.display.flip()
    
    # Limit frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()
