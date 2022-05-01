"""This module contains the implementation of the obstacles."""

from typing import Tuple

import pygame


class Block(pygame.sprite.Sprite):
    """This class implements blocs used to build obstacles."""

    def __init__(self, size: int, color: Tuple[int, int, int], x: int, y: float):
        """Initialize the Block class.
        Args:
            size: an integer specifying the size of block.
            color: a tuple representing the color of the block.
            x: the x position.
            y: the y position.
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))


shape = [
    "  xxxxxxx",
    " xxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxx     xxx",
    "xx       xx",
]
