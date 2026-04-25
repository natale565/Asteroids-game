import sys
import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot


def main():
    print("Starting Asteroids with pygame version: VERSION")
    print('Screen width: 1280')
    print('Screen height: 720')

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print('Game over!')
                sys.exit()

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
