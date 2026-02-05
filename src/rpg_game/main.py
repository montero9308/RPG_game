from __future__ import annotations

import pyglet

from rpg_game import config
from rpg_game.game import Game


class GameWindow(pyglet.window.Window):
    def __init__(self, game: Game) -> None:
        super().__init__(
            width=config.WINDOW_WIDTH,
            height=config.WINDOW_HEIGHT,
            caption=config.WINDOW_TITLE,
        )
        self.game = game

    def on_draw(self) -> None:
        self.clear()
        self.game.draw()


def main() -> None:
    game = Game()
    window = GameWindow(game)
    pyglet.clock.schedule_interval(game.update, 1 / 60)
    pyglet.app.run()
    _ = window


if __name__ == "__main__":
    main()
