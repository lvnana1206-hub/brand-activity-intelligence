import csv
from pathlib import Path


FIELDS = [
    "brand","priority_tier","region","country","activity_name","activity_type","activity_status",
    "start_date","end_date","discovery_date","channel_source","source_url","proof_screenshot",
    "city_or_region","venue","online_offline","product_line","member_only","member_benefit",
    "wecom_or_private_traffic_hook","entry_threshold","signup_flow","target_audience",
    "core_mechanic","ugc_or_creator_mechanic","offer_or_incentive","partnership_or_ip",
    "visual_keyword","engagement_signal","conversion_signal","reuse_score_for_insta360",
    "replication_difficulty","insight_summary","recommendation_for_insta360","owner",
    "review_status","last_updated",
]


def mk(
    brand, title, activity_type, start_date, source, url, online_offline, product_line,
    audience, mechanic, score, summary, recommendation, *, priority="P1", region="China",
    country="China", end_date=None, city="", venue="", member_only="no", member_benefit="",
    entry="public", signup="", offer="", ip="", difficulty="medium",
    review_status="seeded_with_inference",
):
    return {
        "brand": brand,
        "priority_tier": priority,
        "region": region,
        "country": country,
        "activity_name": title,
        "activity_type": activity_type,
        "activity_status": "completed" if start_date != "2026/06/09" else "ongoing",
        "start_date": start_date,
        "end_date": end_date or start_date,
        "discovery_date": "2026/06/09",
        "channel_source": source,
        "source_url": url,
        "proof_screenshot": "",
        "city_or_region": city,
        "venue": venue,
        "online_offline": online_offline,
        "product_line": product_line,
        "member_only": member_only,
        "member_benefit": member_benefit,
        "wecom_or_private_traffic_hook": "",
        "entry_threshold": entry,
        "signup_flow": signup,
        "target_audience": audience,
        "core_mechanic": mechanic,
        "ugc_or_creator_mechanic": "",
        "offer_or_incentive": offer,
        "partnership_or_ip": ip,
        "visual_keyword": "",
        "engagement_signal": "",
        "conversion_signal": "",
        "reuse_score_for_insta360": str(score),
        "replication_difficulty": difficulty,
        "insight_summary": summary,
        "recommendation_for_insta360": recommendation,
        "owner": "codex-recover",
        "review_status": review_status,
        "last_updated": "2026/06/09",
    }


ROWS = [
    mk("lululemon","lululemon 门店社群课入口","community_operation","2026/06/09","official content page","https://www.lululemon.cn/article-l-43.html","offline","women's activewear / community","young women; yoga users","门店课程与社群报名",5,"课程型活动对复访和社区沉淀特别有效。","影石可做固定频次的创作工作坊。",review_status="seeded"),
    mk("lululemon","lululemon 礼品卡","member_benefit","2026/06/09","official giftcard page","https://www.lululemon.cn/giftcard","online","gift card / repeat purchase","repeat customers; gifting buyers","礼品卡与送礼转化",3,"礼品卡属于基础复购工具，但很实用。","影石可做品牌礼卡、体验卡和课程卡。",member_only="yes",review_status="seeded"),
    mk("lululemon","lululemon 618 活动页","member_benefit","2026/06/01","official campaign page","https://www.lululemon.cn/active-1121.html","online","women's activewear / ecommerce","price-sensitive members","品牌大促与复购刺激",4,"购物节是复购刺激最强的短周期节点。","影石可建立大促活动页模板。",end_date="2026/06/18",member_only="yes",offer="campaign offers"),
    mk("lululemon","lululemon 城市门店社群活动周","community_operation","2025/11/01","media coverage on city community activation","https://www.vogue.com.cn/fashion/brand_news/news_125158e7dd2109d1.html","offline","women's activewear / lifestyle","community fitness users","城市社群活动周与门店复访",5,"一月一主题式社群活动适合做复访。","影石可做月度门店主题体验周。",end_date="2025/11/30",review_status="seeded"),
    mk("Salomon","Salomon 安福路概念店","store_experience","2026/06/09","SGB retail coverage","https://sgbonline.com/salomon-shanghai-anfu-road/","offline","outdoor lifestyle / footwear retail","young urban outdoor users","概念店与城市社群",4,"概念店是年轻人和户外用户交汇的好场景。","影石可做主题店或联名店。"),
    mk("Salomon","Salomon XT-Whisper × XSneaker 联名活动","brand_collab_offline_activation","2025/09/01","Hypebeast collaboration coverage","https://hypebeast.cn/2025/9/salomon-xsneaker-xt-whisper","offline","footwear collaboration / youth lifestyle","young sneaker users","联名限量发售与排队热度",4,"联名限量能快速制造社交热度与排队效应。","影石可做联名配件和限定体验空间。",end_date="2025/09/30",review_status="seeded"),
    mk("Salomon","Salomon 101FF 独家发售活动","member_benefit","2025/10/15","Hypebeast release coverage","https://hypebeast.cn/2025/10/salomon-101ff-exclusive-release","online","footwear drop / repeat purchase","loyal Salomon followers","独家发售与老用户回流",4,"独家发售有利于制造稀缺和回访。","影石可为会员做限定发售。",end_date="2025/10/31",member_only="yes"),
    mk("HOKA","HOKA 全球首家品牌体验中心","store_experience","2026/06/09","Hypebeast store coverage","https://hypebeast.cn/2025/5/hoka-one-one-shanghai-flagship-inside-look","offline","running footwear / premium retail","young runners","体验中心与试穿转化",5,"体验中心是线下转化效率最高的形态之一。","影石可设计一站式内容体验空间。"),
    mk("HOKA","HOKA LAB 飞跑研究所","member_service_activity","2026/06/09","Hypebeast store coverage","https://hypebeast.cn/2025/5/hoka-one-one-shanghai-flagship-inside-look","offline","runner service / loyalty","data-minded runners","体测服务与会员粘性",4,"服务型空间利于建立长期关系。","影石可做会员设备体检和创作咨询。",member_only="yes"),
    mk("HOKA","HOKA 中国限定与联名陈列","brand_collab_offline_activation","2026/06/09","Hypebeast store coverage","https://hypebeast.cn/2025/5/hoka-one-one-shanghai-flagship-inside-look","offline","retail drop / lifestyle","young runners; trend users","限定陈列与到店复购",4,"限定货盘能提高门店复访率。","影石可做城市限定壳、配件和作品卡。"),
    mk("On","On 门店查询入口","store_experience","2026/06/09","official store locator","https://www.on.com/zh-cn/stores","offline","running footwear / retail","urban runners","门店查询与到店转化",4,"基础入口不花哨，但转化效率很高。","影石可强化城市体验地图。",review_status="seeded"),
    mk("On","On 广州天环店开业跑","community_run","2025/11/21","PRNasia retail release","https://www.prnasia.com/story/513138-1.shtml","offline","running footwear / community","urban runners","门店开业跑与社群拉新",5,"这是非常典型的门店社群转化动作。","影石可把门店开业和社群活动做绑定。",review_status="seeded"),
    mk("On","On 成都太古里中国首家旗舰店开幕","store_experience","2025/04/27","Hypebeast retail coverage","https://hypebeast.cn/2025/4/on-first-china-flaship-store-chengdu-opening","offline","running footwear / flagship retail","young premium runners","中国首家旗舰店开幕",4,"旗舰店是长期线下经营的重要抓手。","影石可做城市文化主题体验店。",review_status="seeded"),
    mk("Nike","Nike Member Rewards & Offers","member_benefit","2026/06/09","official membership rewards page","https://www.nike.com/membership/member-rewards/","online","sportswear / member rewards","young sports users","会员奖励与返场复购",4,"轻权益对日常复购很有帮助。","影石可做会员券包和生日礼。"),
    mk("Nike","Nike 专属活动与免邮权益","member_service_activity","2025/06/09","official help article","https://www.nike.com/help/a/member-benefits","hybrid","sportswear / member retention","young sports users; runners","专属活动与长期留存",4,"会员活动+生日礼+免邮非常适合长期留存。","影石可做活动优先权和免运费权益。",member_only="yes"),
    mk("New Balance","New Balance Grey Days 2025","brand_collab_offline_activation","2025/05/02","Hypebeast campaign coverage","https://hypebeast.cn/2025/5/new-balance-grey-days-2025-release-info","hybrid","lifestyle footwear / youth campaign","young sneaker users","品牌节与复购机制",4,"年度主题活动非常适合做内容和交易双收。","影石可做年度记录主题月。",end_date="2025/05/29",review_status="seeded"),
    mk("New Balance","New Balance 1000 Grey Metallic 发售","brand_collab_offline_activation","2025/07/01","Hypebeast release coverage","https://hypebeast.cn/2025/7/new-balance-1000-grey-metallic-m1000f-release-info","online","lifestyle footwear / youth drop","young sneaker users","新品发售与社交讨论",3,"这类发售更偏种草，但也能带动复购。","影石可做限定配件周。",end_date="2025/09/30",review_status="seeded"),
    mk("Arc'teryx","Arc'teryx 门店查询入口","store_experience","2026/06/09","official store locator","https://arcteryx.com/cn/zh/store-locator","offline","premium outdoor retail","premium outdoor users","门店查询与高客单转化",4,"这类入口是高客单产品线下转化的基础。","影石可在高端产品线里加强门店入口。",review_status="seeded"),
    mk("Arc'teryx","Arc'teryx Explore 内容入口","community_operation","2026/06/09","official explore page","https://arcteryx.com/cn/zh/explore","online","outdoor content / community","outdoor enthusiasts","内容阵地与身份运营",3,"内容阵地更偏长期运营和品牌认同。","影石可打造品牌内容志。",member_only="yes",review_status="seeded"),
    mk("Arc'teryx","始祖鸟专业场地合作","city_activation","2026/06/09","SGB community climbing coverage","https://sgbonline.com/arcteryx-opens-chinas-first-world-class-climbing-site-at-shegeng-cave/","offline","outdoor climbing / community","climbers; outdoor enthusiasts","场地活动与专业社群",4,"场地级合作非常适合建立专业权威。","影石可做运动基地合作试拍。",review_status="seeded"),
]


def main() -> None:
    base = Path("/Users/insta360/Documents/Codex/2026-06-09/new-chat")
    src = base / "brand-activity-material-library.csv"
    with src.open(newline="", encoding="utf-8") as handle:
        existing = list(csv.DictReader(handle))
    seen = {(row["brand"], row["activity_name"]) for row in existing}
    merged = existing[:]
    for row in ROWS:
        key = (row["brand"], row["activity_name"])
        if key not in seen:
            merged.append(row)
            seen.add(key)
    with src.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(merged)


if __name__ == "__main__":
    main()
