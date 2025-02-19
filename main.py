import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')
        
        updatable.update(dt)

        for drawy in drawable:
            drawy.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()