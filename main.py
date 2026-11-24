"""News-image entry: decode the front-page image beside this file to the output dir.

The image is stored as base64 split across entry.png.b64.0 and entry.png.b64.1
(because a single file is too large to push in one API call).

Run locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The grader runs it with /output as the output dir and no network.
"""
import base64
import os
from pathlib import Path

here = Path(__file__).resolve().parent
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
b64 = (here / "entry.png.b64.0").read_text().strip()
b64 += (here / "entry.png.b64.1").read_text().strip()
data = base64.b64decode(b64)
(out_dir / "entry.png").write_bytes(data)
print(f"wrote {out_dir / 'entry.png'}")
