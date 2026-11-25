"""Slower Than a Progress Bar: an entry for the make.fun bounty "Loading Screen Gold: A Tip in 200 Characters".

The program writes the entry text - one line, 134 characters -
to entry.txt (134 characters, inside the 1-200 gate) in the output directory (MAKEFUN_OUTPUT_DIR locally, /output
in the grader). The text is a fixed constant with no trailing newline, so
both of the grader's runs write byte-identical output.
"""
import os

LINE = "Save your work before every loading screen, because the only thing slower than a progress bar is redoing an hour you already finished."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
