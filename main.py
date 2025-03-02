import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers =(updatable)
    asteroidField = AsteroidField()

    Shot.containers = (drawable, updatable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')

        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collidesWith(shot):
                    asteroid.split()
                    shot.kill()

        for asteroid in asteroids:
            if player.collidesWith(asteroid):
                print("Game over!")
                print(f'asteroid {asteroid.id} killed you')
                exit()
                    
        updatable.update(dt)

        for drawy in drawable:
            drawy.draw(screen)
    
        pygame.display.flip()

if __name__ == "__main__":
    main()