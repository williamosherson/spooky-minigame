import numpy as np 
import pygame

class Character:
    def __init__(self, screen, radius, fast_sound_file,slow_sound_file):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()
        self.position = np.array([self.screen_width//2, self.screen_height//2])
        self.radius = radius
        self.mouth_closed_image = pygame.image.load("mouth_closed.png")  # Load image for closed mouth
        self.mouth_open_image = pygame.image.load("mouth_open.png")      # Load image for open mouth
        self.image_index = 0
        self.last_toggle_time = pygame.time.get_ticks()
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # Load sound file
        self.fast_sound = pygame.mixer.Sound(fast_sound_file)
        self.slow_sound = pygame.mixer.Sound(slow_sound_file)

    def updatePosition(self, velocity):
        dx = (self.moving_right - self.moving_left) * velocity
        dy = (self.moving_down - self.moving_up) * velocity
        self.position += np.array([dx, dy])

    def draw(self,toggle_interval):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_toggle_time >= toggle_interval:
            self.image_index = (self.image_index + 1) % 2  # Toggle between 0 and 1
            self.last_toggle_time = current_time
            if self.image_index ==0:
                if toggle_interval >100:
                    self.slow_sound.play()
                else:
                    self.fast_sound.play()
        if self.image_index == 0:
            self.screen.blit(self.mouth_closed_image, (self.position[0] - self.radius, self.position[1] - self.radius))
        else:
            self.screen.blit(self.mouth_open_image, (self.position[0] - self.radius, self.position[1] - self.radius))
