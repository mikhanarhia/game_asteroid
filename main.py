import pygame
from pygame.time import Clock
from asteroid import Asteroid
import constants
from logger import log_state
from player import Player
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock: Clock = pygame.time.Clock()
    dt: float = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return

        dt = game_clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for drawer in drawable:
            drawer.draw(screen)
        pygame.display.flip()






if __name__ == "__main__":
    main()
