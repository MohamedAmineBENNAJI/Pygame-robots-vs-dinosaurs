"""This module includes the tests for dinosaur module."""
import pytest
from core.utils.dinosaur import Dinosaur, Monster


class TestDinosaur:
    """This class tests the Dinosaur class."""

    @pytest.mark.parametrize("direction,expected_position", [(0, 10), (1, 11)])
    def test_update(self, dinosaur_object, direction, expected_position):
        """This method tests the update function for the Dinosaurs."""
        expected_health_bar_value = 50
        new_position, health_bar_value = dinosaur_object.update(direction=direction)

        assert (
            new_position == expected_position
            and health_bar_value == expected_health_bar_value
        ), "Check the positions and/or the health_bar values of the dinosaurs !"

    def test_get_damage(
        self, dinosaur_object: Dinosaur, current_health: int = 100, amount: int = 10
    ):
        """This method tests getting damage for the dinosaurs."""
        expected_health = current_health - amount
        # Initialize the robot's health with a value
        dinosaur_object.current_health = current_health
        remaining_health = dinosaur_object.get_damage(amount=amount)
        assert (
            remaining_health == expected_health
        ), "Check the Dinosaur damage function !"

    def test_basic_health(
        self, dinosaur_object, current_health: int = 30, health_ratio: float = 2
    ):
        """This method  tests the health bar values for the dinosaurs."""
        health_bar_value = current_health / health_ratio
        dinosaur_object.current_health = current_health

        remaining_health, draw = dinosaur_object.basic_health()
        assert (
            remaining_health == health_bar_value and draw
        ), "Check the basic health function and/or the visuals of the dinosaurs !"


class TestMonster:
    """This class tests the Robot class."""

    @pytest.mark.parametrize("speed,expected_position", [(0, 150), (5, 155)])
    def test_update(self, monster_object, speed, expected_position):
        """This method tests the update function for the Dinosaurs."""
        expected_health_bar_value = 100
        monster_object.speed = speed
        new_position, health_bar_value = monster_object.update()

        assert (
            new_position == expected_position
            and health_bar_value == expected_health_bar_value
        ), "Check the positions and/or the health_bar values of the Monster !"

    def test_get_damage(
        self, monster_object: Monster, current_health: int = 100, amount: int = 10
    ):
        """This method tests getting damage for the Monster."""
        expected_health = current_health - amount
        # Initialize the robot's health with a value
        monster_object.current_health = current_health
        remaining_health = monster_object.get_damage(amount=amount)
        assert remaining_health == expected_health, "Check the Monster damage function !"

    def test_basic_health(
        self, monster_object, current_health: int = 30, health_ratio: float = 5
    ):
        """This method  tests the health bar values for the Monster."""
        health_bar_value = current_health / health_ratio
        monster_object.current_health = current_health

        remaining_health, draw = monster_object.basic_health()
        assert remaining_health == health_bar_value, "Check Monster basic health!"
