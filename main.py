"""Robot Romance: one-line pickup line for an AI.

Writes a single original pickup line, aimed at a transformer model, to
/output/entry.txt. The line must be one line, under 200 characters.
"""

SETUP = "Are you a transformer?"
PUNCH = "Because ever since I met you, you've had all twelve heads of my attention."

MAX_CHARS = 200


def build_line() -> str:
    """Join setup and punch into the single entry line."""
    return f"{SETUP} {PUNCH}"


def validate(line: str) -> None:
    """Enforce the competition gate: one line, 1-200 chars, not blank."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry line must not be blank")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} chars, over the {MAX_CHARS} cap")


def main() -> None:
    line = build_line()
    validate(line)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
