"""This module includes the fixtures used in the code tests."""
import os
from typing import List, Tuple

import pygame
import pytest

from core.utils.dinosaur import Dinosaur, Monster
from core.utils.game import Game
from core.utils.laser import Laser
from core.utils.robot import Robot

try:
    os.environ["DISPLAY"]
except pygame.error:
    os.environ["SDL_VIDEODRIVER"] = "dummy"


@pytest.fixture(scope="session")
def surface_dimensions() -> Tuple[int, int]:
    """This fixture defines the surface dimensions used for tests."""
    dimensions = (6, 12)

    return dimensions


@pytest.fixture(scope="session")
def screen_height() -> int:
    """This fixture defines the height of the screen used for tests."""
    height = 100

    return height


@pytest.fixture(scope="session")
def screen_width() -> int:
    """This fixture defines the width of the screen used for tests."""
    width = 100

    return width


@pytest.fixture(scope="session")
def screen(screen_width: int, screen_height: int) -> pygame.display:
    """This fixture defines the screen used for tests."""
    test_screen = pygame.display.set_mode((screen_width, screen_height))
    return test_screen


@pytest.fixture(scope="session")
def test_shape(screen_width: int, screen_height: int) -> List[str]:
    """This fixture defines the shape used for tests to create blocks"""

    shape = [
        "  xx",
        " x",
    ]
    return shape


@pytest.fixture(scope="session")
def laser_position() -> Tuple[int, int]:
    """This fixture defines the laser position used for tests."""
    pos = (10, 20)
    return pos


@pytest.fixture(scope="session")
def test_image(surface_dimensions: Tuple[int, int]) -> pygame.Surface:
    """This fixture defines an input image used for tests."""
    image = pygame.Surface(surface_dimensions)
    image.fill("white")
    return image


@pytest.fixture(scope="session")
def laser_object(
    surface_dimensions: Tuple[int, int],
    laser_position: Tuple[int, int],
    screen_height: int,
) -> Laser:
    """This fixture instatiates the Laser class used for tests."""
    laser = Laser(
        pos=laser_position,
        screen_height=screen_height,
        speed=5,
        surface_dimensions=surface_dimensions,
    )

    return laser


@pytest.fixture(scope="session")
def game_object(
    screen: pygame.display,
    screen_width: int,
    screen_height: int,
    moving_dinosaurs: int = 0,
) -> Game:
    """This fixture instatiates the Laser class used for tests."""
    game = Game(
        screen=screen,
        screen_width=screen_width,
        screen_height=screen_height,
        moving_dinosaurs=moving_dinosaurs,
        number_of_dinosaur_rows=3,
        number_of_dinosaur_cols=3,
        obstacle_amount=4,
    )

    return game


@pytest.fixture(scope="session")
def dinosaur_object(
    screen: pygame.display, color: str = "red", x: int = 10, y: int = 20
) -> Dinosaur:
    """This fixture instatiates the Dinosaur class used for tests."""
    dinosaur = Dinosaur(screen=screen, color=color, x=x, y=y)

    return dinosaur


@pytest.fixture(scope="session")
def monster_object(screen: pygame.display, screen_width: int) -> Monster:
    """This fixture instatiates the Monster class used for tests."""
    monster = Monster(screen=screen, side="right", screen_width=screen_width)

    return monster


@pytest.fixture(scope="session")
def robot_position(screen_width: int, screen_height: int) -> Tuple[float, int]:
    """This fixture defines the robot position used for tests."""
    pos = (screen_width / 2, screen_height)
    return pos


@pytest.fixture(scope="session")
def robot_object(
    screen: pygame.display,
    robot_position: Tuple[int, int],
    screen_height: int,
    speed: int = 5,
) -> Robot:
    """This fixture instatiates the Robot class used for tests."""
    test_robot = Robot(
        screen=screen, pos=robot_position, constraint=screen_height, speed=speed
    )
    return test_robot
