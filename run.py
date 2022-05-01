""" This module executes the game and its different scenarios."""
import logging
import sys

import pygame
from absl import app, flags

from core.utils.game import Game

flags.DEFINE_integer("screen_width", 600, "the width of the simulation space")
flags.DEFINE_integer("screen_height", 600, "the height of the simulation space")
flags.DEFINE_integer("number_of_dinosaur_rows", 3, "the number of dinosaurs per row")
flags.DEFINE_integer("number_of_dinosaur_cols", 4, "the number of dinosaurs per row")
flags.DEFINE_integer(
    "obstacle_amount", 4, "the number of obstacles in the simulation space"
)

flags.DEFINE_integer(
    "dinosaur_shooting_timer",
    800,
    "the timer in milliseconds for a random dinosaur to shoot.",
)
flags.DEFINE_bool(
    "moving_dinosaurs",
    False,
    "This boolean specifies if the dinosaurs are moving or not",
)

FLAGS = flags.FLAGS


def main(argv):
    """This function defines the main pipeline of the game."""
    flags.mark_flag_as_required("screen_width")
    flags.mark_flag_as_required("screen_height")
    flags.mark_flag_as_required("moving_dinosaurs")

    screen_width = FLAGS.screen_width
    screen_height = FLAGS.screen_height
    number_of_dinosaur_rows = FLAGS.number_of_dinosaur_rows
    number_of_dinosaur_cols = FLAGS.number_of_dinosaur_cols
    obstacle_amount = FLAGS.obstacle_amount

    dinosaur_shooting_timer = FLAGS.dinosaur_shooting_timer
    moving_dinosaurs = FLAGS.moving_dinosaurs
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    game = Game(
        screen,
        screen_width,
        screen_height,
        number_of_dinosaur_rows,
        number_of_dinosaur_cols,
        obstacle_amount,
        moving_dinosaurs,
    )
    DINOSAURLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(DINOSAURLASER, dinosaur_shooting_timer)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                logging.info("GAME OVER!")
                logging.info(f"Final Score:{game.score}")

            if event.type == DINOSAURLASER:
                game.dinosaur_shoot()

        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    app.run(main)
