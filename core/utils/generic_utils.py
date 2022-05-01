"""This module includes some generic utils."""
import logging

import pygame


def load_image(image_path: str) -> pygame.image:
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


def load_font(font_path: str, font_size: int) -> pygame.font:
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
