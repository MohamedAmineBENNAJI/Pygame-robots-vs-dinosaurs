"""This module contains the implementation of the laser."""

from typing import Tuple

import pygame


class Laser(pygame.sprite.Sprite):
    """This class implements the Laser."""

    def __init__(
        self,
        pos: Tuple[int, int],
        screen_height: int,
        speed: int,
        surface_dimensions: Tuple[int, int] = (4, 20),
    ):
        """Initialize the Laser class.
        Args:
            pos: the position of the laser within the character.
            screen_height: the screen height.
            speed: the speed of the laser shot.
            surface_dimensions: the surface dimensions of the laser in the screen.

        """
        super().__init__()
        self.image = pygame.Surface(surface_dimensions)
        self.image.fill("white")
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.height_y_constraint = screen_height

    def update(self):
        """This method is used to move and destroy the laser shot."""
        self.rect.y += self.speed
        self.destroy()
        return self.rect.y

    def destroy(self):
        """This method is used to destroy the laser after meeting certain conditions."""
        condition = self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50
        if condition:

            self.kill()
        return condition
