"""Asteroids guided project."""

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

BLACK = (0, 0, 0)


def main():
  """Run the game."""

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  asteroids = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  updatable = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)
  Player.containers = (updatable, drawable)
  Shot.containers = (updatable, drawable, shots)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidfield = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    # State updates.
    updatable.update(dt)
    for a in asteroids:
      if a.collision(player):
        print("Game over!")
        return

      for s in shots:
        if s.collision(a):
          s.kill()
          a.split()

    # Draw calls.
    # Order of calls is important! Drawing the player before filling the screen
    # will just end up with a black screen.
    screen.fill(BLACK)
    # Unable to use this API atm, sprite requires .image attribute
    # drawable.draw(screen)
    for d in drawable:
      d.draw(screen)

    # Update and tick.
    pygame.display.flip()
    # Limit to 60 FPS.
    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()
