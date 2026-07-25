import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_deg = random.uniform(20, 50)
        split_1 = self.velocity.rotate(split_deg)
        split_2 = self.velocity.rotate(-split_deg)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        aste_1 = Asteroid(self.position.x, self.position.y, new_radius)
        aste_2 = Asteroid(self.position.x, self.position.y, new_radius)
        aste_1.velocity = split_1 * 1.2
        aste_2.velocity = split_2 * 1.2
