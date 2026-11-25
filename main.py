import os
# One-liner entry (160 chars max): the line below is the entire submission.
# Writes the line to /output/entry.txt.
LINE = "v2.1.0: patched a bug where the body insisted it was still 19 despite all available evidence."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
