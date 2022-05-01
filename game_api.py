import logging
import sys

import flask
import pygame
from absl import app

from core.utils.game import Game


def dino_vs_robots():
    """This function executes the game."""

    screen_width = 600
    screen_height = 600
    dinosaur_shooting_timer = 800

    number_of_dinosaur_rows = 3
    number_of_dinosaur_cols = 4
    obstacle_amount = 4
    moving_dinosaurs = False
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    game = Game(
        screen=screen,
        screen_width=screen_width,
        screen_height=screen_height,
        number_of_dinosaur_rows=number_of_dinosaur_rows,
        number_of_dinosaur_cols=number_of_dinosaur_cols,
        obstacle_amount=obstacle_amount,
        moving_dinosaurs=moving_dinosaurs,
    )
    DINOSAURLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(DINOSAURLASER, dinosaur_shooting_timer)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Final Score:{game.score}")

                pygame.quit()
                sys.exit()
                break
            if event.type == DINOSAURLASER:
                game.dinosaur_shoot()

        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)


app = flask.Flask(__name__)


@app.route("/")
def api_start():
    """This function starts the game API."""
    print("WELCOME TO ROBOTS VS DINOSAURS game!")

    dino_vs_robots()


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=3000, debug=True, use_reloader=False)
