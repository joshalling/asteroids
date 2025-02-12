import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)

        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2.velocity = self.velocity.rotate(-angle) * 1.2
