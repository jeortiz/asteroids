import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        
        splitAngle = random.uniform(20, 50)

        cwAngle = self.velocity.rotate(splitAngle)
        ccwAngle = self.velocity.rotate(-splitAngle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS

        cwAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
        ccwAsteroid = Asteroid(self.position.x, self.position.y, newRadius)

        cwAsteroid.velocity = cwAngle*1.2
        ccwAsteroid.velocity = ccwAngle*1.2
        