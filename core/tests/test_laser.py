"""This module includes the tests for laser module."""
from typing import Tuple

import pygame
import pytest

from core.utils.laser import Laser


class TestLaser:
    """This class tests the Laser class."""

    def test_update(
        self,
        test_image: pygame.Surface,
        laser_object: Laser,
        surface_dimensions: Tuple[int, int],
        laser_position: Tuple[int, int],
        speed: int = 5,
    ) -> None:
        """This method tests updating the laser position vertically according to
        a specific speed and positions"""
        expected_rect = test_image.get_rect(center=laser_position)

        expected_new_position = expected_rect.y + speed
        new_position = laser_object.update()
        assert new_position == expected_new_position, "Check the position of the laser!"

    # Testing the destruction of the laser with multiple values
    @pytest.mark.parametrize("position", [-51, 150])
    def test_destroy(self, position: int, laser_object: Laser) -> None:
        """This method checks the destruction of the laser."""
        laser_object.rect.y = position
        assert laser_object.destroy(), "Laser not destructed!"
