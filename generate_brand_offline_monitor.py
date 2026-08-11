import argparse
from pathlib import Path

from brand_offline_page_render import offline_monitor_html
from generate_brand_dashboard import (
    bullets,
    dedupe_items,
    in_window,
    load_rows,
    normalize,
    refresh_time,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--daily", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--window-start", default="2024-01-01")
    parser.add_argument("--window-end", default="2026-06-30")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    rows = normalize(load_rows(csv_path))
    window_rows = [
        row
        for row in rows
        if in_window(row.get("start_date", ""), args.window_start, args.window_end)
    ]
    summary = Path(args.daily).read_text(encoding="utf-8")
    suggestions = dedupe_items(bullets(summary, "## 对影石的即时建议"))
    window_label = f"{args.window_start} - {args.window_end}"
    html = offline_monitor_html(window_rows, suggestions, refresh_time(summary), window_label)
    Path(args.output).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
