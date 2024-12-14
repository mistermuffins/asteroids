"""Asteroids guided project."""

import pygame

from constants import *
from player import Player

BLACK = (0, 0, 0)


def main():
  """Run the game."""

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    # State updates.
    player.update(dt)

    # Draw calls.
    # Order of calls is important! Drawing the player before filling the screen
    # will just end up with a black screen.
    screen.fill(BLACK)
    player.draw(screen)

    # Update and tick.
    pygame.display.flip()
    # Limit to 60 FPS.
    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()
