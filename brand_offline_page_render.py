import html
import json
from collections import Counter

from brand_page_render import bi, css, evidence_panel, row_link_html


def page_css() -> str:
    return (
        css()
        + """
    .nav a.offline,.nav a.active{background:#fff;color:var(--accent)}
    .hero .heroDesc{max-width:980px}
    .denseGrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
    .twoCol{display:grid;grid-template-columns:1.35fr .95fr;gap:18px;margin-top:18px;align-items:start}
    .sectionGrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
    .miniStat{display:flex;justify-content:space-between;gap:10px;padding:10px 0;border-bottom:1px dashed #ead9ca}
    .miniStat:last-child{border-bottom:none}
    .valueInline{font-weight:800;color:var(--accent)}
    .tagRow{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
    .subtle{background:#fff7f1;border:1px solid #edd9cb;border-radius:16px;padding:14px}
    .libraryTable th:nth-child(1){width:110px}.libraryTable th:nth-child(3){width:130px}.libraryTable th:nth-child(4){width:120px}.libraryTable th:nth-child(5){width:120px}
    @media (max-width:1180px){.denseGrid,.sectionGrid,.twoCol{grid-template-columns:1fr}}
    """
    )


def nav() -> str:
    return (
        "<div class='nav'>"
        "<a href='brand-activity-overview.html'>年度总览</a>"
        "<a href='brand-activity-dashboard.html'>品牌活动情报看板</a>"
        "<a class='offline' href='brand-offline-activity-monitor.html'>线下活动专项页</a>"
        "<a href='brand-activity-learning-timeline.html'>品牌活动学习时间线</a>"
        "</div>"
    )


def activity_link(row: dict[str, str]) -> str:
    return row_link_html(row)


def channel_bucket(row: dict[str, str]) -> str:
    label = row.get("channel_label", "")
    if "小红书" in label:
        return "小红书"
    if "微博" in label:
        return "微博"
    if "会员" in label or "奖励" in label or "权益" in label:
        return "会员 / 权益页"
    if any(token in label for token in ["门店", "零售", "试驾", "服务"]):
        return "门店 / 到店入口"
    if any(token in label for token in ["新闻", "活动", "专题", "社区", "发布"]):
        return "官网内容 / 活动页"
    if any(token in label for token in ["媒体", "PR", "潮流"]):
        return "公开媒体 / 潮流媒体"
    return "其他公开来源"


def city_label(row: dict[str, str]) -> str:
    return row.get("city_or_region") or row.get("venue") or "未注明城市"


def is_store_conversion(row: dict[str, str]) -> bool:
    text = " ".join(
        [
            row.get("activity_type", ""),
            row.get("activity_name", ""),
            row.get("entry_threshold", ""),
            row.get("signup_flow", ""),
            row.get("conversion_signal", ""),
            row.get("wecom_or_private_traffic_hook", ""),
        ]
    )
    return row.get("activity_type") in {"store_experience", "test_drive_booking", "city_activation"} or any(
        token in text for token in ["到店", "门店", "试驾", "预约", "核销", "进群"]
    )


def is_member_growth(row: dict[str, str]) -> bool:
    return (
        row.get("member_only", "").lower() == "yes"
        or row.get("activity_type", "").startswith("member_")
        or bool(row.get("member_benefit"))
    )


def is_social_activation(row: dict[str, str]) -> bool:
    text = " ".join(
        [
            row.get("activity_type", ""),
            row.get("activity_name", ""),
            row.get("ugc_or_creator_mechanic", ""),
            row.get("partnership_or_ip", ""),
            row.get("core_mechanic", ""),
            row.get("channel_label", ""),
        ]
    )
    return row.get("activity_type") in {"community_operation", "community_run", "brand_collab_offline_activation"} or any(
        token in text for token in ["联名", "打卡", "跑团", "社群", "小红书", "微博"]
    )


def count_chart(items: list[tuple[str, int]], style: str = "") -> str:
    if not items:
        return "<div class='small'>暂无样本</div>"
    top = max(count for _, count in items) or 1
    total = sum(count for _, count in items) or 1
    rows = []
    for label, count in items:
        width = round(count / top * 100, 2)
        pct = round(count / total * 100)
        rows.append(
            f"<div class='chartRow'><div>{html.escape(label)}</div><div class='track'><div class='fill {style}' style='width:{width}%'></div></div><div class='small'>{count} / {pct}%</div></div>"
        )
    return "".join(rows)


def list_block(rows: list[dict[str, str]], empty: str) -> str:
    if not rows:
        return f"<li>{html.escape(empty)}</li>"
    items = []
    for row in rows[:8]:
        items.append(
            "<li>"
            f"<strong>{html.escape(row['display_brand'])}</strong>：{activity_link(row)}"
            f"<div class='small'>{html.escape(row.get('start_date') or 'Date TBD')} · {html.escape(row.get('activity_type_label') or '')} · {html.escape(row.get('link_note') or '')} · {html.escape(row.get('evidence_label') or '')}</div>"
            "</li>"
        )
    return "".join(items)


def templates(rows: list[dict[str, str]]) -> list[str]:
    types = [row.get("activity_type_label", "") for row in rows]
    top_types = [label for label, _ in Counter(types).most_common(4)]
    mapping = {
        "门店体验": "门店试拍模板：官网预约或小程序报名，现场试拍，结束后用企业微信或会员页承接二次触达。",
        "预约转化": "预约入口模板：把预约试拍、预约讲解、到店核销和后续优惠券放在同一链路里。",
        "社群活动": "社群课模板：城市社群招募 + 门店活动 + 打卡任务，活动结束后沉淀长期社群。",
        "联名线下激活": "联名快闪模板：限定陈列、打卡点、会员专属领取和门店二次消费动线一起设计。",
        "会员 / 复购机制": "会员权益模板：会员专属场次、生日礼、配件券和优先试拍形成长期复购理由。",
    }
    output = [mapping[label] for label in top_types if label in mapping]
    if len(output) < 4:
        output.extend(
            [
                "内容二现场模板：把小红书或微博预热做成门店活动的报名前台，现场活动再反向回流内容平台。",
                "城市巡回模板：每月固定 1-2 座城市做主题活动，形成稳定复盘节奏。",
            ]
        )
    return output[:4]


def offline_monitor_html(rows: list[dict[str, str]], suggestions: list[str], refresh_time: str, window_label: str) -> str:
    offline_rows = [row for row in rows if row.get("online_offline") in {"offline", "hybrid"}]
    offline_rows.sort(
        key=lambda row: (
            row.get("discovery_date", ""),
            row.get("start_date", ""),
            int(row.get("reuse_score_for_insta360") or 0),
        ),
        reverse=True,
    )
    latest_month = max(((row.get("start_date") or "")[:7] for row in offline_rows if row.get("start_date")), default="")
    month_rows = [row for row in offline_rows if (row.get("start_date") or "").startswith(latest_month)]
    detail_rows = [row for row in offline_rows if row.get("link_type") in {"detail", "reference"} and row.get("source_url")]
    brand_rank = Counter(row["display_brand"] for row in month_rows).most_common(6)
    channel_rank = Counter(channel_bucket(row) for row in month_rows).most_common(6)
    type_rank = Counter(row.get("activity_type_label") or "其他" for row in month_rows).most_common(6)
    all_type_rank = Counter(row.get("activity_type_label") or "其他" for row in offline_rows).most_common(8)
    city_rank = Counter(city_label(row) for row in offline_rows).most_common(8)
    all_channel_rank = Counter(channel_bucket(row) for row in offline_rows).most_common(8)
    store_rows = [row for row in offline_rows if is_store_conversion(row)]
    member_rows = [row for row in offline_rows if is_member_growth(row)]
    social_rows = [row for row in offline_rows if is_social_activation(row)]
    hero_stats = (
        ("线下 / 混合样本", len(offline_rows)),
        ("覆盖品牌", len({row["brand"] for row in offline_rows})),
        ("可点详情页", len(detail_rows)),
        ("本月样本", len(month_rows)),
    )
    row_seed = [
        {
            **row,
            "monitor_channel_bucket": channel_bucket(row),
            "city_label": city_label(row),
        }
        for row in offline_rows
    ]
    rows_json = html.escape(json.dumps(row_seed, ensure_ascii=False))
    template_list = "".join(f"<li>{html.escape(item)}</li>" for item in templates(offline_rows))
    suggestion_list = "".join(f"<li>{html.escape(item)}</li>" for item in suggestions[:4]) or "<li>待补充</li>"
    month_brand_list = "".join(
        f"<div class='miniStat'><div><strong>{html.escape(label)}</strong></div><div class='valueInline'>{count} 条</div></div>"
        for label, count in brand_rank
    ) or "<div class='small'>本月暂无线下新增样本</div>"
    month_channel_list = "".join(
        f"<div class='miniStat'><div><strong>{html.escape(label)}</strong></div><div class='valueInline'>{count} 条</div></div>"
        for label, count in channel_rank
    ) or "<div class='small'>本月暂无重点渠道样本</div>"
    month_type_list = "".join(
        f"<div class='miniStat'><div><strong>{html.escape(label)}</strong></div><div class='valueInline'>{count} 条</div></div>"
        for label, count in type_rank
    ) or "<div class='small'>本月暂无重点活动类型</div>"
    library_rows = "".join(
        "<tr>"
        f"<td><strong>{html.escape(row['display_brand'])}</strong><div class='small'>{html.escape(row['priority_label'])}</div></td>"
        f"<td>{activity_link(row)}<div class='small'>{html.escape(row.get('start_date') or 'Date TBD')} · {html.escape(row.get('link_note') or '')}</div><div class='small'>{html.escape(row.get('insight_summary') or '')}</div></td>"
        f"<td>{html.escape(row['monitor_channel_bucket'])}<div class='small'>{html.escape(row.get('channel_label') or '')}</div></td>"
        f"<td>{html.escape(row['city_label'])}</td>"
        f"<td>{html.escape(row.get('activity_type_label') or '')}</td>"
        f"<td class='{html.escape(row.get('evidence_class') or '')}'>{html.escape(row.get('evidence_label') or '')}</td>"
        "</tr>"
        for row in row_seed
    )
    script = """
<script>
const rows = JSON.parse(document.getElementById('offline-seed-data').textContent);
const tbody = document.getElementById('offline-rows');
const search = document.getElementById('offline-search');
const channel = document.getElementById('offline-channel');
const activity = document.getElementById('offline-activity');
const linkType = document.getElementById('offline-link');
const evidence = document.getElementById('offline-evidence');
function renderRows(){
  const q = search.value.trim().toLowerCase();
  const c = channel.value;
  const a = activity.value;
  const l = linkType.value;
  const e = evidence.value;
  tbody.innerHTML = rows.filter(row => {
    const hay = [row.display_brand,row.activity_name,row.activity_type_label,row.city_label,row.insight_summary,row.monitor_channel_bucket].join(' ').toLowerCase();
    return (!q || hay.includes(q)) && (!c || row.monitor_channel_bucket === c) && (!a || row.activity_type_label === a) && (!l || row.link_type === l) && (!e || row.evidence_level === e);
  }).map(row => {
    const title = row.source_url && row.link_type !== 'invalid' ? `<a href="${row.source_url}" target="_blank" rel="noreferrer">${row.activity_name}</a>` : row.activity_name;
    return `<tr><td><strong>${row.display_brand}</strong><div class='small'>${row.priority_label}</div></td><td>${title}<div class='small'>${row.start_date || 'Date TBD'} · ${row.link_note || ''}</div><div class='small'>${row.insight_summary || ''}</div></td><td>${row.monitor_channel_bucket}<div class='small'>${row.channel_label || ''}</div></td><td>${row.city_label || ''}</td><td>${row.activity_type_label || ''}</td><td class='${row.evidence_class || ''}'>${row.evidence_label || ''}</td></tr>`;
  }).join('');
}
[search,channel,activity,linkType,evidence].forEach(el => {el.addEventListener('input', renderRows); el.addEventListener('change', renderRows);});
renderRows();
</script>
"""
    return f"""<!doctype html><html lang='zh-CN'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><title>线下活动专项监控</title><style>{page_css()}</style></head><body><div class='wrap'><section class='hero'>{nav()}{bi('线下活动专项监控', '', 'h1', 'heroTitle bi')}<div class='heroDesc'>{bi('聚焦线下活动、到店转化、会员承接和复购机制，方便快速查看可落地方案。', '', 'p', 'bi')}</div><div class='stats'>{''.join(f"<div class='metric'>{bi(label, '', 'div', 'bi')}<div class='value'>{value}</div></div>" for label, value in hero_stats)}</div><div class='tagRow'><span class='pill'>监控窗口：{html.escape(window_label)}</span><span class='pill'>最新月份：{html.escape(latest_month or '未识别')}</span><span class='pill'>活动详情页可直接点击</span><span class='pill'>转化入口页仅保留说明</span></div></section><section class='twoCol'><div class='stack'><div class='panel'>{bi('影石线下行动建议', '', 'h2', 'bi')}<p class='small'>优先把别的品牌“种草 -> 到店 -> 会员 -> 复购”链路里能直接复用的动作放在前面。</p><ul class='list'>{suggestion_list}</ul></div><div class='denseGrid'><div class='panel'>{bi('本月重点品牌', '', 'h2', 'bi')}<p class='small'>按本月线下 / 混合型样本数量排序。</p>{month_brand_list}</div><div class='panel'>{bi('本月重点渠道', '', 'h2', 'bi')}<p class='small'>看本月线下活动最活跃的入口渠道。</p>{month_channel_list}</div><div class='panel'>{bi('本月重点活动类型', '', 'h2', 'bi')}<p class='small'>看本月品牌更偏爱哪类线下动作。</p>{month_type_list}</div></div><div class='sectionGrid'><div class='panel'>{bi('最近几天线下活动速览', '', 'h2', 'bi')}<p class='small'>优先按最近几天的抓取与活动时间排序，方便先看这轮新补进来的线下动作。</p><ul class='list'>{list_block(detail_rows, '暂无可直接打开的线下活动详情页。')}</ul></div><div class='panel'>{bi('到店转化活动池', '', 'h2', 'bi')}<p class='small'>优先看报名、预约、到店核销、试驾、试拍这类转化强动作。</p><ul class='list'>{list_block(store_rows, '暂无到店转化样本。')}</ul></div><div class='panel'>{bi('会员复购活动池', '', 'h2', 'bi')}<p class='small'>重点观察会员专属场次、权益包、礼品卡、积分和复购券。</p><ul class='list'>{list_block(member_rows, '暂无会员复购样本。')}</ul></div><div class='panel'>{bi('社群 / 联名 / 打卡活动池', '', 'h2', 'bi')}<p class='small'>重点看小红书、微博、门店社群课、联名快闪和打卡任务的联动玩法。</p><ul class='list'>{list_block(social_rows, '暂无社群或联名打卡样本。')}</ul></div></div><div class='panel'>{bi('可直接学习的线下模板', '', 'h2', 'bi')}<p class='small'>这里不是泛灵感，而是可以直接拆成活动 SOP 的结构。</p><ul class='list'>{template_list}</ul></div><div class='panel'>{bi('线下活动样本库', '', 'h2', 'bi')}<p class='small'>活动详情页可直接点击；如果是门店页、会员页、试驾页这类转化入口页，会保留说明但不强制跳转。</p><div class='toolbar'><input id='offline-search' type='search' placeholder='搜索品牌、活动、城市、机制'><select id='offline-channel'><option value=''>全部渠道</option><option value='门店 / 到店入口'>门店 / 到店入口</option><option value='会员 / 权益页'>会员 / 权益页</option><option value='官网内容 / 活动页'>官网内容 / 活动页</option><option value='小红书'>小红书</option><option value='微博'>微博</option><option value='公开媒体 / 潮流媒体'>公开媒体 / 潮流媒体</option></select><select id='offline-activity'><option value=''>全部活动类型</option>{''.join(f"<option value='{html.escape(label)}'>{html.escape(label)}</option>" for label, _ in all_type_rank)}</select><select id='offline-link'><option value=''>全部链接类型</option><option value='detail'>只看活动详情页</option><option value='entry'>只看转化入口页</option><option value='reference'>只看参考页</option></select><select id='offline-evidence'><option value=''>全部证据等级</option><option value='direct'>官方直证</option><option value='support'>官方辅助</option><option value='reference'>公开参考</option><option value='invalid'>失效待核</option></select></div><table class='libraryTable'><thead><tr><th>品牌</th><th>活动</th><th>渠道</th><th>城市 / 场地</th><th>类型</th><th>证据等级</th></tr></thead><tbody id='offline-rows'>{library_rows}</tbody></table></div></div><aside class='stack side'><div class='panel'>{bi('线下活动类型分布', '', 'h2', 'bi')}<p class='small'>看当前线下样本里，什么类型最常被拿来做转化。</p>{count_chart(all_type_rank, 'strong')}</div><div class='panel'>{bi('渠道占比', '', 'h2', 'bi')}<p class='small'>看线下监控里，哪些渠道最值得持续盯。</p>{count_chart(all_channel_rank, 'alt')}</div><div class='panel'>{bi('重点城市分布', '', 'h2', 'bi')}<p class='small'>看活动更集中在哪些城市，方便判断巡回和落地优先级。</p>{count_chart(city_rank)}</div>{evidence_panel()}<div class='panel'>{bi('线下监控说明', '', 'h2', 'bi')}<div class='subtle'><p><strong>这个页面看什么</strong></p><p class='small'>集中看线下活动、到店入口、会员承接和复购机制。</p><p><strong>怎么用</strong></p><p class='small'>先看“最近几天线下活动速览”和“到店转化活动池”，再回到样本库搜品牌或城市。</p></div></div></aside></section></div><script id='offline-seed-data' type='application/json'>{rows_json}</script>{script}</body></html>"""
