from datetime import datetime
from pathlib import Path
import shutil


def main() -> None:
    base = Path("/Users/insta360/Documents/Codex/2026-06-09/new-chat")
    src = base / "brand-activity-material-library.csv"
    snap_dir = base / "snapshots"
    snap_dir.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    dst = snap_dir / f"brand-activity-material-library-{stamp}.csv"
    shutil.copy2(src, dst)
    print(dst)


if __name__ == "__main__":
    main()
