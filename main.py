"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Candidate pitches drafted against the judging criteria (in stated order):
1. single sentence, ridiculous invention fixing a tiny everyday annoyance
2. funny — the laugh comes from the invention itself, not a bolted-on joke
3. clever fix — silly yet weirdly plausible
4. original
5. tight — annoyance + invention + mechanism, no clutter

Candidates (all one sentence, all 1-220 chars):
  A. The Sigh Charger: a phone charger that runs entirely on the long sigh
     you make when your battery hits 1%, converting pure exasperation
     into a full charge by morning. (165 chars)
  B. The Rescue Remote: the moment it slips down the side of the sofa, it
     fires a tiny flare and plays its own heroic theme tune until someone
     fishes it out. (152 chars)
  C. Every night while you sleep, your earbuds slowly do yoga, untangling
     themselves pose by pose, so you wake to straight cables and
     headphones limber enough to touch their toes. (174 chars)
  D. The Polite Doorbell: when a salesperson rings, it answers in your
     voice and books them in for a meeting in 2047, so you never have to
     pretend you are not home again. (165 chars)
  E. The Panic Mug: a coffee mug that reheats itself every time you forget
     it, by quietly vibrating with anxiety until your coffee is warm
     again. (140 chars)

PICK: A, the Sigh Charger. Why, criterion by criterion:
  1. One sentence naming the tiny annoyance (phone battery dying at 1%)
     and a ridiculous invention (a charger powered by sighing).
  2. The laugh IS the invention: a charger that runs on your exasperated
     sigh — the mechanism itself is the joke, no punchline bolted on.
     (C fails here: "limber enough to touch their toes" is a tacked-on
     joke; B splits its laugh across two mechanisms, flare AND theme tune.)
  3. Clever fix with a self-feeding loop: the annoyance itself causes the
     sigh that powers the fix, so the worse the battery, the more fuel —
     silly, yet weirdly plausible as energy harvesting.
  4. Original: a sigh-powered charger is a fresh absurdity, not the
     brief's alarm clock / sock / kettle and not a familiar gadget.
  5. Tight: 165 chars, annoyance + invention + mechanism, nothing else.

Deterministic by construction: ENTRY is a constant string, no input,
no randomness, no network, no clock — every run writes identical bytes.
No trailing newline: the file is exactly the 165-character sentence.
"""

import os

ENTRY = (
    "The Sigh Charger: a phone charger that runs entirely on the long sigh "
    "you make when your battery hits 1%, converting pure exasperation "
    "into a full charge by morning."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
