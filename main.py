import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0))

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print(f"Game over!")
                exit(0)

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
