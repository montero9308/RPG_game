from __future__ import annotations

import pyglet

from rpg_game import config
from rpg_game.localization import load_localization
from rpg_game.ui.menu import build_main_menu


class Game:
    def __init__(self) -> None:
        self.clear_color = config.BACKGROUND_COLOR
        self.localization = load_localization("es")
        self.menu = build_main_menu()
        self.label = pyglet.text.Label(
            self.localization.get(self.menu.label_key),
            font_name="Arial",
            font_size=14,
            x=10,
            y=10,
        )

    def update(self, dt: float) -> None:
        _ = dt

    def draw(self) -> None:
        pyglet.gl.glClearColor(*self.clear_color)
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        self.label.draw()
