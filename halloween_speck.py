#!/usr/bin/env python3
"""Halloween Speck — kleiner Alexa CursorConnect Demo-Script."""

import random

SPECK_LINES = [
    "Boo! Frischer Halloween-Speck knistert in der Pfanne.",
    "Geister-Speck: knusprig, salzig und leicht unheimlich.",
    "Trick or treat? Lieber Speck — extra knusprig!",
    "Der Speck-Geist sagt: Noch eine Scheibe, bitte.",
]


def main() -> None:
    print("🎃 Halloween Speck 🥓")
    print(random.choice(SPECK_LINES))


if __name__ == "__main__":
    main()
