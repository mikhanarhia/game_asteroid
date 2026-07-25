import pygame
import sys
from logger import log_event
from pygame.time import Clock
from asteroid import Asteroid
import constants
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

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

    #PLAYER
    Player.containers = (updatable, drawable)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    # ASTEROID
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    #SHOT
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return

        dt = game_clock.tick(60) / 1000
        screen.fill("black")
        for drawer in drawable:
            drawer.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()

        pygame.display.flip()






if __name__ == "__main__":
    main()
