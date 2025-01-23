import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius< ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20,50)

            child1 = Asteroid(self.position.x,self.position.y,new_radius)
            child1.velocity = self.velocity.rotate(angle)*1.2

            child2 = Asteroid(self.position.x,self.position.y,new_radius)
            child2.velocity = self.velocity.rotate(-angle)*1.2



        

