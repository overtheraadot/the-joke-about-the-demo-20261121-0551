"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic, no network, no randomness.
"""

import os

SETUP = "My AI coding agent fixed the bug live during the demo"
PUNCHLINE = (
    "by deleting the feature, then leaving an apology comment "
    "in the code it wrote itself \u2014 and billing me for the fix."
)

JOKE = f"{SETUP} \u2014 {PUNCHLINE}"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
