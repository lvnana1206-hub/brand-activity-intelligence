import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

from brand_page_meta import ACTIVITY_TYPE_META, PRIORITY_META, STATUS_META, ACTIVE_COLLECTION_BRANDS, STATUS_TABLE_GROUPS, brand_focus, brand_names
from brand_page_render import dashboard_html, overview_html, learning_timeline_html
from clean_activity_links import classify_evidence, classify_link


MONTH_META = {
    "01": {"label": "1月 / 新年启动", "holidays": ["元旦", "春节预热"], "theme": "开年拉新、会员唤醒、年度首发", "prediction_intro": "在新年启动和春节预热期"},
    "02": {"label": "2月 / 开年造势", "holidays": ["春节", "情人节", "开工"], "theme": "团圆送礼、情侣节点、返工复购", "prediction_intro": "在春节余温、情人节和开工节点"},
    "03": {"label": "3月 / 春季上新", "holidays": ["女性节", "春季上新"], "theme": "女性节点、新品首发、春季内容", "prediction_intro": "在女性节和春季焕新期"},
    "04": {"label": "4月 / 春季户外", "holidays": ["清明", "露营季"], "theme": "户外体验、城市社群、运动场景", "prediction_intro": "在清明、露营和春季户外窗口"},
    "05": {"label": "5月 / 五一与主题月", "holidays": ["五一", "母亲节", "520"], "theme": "假期出游、礼赠、情侣与家庭消费", "prediction_intro": "在五一、母亲节和 520 节点"},
    "06": {"label": "6月 / 618 与暑期预热", "holidays": ["儿童节", "618", "父亲节", "端午节"], "theme": "大促转化、亲子节点、男性礼赠、暑期预热", "prediction_intro": "在 618、父亲节和端午节窗口"},
    "07": {"label": "7月 / 暑期流量", "holidays": ["毕业季", "暑期"], "theme": "年轻人社交、旅行记录、门店体验", "prediction_intro": "在毕业季和暑期启动期"},
    "08": {"label": "8月 / 七夕与假日出行", "holidays": ["七夕", "暑期出游"], "theme": "情侣活动、节日打卡、联名出片", "prediction_intro": "在七夕和暑期出游窗口"},
    "09": {"label": "9月 / 秋季新品", "holidays": ["开学季", "中秋预热"], "theme": "秋季上新、校园人群、内容回流", "prediction_intro": "在开学季和秋季上新窗口"},
    "10": {"label": "10月 / 国庆黄金周", "holidays": ["国庆", "中秋窗口"], "theme": "全国巡回、出游打卡、线下大活动", "prediction_intro": "在国庆出游和黄金周节点"},
    "11": {"label": "11月 / 双11与社群复购", "holidays": ["双11", "会员大促"], "theme": "价格转化、会员复购、社群冲量", "prediction_intro": "在双11和会员复购冲刺期"},
    "12": {"label": "12月 / 年终节点", "holidays": ["双12", "圣诞", "跨年"], "theme": "礼物场景、年终复盘、跨年活动", "prediction_intro": "在双12、圣诞和跨年节点"},
}

MONTH_PREDICTIONS = {
    "01": ["新年开运抽奖", "会员开卡礼", "城市首场体验会"],
    "02": ["春节礼盒", "情侣双人活动", "返工唤醒券包"],
    "03": ["女性节限定礼盒", "女性创作者活动", "门店体验课"],
    "04": ["露营试拍日", "户外社群课", "城市跑团联动"],
    "05": ["五一出游打卡", "母亲节礼赠", "520 联名快闪"],
    "06": ["618 券包", "父亲节礼物推荐", "端午出游主题活动"],
    "07": ["毕业季任务赛", "暑期门店体验营", "旅行内容征集"],
    "08": ["七夕联名礼盒", "情侣打卡任务", "暑期城市快闪"],
    "09": ["开学季新手礼包", "秋季新品试用", "校园创作活动"],
    "10": ["国庆巡回活动", "旅行打卡挑战", "多城快闪空间"],
    "11": ["双11 会员券包", "社群复购冲刺", "老客加购权益"],
    "12": ["圣诞礼盒", "跨年主题活动", "年终会员回馈"],
}


def load_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def bullets(markdown_text: str, heading: str) -> list[str]:
    lines = markdown_text.splitlines()
    items, active = [], False
    for line in lines:
        if line.startswith("## "):
            active = line.strip() == heading
            continue
        if not active:
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip())
        elif stripped:
            break
    return items


def refresh_time(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        if line.startswith("最近一次刷新时间："):
            return line.split("：", 1)[1].strip()
    return "Unknown"


def normalize_date(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    parts = [p for p in re.split(r"[^0-9]", raw) if p]
    if len(parts) < 3:
        return raw
    year, month, day = parts[:3]
    return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"


def dedupe_items(items: list[str]) -> list[str]:
    seen = set()
    deduped = []
    for item in items:
        prefix = item.split("：", 1)[0].split(":", 1)[0].strip()
        key = prefix.upper() if prefix and len(prefix) <= 30 else item.strip().lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)
    return deduped


def coverage_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    collected = {row["brand"] for row in rows}
    output = []
    for group_zh, group_en, brands in STATUS_TABLE_GROUPS:
        group_label = group_zh
        for brand in brands:
            brand_zh, brand_en = brand_names(brand)
            if brand in collected:
                status_label = "已采集"
                status_class = "status-clean"
            elif brand in ACTIVE_COLLECTION_BRANDS:
                status_label = "采集中"
                status_class = "status-flagged"
            else:
                status_label = "待采集"
                status_class = ""
            output.append(
                {
                    "display_brand": brand_zh,
                    "group_label": group_label,
                    "status_label": status_label,
                    "status_class": status_class,
                }
            )
    return output


def channel_label(source: str) -> str:
    value = (source or "").lower()
    if "xiaohongshu" in value or "小红书" in value:
        return "小红书"
    if "weibo" in value or "微博" in value:
        return "微博"
    if "official newsroom" in value:
        return "官网新闻稿"
    if "official news article" in value:
        return "官方新闻稿"
    if "official news listing" in value:
        return "官网新闻列表"
    if "official press" in value:
        return "官网新闻稿"
    if "official discover article" in value:
        return "官网专题文章"
    if "official content page" in value or "official editorial page" in value:
        return "官网内容页"
    if "official developer conference page" in value:
        return "官方大会页"
    if "official launch page" in value:
        return "官方发布页"
    if "official store locator" in value or "store locator" in value:
        return "官方门店查询页"
    if "official retail page" in value or "retail map" in value:
        return "官方零售页"
    if "official store page" in value or "store page" in value:
        return "官方门店页"
    if "official test-drive page" in value:
        return "官方试驾预约页"
    if "official support" in value:
        return "官方支持页"
    if "service activity" in value:
        return "官方服务活动页"
    if "service page" in value or "official service" in value:
        return "官方服务页"
    if "official community" in value or "community page" in value:
        return "官方社区页"
    if "events page" in value:
        return "官方活动中心页"
    if "official campaign" in value or "campaign page" in value:
        return "官方活动页"
    if "terms page" in value:
        return "活动规则页"
    if "official membership" in value:
        return "官方会员页"
    if "member benefits" in value:
        return "会员权益说明页"
    if "membership rewards" in value:
        return "会员奖励页"
    if "giftcard" in value:
        return "礼品卡页"
    if "help article" in value:
        return "官网帮助页"
    if "homepage" in value:
        return "官网首页"
    if "official monthly update" in value:
        return "官网运营月报"
    if "pr newswire race release" in value:
        return "PR 赛事稿"
    if "prnasia retail release" in value:
        return "PR 门店稿"
    if "prnasia community race release" in value:
        return "PR 社群稿"
    if "pr newswire" in value or "prnasia" in value:
        return "PR 稿件"
    if "hypebeast retail pop-up coverage" in value:
        return "潮流媒体快闪报道"
    if "hypebeast store coverage" in value:
        return "潮流媒体门店报道"
    if "hypebeast release coverage" in value:
        return "潮流媒体发售报道"
    if "hypebeast event coverage" in value:
        return "潮流媒体活动报道"
    if "hypebeast collaboration coverage" in value:
        return "潮流媒体联名报道"
    if "hypebeast campaign coverage" in value:
        return "潮流媒体品牌日报道"
    if "hypebeast" in value:
        return "潮流媒体报道"
    if "public auto media" in value:
        return "汽车媒体报道"
    if "business media" in value:
        return "商业媒体报道"
    if "award case" in value:
        return "案例奖项页"
    if "media coverage on city community activation" in value:
        return "时尚媒体社群报道"
    if "media coverage" in value or "marketing media" in value:
        return "公开媒体报道"
    return "其他公开来源"


def activity_bucket(row: dict[str, str]) -> str:
    activity_type = row.get("activity_type", "")
    title = row.get("activity_name", "")
    source = row.get("channel_source", "")
    if row.get("wecom_or_private_traffic_hook") or "企微" in row.get("recommendation_for_insta360", ""):
        return "企微 / 私域转化"
    if activity_type in {"member_benefit", "member_service_activity", "member_app_presale", "member_referral"}:
        return "会员 / 复购机制"
    if activity_type == "test_drive_booking":
        return "预约转化"
    if activity_type == "store_experience":
        return "门店体验"
    if activity_type in {"community_operation", "community_run"}:
        return "社群活动"
    if activity_type == "product_launch":
        return "新品发布"
    if activity_type == "conference":
        return "大会活动"
    if activity_type == "brand_collab_offline_activation" or "联名" in title or "×" in title:
        return "联名 / IP 合作"
    if activity_type == "city_activation":
        return "线上线下联动"
    if "小红书" in source or "微博" in source:
        return "社媒引流"
    return "其他高质量活动"


def conversion_index(row: dict[str, str]) -> int:
    score = as_int(row.get("reuse_score_for_insta360", "0")) * 12
    activity_weight = {
        "test_drive_booking": 16,
        "member_referral": 14,
        "member_benefit": 13,
        "member_service_activity": 12,
        "member_app_presale": 12,
        "store_experience": 10,
        "community_operation": 9,
        "brand_collab_offline_activation": 8,
        "community_run": 7,
        "product_launch": 6,
    }
    score += activity_weight.get(row.get("activity_type", ""), 4)
    if row.get("member_only", "").lower() == "yes":
        score += 8
    if row.get("member_benefit"):
        score += 6
    if row.get("wecom_or_private_traffic_hook"):
        score += 5
    signup_flow = (row.get("signup_flow") or "").lower()
    threshold = (row.get("entry_threshold") or "").lower()
    if any(keyword in signup_flow for keyword in ["book", "预约", "register", "registration", "login", "submit", "preorder"]):
        score += 5
    if any(keyword in threshold for keyword in ["book", "预约", "register", "registration", "login", "deposit", "member"]):
        score += 4
    if row.get("online_offline") in {"offline", "hybrid"}:
        score += 4
    if "official" in (row.get("channel_source") or "").lower():
        score += 2
    return min(score, 100)


def propagation_index(row: dict[str, str]) -> int:
    score = 35
    source = (row.get("channel_source") or "").lower()
    if any(keyword in source for keyword in ["hypebeast", "xiaohongshu", "weibo", "media", "prnasia", "pr newswire"]):
        score += 18
    if row.get("ugc_or_creator_mechanic"):
        score += 12
    if row.get("offer_or_incentive"):
        score += 6
    if row.get("partnership_or_ip"):
        score += 8
    if row.get("online_offline") == "hybrid":
        score += 8
    if row.get("activity_type") in {"brand_collab_offline_activation", "community_run", "community_operation"}:
        score += 8
    return min(score, 100)


def activity_overall_index(row: dict[str, str]) -> int:
    return round(conversion_index(row) * 0.65 + propagation_index(row) * 0.35)


def is_launch_activity(row: dict[str, str]) -> bool:
    return row.get("activity_type") in {"product_launch", "conference"}


def overview_priority_index(row: dict[str, str]) -> int:
    score = activity_overall_index(row)
    if is_launch_activity(row):
        score -= 14
    if row.get("activity_type") in {"test_drive_booking", "store_experience", "community_operation", "community_run", "member_benefit", "member_service_activity", "brand_collab_offline_activation"}:
        score += 6
    if row.get("online_offline") in {"offline", "hybrid"}:
        score += 3
    return score


def build_timeline_cards(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    cards = []
    for month_key, meta in MONTH_META.items():
        month_rows = [row for row in rows if (row.get("start_date") or "")[5:7] == month_key]
        ranked_rows = sorted(
            month_rows,
            key=lambda row: (overview_priority_index(row), row.get("start_date", "")),
            reverse=True,
        )
        bucket_counts = Counter(row["activity_bucket"] for row in month_rows)
        brand_counts = Counter(row["brand_zh"] for row in month_rows)
        theme_suffix = "、".join(label for label, _ in bucket_counts.most_common(3)) or "待补活动主题"
        predicted_moves = MONTH_PREDICTIONS.get(month_key, ["会员活动", "门店体验", "节日联名"])
        prediction_text = (
            f"建议关注：{meta['prediction_intro']}，品牌更可能会推 "
            f"{predicted_moves[0]}、{predicted_moves[1]}、{predicted_moves[2]}。"
        )
        activities = [
            {
                "brand_zh": row["brand_zh"],
                "activity_name": row["activity_name"],
                "start_date": row["start_date"],
                "activity_bucket": row["activity_bucket"],
                "source_url": row.get("source_url", ""),
                "evidence_label": row.get("evidence_label", ""),
            }
            for row in ranked_rows[:3]
        ]
        cards.append(
            {
                "month_key": month_key,
                "month_label": meta["label"],
                "holiday_text": " / ".join(meta["holidays"]),
                "theme_text": f"{meta['theme']}；本月高频打法偏 {theme_suffix}",
                "brand_text": " / ".join(label for label, _ in brand_counts.most_common(4)) or "待补品牌",
                "bucket_text": " / ".join(label for label, _ in bucket_counts.most_common(4)) or "待补类型",
                "sample_count": len(month_rows),
                "activities": activities,
                "recommendation": ranked_rows[0]["recommendation_for_insta360"] if ranked_rows else "可优先补节日节点、会员权益、线下体验和联名活动样本。",
                "prediction_text": prediction_text,
            }
        )
    return cards


def overview_metrics(rows: list[dict[str, str]]) -> dict[str, object]:
    brand_scores: dict[str, list[int]] = {}
    for row in rows:
        brand_scores.setdefault(row["brand"], []).append(conversion_index(row))
    brand_ranking = []
    for brand, scores in brand_scores.items():
        avg_score = round(sum(scores) / len(scores))
        brand_ranking.append(
            {
                "brand": brand,
                "brand_zh": rows[[r["brand"] for r in rows].index(brand)]["brand_zh"],
                "avg_conversion_score": avg_score,
            }
        )
    brand_ranking.sort(key=lambda item: item["avg_conversion_score"], reverse=True)
    source_counts: dict[str, int] = {}
    for row in rows:
        label = row["channel_label"]
        source_counts[label] = source_counts.get(label, 0) + 1
    source_pairs = sorted(source_counts.items(), key=lambda item: item[1], reverse=True)[:12]
    best_brand = brand_ranking[0] if brand_ranking else {"brand_zh": "暂无", "avg_conversion_score": 0}
    activity_ranking = sorted(
        [
            {
                "brand_zh": row["brand_zh"],
                "activity_name": row["activity_name"],
                "overall_score": overview_priority_index(row),
                "activity_bucket": row["activity_bucket"],
            }
            for row in rows
        ],
        key=lambda item: item["overall_score"],
        reverse=True,
    )[:12]
    bucket_counts: dict[str, int] = {}
    for row in rows:
        bucket = row["activity_bucket"]
        bucket_counts[bucket] = bucket_counts.get(bucket, 0) + 1
    bucket_pairs = sorted(bucket_counts.items(), key=lambda item: item[1], reverse=True)
    return {
        "brand_ranking": brand_ranking[:10],
        "activity_ranking": activity_ranking,
        "bucket_pairs": bucket_pairs,
        "timeline_cards": build_timeline_cards(rows),
        "source_pairs": source_pairs,
        "best_brand_name": best_brand["brand_zh"],
        "best_brand_score": best_brand["avg_conversion_score"],
        "window_sample_count": len(rows),
        "source_category_count": len(source_counts),
    }


def as_int(value: str) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def in_window(date_value: str, start: str, end: str) -> bool:
    return bool(date_value) and start <= date_value <= end


def normalize(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    normalized = []
    for row in rows:
        link_type = (row.get("link_type") or "").strip()
        link_note = (row.get("link_note") or "").strip()
        if not link_type:
            link_type, link_note = classify_link(row)
        evidence_level, evidence_label = classify_evidence(row, link_type)
        if evidence_level == "invalid":
            row["source_url"] = ""
        brand_zh, brand_en = brand_names(row["brand"])
        focus_zh, focus_en = brand_focus(row["brand"])
        type_zh, type_en = ACTIVITY_TYPE_META.get(row["activity_type"], (row["activity_type"], row["activity_type"]))
        pr_zh, pr_en = PRIORITY_META.get(row["priority_tier"], (row["priority_tier"], row["priority_tier"]))
        st_zh, st_en = STATUS_META.get(row["review_status"], (row["review_status"], row["review_status"]))
        evidence_class = {
            "direct": "status-clean",
            "support": "",
            "reference": "status-flagged",
            "invalid": "status-flagged",
        }.get(evidence_level, "")
        normalized.append(
            {
                **row,
                "brand_zh": brand_zh,
                "brand_en": brand_en,
                "display_brand": brand_zh,
                "start_date": normalize_date(row.get("start_date", "")),
                "end_date": normalize_date(row.get("end_date", "")),
                "discovery_date": normalize_date(row.get("discovery_date", "")),
                "link_type": link_type,
                "link_note": link_note,
                "evidence_level": evidence_level,
                "evidence_label": evidence_label,
                "evidence_class": evidence_class,
                "china_focus_zh": focus_zh,
                "china_focus_en": focus_en,
                "activity_type_label": type_zh,
                "priority_label": f"{row['priority_tier']} · {pr_zh}",
                "status_label": st_zh,
                "channel_label": channel_label(row["channel_source"]),
                "activity_bucket": activity_bucket(row),
                "conversion_index": str(conversion_index(row)),
                "propagation_index": str(propagation_index(row)),
                "overall_index": str(activity_overall_index(row)),
            }
        )
    return normalized


def load_cover_map(base_dir: Path) -> dict[str, str]:
    cover_index = base_dir / "brand_cover_index.json"
    if not cover_index.exists():
        return {}
    try:
        return json.loads(cover_index.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def profiles(rows: list[dict[str, str]], cover_map: dict[str, str]) -> list[dict]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["brand"], []).append(row)

    items = []
    for brand, brand_rows in grouped.items():
        ordered = sorted(brand_rows, key=lambda row: (row.get("start_date", ""), as_int(row.get("reuse_score_for_insta360", "0"))), reverse=True)
        focus = next((row for row in ordered if row["country"] == "China" or row["region"] == "China"), ordered[0])
        items.append(
            {
                "brand": brand,
                "brand_zh": ordered[0]["brand_zh"],
                "brand_en": ordered[0]["brand_en"],
                "display_brand": ordered[0]["display_brand"],
                "priority_label": ordered[0]["priority_label"],
                "max_score": max(as_int(row["reuse_score_for_insta360"]) for row in brand_rows),
                "china_focus_zh": ordered[0]["china_focus_zh"],
                "china_focus_en": ordered[0]["china_focus_en"],
                "focus_activity_name": focus["activity_name"],
                "focus_activity_date": focus["start_date"],
                "focus_activity_url": focus["source_url"],
                "focus_link_type": focus.get("link_type", ""),
                "focus_link_note": focus.get("link_note", ""),
                "focus_evidence_label": focus.get("evidence_label", ""),
                "takeaway_zh": focus["recommendation_for_insta360"] or focus["insight_summary"],
                "takeaway_en": focus["insight_summary"],
                "best_rows": ordered[:3],
                "cover_image_url": cover_map.get(brand, ""),
            }
        )
    return sorted(items, key=lambda item: (item["priority_label"], -item["max_score"], item["brand_en"]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--daily", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--overview-output")
    parser.add_argument("--timeline-output")
    parser.add_argument("--window-start", default="2024-01-01")
    parser.add_argument("--window-end", default="2026-06-30")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    base_dir = csv_path.parent
    rows = normalize(load_rows(csv_path))
    cover_map = load_cover_map(base_dir)
    summary = Path(args.daily).read_text(encoding="utf-8")
    daily_suggestions = dedupe_items(bullets(summary, "## 对影石的即时建议"))
    weekly_mechanics = dedupe_items(bullets(summary, "## 今天最值得抄作业的 5 个机制"))
    Path(args.output).write_text(
        dashboard_html(rows, profiles(rows, cover_map), daily_suggestions, weekly_mechanics, refresh_time(summary), coverage_rows(rows)),
        encoding="utf-8",
    )

    if args.overview_output:
        window_rows = [
            row for row in rows
            if in_window(row.get("start_date", ""), args.window_start, args.window_end)
        ]
        overview_rows = [
            row for row in window_rows
            if as_int(row.get("reuse_score_for_insta360", "0")) >= 4
        ]
        overview_rows.sort(
            key=lambda row: (
                0 if is_launch_activity(row) else 1,
                overview_priority_index(row),
                row.get("start_date", ""),
            ),
            reverse=True,
        )
        label = f"{args.window_start} - {args.window_end}"
        metrics = overview_metrics(window_rows)
        Path(args.overview_output).write_text(overview_html(rows, overview_rows, label, metrics), encoding="utf-8")
        if args.timeline_output:
            Path(args.timeline_output).write_text(learning_timeline_html(rows, label, metrics), encoding="utf-8")


if __name__ == "__main__":
    main()
