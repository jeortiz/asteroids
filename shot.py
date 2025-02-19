import pygame
from circleshape import CircleShape
from constants import SHOTS_RADIUS


class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOTS_RADIUS)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)