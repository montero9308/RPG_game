from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class MenuItem:
    key: str
    label_key: str
    children: List["MenuItem"] = field(default_factory=list)
    show_back: bool = True
    show_save: bool = False


def build_main_menu() -> MenuItem:
    return MenuItem(
        key="main",
        label_key="menu.main.title",
        show_back=False,
        children=[
            MenuItem(key="start_game", label_key="menu.main.start_game"),
            MenuItem(key="customize_avatar", label_key="menu.main.customize_avatar"),
            MenuItem(
                key="settings",
                label_key="menu.main.settings",
                children=[
                    MenuItem(
                        key="settings_video",
                        label_key="menu.settings.video",
                        show_save=True,
                        children=[
                            MenuItem(key="resolution", label_key="menu.video.resolution"),
                            MenuItem(key="fullscreen", label_key="menu.video.fullscreen"),
                            MenuItem(key="fps", label_key="menu.video.fps"),
                            MenuItem(key="quality", label_key="menu.video.quality"),
                            MenuItem(key="other_video", label_key="menu.video.other"),
                        ],
                    ),
                    MenuItem(
                        key="settings_audio",
                        label_key="menu.settings.audio",
                        show_save=True,
                        children=[
                            MenuItem(key="master_volume", label_key="menu.audio.master_volume"),
                            MenuItem(key="music_volume", label_key="menu.audio.music"),
                            MenuItem(key="effects_volume", label_key="menu.audio.effects"),
                            MenuItem(key="hd_audio", label_key="menu.audio.hd"),
                            MenuItem(key="other_audio", label_key="menu.audio.other"),
                        ],
                    ),
                    MenuItem(
                        key="settings_controls",
                        label_key="menu.settings.controls",
                        show_save=True,
                        children=[
                            MenuItem(
                                key="controls_pc",
                                label_key="menu.controls.pc",
                                children=[
                                    MenuItem(
                                        key="controls_pc_global",
                                        label_key="menu.controls.pc_global",
                                    ),
                                ],
                            ),
                            MenuItem(
                                key="controls_touch",
                                label_key="menu.controls.touch",
                                children=[
                                    MenuItem(
                                        key="controls_touch_layout",
                                        label_key="menu.controls.touch_layout",
                                    ),
                                    MenuItem(
                                        key="controls_touch_analog",
                                        label_key="menu.controls.touch_analog",
                                    ),
                                    MenuItem(
                                        key="controls_touch_actions",
                                        label_key="menu.controls.touch_actions",
                                    ),
                                ],
                            ),
                            MenuItem(
                                key="controls_joystick",
                                label_key="menu.controls.joystick",
                                children=[
                                    MenuItem(
                                        key="controls_joystick_compat",
                                        label_key="menu.controls.joystick_compat",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            MenuItem(key="about", label_key="menu.main.about"),
            MenuItem(key="exit", label_key="menu.main.exit"),
        ],
    )
