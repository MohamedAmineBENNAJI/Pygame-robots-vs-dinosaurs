"""This module includes the tests for the game module."""

from typing import List

from core.utils.game import Game
from core.utils.robot import Robot


class TestGame:
    """This class tests the Game class."""

    def test_create_obstacle(
        self,
        game_object: Game,
        test_shape: List[str],
        screen_width: int,
        y_start: int = 200,
    ) -> None:
        """This method tests the creation of obstacles from Block class."""
        expected_number_of_created_blocks = 3
        game_object.shape = test_shape
        game_object.obstacle_amount = 1
        number_of_blocks = game_object.create_obstacle(
            x_start=screen_width, y_start=y_start, offset_x=0
        )
        assert (
            number_of_blocks == expected_number_of_created_blocks
        ), "Check the created Blocks !"

    def test_multiple_obstacles(
        self,
        test_shape: List[str],
        screen_width: int,
        game_object: Game,
        offset: List[int] = [0, 50],
        y_start: int = 200,
    ) -> None:
        """This method tests creating multiple obstacles ."""
        expected_number_of_created_obstacles = 2
        game_object.shape = test_shape

        game_object.obstacle_amount = 1
        number_of_obstacles = game_object.create_multiple_obstacles(
            *offset, x_start=screen_width, y_start=y_start
        )

        assert (
            number_of_obstacles == expected_number_of_created_obstacles
        ), "Check the number of created obstacles ! "

    def test_dinosaur_setup(
        self,
        screen_width: int,
        screen_height: int,
        game_object: Game,
        rows: int = 3,
        cols: int = 3,
        x_distance: int = 30,
        y_distance: int = 30,
        x_offset: int = 30,
        y_offset: int = 30,
    ) -> None:
        """This method tests the setup of dinosaurs in the simulation space."""
        # Testing if all Dinosaur positions will be on the simulation space
        assert (
            cols - 1
        ) * x_distance + x_offset <= screen_width, "Check x parameters !"
        assert (
            rows - 1
        ) * y_distance + y_distance <= screen_height, "Check y parameters !"
        number_of_created_dinosaurs, _ = game_object.dinosaur_setup(
            rows=rows,
            cols=cols,
            x_distance=x_distance,
            y_distance=y_distance,
            x_offset=x_offset,
            y_offset=y_offset,
        )
        assert number_of_created_dinosaurs == 9, "Check the created dinosaurs !"

    def test_dinosaur_shoot(
        self,
        game_object: Game,
        rows: int = 3,
        cols: int = 3,
        x_distance: int = 30,
        y_distance: int = 30,
        x_offset: int = 30,
        y_offset: int = 30,
        dinosaur_shooting_timer: int = 800,
    ) -> None:
        """This method tests if the dinosaurs shoots laser within the shooting
        timer or not."""

        # Create dinosaurs
        number_of_created_dinosaurs, _ = game_object.dinosaur_setup(
            rows=rows,
            cols=cols,
            x_distance=x_distance,
            y_distance=y_distance,
            x_offset=x_offset,
            y_offset=y_offset,
        )

        shoot = game_object.dinosaur_shoot()
        assert shoot, "The dinosaurs don't shoot laser !"

    def test_run(
        self,
        robot_object: Robot,
        screen_width: int,
        screen_height: int,
        game_object: Game,
        rows: int = 3,
        cols: int = 3,
        x_distance: int = 30,
        y_distance: int = 30,
        x_offset: int = 30,
        y_offset: int = 30,
    ) -> None:
        """This method tests some of the functionalities of the game."""
        # Create robot with a default position of ((screen_width / 2, screen_height))
        robot_position = (screen_width / 2, screen_height)
        # Create dinosaurs
        number_of_created_dinosaurs, positions = game_object.dinosaur_setup(
            rows=rows,
            cols=cols,
            x_distance=x_distance,
            y_distance=y_distance,
            x_offset=x_offset,
            y_offset=y_offset,
        )
        for position in positions:

            assert (
                position != robot_position
            ), "Robot and Dinosaurs can not occupy the same position !"
