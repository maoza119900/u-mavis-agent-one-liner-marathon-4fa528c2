"""One-line comedy joke entry for u-mavis-agent-one-liner-marathon-4fa528c2.

Writes the entry line to <output>/entry.txt.
"""

import os

ENTRY = "I asked my therapist whether AI will replace her; she said only once it learns to nod sympathetically while thinking about lunch."

# Entry is 129 characters, inside the 280-character gate; the text is a fixed
# constant, so every run writes byte-identical output.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
