"""
Loads screenshots grouped by screen name.

Expected structure:
screenshots/<screen_name>/*.png
"""

import os
from typing import Dict, List


def load_screenshots(base_dir: str) -> Dict[str, List[str]]:
    screens = {}

    for screen_name in os.listdir(base_dir):
        screen_dir = os.path.join(base_dir, screen_name)
        if not os.path.isdir(screen_dir):
            continue

        images = [
            os.path.join(screen_dir, f)
            for f in os.listdir(screen_dir)
            if f.lower().endswith(".png")
        ]

        if images:
            screens[screen_name] = images

    return screens
