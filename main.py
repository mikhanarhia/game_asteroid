import pygame
from pygame.time import Clock
import constants
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock: Clock = pygame.time.Clock()
    dt: float = 0.0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return
        screen.fill("black")
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000






if __name__ == "__main__":
    main()
