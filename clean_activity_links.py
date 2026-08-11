import csv
from pathlib import Path


OFFICIAL_DETAIL_SOURCE_KEYS = [
    "official news article",
    "official newsroom",
    "official discover article",
    "official content page",
    "official editorial page",
    "official launch page",
    "official press",
]

OFFICIAL_ENTRY_SOURCE_KEYS = [
    "official store page",
    "official store locator",
    "official retail page",
    "official retail map",
    "official support page",
    "official community page",
    "official test-drive page",
    "official homepage",
    "official service page",
    "official service activity",
    "official membership",
    "membership rewards",
    "member benefits",
    "giftcard",
    "help article",
    "official referral page",
    "official coupon page",
    "official events page",
]

PUBLIC_REFERENCE_SOURCE_KEYS = [
    "prnasia",
    "pr newswire",
    "hypebeast",
    "media coverage",
    "business media",
    "public auto media",
    "award case",
    "marketing media coverage",
]


def classify_link(row: dict[str, str]) -> tuple[str, str]:
    source = (row.get("channel_source") or "").lower()
    url = (row.get("source_url") or "").lower()
    title = row.get("activity_name") or ""

    broken_hosts = [
        "mp.weixin.qq.com/s/",
        "gopro.com/en/us/news/gopro-announces-updated-max-360-camera-and-quik-reframe-editing",
        "ca.shokz.com/pages/2025-shokz-brand-day-rewards-terms-conditions",
        "www.nio.com/news",
        "www.lixiang.com/news",
    ]
    if any(token in url for token in broken_hosts):
        return "invalid", "链接不可直接打开或已失效"
    if url.endswith(".pdf"):
        return "reference", "PDF / 规则 / 证明页"
    if "terms page" in source or "规则" in title:
        return "reference", "活动规则或说明页"
    if any(key in source for key in PUBLIC_REFERENCE_SOURCE_KEYS):
        return "reference", "公开参考页"
    if (
        "入口" in title
        or "查询" in title
        or "预约" in title
        or "门店地图" in title
        or "活动中心" in title
        or "优惠券" in title
        or "邀请有礼" in title
        or "礼品卡" in title
    ):
        return "entry", "转化入口页"
    if any(key in source for key in OFFICIAL_ENTRY_SOURCE_KEYS):
        return "entry", "转化入口页"
    if any(key in source for key in OFFICIAL_DETAIL_SOURCE_KEYS):
        return "detail", "活动详情页"
    if "official campaign" in source or "campaign page" in source:
        return "detail", "官方活动页"
    return "reference", "公开参考页"


def classify_evidence(row: dict[str, str], link_type: str | None = None) -> tuple[str, str]:
    source = (row.get("channel_source") or "").lower()
    url = (row.get("source_url") or "").strip()
    resolved_link_type = link_type or classify_link(row)[0]
    if resolved_link_type == "invalid" or not url:
        return "invalid", "D级 · 失效待核"
    if any(key in source for key in OFFICIAL_DETAIL_SOURCE_KEYS) and resolved_link_type == "detail":
        return "direct", "A级 · 官方直证"
    if "official" in source:
        return "support", "B级 · 官方辅助"
    return "reference", "C级 · 公开参考"


def main() -> None:
    path = Path("/Users/insta360/Documents/Codex/2026-06-09/new-chat/brand-activity-material-library.csv")
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fieldnames = list(rows[0].keys())

    extra_fields = ["link_type", "link_note"]
    for field in extra_fields:
        if field not in fieldnames:
            fieldnames.append(field)

    cleaned = []
    for row in rows:
        link_type, link_note = classify_link(row)
        row["link_type"] = link_type
        row["link_note"] = link_note
        if link_type == "invalid":
            row["source_url"] = ""
        cleaned.append(row)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned)


if __name__ == "__main__":
    main()
