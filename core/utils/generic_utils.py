"""This module includes some generic utils."""
import logging
import pathlib
from typing import Union

import pygame


def load_image(image_path: Union[str, pathlib.Path]):
    """This function loads an image and handles file errors.
    Args:
        image_path: path of an image.
    Returns:
        image: converted alpha pixels
    """
    try:
        image = pygame.image.load(image_path)
    except pygame.error as message:
        logging.error("Cannot load image: " + image_path)
        raise SystemExit(message)
    return image.convert_alpha()


def load_font(font_path: Union[str, pathlib.Path], font_size: int):
    """This function loads an image and handles file errors.
    Args:
        font_path: path of an image.
        font_size: the font size.
    Returns:
        font: the imported font object.
    """
    try:
        font = pygame.font.Font(font_path, font_size)
    except pygame.error as message:
        logging.error("Cannot load font: " + font_path)
        raise SystemExit(message)
    return font
