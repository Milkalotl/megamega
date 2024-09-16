from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional, Literal

import time
from subprocess import Popen


def watch_options(
    popen: Popen,
    player: Player,
    platform: SUPPORTED_PLATFORMS,
    media: Media,
    fzf_enabled: bool
) -> Optional[Literal["next", "previous", "select"]]:
    options = [
        "replay",
        "quit"
    ]

    if isinstance(media, Multi):
        options.insert(0, "next")
        options.insert(1, "previous")
        options.insert(2, "select")
    choice = prompt(
        text = f"Playing '{media.display_name}'",
        choices = options,
        display = lambda x: x,
        fzf_enabled = fzf_enabled
    )

    if choice == "quit":
        popen.kill()

    elif choice == "replay":
        popen.kill()

        new_popen = player.play(media)

        return watch_options(
            new_popen, player, platform, media, fzf_enabled
        )

    return choice