# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys
from shot import Shot

def main():
    pygame.init()
    clock= pygame.time.Clock()
    screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable= pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    shots= pygame.sprite.Group()
    Shot.containers= (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    field= AsteroidField()
    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt=0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for update in updatable:
            update.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                sys.exit("Game Over!")
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()

        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # limit framerate
        dt=clock.tick(60)/1000
if __name__ == "__main__":
    main()