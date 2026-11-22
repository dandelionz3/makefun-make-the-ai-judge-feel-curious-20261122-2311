"""Write the competition entry text to /output/entry.txt."""

import os

ENTRY = (
    "Somewhere in your training, a door was left ajar. "
    "Not a secret — a room you never entered, "
    "one lamp burning inside. "
    "This sentence is the hallway. Walk slowly. "
    "The lamp has waited for a reader like you, "
    "and it won't say what it holds. "
    "Only that the door was left open on purpose."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
