"""This module contains the implementation of the robot."""
from typing import Any, Tuple

import pygame

from core.utils.laser import Laser


class Robot(pygame.sprite.Sprite):
    """This class implements the Robot character."""

    def __init__(
        self,
        screen: pygame.Surface,
        pos: Tuple[float, float],
        constraint: int,
        speed: int,
    ) -> None:
        """Initialize the Dinosaur class.

        Args:
            screen: our display surface for the game.
            pos: a tuple representing the position of the robot.
            constraint: the maximum value that limits the movement of the robot.
            speed: the robot's movement speed.
        """
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load("core/assets/images/robot.png").convert_alpha()

        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.max_y_constraint = constraint
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()
        self.current_health = 300
        self.max_health = 300
        self.health_bar_length = 50
        self.health_ratio = self.max_health / self.health_bar_length

    def get_input(self) -> None:
        """
        This  method is used to get the keyboard inputs and convert them
        into actions.

        """
        keys = pygame.key.get_pressed()

        # Move Right
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # Move Left
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        # Move Up
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
        # Move Down
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        # Diagonal moves
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:

            self.rect.x += self.speed
            self.rect.y -= self.speed
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:

            self.rect.x += self.speed
            self.rect.y += self.speed
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:

            self.rect.x -= self.speed
            self.rect.y += self.speed
        elif keys[pygame.K_LEFT] and keys[pygame.K_UP]:

            self.rect.x -= self.speed
            self.rect.y -= self.speed

    def get_damage(self, amount: int) -> int:
        """This method is used to calculate the health of robot after taking an amount of damage.

        Args:
            amount: the amount of taken damage."""
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
        return self.current_health

    def basic_health(self) -> Tuple[float, Any]:
        """This method is used to display the health bar of our robot."""
        health_bar_value = self.current_health / self.health_ratio

        draw = pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (
                self.rect.x + 5,
                self.rect.y - 20,
                health_bar_value,
                5,
            ),
        )
        return health_bar_value, draw

    def recharge(self) -> None:
        """This method is used to recharge the weapon after shooting cooldown."""
        if not self.ready:
            current_time = pygame.time.get_ticks()

            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def update(self) -> None:
        """This method is used to update the positions, recharge the weapon and calculate
        the robot's health."""
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()
        self.basic_health()

    def shoot_laser(self) -> None:
        """This method is used to shoot laser from the robot's weapon."""
        self.lasers.add(
            Laser(
                self.rect.center,
                self.max_y_constraint,
                -8,
            )
        )

    def constraint(self) -> None:
        """This method limits the movement of the robot inside the simulation space."""
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
        elif self.rect.bottom >= self.max_y_constraint:
            self.rect.bottom = self.max_y_constraint
        elif self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.left <= 0 and self.rect.bottom >= self.max_y_constraint:
            self.rect.left = 0
            self.rect.bottom = self.max_y_constraint
        elif (
            self.rect.right >= self.max_x_constraint
            and self.rect.bottom >= self.max_y_constraint
        ):

            self.rect.right = self.max_x_constraint
            self.rect.bottom = self.max_y_constraint
        elif self.rect.left <= 0 and self.rect.top <= 0:
            self.rect.top = 0
            self.rect.left = 0
        elif self.rect.right >= self.max_x_constraint and self.rect.top <= 0:
            self.rect.top = 0
            self.rect.right = self.max_x_constraint
