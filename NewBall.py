import pygame
import numpy as np 
from Ball import Ball

class NewBall(Ball):
    def __init__(self,screen, position, velocity, radius):
        super().__init__(screen, position, velocity, radius)
    
    def update(self, direction,dt=0.01):
        self.checkCollisionWithWalls()  # Check for collision with walls
        self.velocity += dt*direction  # Simulate gravity
        self.position += self.velocity
        self.position = self.position/np.linalg.norm(self.position)