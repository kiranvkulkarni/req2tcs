"""
Builds the UI Intermediate Model (UIM) from screenshots.
"""

import os
from uim.models import Screen, ScreenState, UIComponent
from vision.ocr import extract_text


def build_screen(screen_name: str, image_paths: list) -> Screen:
    states = []

    for image_path in image_paths:
        state_name = os.path.basename(image_path).replace(".png", "")
        texts = extract_text(image_path)

        components = []
        for t in texts:
            # Simple, explicit heuristic (replace with vision model later)
            if "HDR" in t.upper():
                components.append(
                    UIComponent(label="HDR", state=state_name)
                )

        states.append(
            ScreenState(
                name=state_name,
                components=components
            )
        )

    return Screen(
        name=screen_name,
        states=states
    )
