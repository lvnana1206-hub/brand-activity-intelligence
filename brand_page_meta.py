from __future__ import annotations
BRAND_META = {
    "DJI": ("大疆", "DJI"),
    "Apple": ("苹果", "Apple"),
    "OPPO": ("OPPO", "OPPO"),
    "vivo": ("vivo", "vivo"),
    "Samsung": ("三星", "Samsung"),
    "LEGO": ("乐高", "LEGO"),
    "DESCENTE": ("迪桑特", "DESCENTE"),
    "POP MART": ("泡泡玛特", "POP MART"),
    "CHAGEE": ("霸王茶姬", "CHAGEE"),
    "GoPro": ("GoPro", "GoPro"),
    "Garmin": ("佳明", "Garmin"),
    "Shokz": ("韶音", "Shokz"),
    "Huawei": ("华为", "Huawei"),
    "Xiaomi": ("小米", "Xiaomi"),
    "HONOR": ("荣耀", "HONOR"),
    "OnePlus": ("一加", "OnePlus"),
    "realme": ("真我", "realme"),
    "Lenovo": ("联想", "Lenovo"),
    "Sony": ("索尼", "Sony"),
    "Canon": ("佳能", "Canon"),
    "Fujifilm": ("富士", "Fujifilm"),
    "Bose": ("博士", "Bose"),
    "JBL": ("JBL", "JBL"),
    "Marshall": ("Marshall", "Marshall"),
    "Anker": ("安克", "Anker"),
    "Arc'teryx": ("始祖鸟", "Arc'teryx"),
    "Salomon": ("萨洛蒙", "Salomon"),
    "HOKA": ("HOKA", "HOKA"),
    "On": ("On昂跑", "On"),
    "lululemon": ("lululemon", "lululemon"),
    "Nike": ("耐克", "Nike"),
    "New Balance": ("New Balance", "New Balance"),
    "HEYTEA": ("喜茶", "HEYTEA"),
    "Nayuki": ("奈雪的茶", "Nayuki"),
    "ChaPanda": ("茶百道", "ChaPanda"),
    "Guming": ("古茗", "Guming"),
    "Auntea Jenny": ("沪上阿姨", "Auntea Jenny"),
    "Shuyi": ("书亦烧仙草", "Shuyi"),
    "MANNER": ("MANNER", "MANNER"),
    "BYD": ("比亚迪", "BYD"),
    "NIO": ("蔚来", "NIO"),
    "XPeng": ("小鹏汽车", "XPeng"),
    "Li Auto": ("理想汽车", "Li Auto"),
    "AITO": ("问界", "AITO"),
    "ZEEKR": ("极氪", "ZEEKR"),
    "Xiaomi EV": ("小米汽车", "Xiaomi EV"),
    "Tesla": ("特斯拉", "Tesla"),
}

CHINA_FOCUS_META = {
    "DJI": ("围绕新品发布和产品页跳转做高效转化，重点放在新手创作者的首购教育。", "Use launch moments and product-page handoff to convert first-time creators in China."),
    "Apple": ("通过体验活动与生态内容教育，驱动到店互动和长期品牌留存。", "Use educational experiences and ecosystem events to drive store traffic and retention in China."),
    "OPPO": ("用开发者大会和生态发布持续拉动社区活跃与新品认知。", "Turn ecosystem conferences into community retention and product awareness in China."),
    "vivo": ("以影像馆和零售体验驱动到店试拍、入会与高意向线索沉淀。", "Use immersive retail imaging spaces to drive store trials, membership sign-ups, and leads in China."),
    "Samsung": ("用发布会热度叠加体验空间和预约激励，延长转化窗口。", "Extend launch momentum with experience spaces and preorder incentives in China."),
    "LEGO": ("通过会员日、门店活动和城市亲子体验，把品牌好感转成高频到店与复购。", "Use membership moments and store events to turn brand affinity into store traffic and repeat purchase in China."),
    "DESCENTE": ("把新品发布和 App 先行权益绑定，优先收口会员与高意向用户。", "Tie launches to app-first access to capture members and high-intent shoppers in China."),
    "POP MART": ("用 IP 展览、限定发售和乐园活动，推动到场、社交传播和现场购买。", "Use IP exhibitions, limited drops, and park events to drive attendance, sharing, and on-site purchase in China."),
    "CHAGEE": ("把文化联名、小程序任务和门店动线合在一起，形成到店和复购转化。", "Combine cultural collaborations, mini-program tasks, and store routes to drive visits and repeat purchase in China."),
    "HEYTEA": ("用节日限定、联名杯套、小程序券包和门店核销把流量快速收口。", "Use seasonal drops, collab packaging, mini-program coupons, and store redemption to convert traffic quickly in China."),
    "Nayuki": ("把 IP 联名、答题互动、小程序抽奖和到店核销结合，适合做年轻女性高频复购。", "Combine IP tie-ins, quiz games, mini-program lotteries, and store redemption to drive frequent repeat purchase in China."),
    "ChaPanda": ("用社群群发、小程序任务和低门槛抽奖快速做拉新与短期回流。", "Use group messaging, mini-program tasks, and low-threshold giveaways to drive acquisition and short-term reactivation in China."),
    "Guming": ("把猜口令、签到、优惠券和门店兑换串起来，适合做高频日更型活动。", "Connect code-guessing, check-ins, coupons, and store redemption for high-frequency daily promotions in China."),
    "Auntea Jenny": ("用集卡、小程序互动和企业微信社群做连续复访与新品转化。", "Use card collection, mini-program interactions, and enterprise WeChat groups to drive repeat visits and new-product conversion in China."),
    "Shuyi": ("用区域门店活动、买赠和小程序券包强化即时购买与复购。", "Use regional store activations, bundled offers, and mini-program coupon packs to drive immediate purchase and repeat purchase in China."),
    "GoPro": ("把硬件上新与软件工作流、订阅权益一起卖，提升单次活动的转化深度。", "Tie hardware refreshes to editing workflows and subscriptions to deepen conversion in China."),
    "Garmin": ("以跑团、训练营和赛事合作沉淀长期高频运动用户，再带动设备购买。", "Use run clubs, training camps, and races to build loyal sports communities before conversion in China."),
    "Shokz": ("用抽奖留资和赛事合作沉淀私域线索，再承接后续购买转化。", "Use lead-capture giveaways and sports-event tie-ins to grow private traffic leads in China."),
    "Huawei": ("通过旗舰发布会和开发者生态活动拉动高端机型关注、到店体验和鸿蒙生态认知。", "Drive flagship awareness and ecosystem adoption through launches and developer events in China."),
    "Xiaomi": ("通过人车家全生态发布会放大新品联动，提升整套生活方式场景的购买转化。", "Use Human x Car x Home launches to boost bundled ecosystem conversion in China."),
    "HONOR": ("通过旗舰新品发布和技术故事强化高端形象，再承接预约和首购转化。", "Use flagship launches and tech narratives to support premium conversion in China."),
    "OnePlus": ("通过新品发布和快闪体验增强社群热度，带动性能旗舰购买。", "Combine launches and pop-up experiences to convert community attention into device sales."),
    "BYD": ("通过车型上市和区域试驾活动放大到店咨询与订单转化。", "Use model launches and regional test-drive events to convert interest into showroom visits and orders."),
    "NIO": ("通过 NIO Day、交付中心和用户社区活动强化高端用户黏性与转介绍。", "Use NIO Day, delivery centers, and community events to deepen loyalty and referrals."),
    "XPeng": ("通过 AI 技术发布和新车上市强化科技心智，承接试驾和预订。", "Use AI announcements and new-car launches to convert tech attention into drives and reservations."),
    "Li Auto": ("通过家庭场景和发布会叙事驱动到店试驾与高意向订单。", "Use family scenario storytelling and launch events to drive test drives and order intent."),
    "Xiaomi EV": ("通过发布会和生态联动把汽车新品直接接入小米既有用户池。", "Connect EV launches directly into Xiaomi's existing ecosystem user base."),
    "lululemon": ("通过社区课程、门店活动和主题 IP 把线上社交热度沉淀成线下到店与复购。", "Turn community classes and branded IP events into store visits and repeat purchase in China."),
    "Salomon": ("通过越野赛事、社区跑和会员权益强化高黏性户外人群的复购与门店转化。", "Use trail races, community runs, and member benefits to convert core outdoor users in China."),
    "Arc'teryx": ("通过高端门店、会员权益和稀缺活动放大身份认同与高客单复购。", "Use premium stores, member privileges, and scarce events to reinforce identity and repeat purchase."),
    "HOKA": ("通过跑者社群空间、赛事和快闪体验把线上兴趣导向门店和试穿转化。", "Turn runner communities, races, and pop-ups into store traffic and try-on conversion in China."),
    "On": ("通过旗舰店、城市跑和社群空间把线上热度转成日常到店和持续互动。", "Use flagships, city runs, and community spaces to convert online attention into store visits in China."),
    "Nike": ("通过 Nike Membership、App 内会员活动和城市社群运营提升复购与线下参与。", "Use Nike Membership and app-based member events to drive repeat purchase and offline participation."),
    "New Balance": ("通过快闪、门店互动展区和灰日主题活动强化年轻人到店体验与社交分享。", "Use pop-ups and themed in-store activations to drive youth store visits and social sharing."),
}

UNIVERSE_GROUPS = [
    ("消费电子", "Consumer Electronics", ["DJI", "Apple", "Huawei", "Xiaomi", "HONOR", "OPPO", "vivo", "Samsung", "OnePlus", "realme", "Lenovo", "Sony", "Canon", "Fujifilm", "GoPro", "Garmin", "Shokz", "Anker", "Bose", "JBL", "Marshall"]),
    ("户外运动与生活方式", "Outdoor & Lifestyle", ["DESCENTE", "Arc'teryx", "Salomon", "HOKA", "On", "lululemon", "Nike", "New Balance"]),
    ("潮流与城市消费", "Pop Culture & Urban Consumption", ["LEGO", "POP MART", "CHAGEE", "HEYTEA", "Nayuki", "ChaPanda", "Guming", "Auntea Jenny", "Shuyi", "MANNER"]),
    ("车企", "Automotive", ["BYD", "NIO", "XPeng", "Li Auto", "AITO", "ZEEKR", "Xiaomi EV", "Tesla"]),
]

STATUS_TABLE_GROUPS = [
    ("中国消费电子", "China Consumer Electronics", ["DJI", "Huawei", "Xiaomi", "HONOR", "OPPO", "vivo", "OnePlus", "realme", "Lenovo", "Anker"]),
    ("重点车企", "Key Automotive Brands", ["BYD", "NIO", "XPeng", "Li Auto", "AITO", "ZEEKR", "Xiaomi EV", "Tesla"]),
    ("户外运动品牌", "Outdoor Sports Brands", ["lululemon", "Salomon", "Arc'teryx", "HOKA", "On", "Nike", "New Balance"]),
    ("年轻生活方式品牌", "Youth Lifestyle Brands", ["LEGO", "POP MART", "CHAGEE", "HEYTEA", "Nayuki", "ChaPanda", "Guming", "Auntea Jenny", "Shuyi", "MANNER"]),
]

ACTIVE_COLLECTION_BRANDS = {
    "Huawei",
    "Xiaomi",
    "HONOR",
    "OnePlus",
    "Sony",
    "BYD",
    "NIO",
    "XPeng",
    "Li Auto",
    "AITO",
    "ZEEKR",
    "Xiaomi EV",
    "Tesla",
    "lululemon",
    "Salomon",
    "Arc'teryx",
    "HOKA",
    "On",
    "Nike",
    "New Balance",
}

SOURCE_CHANNELS = [
    ("官网", "Official Site", "高结构化，适合稳定抓取", "Most structured and the most stable for repeatable crawling."),
    ("小红书", "Xiaohongshu", "适合抓活动预热、打卡反馈和用户讨论", "Best for event previews, check-in content, and user discussion."),
    ("大众点评", "Dianping", "适合抓门店活动、快闪位置和用户评价", "Best for store events, pop-up locations, and venue feedback."),
    ("微博", "Weibo", "适合抓官宣、联名预告和实时讨论热度", "Best for official announcements, collab teasers, and real-time buzz."),
    ("微信公众号/视频号", "WeChat Official Accounts / Channels", "适合抓私域活动公告和报名转化", "Best for private-traffic announcements and sign-up conversion."),
]

ACTIVITY_TYPE_META = {
    "product_launch": ("新品发布", "Product Launch"),
    "conference": ("大会活动", "Conference"),
    "store_experience": ("门店体验", "Store Experience"),
    "test_drive_booking": ("预约转化", "Booking Conversion"),
    "community_operation": ("社群活动", "Community Operation"),
    "retail_experience": ("零售体验", "Retail Experience"),
    "city_activation": ("城市激活", "City Activation"),
    "member_benefit": ("会员权益", "Member Benefit"),
    "member_service_activity": ("会员服务活动", "Member Service Activity"),
    "member_app_presale": ("会员/App 先行", "Member/App Presale"),
    "member_referral": ("邀请裂变", "Member Referral"),
    "ip_exhibition_series": ("IP 展览系列", "IP Exhibition Series"),
    "brand_collab_offline_activation": ("联名线下激活", "Brand Collaboration Activation"),
    "community_run": ("社群跑团", "Community Run"),
    "ugc_creator_competition": ("UGC 创作征集", "UGC Creator Competition"),
    "email_signup_promo": ("留资抽奖", "Lead-Capture Promo"),
}

PRIORITY_META = {
    "P0": ("核心必看", "Core Watchlist"),
    "P1": ("重点扩展", "Expansion Watchlist"),
    "P2": ("灵感补充", "Inspiration Pool"),
}

STATUS_META = {
    "seeded": ("已确认", "Verified Seed"),
    "seeded_with_inference": ("待补强", "Needs Follow-up"),
}


def brand_names(brand: str) -> tuple[str, str]:
    return BRAND_META.get(brand, (brand, brand))


def brand_focus(brand: str) -> tuple[str, str]:
    return CHINA_FOCUS_META.get(
        brand,
        ("待补充中国区重点转化活动。", "China conversion focus to be enriched."),
    )
