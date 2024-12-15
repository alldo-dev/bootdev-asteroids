import pygame
import constants as c
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")

    # Containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # asign the containers to classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    run = True

    player = Player(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    asteroidsfield = AsteroidField()

    # Game LOOP
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("#000000")

        for ug in updatable:
            ug.update(dt)

        for dg in drawable:
            dg.draw(screen)

        # drawable group
        # for drawable in player.containers[1]:
            # drawable.draw(screen)

        pygame.display.flip()
        delta = clock.tick(60)  # 60 FPS
        print(f"FPS {clock.get_fps()}")
        dt = delta / 1000


if __name__ == "__main__":
    main()
