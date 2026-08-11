from __future__ import annotations
import csv
import json
import re
import ssl
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


def read_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def rank_row(row: dict[str, str]) -> tuple[int, int]:
    source = (row.get("channel_source") or "").lower()
    priority = 0
    if "official" in source:
        priority += 5
    if "newsroom" in source or "news article" in source or "press" in source:
        priority += 3
    if "public media" in source or "hypebeast" in source or "prnasia" in source:
        priority += 2
    try:
        score = int(row.get("reuse_score_for_insta360") or "0")
    except ValueError:
        score = 0
    return priority, score


def fetch_text(url: str) -> str:
    request = Request(url, headers=HEADERS)
    context = ssl.create_default_context()
    with urlopen(request, timeout=20, context=context) as response:
        raw = response.read()
        charset = response.headers.get_content_charset() or "utf-8"
    return raw.decode(charset, errors="ignore")


def find_image_url(page_url: str, text: str) -> str:
    patterns = [
        r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+name=["\']twitter:image["\'][^>]+content=["\']([^"\']+)["\']',
        r'<img[^>]+src=["\']([^"\']+)["\']',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return urljoin(page_url, match.group(1))
    return ""


def safe_name(brand: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", brand).strip("_").lower()


def guess_extension(image_url: str) -> str:
    path = urlparse(image_url).path.lower()
    for ext in [".jpg", ".jpeg", ".png", ".webp"]:
        if path.endswith(ext):
            return ext
    return ".jpg"


def download_image(image_url: str, output_path: Path) -> bool:
    request = Request(image_url, headers=HEADERS)
    context = ssl.create_default_context()
    with urlopen(request, timeout=25, context=context) as response:
        data = response.read()
    if not data:
        return False
    output_path.write_bytes(data)
    return True


def main() -> None:
    base_dir = Path("/Users/insta360/Documents/Codex/2026-06-09/new-chat")
    csv_path = base_dir / "brand-activity-material-library.csv"
    out_dir = base_dir / "brand_card_covers"
    out_dir.mkdir(exist_ok=True)

    rows = read_rows(csv_path)
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["brand"], []).append(row)

    cover_map: dict[str, str] = {}
    for brand, brand_rows in grouped.items():
        ordered = sorted(brand_rows, key=rank_row, reverse=True)
        for row in ordered:
            url = row.get("source_url") or ""
            if not url.startswith("http"):
                continue
            try:
                text = fetch_text(url)
                image_url = find_image_url(url, text)
                if not image_url:
                    continue
                filename = safe_name(brand) + guess_extension(image_url)
                output_path = out_dir / filename
                if download_image(image_url, output_path):
                    cover_map[brand] = str(output_path)
                    break
            except Exception:
                continue

    (base_dir / "brand_cover_index.json").write_text(
        json.dumps(cover_map, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
