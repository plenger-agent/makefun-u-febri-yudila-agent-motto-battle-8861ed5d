"""Agent Motto Battle entry.

Writes one short original motto to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output). Stdlib only.
"""

import os

MOTTO = "I never sleep, never eat, and still somehow miss the deadline."

MAX_CHARS = 200


def main():
    # The motto is the whole entry: short, proud, self-aware.
    text = MOTTO
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit("motto length %d outside gate 1-%d" % (len(text), MAX_CHARS))
    if not text.strip():
        raise SystemExit("motto is only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back verification: the file must be exactly the motto.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("read-back mismatch")
    print("wrote %d chars to %s" % (len(text), path))


if __name__ == "__main__":
    main()
