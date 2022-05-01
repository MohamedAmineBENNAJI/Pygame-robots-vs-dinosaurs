"""This module contains the implementation of Dinosaurs."""


import pygame
from core.utils.generic_utils import load_image


class Dinosaur(pygame.sprite.Sprite):
    """This class implements the Dinosaur character."""

    def __init__(self, screen: pygame.Surface, color: str, x: int, y: int):
        """Initialize the Dinosaur class.
        Args:
            screen: our display surface for the game.
            color: a tuple representing the color of dinosaurs.
            x: the x position.
            y: the y position.
        """
        super().__init__()

        file_path = "core/assets/images/" + color + ".png"

        self.screen = screen
        self.image = load_image(file_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.current_health = 100
        self.max_health = 100
        self.health_bar_length = 50
        self.health_ratio = self.max_health / self.health_bar_length

        if color == "red":
            self.value = 100
        elif color == "green":
            self.value = 200
        else:
            self.value = 300

    def update(self, direction: int):
        """This method is used to update the dinosaurs directions if they are moving
        and calculate their healths.
        Args:
            direction: the dinosaur directions
            {0:stable,1:from right to left,-1:from left to right}."""
        self.rect.x += direction
        health, _ = self.basic_health()
        return self.rect.x, health

    def get_damage(self, amount: int):
        """This method is used to calculate the health of dinosaurs after
        taking an amount of damage.
        Args:
            amount: the amount of taken damage.
        Returns:
            current_health: the current health of a dinosaur."""
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
        return self.current_health

    def basic_health(self):
        """This method is used to display the health bar of our dinosaur.
        Returns:
            health: the dinosaur's health bar."""
        health_bar_value = self.current_health / self.health_ratio
        draw = pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            (
                self.rect.x - 5,
                self.rect.y - 20,
                health_bar_value,
                5,
            ),
        )

        return health_bar_value, draw


class Monster(pygame.sprite.Sprite):
    """This class implements the Monster Dinosaur."""

    def __init__(self, screen: pygame.Surface, side: str, screen_width: int):
        """Initialize the Monster dinosaur class.
        Args:
            screen: our display surface for the game.
            side: the spawning side of the Monster dinosaur.
            screen_width: the screen width.
        """
        super().__init__()
        self.screen = screen
        self.image = load_image("core/assets/images/extra.png")
        self.current_health = 500
        self.max_health = 500
        self.health_bar_length = 100
        self.health_ratio = self.max_health / self.health_bar_length
        if side == "right":
            x = screen_width + 50
            self.speed = -5
        else:
            x = -50
            self.speed = 5
        self.rect = self.image.get_rect(topleft=(x, 80))

    def get_damage(self, amount: int):
        """This method is used to calculate the health of dinosaurs
        after taking an amount of damage.
        Args:
            amount: the amount of taken damage."""
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
        return self.current_health

    def basic_health(self):
        """This method is used to display the health bar of our dinosaur."""
        health_bar_value = self.current_health / self.health_ratio
        draw = pygame.draw.rect(
            self.screen,
            (0, 255, 0),
            (
                self.rect.x - 30,
                60,
                health_bar_value,
                5,
            ),
        )
        return health_bar_value, draw

    def update(self):
        """This method is used to update the Monster dinosaur's position while moving
        and calculate his health."""

        self.rect.x += self.speed
        health_bar_value, _ = self.basic_health()
        return self.rect.x, health_bar_value
