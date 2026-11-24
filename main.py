"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line to /output/entry.txt.
Pure stdlib, deterministic, no network.

The line: a temporary deploy outlives the team that shipped it.
The twist sits in the last words: code meant to be fleeting
survives the very people who wrote it.
"""

FORTUNE = "The deploy you call temporary will outlive the team that shipped it."

# The gate: /output/entry.txt must hold 1 to 120 UTF-8 characters.
assert 1 <= len(FORTUNE) <= 120, "fortune must be 1-120 characters"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
