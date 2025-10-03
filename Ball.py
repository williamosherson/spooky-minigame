import pygame
import numpy as np

class Ball:
    def __init__(self, screen, position, velocity, radius):
        self.screen = screen
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.radius = radius
        self.screen_width, self.screen_height = self.screen.get_size()
    
    def checkCollisionWithWalls(self):
        if self.position[0] - self.radius < 0 or self.position[0] + self.radius > self.screen_width:
            self.velocity[0] = -self.velocity[0]  # Reverse horizontal velocity if hit side walls
        
        if self.position[1] - self.radius < 0 or self.position[1] + self.radius > self.screen_height:
            self.velocity[1] = -self.velocity[1]  # Simulate bounce if hit top or bottom walls
    
    def update(self, force,counter,dt=0.01):
        self.checkCollisionWithWalls()  # Check for collision with walls
        self.velocity += dt * force  # Simulate gravity
        self.velocity = self.velocity*counter / np.linalg.norm(self.velocity)
        self.position += self.velocity
    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.position[0]), int(self.position[1])), self.radius)