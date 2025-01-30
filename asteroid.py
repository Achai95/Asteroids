import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity* dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.ran_angl= random.uniform(20,50)
        aster1=self.velocity.rotate(self.ran_angl)
        aster2=self.velocity.rotate(-self.ran_angl)
        new_radius=self.radius-ASTEROID_MIN_RADIUS
        ast1= Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity= aster1 *1.2
        ast2= Asteroid(self.position.x, self.position.y, new_radius)
        ast2.velocity= aster2 *1.2

        