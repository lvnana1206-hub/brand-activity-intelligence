from __future__ import annotations
import html
import json
from datetime import date

from brand_page_meta import SOURCE_CHANNELS, UNIVERSE_GROUPS, brand_names


MONTH_META_TEXT = {
    "01": "1月 / 新年启动",
    "02": "2月 / 开年造势",
    "03": "3月 / 春季上新",
    "04": "4月 / 春季户外",
    "05": "5月 / 五一与主题月",
    "06": "6月 / 618 与暑期预热",
    "07": "7月 / 暑期流量",
    "08": "8月 / 七夕与假日出行",
    "09": "9月 / 秋季新品",
    "10": "10月 / 国庆黄金周",
    "11": "11月 / 双11与社群复购",
    "12": "12月 / 年终节点",
}

MONTH_HOLIDAYS_TEXT = {
    "01": "元旦 / 春节预热",
    "02": "春节 / 情人节 / 开工",
    "03": "女性节 / 春季上新",
    "04": "清明 / 露营季",
    "05": "五一 / 母亲节 / 520",
    "06": "儿童节 / 618 / 父亲节 / 端午节",
    "07": "毕业季 / 暑期",
    "08": "七夕 / 暑期出游",
    "09": "开学季 / 中秋预热",
    "10": "国庆 / 中秋窗口",
    "11": "双11 / 会员大促",
    "12": "双12 / 圣诞 / 跨年",
}

MONTH_THEME_TEXT = {
    "01": "开年拉新、会员唤醒、年度首发",
    "02": "团圆送礼、情侣节点、返工复购",
    "03": "女性节点、新品首发、春季内容",
    "04": "户外体验、城市社群、运动场景",
    "05": "假期出游、礼赠、情侣与家庭消费",
    "06": "大促转化、亲子节点、男性礼赠、暑期预热",
    "07": "年轻人社交、旅行记录、门店体验",
    "08": "情侣活动、节日打卡、联名出片",
    "09": "秋季上新、校园人群、内容回流",
    "10": "全国巡回、出游打卡、线下大活动",
    "11": "价格转化、会员复购、社群冲量",
    "12": "礼物场景、年终复盘、跨年活动",
}

MONTH_PREDICTION_INTRO_TEXT = {
    "01": "在新年启动和春节预热期",
    "02": "在春节余温、情人节和开工节点",
    "03": "在女性节和春季焕新期",
    "04": "在清明、露营和春季户外窗口",
    "05": "在五一、母亲节和 520 节点",
    "06": "在 618、父亲节和端午节窗口",
    "07": "在毕业季和暑期启动期",
    "08": "在七夕和暑期出游窗口",
    "09": "在开学季和秋季上新窗口",
    "10": "在国庆出游和黄金周节点",
    "11": "在双11和会员复购冲刺期",
    "12": "在双12、圣诞和跨年节点",
}

MONTH_PREDICTIONS_TEXT = {
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


def css() -> str:
    return """
    :root{--bg:#f7f2ff;--panel:#fffaff;--ink:#22193b;--muted:#74658f;--line:#e8dcff;--accent:#f15bc1;--accent2:#7d63ff;--soft:#f8dcff;--good:#169d87;--warn:#c6841d;--shadow:0 12px 30px rgba(109,84,171,.10)}
    *{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:"PingFang SC","Noto Sans SC","Helvetica Neue",Arial,sans-serif;background:linear-gradient(180deg,#fff8fe 0%,var(--bg) 58%,#eef5ff 100%)}a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
    .wrap{max-width:1480px;margin:0 auto;padding:20px 16px 48px}.hero{background:linear-gradient(135deg,#ff78d1 0%,#9a6bff 52%,#5dc7ff 100%);color:#fff;border-radius:28px;padding:26px;box-shadow:0 22px 54px rgba(117,77,181,.20)}.nav{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:14px}.nav a{padding:9px 14px;border-radius:999px;background:rgba(255,255,255,.16);color:#fff}.nav a.active{background:#fff;color:#d94cb0}
    .bi{display:flex;flex-direction:column;gap:2px}.zh{font-weight:700}.heroTitle .zh{font-size:32px}.heroDesc{margin-top:10px;max-width:780px;line-height:1.6}
    .stats,.charts,.brandGrid,.sourceGrid,.universeGrid,.overviewGrid,.heroCharts{display:grid;gap:14px}.stats{grid-template-columns:repeat(4,minmax(0,1fr));margin-top:18px}.heroCharts{grid-template-columns:1fr 1.2fr;margin-top:18px}.layout{display:grid;grid-template-columns:minmax(0,1.2fr) 360px;gap:18px;margin-top:18px;align-items:start}.stack{display:grid;gap:18px}.side{position:sticky;top:16px}
    .dashboard-shell{margin-top:18px}
    .panel,.metric,.box,.heroHighlight{background:var(--panel);border:1px solid var(--line);border-radius:22px;color:var(--ink);box-shadow:var(--shadow)}.panel,.box,.heroHighlight{padding:18px}.metric{padding:16px}.heroHighlight{background:rgba(255,255,255,.96)}.value{font-size:28px;font-weight:800;margin-top:8px;color:var(--ink)}.muted{color:var(--muted)}
    .toolbar{display:flex;gap:12px;flex-wrap:wrap;margin:14px 0}.toolbar>*{flex:1 1 180px}input,select{width:100%;border:1px solid var(--line);border-radius:12px;padding:11px 12px;background:#fff;color:var(--ink)}
    table{width:100%;border-collapse:collapse}th,td{text-align:left;padding:12px 8px;vertical-align:top;border-bottom:1px solid #eee5db}th{font-size:12px;color:var(--muted);letter-spacing:.04em}td{font-size:14px;line-height:1.5}
    .small{font-size:12px;color:var(--muted);line-height:1.5}.pill{display:inline-flex;align-items:center;border-radius:999px;padding:4px 10px;font-size:12px;background:var(--soft);color:var(--accent);font-weight:700}
    .chartRow{display:grid;grid-template-columns:minmax(0,180px) minmax(0,1fr) 34px;gap:10px;align-items:center;margin-top:12px}.track{height:12px;background:#eee3ff;border-radius:999px;overflow:hidden}.fill{height:100%;background:linear-gradient(90deg,var(--accent2),#5dc7ff);border-radius:999px}.fill.alt{background:linear-gradient(90deg,var(--accent),#ff9ada)}.fill.strong{background:linear-gradient(90deg,#8057ff,#ff74c7)}
    .brandCard{padding:18px;border-radius:20px;border:1px solid var(--line);background:#fffaff;color:var(--ink);box-shadow:var(--shadow)}.brandCard a,.box a,.panel a{color:var(--accent)}.brandTop{display:flex;justify-content:space-between;gap:10px;align-items:start;margin-bottom:12px}.brand-card-cover{width:100%;height:180px;border-radius:16px;object-fit:cover;background:linear-gradient(135deg,#ffd9f2 0%,#e5dcff 54%,#d3efff 100%);border:1px solid #ebdcff;margin:12px 0}.focus{padding:14px;border-radius:16px;background:#fff2fb;border:1px solid #f0d6fb;margin:12px 0;color:var(--ink)}.sectionTitle{margin:0 0 8px;font-size:14px;color:var(--ink)}.list{margin:8px 0 0;padding-left:18px}.sourceGrid,.universeGrid{grid-template-columns:repeat(2,minmax(0,1fr))}.overviewGrid{grid-template-columns:repeat(3,minmax(0,1fr))}.timelineFacts{display:grid;gap:8px;margin-top:10px}.timelineFacts p{margin:0}.timelineActivities{margin:10px 0 0;padding-left:18px}
    .status-clean{color:var(--good);font-weight:700}.status-flagged{color:var(--warn);font-weight:700}.note{padding:12px;border-radius:14px;background:#fff2fb;border:1px solid #efd5fb}.headline{font-size:14px;color:rgba(255,255,255,.88)}.bigBrand{font-size:30px;font-weight:800;margin-top:8px}.bigScore{font-size:48px;font-weight:800;line-height:1;margin-top:12px;color:var(--accent)}.heroHighlight .small{color:#71618d}
    @media (max-width:1180px){.layout,.stats,.charts,.brandGrid,.sourceGrid,.universeGrid,.overviewGrid,.heroCharts{grid-template-columns:1fr}.side{position:static}}
    """


def bi(zh: str, en: str, tag: str = "div", cls: str = "bi") -> str:
    return f"<{tag} class='{cls}'><span class='zh'>{html.escape(zh)}</span></{tag}>"


def row_is_clickable(row: dict) -> bool:
    return bool(row.get("source_url")) and row.get("link_type") != "invalid"


def row_link_html(row: dict, title=None) -> str:
    text = html.escape(title or row["activity_name"])
    if row_is_clickable(row):
        return f"<a href='{html.escape(row['source_url'])}' target='_blank' rel='noreferrer'>{text}</a>"
    return text


def nav(current: str) -> str:
    o = "active" if current == "overview" else ""
    d = "active" if current == "dashboard" else ""
    f = "active" if current == "offline" else ""
    t = "active" if current == "timeline" else ""
    return (
        "<div class='nav'>"
        f"<a class='{o}' href='brand-activity-overview.html'>年度总览</a>"
        f"<a class='{d}' href='brand-activity-dashboard.html'>品牌活动情报看板</a>"
        f"<a class='{f}' href='brand-offline-activity-monitor.html'>线下活动专项页</a>"
        f"<a class='{t}' href='brand-activity-learning-timeline.html'>品牌活动学习时间线</a>"
        "</div>"
    )


def chart_rows(items: list[tuple[str, int]], style: str = "") -> str:
    max_count = max((count for _, count in items), default=1)
    out = []
    for label, count in items:
        width = round(count / max_count * 100, 2) if max_count else 0
        out.append(f"<div class='chartRow'><div>{html.escape(label)}</div><div class='track'><div class='fill {style}' style='width:{width}%'></div></div><div class='small'>{count}</div></div>")
    return "".join(out)


def list_html(items: list[str]) -> str:
    return "".join(f"<li>{html.escape(item)}</li>" for item in items[:5]) or "<li>待补充</li>"


def dedupe_lines(items: list[str]) -> list[str]:
    seen = set()
    output = []
    for item in items:
        key = item.strip().lower()
        if key in seen:
            continue
        seen.add(key)
        output.append(item)
    return output


def non_launch_priority(row: dict) -> int:
    return 0 if row.get("activity_type") in {"product_launch", "conference"} else 1


def top_conversion_rows(rows: list[dict], limit: int = 8) -> list[dict]:
    return sorted(
        rows,
        key=lambda row: (
            non_launch_priority(row),
            int(row.get("conversion_index") or 0),
            int(row.get("reuse_score_for_insta360") or 0),
            1 if row.get("online_offline") in {"offline", "hybrid"} else 0,
            row.get("start_date") or "",
        ),
        reverse=True,
    )[:limit]


def suggestion_title(row: dict) -> str:
    mapping = {
        "企微 / 私域转化": "私域承接",
        "会员 / 复购机制": "会员复购",
        "门店体验": "门店体验",
        "预约转化": "预约转化",
        "社群活动": "社群运营",
        "联名 / IP 合作": "联名打卡",
        "线上线下联动": "线上线下联动",
        "新品发布": "新品收口",
        "大会活动": "大会承接",
    }
    return mapping.get(row.get("activity_bucket", ""), "高分机制")


def has_cjk(text: str) -> bool:
    return any("\u4e00" <= ch <= "\u9fff" for ch in text or "")


def derived_suggestions(rows: list[dict], limit: int = 8) -> list[str]:
    suggestions = []
    for row in top_conversion_rows(rows, limit=limit * 2):
        tail = row.get("recommendation_for_insta360") or row.get("insight_summary") or row.get("core_mechanic") or row["activity_name"]
        suggestions.append(f"{suggestion_title(row)}：参考{row['display_brand']}的《{row['activity_name']}》，{tail}")
    return dedupe_lines(suggestions)[:limit]


def derived_mechanics(rows: list[dict], limit: int = 8) -> list[str]:
    items = []
    for row in top_conversion_rows(rows, limit=limit * 2):
        core_mechanic = row.get("core_mechanic") or ""
        if not has_cjk(core_mechanic):
            core_mechanic = row.get("activity_type_label") or row["activity_name"]
        mechanic = core_mechanic
        signal = row.get("conversion_signal") or row.get("offer_or_incentive") or row.get("link_note") or "清晰转化动作"
        if not has_cjk(signal):
            signal = row.get("link_note") or row.get("activity_bucket") or "清晰转化动作"
        items.append(f"{suggestion_title(row)}：{row['display_brand']}用{mechanic}，通过{signal}完成转化。")
    return dedupe_lines(items)[:limit]


def estimated_conversion_rate_label(row: dict) -> str:
    score = int(row.get("conversion_index") or row.get("overall_index") or 0)
    if score >= 95:
        return "8% - 12%"
    if score >= 90:
        return "6% - 8%"
    if score >= 80:
        return "4% - 6%"
    if score >= 70:
        return "2.5% - 4%"
    if score >= 60:
        return "1.5% - 2.5%"
    return "< 1.5%"


def checklist_html(items: list[str]) -> str:
    if not items:
        return "<li>待补充</li>"
    bullets = []
    for item in items[:3]:
        text = item.split("：", 1)[1].strip() if "：" in item else item
        bullets.append(f"<li>[ ] {html.escape(text)}</li>")
    return "".join(bullets)


def score_panel() -> str:
    return (
        "<div class='panel'>"
        f"{bi('品牌建议分是什么','Brand Reuse Score','h2','bi')}"
        "<div class='note' style='margin-top:12px'>"
        "<p><strong>5 分：可以直接复用</strong>，适合直接转成会员、企微或购买动作。</p>"
        "<p><strong>4 分：高价值参考</strong>，核心机制强，只需小幅改造。</p>"
        "<p><strong>3 分：中等参考</strong>，更适合作为灵感，不适合原样照搬。</p>"
        "<p><strong>2-1 分：弱相关</strong>，重在观察品牌表达，不做直接执行模板。</p>"
        "<p class='small'>品牌建议分看的是“这家品牌当前最值得影石优先拆解的活动上限”，不是品牌真实成交转化率。</p>"
        "</div></div>"
    )


def evidence_panel() -> str:
    return (
        "<div class='panel'>"
        f"{bi('证据等级说明', '', 'h2', 'bi')}"
        "<div class='note' style='margin-top:12px'>"
        "<p><strong>A级 · 官方直证</strong>：官网新闻、官方活动正文、官方发布页，可直接作为高置信参考。</p>"
        "<p><strong>B级 · 官方辅助</strong>：门店页、会员页、试驾页、规则页、商城入口，适合看转化路径。</p>"
        "<p><strong>C级 · 公开参考</strong>：公开媒体、案例页、攻略页，用来补机制与活动外观。</p>"
        "<p><strong>D级 · 失效待核</strong>：链接失效或公开访问不稳定，需后续补证。</p>"
        "</div></div>"
    )


def coverage_status_table(rows: list[dict]) -> str:
    body = "".join(
        f"<tr><td><strong>{html.escape(row['display_brand'])}</strong></td><td>{html.escape(row['group_label'])}</td><td class='{row['status_class']}'>{html.escape(row['status_label'])}</td></tr>"
        for row in rows
    )
    return "<div class='panel'>" + bi("品牌覆盖状态表", "", "h2", "bi") + "<table style='margin-top:12px'><thead><tr><th>品牌</th><th>分组</th><th>状态</th></tr></thead><tbody>" + body + "</tbody></table></div>"


def source_cards() -> str:
    cards = []
    for zh, _en, use_zh, _use_en in SOURCE_CHANNELS:
        cards.append(f"<div class='box'><h4 class='sectionTitle'>{html.escape(zh)}</h4><p>{html.escape(use_zh)}</p></div>")
    return "".join(cards)


def universe_cards() -> str:
    cards = []
    for zh, _en, brands in UNIVERSE_GROUPS:
        pills = "".join(f"<span class='pill' style='margin:4px 6px 0 0'>{html.escape(brand_names(brand)[0])}</span>" for brand in brands)
        cards.append(f"<div class='box'><h4 class='sectionTitle'>{html.escape(zh)}</h4><div>{pills}</div></div>")
    return "".join(cards)


def brand_card(profile: dict) -> str:
    best = "".join(
        (
            f"<li>{row_link_html(row)}"
            f"<div class='small'>{html.escape(row['start_date'] or 'Date TBD')} · {html.escape(row['activity_type_label'])} · {html.escape(row.get('link_note',''))} · {html.escape(row.get('evidence_label',''))}</div></li>"
        )
        for row in profile["best_rows"]
    )
    cover = ""
    cover_url = profile.get("cover_image_url", "")
    if cover_url:
        cover = f"<img class='brand-card-cover' src='{html.escape(cover_url)}' alt='{html.escape(profile['brand_zh'])} 封面图'>"
    else:
        cover = "<div class='brand-card-cover'></div>"
    if profile.get("focus_link_type") != "invalid" and profile.get("focus_activity_url"):
        focus_link = f"<a href='{html.escape(profile['focus_activity_url'])}' target='_blank' rel='noreferrer'>{html.escape(profile['focus_activity_name'])}</a>"
    else:
        focus_link = html.escape(profile['focus_activity_name'])
    return (
        "<article class='brandCard'>"
        f"<div class='brandTop'><div>{bi(profile['brand_zh'], profile['brand_en'], 'h3', 'bi')}</div><span class='pill'>{html.escape(profile['priority_label'])}</span></div>"
        f"{cover}"
        f"<div class='focus'>{bi('中国区重点转化活动', '', 'h4', 'sectionTitle bi')}"
        f"{focus_link}"
        f"<div class='small'>{html.escape(profile['focus_activity_date'] or 'Date TBD')} · {html.escape(profile.get('focus_link_note',''))} · {html.escape(profile.get('focus_evidence_label',''))}</div></div>"
        f"<div>{bi('中国区转化重点', '', 'h4', 'sectionTitle bi')}<p>{html.escape(profile['china_focus_zh'])}</p></div>"
        f"<div style='margin-top:14px'>{bi('近一年优势活动', '', 'h4', 'sectionTitle bi')}<ul class='list'>{best}</ul></div>"
        f"<div style='margin-top:14px'>{bi('给影石的启发', '', 'h4', 'sectionTitle bi')}<p>{html.escape(profile['takeaway_zh'])}</p></div>"
        "</article>"
    )


def dashboard_html(rows: list[dict], profiles: list[dict], suggestions: list[str], mechanics: list[str], refresh_time: str, coverage_rows: list[dict]) -> str:
    rows_json = html.escape(json.dumps(rows, ensure_ascii=False))
    expanded_suggestions = dedupe_lines(suggestions + derived_suggestions(rows, limit=8))[:8]
    expanded_mechanics = dedupe_lines(mechanics + derived_mechanics(rows, limit=8))[:8]
    activity_pairs = sorted([(label, count) for label, count in __import__("collections").Counter(row["activity_type_label"] for row in rows).items()], key=lambda x: x[1], reverse=True)[:8]
    brand_pairs = [(profile["display_brand"], profile["max_score"]) for profile in profiles]
    offline_rows = [row for row in rows if row.get("online_offline") in {"offline", "hybrid"}]
    offline_count = len(offline_rows)
    offline_high_score = sum(1 for row in offline_rows if int(row.get("reuse_score_for_insta360") or 0) >= 4)
    offline_branch_counts = __import__("collections").Counter(row["activity_type_label"] for row in offline_rows)
    offline_branch_list = "".join(
        f"<li><strong>{html.escape(label)}</strong><span class='small'> · {count} 条</span></li>"
        for label, count in offline_branch_counts.most_common(6)
    ) or "<li>待补充</li>"
    current_month = refresh_time[:7] if len(refresh_time) >= 7 else ""
    current_month_rows = [row for row in rows if (row.get("start_date") or "").startswith(current_month)]
    current_month_stats = {}
    for row in current_month_rows:
        brand = row["display_brand"]
        if brand not in current_month_stats:
            current_month_stats[brand] = {"count": 0, "max_score": 0, "latest_activity": row["activity_name"]}
        current_month_stats[brand]["count"] += 1
        current_month_stats[brand]["max_score"] = max(current_month_stats[brand]["max_score"], int(row.get("reuse_score_for_insta360") or 0))
        current_month_stats[brand]["latest_activity"] = row["activity_name"]
    current_month_rank = sorted(
        current_month_stats.items(),
        key=lambda item: (item[1]["count"], item[1]["max_score"]),
        reverse=True,
    )[:6]
    current_month_channel_stats = {}
    for row in current_month_rows:
        channel = row.get("channel_label") or "其他公开来源"
        current_month_channel_stats[channel] = current_month_channel_stats.get(channel, 0) + 1
    current_month_channel_rank = sorted(
        current_month_channel_stats.items(),
        key=lambda item: item[1],
        reverse=True,
    )[:6]
    current_month_type_stats = {}
    for row in current_month_rows:
        activity_type = row.get("activity_type_label") or "其他高质量活动"
        current_month_type_stats[activity_type] = current_month_type_stats.get(activity_type, 0) + 1
    current_month_type_rank = sorted(
        current_month_type_stats.items(),
        key=lambda item: item[1],
        reverse=True,
    )[:6]
    current_month_list = "".join(
        f"<li><strong>{html.escape(brand)}</strong><span class='small'> · 本月样本 {stats['count']} 条 · 最高建议分 {stats['max_score']}</span><div class='small'>{html.escape(stats['latest_activity'])}</div></li>"
        for brand, stats in current_month_rank
    ) or "<li>本月暂无新增样本，可优先补门店活动、会员页和社媒引流样本。</li>"
    current_month_channel_list = "".join(
        f"<li><strong>{html.escape(channel)}</strong><span class='small'> · 本月样本 {count} 条</span></li>"
        for channel, count in current_month_channel_rank
    ) or "<li>本月暂无重点渠道样本。</li>"
    current_month_type_list = "".join(
        f"<li><strong>{html.escape(activity_type)}</strong><span class='small'> · 本月样本 {count} 条</span></li>"
        for activity_type, count in current_month_type_rank
    ) or "<li>本月暂无重点活动类型样本。</li>"
    offline_rows_sorted = sorted(
        offline_rows,
        key=lambda row: (int(row.get("reuse_score_for_insta360") or 0), row.get("start_date") or ""),
        reverse=True,
    )[:8]
    offline_priority_list = "".join(
        f"<li><strong>{html.escape(row['display_brand'])}</strong>：<a href='{html.escape(row['source_url'])}' target='_blank' rel='noreferrer'>{html.escape(row['activity_name'])}</a><div class='small'>{html.escape(row['start_date'] or 'Date TBD')} · {html.escape(row['activity_type_label'])} · {html.escape(row['online_offline'])}</div></li>"
        if row.get("link_type") == "detail" and row.get("source_url")
        else f"<li><strong>{html.escape(row['display_brand'])}</strong>：{html.escape(row['activity_name'])}<div class='small'>{html.escape(row['start_date'] or 'Date TBD')} · {html.escape(row['activity_type_label'])} · {html.escape(row['online_offline'])}</div></li>"
        for row in offline_rows_sorted
    ) or "<li>暂无重点线下样本。</li>"
    offline_type_counts = __import__("collections").Counter(row["activity_type_label"] for row in offline_rows)
    top_offline_types = [label for label, _ in offline_type_counts.most_common(4)]
    offline_template_list = "".join(
        f"<li><strong>{html.escape(label)}</strong>：优先拆活动报名入口、到店动线、现场体验环节、会员承接和复购激励。</li>"
        for label in top_offline_types
    ) or "<li>优先拆门店体验、社群活动、联名快闪和预约转化这四类线下模型。</li>"
    top_brand_list = "".join(
        f"<li><strong>{html.escape(profile['display_brand'])}</strong><span class='small'> · 建议分 {profile['max_score']}</span></li>"
        for profile in profiles[:8]
    ) or "<li>待补充</li>"
    latest_rows = [
        row
        for row in sorted(
            rows,
            key=lambda row: (
                row.get("discovery_date") or "",
                row.get("start_date") or "",
                int(row.get("reuse_score_for_insta360") or 0),
            ),
            reverse=True,
        )
        if row.get("link_type") in {"detail", "reference"} and row.get("source_url")
    ][:8]
    latest_activity_list = "".join(
        f"<li><strong>{html.escape(row['display_brand'])}</strong>：{row_link_html(row)}<div class='small'>{html.escape(row['start_date'] or 'Date TBD')} · {html.escape(row['activity_type_label'])} · {html.escape(row.get('link_note',''))} · {html.escape(row.get('evidence_label',''))}</div></li>"
        for row in latest_rows
    ) or "<li>暂无可直接打开的高质量正文或参考页，可在样本库中查看“转化入口页 / 参考页”类型样本。</li>"
    conversion_rows = top_conversion_rows(rows, limit=8)
    conversion_rate_list = "".join(
        f"<li><strong>{html.escape(row['display_brand'])}</strong>：{row_link_html(row)}<div class='small'>预估转化率区间 {html.escape(estimated_conversion_rate_label(row))} · {html.escape(row.get('evidence_label',''))} · {html.escape(row.get('activity_bucket',''))}</div></li>"
        for row in conversion_rows
    ) or "<li>待补充</li>"
    table_rows = "".join(
        f"<tr><td><strong>{html.escape(row['display_brand'])}</strong><div class='small'>{html.escape(row['priority_label'])} · {html.escape(row['online_offline'] or 'unknown')}</div></td><td>{row_link_html(row)}<div class='small'>{html.escape(row['start_date'] or 'Date TBD')} · {html.escape(row.get('link_note',''))}</div><div class='small'>{html.escape(row['insight_summary'])}</div></td><td>{html.escape(row['activity_type_label'])}</td><td class='{html.escape(row.get('evidence_class',''))}'>{html.escape(row.get('evidence_label',''))}</td><td>{html.escape(row['reuse_score_for_insta360'] or '-')}</td><td class='{'status-flagged' if row['review_status']=='seeded_with_inference' else 'status-clean'}'>{html.escape(row['status_label'])}</td></tr>"
        for row in rows
    )
    brand_cards = "".join(brand_card(profile) for profile in profiles)
    action_panel = "<div class='panel'>" + bi("影石行动建议", "", "h2", "bi") + "<p class='small'>基于日更建议和高分样本自动补强，优先放最值得立刻执行的动作。</p>" + f"<ul class='list'>{''.join(f'<li>{html.escape(item)}</li>' for item in expanded_suggestions)}</ul></div>"
    summary_detail_panels = (
        "<div class='charts'>"
        f"<div class='panel'>{bi('高分品牌速览', '', 'h2', 'bi')}<p class='small'>按当前品牌建议分从高到低快速浏览，适合先决定“先抄谁”。</p><ul class='list'>{top_brand_list}</ul></div>"
        f"<div class='panel'>{bi('最近几天活动速览', '', 'h2', 'bi')}<p class='small'>优先按最近几天的抓取与活动时间排序，先看这轮最新补进来的动作；官方直证与公开参考已明确区分。</p><ul class='list'>{latest_activity_list}</ul></div>"
        f"<div class='panel'>{bi('高转化活动预估转化率', '', 'h2', 'bi')}<p class='small'>公开真实转化率通常不可得，这里基于报名门槛、私域承接、会员权益、补贴力度和到店链路做预估转化率区间。</p><ul class='list'>{conversion_rate_list}</ul></div>"
        "</div>"
    )
    current_month_panel = (
        "<div class='panel'>"
        f"{bi('本月重点品牌', '', 'h2', 'bi')}"
        "<p class='small'>按本月样本活跃度和最高建议分排序，优先看谁最近动作最多、最值得先拆。</p>"
        f"<ul class='list'>{current_month_list}</ul>"
        "</div>"
    )
    current_month_channel_panel = (
        "<div class='panel'>"
        f"{bi('本月重点渠道', '', 'h2', 'bi')}"
        "<p class='small'>看本月哪些渠道最活跃，方便判断优先监控和投放观察重点。</p>"
        f"<ul class='list'>{current_month_channel_list}</ul>"
        "</div>"
    )
    current_month_type_panel = (
        "<div class='panel'>"
        f"{bi('本月重点活动类型', '', 'h2', 'bi')}"
        "<p class='small'>看本月哪些活动类型出现最多，方便判断当下市场更偏哪种打法。</p>"
        f"<ul class='list'>{current_month_type_list}</ul>"
        "</div>"
    )
    offline_overview_panel = (
        "<div class='panel'>"
        f"{bi('线下活动总览', '', 'h2', 'bi')}"
        "<p class='small'>当前系统重点追踪的是线下可落地活动，尤其是能直接导流门店、社群、会员和复购的动作。</p>"
        f"<div class='stats'><div class='metric'>{bi('线下样本数','', 'div', 'bi')}<div class='value'>{offline_count}</div></div><div class='metric'>{bi('高分线下样本','', 'div', 'bi')}<div class='value'>{offline_high_score}</div></div></div>"
        "</div>"
    )
    offline_branch_panel = (
        "<div class='panel'>"
        f"{bi('线下活动重点分支', '', 'h2', 'bi')}"
        "<p class='small'>垂类活动只是其中一个重要分支，系统会同时关注门店体验、社群活动、联名快闪、预约转化和会员复购。</p>"
        f"<ul class='list'>{offline_branch_list}</ul>"
        "</div>"
    )
    offline_priority_panel = (
        "<div class='panel'>"
        f"{bi('线下垂类活动优先池', '', 'h2', 'bi')}"
        "<p class='small'>优先把线下、混合型、到店强相关的活动放在前面，方便你直接学习可落地方案。</p>"
        f"<ul class='list'>{offline_priority_list}</ul>"
        "</div>"
    )
    offline_template_panel = (
        "<div class='panel'>"
        f"{bi('可落地线下活动模板', '', 'h2', 'bi')}"
        "<p class='small'>这些模板不是泛灵感，而是适合直接拆成活动 SOP 的结构化方案。</p>"
        f"<ul class='list'>{offline_template_list}</ul>"
        "</div>"
    )
    summary_section = (
        "<div class='dashboard-section' data-section='summary' style='display:block'>"
        "<div class='layout'><div class='stack'>"
        f"{action_panel}"
        f"<div class='panel'>{bi('样本快览', '', 'h2', 'bi')}<p class='muted'>当前最适合先看的，是高优先级品牌、最新样本和高建议分活动。</p><div class='stats'><div class='metric'>{bi('总样本数','', 'div', 'bi')}<div class='value'>{len(rows)}</div></div><div class='metric'>{bi('P0 样本数','', 'div', 'bi')}<div class='value'>{sum(1 for row in rows if row['priority_tier']=='P0')}</div></div><div class='metric'>{bi('待补强样本','', 'div', 'bi')}<div class='value'>{sum(1 for row in rows if row['review_status']=='seeded_with_inference')}</div></div><div class='metric'>{bi('最近一次刷新','', 'div', 'bi')}<div class='value'>{html.escape(refresh_time)}</div></div></div></div>"
        f"{offline_overview_panel}"
        f"{offline_branch_panel}"
        "<div class='charts'>"
        f"{current_month_panel}"
        f"{current_month_channel_panel}"
        f"{current_month_type_panel}"
        "</div>"
        "<div class='charts'>"
        f"{offline_priority_panel}"
        f"{offline_template_panel}"
        "</div>"
        f"{summary_detail_panels}"
        "</div><aside class='stack side'>"
        f"<div class='panel'>{bi('本周最值得抄作业 TOP 8','', 'h2', 'bi')}<ul class='list'>{''.join(f'<li>{html.escape(item)}</li>' for item in expanded_mechanics)}</ul></div>"
        f"{score_panel()}"
        "</aside></div></div>"
    )
    chart_section = (
        "<div class='dashboard-section' data-section='charts' style='display:block'>"
        "<div class='charts'>"
        f"<div class='panel'>{bi('品牌活动类型','', 'h2', 'bi')}<p class='small'>看当前样本库里，哪些活动类型最常被品牌拿来做拉新、到店、复购和社群运营。</p>{chart_rows(activity_pairs)}</div>"
        f"<div class='panel'>{bi('品牌建议分','', 'h2', 'bi')}<p class='small'>优先看高分品牌，表示更值得影石先拆解、先复用，不代表真实成交率更高。</p>{chart_rows(brand_pairs, 'alt')}</div>"
        "</div></div>"
    )
    library_section = (
        "<div class='dashboard-section' data-section='library' style='display:block'>"
        f"<div class='panel'>{bi('样本库','', 'h2', 'bi')}<p class='muted'>当前表格展示已入库活动；品牌覆盖范围已扩展到中国消费电子、重点车企、年轻人品牌和户外运动品牌。</p><div class='toolbar'><div><div class='small'>样本视角</div><select id='scope-filter'><option value='offline_focus' selected>只看线下 / 混合型活动</option><option value='all'>看全部样本</option></select></div><div><div class='small'>链接类型</div><select id='link-filter'><option value='detail'>只看活动详情页</option><option value='entry'>只看转化入口页</option><option value='reference'>只看参考页</option><option value='invalid'>只看失效链接</option><option value='all'>看全部链接</option></select></div><div><div class='small'>证据等级</div><select id='evidence-filter'><option value=''>全部证据等级</option><option value='direct'>官方直证</option><option value='support'>官方辅助</option><option value='reference'>公开参考</option><option value='invalid'>失效待核</option></select></div><input id='search' type='search' placeholder='搜索品牌、活动、机制'><select id='tier'><option value=''>全部优先级</option><option value='P0'>P0</option><option value='P1'>P1</option><option value='P2'>P2</option></select><select id='status'><option value=''>全部状态</option><option value='seeded'>已确认</option><option value='seeded_with_inference'>待补强</option></select></div><table><thead><tr><th>品牌</th><th>活动</th><th>类型</th><th>证据等级</th><th>建议分</th><th>状态</th></tr></thead><tbody id='rows'>{table_rows}</tbody></table></div>"
        "</div>"
    )
    cards_section = (
        "<div class='dashboard-section' data-section='cards' style='display:block'>"
        f"<div class='panel'>{bi('品牌分组卡片','', 'h2', 'bi')}<p class='muted'>每个品牌展示重点转化活动、近一年优势活动，以及对影石的启发。</p><div class='brandGrid' style='margin-top:14px'>{brand_cards}</div></div>"
        "</div>"
    )
    coverage_section = (
        "<div class='dashboard-section' data-section='coverage' style='display:block'>"
        f"<div class='layout'><div class='stack'>{coverage_status_table(coverage_rows)}</div><aside class='stack side'><div class='panel'>{bi('采集渠道范围','', 'h2', 'bi')}<div class='sourceGrid' style='margin-top:14px'>{source_cards()}</div></div>{evidence_panel()}<div class='panel'>{bi('品牌覆盖范围','', 'h2', 'bi')}<div class='universeGrid' style='margin-top:14px'>{universe_cards()}</div></div></aside></div>"
        "</div>"
    )
    script = """<script>
const rows = JSON.parse(document.getElementById('seed-data').textContent);
const tbody = document.getElementById('rows');
const scopeFilter = document.getElementById('scope-filter');
const linkFilter = document.getElementById('link-filter');
const evidenceFilter = document.getElementById('evidence-filter');
const search = document.getElementById('search');
const tier = document.getElementById('tier');
const status = document.getElementById('status');
function render() {
  const q = search.value.trim().toLowerCase();
  const scope = scopeFilter.value;
  const linkType = linkFilter.value;
  const evidence = evidenceFilter.value;
  const t = tier.value;
  const s = status.value;
  tbody.innerHTML = rows.filter(row => (!q || [row.display_brand,row.activity_name,row.activity_type_label,row.insight_summary,row.evidence_label].join(' ').toLowerCase().includes(q)) && (!t || row.priority_tier === t) && (!s || row.review_status === s) && (!evidence || row.evidence_level === evidence) && (scope !== 'offline_focus' || ['offline','hybrid'].includes(row.online_offline)) && (linkType === 'all' || row.link_type === linkType)).map(row => {
    const title = row.source_url && row.link_type !== 'invalid' ? `<a href="${row.source_url}" target="_blank" rel="noreferrer">${row.activity_name}</a>` : row.activity_name;
    return `<tr><td><strong>${row.display_brand}</strong><div class='small'>${row.priority_label} · ${row.online_offline||'unknown'}</div></td><td>${title}<div class='small'>${row.start_date||'Date TBD'} · ${row.link_note||''}</div><div class='small'>${row.insight_summary}</div></td><td>${row.activity_type_label}</td><td class='${row.evidence_class||''}'>${row.evidence_label||''}</td><td>${row.reuse_score_for_insta360||'-'}</td><td class='${row.review_status==='seeded_with_inference'?'status-flagged':'status-clean'}'>${row.status_label}</td></tr>`;
  }).join('');
}
[scopeFilter, linkFilter, evidenceFilter, search, tier, status].forEach(el => {el.addEventListener('input', render); el.addEventListener('change', render);});
render();
</script>"""
    long_page = (
        "<div class='dashboard-shell'>"
        f"{summary_section}"
        f"{chart_section}"
        f"{library_section}"
        f"{cards_section}"
        f"{coverage_section}"
        "</div>"
    )
    return f"""<!doctype html><html lang='zh-CN'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><title>品牌活动情报看板</title><style>{css()}</style></head><body><div class='wrap'><section class='hero'>{nav('dashboard')}{bi('品牌活动情报看板','', 'h1', 'heroTitle bi')}<div class='heroDesc'>{bi('这个页面聚焦当前已入库的品牌活动样本，同时把目标覆盖范围扩展到中国消费电子、重点车企、年轻人品牌和户外运动品牌。','', 'p', 'bi')}</div><div class='stats'><div class='metric'>{bi('最近一次刷新','', 'div', 'bi')}<div class='value'>{html.escape(refresh_time)}</div></div><div class='metric'>{bi('总样本数','', 'div', 'bi')}<div class='value'>{len(rows)}</div></div><div class='metric'>{bi('P0 样本数','', 'div', 'bi')}<div class='value'>{sum(1 for row in rows if row['priority_tier']=='P0')}</div></div><div class='metric'>{bi('待补强样本','', 'div', 'bi')}<div class='value'>{sum(1 for row in rows if row['review_status']=='seeded_with_inference')}</div></div></div></section>{long_page}</div><script id='seed-data' type='application/json'>{rows_json}</script>{script}</body></html>"""


def timeline_cards_markup(cards: list[dict]) -> str:
    return "".join(
        "<article class='brandCard'>"
        f"<div class='brandTop'><div>{bi(card['month_label'],'','h3','bi')}</div><span class='pill'>{html.escape(str(card['sample_count']))} 条样本</span></div>"
        f"<div class='timelineFacts small'><p><strong>特殊节日：</strong>{html.escape(str(card['holiday_text']))}</p><p><strong>月度主题：</strong>{html.escape(str(card['theme_text']))}</p><p><strong>代表品牌：</strong>{html.escape(str(card['brand_text']))}</p><p><strong>活动类型：</strong>{html.escape(str(card['bucket_text']))}</p></div>"
        "<div style='margin-top:12px'><h4 class='sectionTitle bi'><span class='zh'>代表活动</span></h4><ul class='timelineActivities'>"
        + "".join(
            (
                f"<li><a href='{html.escape(activity['source_url'])}' target='_blank' rel='noreferrer'><strong>{html.escape(activity['brand_zh'])}</strong> · {html.escape(activity['activity_name'])}</a><div class='small'>{html.escape(activity['start_date'])} · {html.escape(activity['activity_bucket'])} · {html.escape(activity.get('evidence_label',''))}</div></li>"
                if activity.get("source_url")
                else f"<li><strong>{html.escape(activity['brand_zh'])}</strong> · {html.escape(activity['activity_name'])}<div class='small'>{html.escape(activity['start_date'])} · {html.escape(activity['activity_bucket'])} · {html.escape(activity.get('evidence_label',''))}</div></li>"
            )
            for activity in card["activities"]
        )
        + ("<li>本月建议继续补节日节点、会员权益和线下活动样本。</li>" if not card["activities"] else "")
        + "</ul></div>"
        f"<div style='margin-top:12px'><h4 class='sectionTitle bi'><span class='zh'>建议关注</span></h4><p>{html.escape(str(card['prediction_text']))}</p></div>"
        "</article>"
        for card in cards
    ) or "<div class='box'>暂无时间线样本</div>"


def build_learning_timeline_nodes(rows: list[dict], window_label: str) -> list[dict]:
    start_raw, end_raw = window_label.split(" - ")
    start_year, start_month, _ = [int(x) for x in start_raw.split("-")]
    end_year, end_month, _ = [int(x) for x in end_raw.split("-")]
    cursor = date(start_year, start_month, 1)
    end_marker = date(end_year, end_month, 1)
    nodes = []
    while cursor <= end_marker:
        month_key = f"{cursor.month:02d}"
        meta = {
            "label": MONTH_META_TEXT.get(month_key, f"{cursor.month}月"),
            "holidays": MONTH_HOLIDAYS_TEXT.get(month_key, ""),
            "theme": MONTH_THEME_TEXT.get(month_key, "待补月度主题"),
            "prediction_intro": MONTH_PREDICTION_INTRO_TEXT.get(month_key, "在这个月份的关键窗口"),
            "predictions": MONTH_PREDICTIONS_TEXT.get(month_key, ["会员活动", "门店体验", "节日联名"]),
        }
        month_id = f"{cursor.year:04d}-{cursor.month:02d}"
        month_rows = [row for row in rows if (row.get("start_date") or "").startswith(month_id) and int(row.get("reuse_score_for_insta360") or 0) >= 4]
        ranked_rows = sorted(
            month_rows,
            key=lambda row: (int(row.get("overall_index") or 0), row.get("start_date") or ""),
            reverse=True,
        )
        bucket_counts = {}
        brand_counts = {}
        for row in month_rows:
            bucket_counts[row["activity_bucket"]] = bucket_counts.get(row["activity_bucket"], 0) + 1
            brand_counts[row["brand_zh"]] = brand_counts.get(row["brand_zh"], 0) + 1
        top_buckets = [label for label, _count in sorted(bucket_counts.items(), key=lambda item: item[1], reverse=True)[:4]]
        top_brands = [label for label, _count in sorted(brand_counts.items(), key=lambda item: item[1], reverse=True)[:4]]
        hotspot = "轻量观察"
        if len(month_rows) >= 8:
            hotspot = "品牌扎堆高峰"
        elif len(month_rows) >= 4:
            hotspot = "中高活跃节点"
        month_end = date(cursor.year + (1 if cursor.month == 12 else 0), 1 if cursor.month == 12 else cursor.month + 1, 1)
        month_end = date.fromordinal(month_end.toordinal() - 1)
        nodes.append(
            {
                "month_id": month_id,
                "month_label": f"{cursor.year}年{cursor.month:02d}月 / {meta['label'].split(' / ')[1] if ' / ' in meta['label'] else meta['label']}",
                "date_range_text": f"{cursor.year:04d}-{cursor.month:02d}-01 至 {month_end.year:04d}-{month_end.month:02d}-{month_end.day:02d}",
                "holiday_text": meta["holidays"],
                "theme_text": f"{meta['theme']}；本月高频打法偏 {'、'.join(top_buckets) if top_buckets else '待补活动主题'}",
                "brand_text": " / ".join(top_brands) if top_brands else "待补品牌",
                "bucket_text": " / ".join(top_buckets) if top_buckets else "待补类型",
                "sample_count": len(month_rows),
                "activities": [
                    {
                        "brand_zh": row["brand_zh"],
                        "activity_name": row["activity_name"],
                        "start_date": row["start_date"],
                        "activity_bucket": row["activity_bucket"],
                        "source_url": row.get("source_url", ""),
                        "evidence_label": row.get("evidence_label", ""),
                    }
                    for row in ranked_rows[:3]
                ],
                "prediction_text": f"建议关注：{meta['prediction_intro']}，品牌更可能会推 {meta['predictions'][0]}、{meta['predictions'][1]}、{meta['predictions'][2]}。",
                "hotspot_label": hotspot,
            }
        )
        next_month = date(cursor.year + (1 if cursor.month == 12 else 0), 1 if cursor.month == 12 else cursor.month + 1, 1)
        cursor = next_month
    return nodes


def learning_timeline_strip_markup(nodes: list[dict]) -> str:
    return "".join(
        "<button class='timeline-month-chip {active}' data-target='timeline-month-{month_id}'>"
        "<span class='timeline-chip-dot {dot}'></span>"
        "<span class='timeline-chip-hotspot'>{hotspot}</span>"
        "<span class='timeline-chip-label'>{label}</span>"
        "<span class='timeline-chip-meta timeline-node-date'>{date_range}</span>"
        "<span class='timeline-chip-meta timeline-node-range'>重点节日 / 时间点：{holiday}</span>"
        "<span class='timeline-chip-brands'>扎堆品牌：{brands}</span>"
        "<span class='timeline-chip-meta'>{count} 条样本</span>"
        "</button>".format(
            active="is-active" if node["sample_count"] > 0 else "",
            dot="is-hot" if node["sample_count"] > 0 else "",
            month_id=html.escape(node["month_id"]),
            hotspot=html.escape(node["hotspot_label"]),
            label=html.escape(node["month_label"]),
            date_range=html.escape(node["date_range_text"]),
            holiday=html.escape(node["holiday_text"]),
            brands=html.escape(node["brand_text"]),
            count=html.escape(str(node["sample_count"])),
        )
        for node in nodes
    )


def learning_timeline_cards_markup(nodes: list[dict]) -> str:
    return "".join(
        "<article id='timeline-month-{month_id}' class='brandCard timeline-month-card'>"
        "<div class='timeline-section-head'><div><h3 class='bi'><span class='zh'>{label}</span></h3><div class='small'><strong>时间节点：</strong>{date_range}</div></div><span class='timeline-badge'>{count} 条样本</span></div>"
        "<div class='timelineFacts small'><p><strong>特殊节日：</strong>{holiday}</p><p><strong>月度主题：</strong>{theme}</p><p><strong>重点品牌：</strong>{brands}</p><p><strong>活动类型：</strong>{buckets}</p></div>"
        "<div style='margin-top:12px'><h4 class='sectionTitle bi'><span class='zh'>代表活动</span></h4><ul class='timelineActivities'>{activities}</ul></div>"
        "<div style='margin-top:12px'><h4 class='sectionTitle bi'><span class='zh'>建议关注</span></h4><p>{prediction}</p></div>"
        "</article>".format(
            month_id=html.escape(node["month_id"]),
            label=html.escape(node["month_label"]),
            date_range=html.escape(node["date_range_text"]),
            count=html.escape(str(node["sample_count"])),
            holiday=html.escape(node["holiday_text"]),
            theme=html.escape(node["theme_text"]),
            brands=html.escape(node["brand_text"]),
            buckets=html.escape(node["bucket_text"]),
            activities="".join(
                (
                    f"<li><a href='{html.escape(activity['source_url'])}' target='_blank' rel='noreferrer'><strong>{html.escape(activity['brand_zh'])}</strong> · {html.escape(activity['activity_name'])}</a><div class='small'>{html.escape(activity['start_date'])} · {html.escape(activity['activity_bucket'])} · {html.escape(activity.get('evidence_label',''))}</div></li>"
                    if activity.get("source_url")
                    else f"<li><strong>{html.escape(activity['brand_zh'])}</strong> · {html.escape(activity['activity_name'])}<div class='small'>{html.escape(activity['start_date'])} · {html.escape(activity['activity_bucket'])} · {html.escape(activity.get('evidence_label',''))}</div></li>"
                )
                for activity in node["activities"]
            ) or "<li>本月建议继续补节日节点、会员权益和线下活动样本。</li>",
            prediction=html.escape(node["prediction_text"]),
        )
        for node in nodes
    ) or "<div class='box'>暂无时间线样本</div>"


def overview_html(rows: list[dict], overview_rows: list[dict], window_label: str, metrics: dict) -> str:
    overview_seed = [row for row in rows if row.get("start_date")]
    overview_json = html.escape(json.dumps(overview_seed, ensure_ascii=False))
    cards = "".join(
        f"<article class='brandCard'><div class='brandTop'><div>{bi(row['brand_zh'], row['brand_en'], 'h3', 'bi')}</div><span class='pill'>{html.escape(row['activity_type_label'])}</span></div>{row_link_html(row)}<div class='small'>{html.escape(row['start_date'] or 'Date TBD')} · {html.escape(row['priority_label'])} · {html.escape(row.get('evidence_label',''))} · {html.escape(row.get('link_note',''))}</div><p style='margin-top:10px'>{html.escape(row['insight_summary'])}</p><div style='margin-top:12px'>{bi('对影石的建议','', 'h4', 'sectionTitle bi')}<p>{html.escape(row['recommendation_for_insta360'])}</p></div></article>"
        for row in overview_rows
    ) or "<div class='box'>暂无活动</div>"
    covered_brand_count = len({row["brand"] for row in overview_rows})
    top_brand_pairs = [(item["brand_zh"], item["avg_conversion_score"]) for item in metrics["brand_ranking"]]
    top_activity_pairs = [(f"{item['brand_zh']} · {item['activity_name'][:16]}", item["overall_score"]) for item in metrics["activity_ranking"]]
    top_conversion_cards = top_conversion_rows(overview_rows, limit=8)
    conversion_cards = "".join(
        f"<li><strong>{html.escape(row['brand_zh'])}</strong>：{row_link_html(row)}<div class='small'>预估转化率区间 {html.escape(estimated_conversion_rate_label(row))} · {html.escape(row.get('evidence_label',''))} · {html.escape(row.get('activity_bucket',''))}</div></li>"
        for row in top_conversion_cards
    ) or "<li>待补充</li>"
    bucket_pairs = metrics["bucket_pairs"]
    source_pairs = metrics["source_pairs"]
    timeline_cards = timeline_cards_markup(metrics["timeline_cards"])
    controls = (
        "<div class='panel' style='margin-top:16px'>"
        "<h2 class='bi'><span class='zh'>时间线筛选</span></h2>"
        f"<div class='toolbar'><div><div class='small'>开始日期</div><input id='window-start' type='date' value='{html.escape(window_label.split(' - ')[0])}'></div>"
        f"<div><div class='small'>结束日期</div><input id='window-end' type='date' value='{html.escape(window_label.split(' - ')[1])}'></div></div>"
        "<p class='small'>修改时间后可在当前页即时筛选活动卡片、排名和时间线。</p></div>"
    )
    best_brand_panel = (
        "<div class='heroHighlight'>"
        "<div class='headline'>年度做得最好 / 转化最强品牌</div>"
        f"<div class='bigBrand' id='best-brand-name'>{html.escape(str(metrics['best_brand_name']))}</div>"
        f"<div class='bigScore' id='best-brand-score'>{metrics['best_brand_score']}</div>"
        "<div class='small'>基于样本转化信号推算，不是品牌真实成交转化率。</div>"
        "</div>"
    )
    script = """
<script>
const overviewRows = JSON.parse(document.getElementById('overview-seed-data').textContent);
const startInput = document.getElementById('window-start');
const endInput = document.getElementById('window-end');
const cardWrap = document.getElementById('overview-cards');
const countWrap = document.getElementById('overview-activity-count');
const brandWrap = document.getElementById('overview-brand-count');
const sampleWrap = document.getElementById('window-sample-count');
const bestBrandWrap = document.getElementById('best-brand-name');
const bestBrandScoreWrap = document.getElementById('best-brand-score');
const brandRankWrap = document.getElementById('conversion-ranking');
const activityRankWrap = document.getElementById('activity-ranking');
const conversionCardWrap = document.getElementById('overview-conversion-rate');
const bucketWrap = document.getElementById('bucket-ranking');
const sourceWrap = document.getElementById('source-ranking');
const timelineWrap = document.getElementById('timeline-cards');
const sourceMetaWrap = document.getElementById('source-meta');
function sum(arr){return arr.reduce((a,b)=>a+b,0)}
function chart(items, style){
  const max = items[0] ? items[0][1] : 1;
  return items.map(([label,count]) => {
    const width = max ? Math.round((count/max)*10000)/100 : 0;
    return `<div class='chartRow'><div>${label}</div><div class='track'><div class='fill ${style||''}' style='width:${width}%'></div></div><div class='small'>${count}</div></div>`;
  }).join('');
}
function isLaunch(row){
  return ['product_launch','conference'].includes(row.activity_type);
}
function overviewPriorityIndex(row){
  let score = Number(row.overall_index || 0);
  if (isLaunch(row)) score -= 14;
  if (['test_drive_booking','store_experience','community_operation','community_run','member_benefit','member_service_activity','brand_collab_offline_activation'].includes(row.activity_type)) score += 6;
  if (['offline','hybrid'].includes(row.online_offline)) score += 3;
  return score;
}
const monthMeta = {
  '01': {label:'1月 / 新年启动', holidays:'元旦 / 春节预热', theme:'开年拉新、会员唤醒、年度首发', predictionIntro:'在新年启动和春节预热期'},
  '02': {label:'2月 / 开年造势', holidays:'春节 / 情人节 / 开工', theme:'团圆送礼、情侣节点、返工复购', predictionIntro:'在春节余温、情人节和开工节点'},
  '03': {label:'3月 / 春季上新', holidays:'女性节 / 春季上新', theme:'女性节点、新品首发、春季内容', predictionIntro:'在女性节和春季焕新期'},
  '04': {label:'4月 / 春季户外', holidays:'清明 / 露营季', theme:'户外体验、城市社群、运动场景', predictionIntro:'在清明、露营和春季户外窗口'},
  '05': {label:'5月 / 五一与主题月', holidays:'五一 / 母亲节 / 520', theme:'假期出游、礼赠、情侣与家庭消费', predictionIntro:'在五一、母亲节和 520 节点'},
  '06': {label:'6月 / 618 与暑期预热', holidays:'儿童节 / 618 / 父亲节 / 端午节', theme:'大促转化、亲子节点、男性礼赠、暑期预热', predictionIntro:'在 618、父亲节和端午节窗口'},
  '07': {label:'7月 / 暑期流量', holidays:'毕业季 / 暑期', theme:'年轻人社交、旅行记录、门店体验', predictionIntro:'在毕业季和暑期启动期'},
  '08': {label:'8月 / 七夕与假日出行', holidays:'七夕 / 暑期出游', theme:'情侣活动、节日打卡、联名出片', predictionIntro:'在七夕和暑期出游窗口'},
  '09': {label:'9月 / 秋季新品', holidays:'开学季 / 中秋预热', theme:'秋季上新、校园人群、内容回流', predictionIntro:'在开学季和秋季上新窗口'},
  '10': {label:'10月 / 国庆黄金周', holidays:'国庆 / 中秋窗口', theme:'全国巡回、出游打卡、线下大活动', predictionIntro:'在国庆出游和黄金周节点'},
  '11': {label:'11月 / 双11与社群复购', holidays:'双11 / 会员大促', theme:'价格转化、会员复购、社群冲量', predictionIntro:'在双11和会员复购冲刺期'},
  '12': {label:'12月 / 年终节点', holidays:'双12 / 圣诞 / 跨年', theme:'礼物场景、年终复盘、跨年活动', predictionIntro:'在双12、圣诞和跨年节点'}
};
const monthPredictions = {
  '01': ['新年开运抽奖','会员开卡礼','城市首场体验会'],
  '02': ['春节礼盒','情侣双人活动','返工唤醒券包'],
  '03': ['女性节限定礼盒','女性创作者活动','门店体验课'],
  '04': ['露营试拍日','户外社群课','城市跑团联动'],
  '05': ['五一出游打卡','母亲节礼赠','520 联名快闪'],
  '06': ['618 券包','父亲节礼物推荐','端午出游主题活动'],
  '07': ['毕业季任务赛','暑期门店体验营','旅行内容征集'],
  '08': ['七夕联名礼盒','情侣打卡任务','暑期城市快闪'],
  '09': ['开学季新手礼包','秋季新品试用','校园创作活动'],
  '10': ['国庆巡回活动','旅行打卡挑战','多城快闪空间'],
  '11': ['双11 会员券包','社群复购冲刺','老客加购权益'],
  '12': ['圣诞礼盒','跨年主题活动','年终会员回馈']
};
function buildTimelineCards(filtered){
  return Object.entries(monthMeta).map(([monthKey, meta]) => {
    const monthRows = filtered.filter(row => (row.start_date || '').slice(5,7) === monthKey);
    const rankedRows = monthRows.slice().sort((a,b) => {
      const scoreDiff = overviewPriorityIndex(b) - overviewPriorityIndex(a);
      if (scoreDiff) return scoreDiff;
      return (b.start_date || '').localeCompare(a.start_date || '');
    });
    const bucketCounts = {};
    const brandCounts = {};
    monthRows.forEach(row => {
      bucketCounts[row.activity_bucket] = (bucketCounts[row.activity_bucket] || 0) + 1;
      brandCounts[row.brand_zh] = (brandCounts[row.brand_zh] || 0) + 1;
    });
    const topBuckets = Object.entries(bucketCounts).sort((a,b)=>b[1]-a[1]).slice(0,4).map(([label]) => label);
    const topBrands = Object.entries(brandCounts).sort((a,b)=>b[1]-a[1]).slice(0,4).map(([label]) => label);
    const predictedMoves = monthPredictions[monthKey] || ['会员活动','门店体验','节日联名'];
    return {
      monthKey,
      monthLabel: meta.label,
      holidayText: meta.holidays,
      themeText: `${meta.theme}；本月高频打法偏 ${topBuckets.join('、') || '待补活动主题'}`,
      brandText: topBrands.join(' / ') || '待补品牌',
      bucketText: topBuckets.join(' / ') || '待补类型',
      sampleCount: monthRows.length,
      activities: rankedRows.slice(0,3),
      recommendation: rankedRows[0] ? rankedRows[0].recommendation_for_insta360 : '可优先补节日节点、会员权益、线下体验和联名活动样本。',
      predictionText: `建议关注：${meta.predictionIntro}，品牌更可能会推 ${predictedMoves[0]}、${predictedMoves[1]}、${predictedMoves[2]}。`
    };
  });
}
function renderTimelineCard(card){
  const activityHtml = card.activities.length
    ? card.activities.map(activity => {
        const title = activity.source_url ? `<a href='${activity.source_url}' target='_blank' rel='noreferrer'><strong>${activity.brand_zh}</strong> · ${activity.activity_name}</a>` : `<strong>${activity.brand_zh}</strong> · ${activity.activity_name}`;
        return `<li>${title}<div class='small'>${activity.start_date || 'Date TBD'} · ${activity.activity_bucket || ''} · ${activity.evidence_label || ''}</div></li>`;
      }).join('')
    : "<li>本月建议继续补节日节点、会员权益和线下活动样本。</li>";
  return `<article class='brandCard'><div class='brandTop'><div><h3 class='bi'><span class='zh'>${card.monthLabel}</span></h3></div><span class='pill'>${card.sampleCount} 条样本</span></div><div class='timelineFacts small'><p><strong>特殊节日：</strong>${card.holidayText}</p><p><strong>月度主题：</strong>${card.themeText}</p><p><strong>代表品牌：</strong>${card.brandText}</p><p><strong>活动类型：</strong>${card.bucketText}</p></div><div style='margin-top:12px'><h4 class='sectionTitle bi'><span class='zh'>代表活动</span></h4><ul class='timelineActivities'>${activityHtml}</ul></div><div style='margin-top:12px'><h4 class='sectionTitle bi'><span class='zh'>建议关注</span></h4><p>${card.predictionText}</p></div></article>`;
}
function renderOverview(){
  const start = startInput.value;
  const end = endInput.value;
  const filtered = overviewRows.filter(row => (!start || row.start_date >= start) && (!end || row.start_date <= end));
  const highQuality = filtered.filter(row => Number(row.reuse_score_for_insta360 || 0) >= 4);
  countWrap.textContent = highQuality.length;
  brandWrap.textContent = new Set(filtered.map(row => row.brand)).size;
  sampleWrap.textContent = filtered.length;

  const brandScores = {};
  const sourceScores = {};
  const bucketScores = {};
  filtered.forEach(row => {
    const conv = Number(row.conversion_index || 0);
    if (!brandScores[row.brand_zh]) brandScores[row.brand_zh] = [];
    brandScores[row.brand_zh].push(conv);
    sourceScores[row.channel_label] = (sourceScores[row.channel_label] || 0) + 1;
    if (Number(row.reuse_score_for_insta360 || 0) >= 4) {
      bucketScores[row.activity_bucket] = (bucketScores[row.activity_bucket] || 0) + 1;
    }
  });

  const brandRank = Object.entries(brandScores).map(([label, scores]) => [label, Math.round(sum(scores)/scores.length)]).sort((a,b)=>b[1]-a[1]).slice(0,12);
  const activityRank = highQuality.map(row => [`${row.brand_zh} · ${row.activity_name.slice(0,16)}`, overviewPriorityIndex(row)]).sort((a,b)=>b[1]-a[1]).slice(0,12);
  const topConversionRows = highQuality.slice().sort((a,b) => {
    const rankDiff = overviewPriorityIndex(b) - overviewPriorityIndex(a);
    if (rankDiff) return rankDiff;
    return Number(b.conversion_index || 0) - Number(a.conversion_index || 0);
  }).slice(0,8);
  const bucketRank = Object.entries(bucketScores).sort((a,b)=>b[1]-a[1]).map(([label,count]) => [`${label}（${Math.round(count / (highQuality.length || 1) * 100)}%）`, count]);
  const sourceRank = Object.entries(sourceScores).sort((a,b)=>b[1]-a[1]).slice(0,12).map(([label,count]) => [`${label}（${Math.round(count / (filtered.length || 1) * 100)}%）`, count]);
  const bestBrand = brandRank[0] || ['暂无', 0];
  bestBrandWrap.textContent = bestBrand[0];
  bestBrandScoreWrap.textContent = bestBrand[1];
  if (sourceMetaWrap) sourceMetaWrap.textContent = `统计口径：基于当前时间窗内全部样本，共 ${filtered.length} 条样本、${sourceRank.length} 类渠道；不是只看高分活动。`;

  brandRankWrap.innerHTML = chart(brandRank, 'strong');
  activityRankWrap.innerHTML = chart(activityRank, 'alt');
  bucketWrap.innerHTML = chart(bucketRank, '');
  sourceWrap.innerHTML = chart(sourceRank, '');

  const sortedHighQuality = highQuality.slice().sort((a,b) => {
    const launchBias = (isLaunch(a) ? 1 : 0) - (isLaunch(b) ? 1 : 0);
    if (launchBias) return launchBias;
    return overviewPriorityIndex(b) - overviewPriorityIndex(a);
  });
  cardWrap.innerHTML = sortedHighQuality.map(row => {
    const title = row.source_url && row.link_type !== 'invalid' ? `<a href='${row.source_url}' target='_blank' rel='noreferrer'>${row.activity_name}</a>` : row.activity_name;
    return `<article class='brandCard'><div class='brandTop'><div><h3 class='bi'><span class='zh'>${row.brand_zh}</span></h3></div><span class='pill'>${row.activity_type_label}</span></div>${title}<div class='small'>${row.start_date || 'Date TBD'} · ${row.priority_label} · ${row.evidence_label || ''} · ${row.link_note || ''}</div><p style='margin-top:10px'>${row.insight_summary}</p><div style='margin-top:12px'><h4 class='sectionTitle bi'><span class='zh'>对影石的建议</span></h4><p>${row.recommendation_for_insta360}</p></div></article>`;
  }).join('') || "<div class='box'>暂无活动</div>";
  conversionCardWrap.innerHTML = topConversionRows.map(row => {
    const title = row.source_url && row.link_type !== 'invalid' ? `<a href='${row.source_url}' target='_blank' rel='noreferrer'>${row.activity_name}</a>` : row.activity_name;
    let rate = '< 1.5%';
    const score = Number(row.conversion_index || row.overall_index || 0);
    if (score >= 95) rate = '8% - 12%';
    else if (score >= 90) rate = '6% - 8%';
    else if (score >= 80) rate = '4% - 6%';
    else if (score >= 70) rate = '2.5% - 4%';
    else if (score >= 60) rate = '1.5% - 2.5%';
    return `<li><strong>${row.brand_zh}</strong>：${title}<div class='small'>预估转化率区间 ${rate} · ${row.evidence_label || ''} · ${row.activity_bucket || ''}</div></li>`;
  }).join('') || "<li>待补充</li>";
  const timelineCards = buildTimelineCards(highQuality).map(renderTimelineCard);
  timelineWrap.innerHTML = timelineCards.join('') || "<div class='box'>暂无时间线样本</div>";
}
[startInput, endInput].forEach(el => el.addEventListener('change', renderOverview));
renderOverview();
</script>
"""
    page = """<!doctype html><html lang='zh-CN'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><title>年度优质品牌活动总览</title><style>{style}</style></head><body><div class='wrap'><section class='hero'>{nav_html}{title}{desc}<div class='stats'><div class='metric'>{window_title}<div class='value'>{window_value}</div></div><div class='metric'>{activity_count_title}<div class='value' id='overview-activity-count'>{activity_count}</div></div><div class='metric'>{brand_count_title}<div class='value' id='overview-brand-count'>{brand_count}</div></div><div class='metric'>{sample_count_title}<div class='value' id='window-sample-count'>{sample_count}</div></div></div><div class='heroCharts'>{best_brand_html}<div class='panel'>{brand_rank_title}<p class='small'>基于样本转化信号推算，综合了建议分、会员权益、试驾/报名、门店与私域承接等因素。</p><div id='conversion-ranking'>{brand_rank_rows}</div></div></div>{controls}</section><section class='layout'><div class='stack'><div class='panel'>{activity_list_title}<p class='muted'>筛选标准：目标时间窗口内，且建议分大于等于 4；默认优先展示非发布会的转化型活动。</p><div class='overviewGrid' id='overview-cards' style='margin-top:14px'>{cards}</div></div><div class='charts'><div class='panel'>{activity_rank_title}<p class='small'>默认弱化单纯发布会和大会页，优先把会员、门店、社群、联名、预约等更适合复用的活动顶上来。</p><div id='activity-ranking'>{activity_rank_rows}</div></div><div class='panel'>{bucket_title}<p class='small'>把高质量活动按“企微 / 私域、会员复购、线上线下联动、联名、新品发布、门店体验、社群活动”等维度做分类。</p><div id='bucket-ranking'>{bucket_rows}</div></div></div><div class='panel'><h2 class='bi'><span class='zh'>高转化活动预估转化率</span></h2><p class='small'>公开真实转化率通常不可得，这里基于报名门槛、私域承接、会员权益、补贴力度和到店链路做预估转化率区间。</p><ul class='list' id='overview-conversion-rate'>{conversion_cards}</ul></div><div class='panel'>{timeline_title}<p class='small'>按月份把特殊节日、主题打法、重点品牌和代表活动放在一起，方便直接看清“什么时间适合做什么活动”。</p><div class='overviewGrid' id='timeline-cards' style='margin-top:14px'>{timeline_cards}</div></div></div><aside class='stack side'><div class='panel'>{source_title}<p class='small' id='source-meta'>统计口径：基于当前时间窗内全部样本，共 {sample_count} 条样本、{source_count} 类渠道；不是只看高分活动。</p><div id='source-ranking'>{source_rows}</div></div><div class='panel'>{diff_title}<ul class='list'><li>总页：看近一年高质量活动全量脉络。</li><li>看板页：看品牌策略、渠道抓取范围和给影石的动作建议。</li></ul></div></aside></section></div><script id='overview-seed-data' type='application/json'>{overview_json}</script>{script}</body></html>"""
    return page.format(
        style=css(),
        nav_html=nav("overview"),
        title=bi("年度优质品牌活动总览", "", "h1", "heroTitle bi"),
        desc=f"<div class='heroDesc'>{bi('这个总页面聚焦 2024 年到 2026 年窗口内，值得长期复盘的高质量品牌活动。', '', 'p', 'bi')}</div>",
        window_title=bi("时间窗口", "", "div", "bi"),
        window_value=html.escape(window_label),
        activity_count_title=bi("优质活动数", "", "div", "bi"),
        activity_count=len(overview_rows),
        brand_count_title=bi("覆盖品牌数", "", "div", "bi"),
        brand_count=covered_brand_count,
        sample_count_title=bi("时间窗样本数", "", "div", "bi"),
        sample_count=metrics["window_sample_count"],
        best_brand_html=best_brand_panel,
        brand_rank_title=bi("各品牌预估活动转化率排名（高转化品牌榜）", "", "h2", "bi"),
        brand_rank_rows=chart_rows(top_brand_pairs, "strong"),
        controls=controls,
        activity_list_title=bi("近一年优质活动列表", "", "h2", "bi"),
        cards=cards,
        activity_rank_title=bi("各品牌优质活动比较排名", "", "h2", "bi"),
        activity_rank_rows=chart_rows(top_activity_pairs, "alt"),
        bucket_title=bi("高转化优质活动分类分布", "", "h2", "bi"),
        bucket_rows=chart_rows(bucket_pairs),
        conversion_cards=conversion_cards,
        timeline_title=bi("年度节奏学习时间线", "", "h2", "bi"),
        timeline_cards=timeline_cards,
        source_title=bi("渠道热度分布", "", "h2", "bi"),
        source_rows=chart_rows(source_pairs),
        source_count=metrics["source_category_count"],
        diff_title=bi("总页与看板的区别", "", "h2", "bi"),
        overview_json=overview_json,
        script=script,
    )


def learning_timeline_html(rows: list[dict], window_label: str, metrics: dict) -> str:
    overview_seed = [row for row in rows if row.get("start_date")]
    overview_json = html.escape(json.dumps(overview_seed, ensure_ascii=False))
    learning_nodes = build_learning_timeline_nodes(rows, window_label)
    timeline_strip = learning_timeline_strip_markup(learning_nodes)
    timeline_cards = learning_timeline_cards_markup(learning_nodes)
    months_with_samples = sum(1 for card in learning_nodes if card["sample_count"])
    timeline_style = (
        css()
        + """
    :root{--tl-bg:#f7f1ff;--tl-panel:#fff9ff;--tl-ink:#25193e;--tl-line:#ead8ff;--tl-accent:#f15bc1;--tl-accent2:#7d63ff;--tl-accent3:#5dc7ff;--tl-soft:#ffe3f8}
    body{background:radial-gradient(circle at top left,#fff7fe 0%,#f7efff 38%,#eef6ff 100%);color:var(--tl-ink)}
    .hero{background:linear-gradient(135deg,#ff78d1 0%,#9a6bff 52%,#5dc7ff 100%);box-shadow:0 20px 52px rgba(113,83,176,.20)}
    .nav a{background:rgba(255,255,255,.18)}
    .nav a.active{background:#fff;color:#d94cb0}
    .panel,.metric,.box,.heroHighlight,.brandCard{background:var(--tl-panel);border-color:var(--tl-line)}
    .pill{background:#ffe6f7;color:#cc4bac}
    .track{background:#ebe0ff}
    .fill{background:linear-gradient(90deg,#7d63ff,#5dc7ff)}
    .fill.alt{background:linear-gradient(90deg,#f15bc1,#ff9ada)}
    .fill.strong{background:linear-gradient(90deg,#7f53ff,#ff78d1)}
    .timeline-shell{padding:20px;border-radius:24px;background:linear-gradient(180deg,#fffaff 0%,#f7f0ff 58%,#eef6ff 100%)}
    .timeline-strip{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;padding:6px 4px 8px}
    .timeline-month-chip{position:relative;display:flex;flex-direction:column;gap:8px;min-width:150px;padding:14px 14px 16px;border-radius:18px;border:1px solid #ead8ff;background:linear-gradient(180deg,#fffaff 0%,#f7f0ff 100%);box-shadow:0 10px 24px rgba(112,86,178,.10);cursor:pointer;transition:transform .18s ease, box-shadow .18s ease, border-color .18s ease}
    .timeline-month-chip:hover{transform:translateY(-2px);box-shadow:0 14px 28px rgba(112,86,178,.14)}
    .timeline-month-chip.is-active{border-color:#d94cb0;box-shadow:0 0 0 3px rgba(241,91,193,.14),0 16px 28px rgba(112,86,178,.15)}
    .timeline-chip-label{font-size:15px;font-weight:800;color:#24193e}
    .timeline-chip-meta{font-size:12px;line-height:1.45;color:#74658f}
    .timeline-chip-hotspot{display:inline-flex;align-self:flex-start;padding:4px 8px;border-radius:999px;background:#ffe6f7;color:#cb4da9;font-size:11px;font-weight:800}
    .timeline-chip-dot{width:12px;height:12px;border-radius:999px;background:linear-gradient(135deg,#7d63ff,#5dc7ff);box-shadow:0 0 0 4px rgba(125,99,255,.12)}
    .timeline-chip-dot.is-hot{background:linear-gradient(135deg,#f15bc1,#5dc7ff);box-shadow:0 0 0 4px rgba(241,91,193,.14)}
    .timeline-node-date{font-size:12px;color:#5d4d86;font-weight:700}
    .timeline-node-range{font-size:11px;color:#7f70a4}
    .timeline-chip-brands{font-size:11px;color:#554885;line-height:1.5}
    .timeline-month-card{scroll-margin-top:22px}
    .timeline-section-head{display:flex;justify-content:space-between;gap:12px;align-items:flex-start;margin-bottom:14px}
    .timeline-badge{display:inline-flex;align-items:center;padding:6px 11px;border-radius:999px;background:#ffe6f7;color:#cb4da9;font-size:12px;font-weight:700}
    @media (max-width:1180px){.timeline-strip{grid-template-columns:repeat(2,minmax(0,1fr))}.timeline-month-chip{min-width:0}}
    @media (max-width:760px){.timeline-strip{grid-template-columns:1fr}}
    """
    )
    controls = (
        "<div class='panel' style='margin-top:16px'>"
        "<h2 class='bi'><span class='zh'>时间线筛选</span></h2>"
        f"<div class='toolbar'><div><div class='small'>开始日期</div><input id='window-start' type='date' value='{html.escape(window_label.split(' - ')[0])}'></div>"
        f"<div><div class='small'>结束日期</div><input id='window-end' type='date' value='{html.escape(window_label.split(' - ')[1])}'></div></div>"
        "<p class='small'>修改时间后可在当前页即时筛选月度时间线。</p></div>"
    )
    script = """
<script>
    const overviewRows = JSON.parse(document.getElementById('timeline-seed-data').textContent);
    const startInput = document.getElementById('window-start');
    const endInput = document.getElementById('window-end');
    const timelineStripWrap = document.getElementById('timeline-strip');
    const timelineWrap = document.getElementById('timeline-cards');
    const monthCountWrap = document.getElementById('timeline-month-count');
    const sampleWrap = document.getElementById('timeline-sample-count');
function isLaunch(row){
  return ['product_launch','conference'].includes(row.activity_type);
}
function overviewPriorityIndex(row){
  let score = Number(row.overall_index || 0);
  if (isLaunch(row)) score -= 14;
  if (['test_drive_booking','store_experience','community_operation','community_run','member_benefit','member_service_activity','brand_collab_offline_activation'].includes(row.activity_type)) score += 6;
  if (['offline','hybrid'].includes(row.online_offline)) score += 3;
  return score;
}
const monthMeta = {
  '01': {label:'1月 / 新年启动', holidays:'元旦 / 春节预热', theme:'开年拉新、会员唤醒、年度首发', predictionIntro:'在新年启动和春节预热期'},
  '02': {label:'2月 / 开年造势', holidays:'春节 / 情人节 / 开工', theme:'团圆送礼、情侣节点、返工复购', predictionIntro:'在春节余温、情人节和开工节点'},
  '03': {label:'3月 / 春季上新', holidays:'女性节 / 春季上新', theme:'女性节点、新品首发、春季内容', predictionIntro:'在女性节和春季焕新期'},
  '04': {label:'4月 / 春季户外', holidays:'清明 / 露营季', theme:'户外体验、城市社群、运动场景', predictionIntro:'在清明、露营和春季户外窗口'},
  '05': {label:'5月 / 五一与主题月', holidays:'五一 / 母亲节 / 520', theme:'假期出游、礼赠、情侣与家庭消费', predictionIntro:'在五一、母亲节和 520 节点'},
  '06': {label:'6月 / 618 与暑期预热', holidays:'儿童节 / 618 / 父亲节 / 端午节', theme:'大促转化、亲子节点、男性礼赠、暑期预热', predictionIntro:'在 618、父亲节和端午节窗口'},
  '07': {label:'7月 / 暑期流量', holidays:'毕业季 / 暑期', theme:'年轻人社交、旅行记录、门店体验', predictionIntro:'在毕业季和暑期启动期'},
  '08': {label:'8月 / 七夕与假日出行', holidays:'七夕 / 暑期出游', theme:'情侣活动、节日打卡、联名出片', predictionIntro:'在七夕和暑期出游窗口'},
  '09': {label:'9月 / 秋季新品', holidays:'开学季 / 中秋预热', theme:'秋季上新、校园人群、内容回流', predictionIntro:'在开学季和秋季上新窗口'},
  '10': {label:'10月 / 国庆黄金周', holidays:'国庆 / 中秋窗口', theme:'全国巡回、出游打卡、线下大活动', predictionIntro:'在国庆出游和黄金周节点'},
  '11': {label:'11月 / 双11与社群复购', holidays:'双11 / 会员大促', theme:'价格转化、会员复购、社群冲量', predictionIntro:'在双11和会员复购冲刺期'},
  '12': {label:'12月 / 年终节点', holidays:'双12 / 圣诞 / 跨年', theme:'礼物场景、年终复盘、跨年活动', predictionIntro:'在双12、圣诞和跨年节点'}
};
const monthPredictions = {
  '01': ['新年开运抽奖','会员开卡礼','城市首场体验会'],
  '02': ['春节礼盒','情侣双人活动','返工唤醒券包'],
  '03': ['女性节限定礼盒','女性创作者活动','门店体验课'],
  '04': ['露营试拍日','户外社群课','城市跑团联动'],
  '05': ['五一出游打卡','母亲节礼赠','520 联名快闪'],
  '06': ['618 券包','父亲节礼物推荐','端午出游主题活动'],
  '07': ['毕业季任务赛','暑期门店体验营','旅行内容征集'],
  '08': ['七夕联名礼盒','情侣打卡任务','暑期城市快闪'],
  '09': ['开学季新手礼包','秋季新品试用','校园创作活动'],
  '10': ['国庆巡回活动','旅行打卡挑战','多城快闪空间'],
  '11': ['双11 会员券包','社群复购冲刺','老客加购权益'],
  '12': ['圣诞礼盒','跨年主题活动','年终会员回馈']
};
function padMonth(value){
  return String(value).padStart(2,'0');
}
function buildMonthNodes(start, end){
  const startDate = new Date(`${start}T00:00:00`);
  const endDate = new Date(`${end}T00:00:00`);
  const cursor = new Date(startDate.getFullYear(), startDate.getMonth(), 1);
  const nodes = [];
  while (cursor <= endDate) {
    const year = cursor.getFullYear();
    const monthNum = cursor.getMonth() + 1;
    const monthKey = padMonth(monthNum);
    const monthId = `${year}-${monthKey}`;
    const monthEndDate = new Date(year, monthNum, 0);
    const monthMetaItem = monthMeta[monthKey];
    nodes.push({
      monthId,
      monthKey,
      dateRangeText: `${year}-${monthKey}-01 至 ${year}-${monthKey}-${String(monthEndDate.getDate()).padStart(2,'0')}`,
      label: `${year}年${monthKey}月 / ${monthMetaItem.label.split(' / ')[1]}`
    });
    cursor.setMonth(cursor.getMonth() + 1);
  }
  return nodes;
}
function buildTimelineCards(filtered, nodes){
  return nodes.map(node => {
    const meta = monthMeta[node.monthKey];
    const monthRows = filtered.filter(row => (row.start_date || '').slice(0,7) === node.monthId);
    const rankedRows = monthRows.slice().sort((a,b) => {
      const scoreDiff = overviewPriorityIndex(b) - overviewPriorityIndex(a);
      if (scoreDiff) return scoreDiff;
      return (b.start_date || '').localeCompare(a.start_date || '');
    });
    const bucketCounts = {};
    const brandCounts = {};
    monthRows.forEach(row => {
      bucketCounts[row.activity_bucket] = (bucketCounts[row.activity_bucket] || 0) + 1;
      brandCounts[row.brand_zh] = (brandCounts[row.brand_zh] || 0) + 1;
    });
    const topBuckets = Object.entries(bucketCounts).sort((a,b)=>b[1]-a[1]).slice(0,4).map(([label]) => label);
    const topBrands = Object.entries(brandCounts).sort((a,b)=>b[1]-a[1]).slice(0,4).map(([label]) => label);
    const predictedMoves = monthPredictions[node.monthKey] || ['会员活动','门店体验','节日联名'];
    let hotspotLabel = '轻量观察';
    if (monthRows.length >= 8) hotspotLabel = '品牌扎堆高峰';
    else if (monthRows.length >= 4) hotspotLabel = '中高活跃节点';
    return {
      monthKey: node.monthId,
      monthLabel: node.label,
      dateRangeText: node.dateRangeText,
      holidayText: meta.holidays,
      themeText: `${meta.theme}；本月高频打法偏 ${topBuckets.join('、') || '待补活动主题'}`,
      brandText: topBrands.join(' / ') || '待补品牌',
      bucketText: topBuckets.join(' / ') || '待补类型',
      sampleCount: monthRows.length,
      hotspotLabel,
      activities: rankedRows.slice(0,3),
      predictionText: `建议关注：${meta.predictionIntro}，品牌更可能会推 ${predictedMoves[0]}、${predictedMoves[1]}、${predictedMoves[2]}。`
    };
  });
}
function renderTimelineCard(card){
  const activityHtml = card.activities.length
    ? card.activities.map(activity => {
        const title = activity.source_url ? `<a href='${activity.source_url}' target='_blank' rel='noreferrer'><strong>${activity.brand_zh}</strong> · ${activity.activity_name}</a>` : `<strong>${activity.brand_zh}</strong> · ${activity.activity_name}`;
        return `<li>${title}<div class='small'>${activity.start_date || 'Date TBD'} · ${activity.activity_bucket || ''} · ${activity.evidence_label || ''}</div></li>`;
      }).join('')
    : "<li>本月建议继续补节日节点、会员权益和线下活动样本。</li>";
  return `<article id='timeline-month-${card.monthKey}' class='brandCard timeline-month-card'><div class='timeline-section-head'><div><h3 class='bi'><span class='zh'>${card.monthLabel}</span></h3><div class='small'><strong>时间节点：</strong>${card.dateRangeText}</div></div><span class='timeline-badge'>${card.sampleCount} 条样本</span></div><div class='timelineFacts small'><p><strong>特殊节日：</strong>${card.holidayText}</p><p><strong>月度主题：</strong>${card.themeText}</p><p><strong>重点品牌：</strong>${card.brandText}</p><p><strong>活动类型：</strong>${card.bucketText}</p></div><div style='margin-top:12px'><h4 class='sectionTitle bi'><span class='zh'>代表活动</span></h4><ul class='timelineActivities'>${activityHtml}</ul></div><div style='margin-top:12px'><h4 class='sectionTitle bi'><span class='zh'>建议关注</span></h4><p>${card.predictionText}</p></div></article>`;
}
function renderTimelineStrip(cards){
  timelineStripWrap.innerHTML = cards.map(card => {
    const activeClass = card.sampleCount > 0 ? 'is-hot' : '';
    const activeCard = card.sampleCount > 0 ? 'is-active' : '';
    return `<button class='timeline-month-chip ${activeCard}' data-target='timeline-month-${card.monthKey}'><span class='timeline-chip-dot ${activeClass}'></span><span class='timeline-chip-hotspot'>${card.hotspotLabel}</span><span class='timeline-chip-label'>${card.monthLabel}</span><span class='timeline-chip-meta timeline-node-date'>${card.dateRangeText}</span><span class='timeline-chip-meta timeline-node-range'>重点节日 / 时间点：${card.holidayText}</span><span class='timeline-chip-brands'>扎堆品牌：${card.brandText}</span><span class='timeline-chip-meta'>${card.sampleCount} 条样本</span></button>`;
  }).join('');
  timelineStripWrap.querySelectorAll('.timeline-month-chip').forEach(button => {
    button.addEventListener('click', () => {
      const target = document.getElementById(button.dataset.target);
      if (target) target.scrollIntoView({behavior:'smooth', block:'start'});
    });
  });
}
function renderTimelinePage(){
  const start = startInput.value;
  const end = endInput.value;
  const filtered = overviewRows.filter(row => (!start || row.start_date >= start) && (!end || row.start_date <= end));
  const nodes = buildMonthNodes(start, end);
  const cards = buildTimelineCards(filtered, nodes);
  renderTimelineStrip(cards);
  timelineWrap.innerHTML = cards.map(renderTimelineCard).join('') || "<div class='box'>暂无时间线样本</div>";
  monthCountWrap.textContent = cards.filter(card => card.sampleCount > 0).length;
  sampleWrap.textContent = filtered.length;
}
[startInput, endInput].forEach(el => el.addEventListener('change', renderTimelinePage));
renderTimelinePage();
</script>
"""
    page = """<!doctype html><html lang='zh-CN'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><title>品牌活动学习时间线</title><style>{style}</style></head><body><div class='wrap'><section class='hero'>{nav_html}{title}{desc}<div class='stats'><div class='metric'>{window_title}<div class='value'>{window_value}</div></div><div class='metric'>{month_count_title}<div class='value' id='timeline-month-count'>{month_count}</div></div><div class='metric'>{sample_count_title}<div class='value' id='timeline-sample-count'>{sample_count}</div></div><div class='metric'>{focus_title}<div class='value'>月度节奏卡</div></div></div>{controls}</section><section class='layout'><div class='stack'><div class='panel timeline-shell'><h2 class='bi'><span class='zh'>月份时间轴导航</span></h2><p class='muted'>这里按品牌扎堆举办的时间点，标出重点节日、重要时间点和扎堆品牌，方便快速看联动窗口和竞品节奏。</p><div id='timeline-strip' class='timeline-strip'>{timeline_strip}</div></div><div class='panel'>{timeline_title}<p class='muted'>按月份把特殊节日、主题打法、重点品牌和代表活动放在一起，方便直接看清“什么时间适合做什么活动”。</p><div class='overviewGrid' id='timeline-cards' style='margin-top:14px'>{timeline_cards}</div></div></div><aside class='stack side'><div class='panel'>{use_title}<ul class='list'><li>先看顶部的品牌扎堆节点，判断哪些月份更适合做联动或跟进竞品。</li><li>再看对应月份卡片，拆重点品牌和代表活动。</li><li>最后结合“建议关注”，判断影石下一阶段更适合推进什么活动方向。</li></ul></div><div class='panel'>{note_title}<p class='small'>这里是独立时间线页面，优先看品牌扎堆时间点和节日节点，不混入总览中的其他排名模块。</p></div></aside></section></div><script id='timeline-seed-data' type='application/json'>{overview_json}</script>{script}</body></html>"""
    return page.format(
        style=timeline_style,
        nav_html=nav("timeline"),
        title=bi("品牌活动学习时间线", "", "h1", "heroTitle bi"),
        desc=f"<div class='heroDesc'>{bi('把年度节奏学习时间线单独拆成一个页面，专门看每个月的特殊节日、主题打法、重点品牌和代表活动。', '', 'p', 'bi')}</div>",
        window_title=bi("时间窗口", "", "div", "bi"),
        window_value=html.escape(window_label),
        month_count_title=bi("有样本月份", "", "div", "bi"),
        month_count=months_with_samples,
        sample_count_title=bi("时间窗样本数", "", "div", "bi"),
        sample_count=metrics["window_sample_count"],
        focus_title=bi("当前视角", "", "div", "bi"),
        controls=controls,
        timeline_title=bi("年度节奏学习时间线", "", "h2", "bi"),
        timeline_strip=timeline_strip,
        timeline_cards=timeline_cards,
        use_title=bi("怎么使用", "", "h2", "bi"),
        note_title=bi("页面说明", "", "h2", "bi"),
        overview_json=overview_json,
        script=script,
    )
