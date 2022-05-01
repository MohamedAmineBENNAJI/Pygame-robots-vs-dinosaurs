"""This module includes the tests for robot module."""
from core.utils.robot import Robot


class TestRobot:
    """This class tests the Robot class."""

    def test_get_damage(
        self, robot_object: Robot, current_health: int = 100, amount: int = 10
    ) -> None:
        """This method tests getting damage for the robot."""
        expected_health = current_health - amount
        # Initialize the robot's health with a value
        robot_object.current_health = current_health
        remaining_health = robot_object.get_damage(amount=amount)
        assert remaining_health == expected_health, "Check the Robot damage function !"

    def test_basic_health(
        self, robot_object: Robot, current_health: int = 30, health_ratio: float = 6.0
    ) -> None:
        """This method  tests the health bar values for the robot."""
        health_bar_value = current_health / health_ratio
        robot_object.current_health = current_health

        remaining_health, draw = robot_object.basic_health()
        assert (
            remaining_health == health_bar_value and draw
        ), "Check the basic health function and/or the visuals of the robot !"
