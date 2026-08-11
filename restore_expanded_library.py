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
    brand, priority, region, country, title, activity_type, start_date, source, url,
    online_offline, product_line, target_audience, mechanic, score, summary, recommendation,
    *, end_date=None, city="", venue="", member_only="no", member_benefit="", hook="",
    entry="public", signup="", ugc="", offer="", ip="", visual="", engagement="",
    conversion="", difficulty="medium", review_status="seeded_with_inference",
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
        "wecom_or_private_traffic_hook": hook,
        "entry_threshold": entry,
        "signup_flow": signup,
        "target_audience": target_audience,
        "core_mechanic": mechanic,
        "ugc_or_creator_mechanic": ugc,
        "offer_or_incentive": offer,
        "partnership_or_ip": ip,
        "visual_keyword": visual,
        "engagement_signal": engagement,
        "conversion_signal": conversion,
        "reuse_score_for_insta360": str(score),
        "replication_difficulty": difficulty,
        "insight_summary": summary,
        "recommendation_for_insta360": recommendation,
        "owner": "codex-recover",
        "review_status": review_status,
        "last_updated": "2026/06/09",
    }


RECOVERED_ROWS = [
    mk("Huawei","P0","China","China","HDC 2025 华为开发者大会","conference","2025/06/20","official developer conference page","https://developer.huawei.com/consumer/cn/hdc2025/","offline","HarmonyOS ecosystem / developer platform","developers; ecosystem partners","年度开发者大会与生态路线图发布",4,"华为用开发者大会沉淀生态伙伴与技术社群。","影石可做创作者开放日或 SDK 训练营。",end_date="2025/06/22",city="Dongguan",venue="松山湖",signup="conference page to registration"),
    mk("Huawei","P0","China","China","华为影像 XMAGE Awards 2025 共见上海","brand_collab_offline_activation","2025/06/11","official press article","https://consumer.huawei.com/cn/press/news/2025/xmage-event-sh/","hybrid","mobile imaging / creator community","mobile photographers; creators","影像赛事与城市展览",5,"影像赛事和城市展览兼顾内容生产与品牌展示。","影石可复制赛事+城市展览+创作者社群组合。",end_date="2025/10/08",city="Shanghai",ip="XMAGE Awards",ugc="creator submission and social exposure"),
    mk("Huawei","P0","China","China","华为线下零售门店体验入口","store_experience","2026/06/09","official retail page","https://consumer.huawei.com/cn/retail/","offline","smartphone retail","premium device users","门店查询与顾问咨询转化",4,"门店入口是典型的线上引流到店基础设施。","影石可把门店试拍和顾问咨询统一收口。"),
    mk("Huawei","P0","China","China","华为消费者服务活动与到店支持入口","member_service_activity","2026/06/09","official support page","https://consumer.huawei.com/cn/support/","hybrid","after-sales / user retention","existing users; members","服务活动与售后复访",3,"售后活动会反向促进复购和会员留存。","影石可做会员服务月与到店设备体检。",member_only="yes",member_benefit="service campaigns and support resources"),
    mk("Huawei","P0","China","China","华为社区活动入口","community_operation","2026/06/09","official community page","https://consumer.huawei.com/cn/community/","online","community / content ecosystem","brand community users; creators","社区内容与活动聚合",4,"社区阵地适合承接作品活动和长期留存。","影石可做官方创作者社区首页。",member_only="yes"),

    mk("Xiaomi","P0","China","China","New Beginnings：小米北京人车家全生态发布活动","product_launch","2025/06/26","official global event page","https://www.mi.com/global/discover/","hybrid","smartphone / smart home ecosystem","ecosystem shoppers; urban lifestyle users","人车家全生态发布",5,"小米擅长把多产品线打成同一场发布事件。","影石可把相机、配件、软件和服务做一体化套餐发布。",city="Beijing"),
    mk("Xiaomi","P0","China","Global","Xiaomi Launch February 2026","product_launch","2026/02/28","official global event page","https://www.mi.com/global/event/2026/xiaomi-launch-february-2026/","hybrid","smartphone / imaging","technology users; Xiaomi fans","旗舰影像与合作叙事发布",4,"旗舰影像和合作叙事适合参考到影像合作品牌活动包装。","影石可围绕合作品牌做联名视觉和内容发布。"),
    mk("Xiaomi","P0","China","Global","Xiaomi Fan Festival 2026","member_app_presale","2026/04/01","official campaign terms page","https://www.mi.com/global/support/terms/xiaomi-fan-festival-2026/","online","membership / commerce promotion","Mi community users; repeat buyers","品牌节与会员运营",4,"品牌节是典型的高频会员运营工具。","影石可做影石会员月或创作者福利周。",end_date="2026/04/30",member_only="yes"),
    mk("Xiaomi","P0","China","Global","Xiaomi 客服与线下支持联系入口","store_experience","2026/06/09","official support page","https://www.mi.com/global/support/contact/","hybrid","support / retail contact","existing users; new buyers","客服与联系页承接到店支持",3,"客服与联系页是私域承接和到店支持的底层入口。","影石可把客服、门店、试拍和维修统一到一个入口。"),
    mk("Xiaomi","P0","China","Global","Xiaomi Imagery Awards 2025","ugc_creator_competition","2026/06/09","official campaign page","https://www.mi.com/global/xiaomiImageryawards/","online","mobile imaging / creator community","mobile photographers; creators","UGC 赛事与作品征集",4,"UGC 赛事非常适合影石这类内容驱动型品牌。","影石可做年度影像奖，串联投稿、评选、展览和社群。"),

    mk("HONOR","P0","China","China","荣耀 500 系列正式发布","product_launch","2025/11/24","official news article","https://www.honor.com/cn/news/honor-500-launch/","hybrid","smartphone / AI devices","mobile users; content creators","主流旗舰发布",4,"荣耀 500 的发布方式适合借鉴到年轻用户导向的产品活动。","影石可为 GO 系列做更年轻化的内容场景包装。"),
    mk("HONOR","P0","China","China","荣耀与中国联通签署战略合作协议","brand_collab_offline_activation","2025/07/18","official news article","https://www.honor.com/cn/news/honor-china-unicom-strategic-cooperation/","offline","channel partnership / retail ecosystem","operator channel users; enterprise partners","渠道合作与门店触点扩张",3,"渠道合作类活动更适合放大触点和到店效率。","影石可与渠道方做联合体验日或包场体验。"),
    mk("HONOR","P0","China","China","荣耀线下零售门店体验入口","store_experience","2026/06/09","official retail page","https://www.honor.com/cn/retail/","offline","smartphone retail","young users; gift shoppers","门店查询与到店体验",4,"荣耀门店页的作用是把线上热度快速导流到线下触点。","影石可把门店活动、预约体验和会员绑定。"),
    mk("HONOR","P0","China","China","荣耀服务活动专区","member_service_activity","2026/06/09","official service activity page","https://www.honor.com/cn/support/activity-list/","hybrid","service / member loyalty","existing users; members","服务活动区与售后复访",3,"服务活动对高客单硬件的复购和口碑沉淀很关键。","影石可做会员服务月和售后权益活动。",member_only="yes"),
    mk("HONOR","P0","China","China","荣耀 HONOR Talks 城市互动活动","brand_collab_offline_activation","2026/06/09","official retail campaign page","https://www.honor.com/cn/retail/honor-talks/","offline","brand retail / community","young users; culture and lifestyle users","城市互动活动与门店引流",4,"这种活动兼顾了内容感和到店效率。","影石可做城市分享会、体验会、创作者对谈。"),

    mk("OnePlus","P0","China","China","OnePlus Photography Awards 2025","ugc_creator_competition","2025/06/01","official campaign page","https://www.oneplus.com/cn/photography-awards-2025","online","smartphone imaging / community","mobile photographers; community users","影像赛事与作品征集",4,"UGC 赛事非常适合影石学习。","影石可同步做作品评审、社群分享和优胜者线下展。",end_date="2025/06/30"),
    mk("OnePlus","P0","China","China","一加 Ace 6 至尊版发布活动","product_launch","2026/06/05","official launch page","https://www.oneplus.com/cn/ace-6-ultra-launch","hybrid","performance smartphone","performance phone buyers","性能旗舰直播发布",4,"一加这种性能机发布适合参考到参数强卖点 + 直播首发转化结构。","影石可为高性能产品做直播首发和限时权益。"),
    mk("OnePlus","P0","China","China","一加线下门店地图","store_experience","2026/06/09","official retail map","https://www.oneplus.com/cn/retail/map","offline","smartphone retail","young tech users","门店地图导流到店",4,"门店地图是典型的线上热度导流线下体验入口。","影石可把门店、体验点和城市试拍活动统一聚合。"),
    mk("OnePlus","P0","China","China","一加邀请有礼","member_referral","2026/06/09","official referral page","https://www.oneplus.com/cn/invite","online","member referral / commerce","existing users; members","推荐奖励与裂变",5,"推荐奖励极适合影石做社群裂变和会员拉新。","影石可做邀请好友试拍得周边/积分。",member_only="yes",member_benefit="invite rewards"),
    mk("OnePlus","P0","China","China","一加优惠券中心","member_benefit","2026/06/09","official coupon page","https://www.oneplus.com/cn/coupon","online","coupon / member benefit","price-sensitive members; repeat buyers","优惠券与直接转化",4,"简单粗暴，但对复购和清库存很有效。","影石可把会员券与活动报名绑定。",member_only="yes",member_benefit="coupon and price incentives"),

    mk("BYD","P0","China","China","比亚迪海豹 06EV 广州上市","product_launch","2025/06/11","official news listing","https://www.byd.com/cn/news","offline","EV sedan","mass EV buyers","区域上市活动",4,"区域上市活动有助于迅速拉动门店线索和试驾需求。","影石可围绕重点城市做线下体验与限时权益组合。",city="Guangzhou"),
    mk("BYD","P0","China","China","比亚迪全地形赛车场正式开业","city_activation","2025/08/15","official news article","https://www.byd.com/cn/news/2025/detail602","offline","off-road experiential driving","driving enthusiasts","自有场地体验",4,"场地型活动能把复杂产品卖点转成用户可体验内容。","影石可与营地、摄影基地合作搭建固定体验空间。"),
    mk("BYD","P0","China","China","比亚迪和美的开启智慧家生活解决方案战略合作","brand_collab_offline_activation","2025/11/24","official news article","https://www.byd.com/cn/news/2025/detail610","offline","smart home / auto ecosystem","family users; ecosystem buyers","生态合作场景方案",3,"生态合作有助于把品牌从单品升级为生活方式方案。","影石可与露营、骑行、户外家居品牌做联合活动。",ip="美的"),
    mk("BYD","P0","China","China","比亚迪试驾预约入口","test_drive_booking","2026/06/09","official test-drive page","https://www.byd.com/cn/test-driver","online","vehicle sales conversion","mass EV buyers","试驾预约与线索收口",5,"试驾预约是车企最强的线索收口页面之一。","影石可以做预约试拍主入口并配顾问跟进。"),
    mk("BYD","P0","China","China","比亚迪王朝门店查询入口","store_experience","2026/06/09","official store page","https://www.byd.com/cn/dynasty-home/find-store","offline","showroom / retail","family buyers","王朝门店分流",4,"按产品线拆门店更容易承接高意向用户。","影石可按产品线拆分体验点和预约入口。"),
    mk("BYD","P0","China","China","比亚迪海洋门店查询入口","store_experience","2026/06/09","official store page","https://www.byd.com/cn/ocean-home/find-store","offline","showroom / retail","young buyers","海洋门店分流",4,"年轻向产品线更适合单独的门店表达。","影石可对 GO 系列做年轻化体验入口。"),

    mk("NIO","P0","China","China","NIO Day 2025 将在杭州举办","city_activation","2025/08/25","official news listing","https://www.nio.com/news","offline","premium EV / owner community","premium EV owners; brand community","年度品牌日与城市落地",5,"品牌日更像高净值用户关系运营，而不只是一次发布会。","影石可做年度创作者日或用户大会。",city="Hangzhou"),
    mk("NIO","P0","China","China","NIO All-New ES8 开启预订","member_app_presale","2025/08/21","official news article","https://www.nio.com/news/20250821001","online","premium EV / member ecosystem","premium EV owners","预订权益与老车主转化",5,"蔚来非常擅长把老用户权益和新车预订绑定起来。","影石可做老用户专属升级、预订和积分权益。",member_only="yes",member_benefit="pre-order benefits and repurchase vouchers"),
    mk("NIO","P0","China","China","NIO ES9 正式发布","product_launch","2026/05/27","official news article","https://www.nio.com/news/20260527001","hybrid","premium executive EV","premium executive users","发布即交付",4,"发布即交付/即体验的节奏很适合高客单产品。","影石可尝试新品发布当周开放核心城市试拍。"),
    mk("NIO","P0","China","China","NIO Summer 2025 社区派对与主题试驾","community_operation","2025/07/01","official monthly update","https://www.nio.com/news/20250702001","offline","owner community / lifestyle events","owners; prospects","社区派对与主题试驾",5,"这是非常接近影石可复用的社区运营打法。","影石可做夏季城市记录季，结合主题试拍和线下社群活动。",end_date="2025/08/31"),
    mk("NIO","P0","China","China","蔚来 80 万台下线暨 ONVO L90 试驾开放","test_drive_booking","2025/07/24","official news article","https://www.nio.com/news/20250724001","offline","family SUV","family users; prospective buyers","试驾开放与城市门店名单",5,"这个动作本质上是在把新品关注直接导向线下体验。","影石可做试拍开放日 + 城市名单联动。"),
    mk("NIO","P0","China","China","蔚来进博会官方出行合作","brand_collab_offline_activation","2025/11/04","official news article","https://www.nio.com/news/20251104001","offline","brand partnership / service experience","public guests; premium mobility users","大型活动服务合作",4,"大型活动服务合作能提升品牌服务心智和口碑。","影石可与大型展会或赛事合作做官方影像服务伙伴。",end_date="2025/11/10",city="Shanghai"),

    mk("Li Auto","P0","China","China","理想汽车首款纯电 SUV 理想 i8 正式发布","product_launch","2025/07/29","official news listing","https://www.lixiang.com/news","hybrid","family EV / premium SUV","family car buyers","家庭场景叙事发布",5,"理想非常重家庭使用场景，对影石生活记录产品很有参考价值。","影石可围绕亲子、出行、露营等场景设计活动叙事。"),
    mk("Li Auto","P0","China","China","理想汽车新形态五座 SUV 理想 i6 正式发布","product_launch","2025/09/26","official news article","https://www.lixiang.com/news/145.html","hybrid","family EV / lifestyle SUV","young family users","场景叙事后承接试驾",5,"发布会直接承接试驾与限时权益。","影石可围绕生活场景先讲故事，再引导到试拍预约。"),
    mk("Li Auto","P0","China","China","理想 AI 眼镜 Livis 发布会","conference","2025/12/03","official news listing","https://www.lixiang.com/news.html","offline","AI wearables / ecosystem","tech enthusiasts; community users","跨品类生态发布",4,"跨品类发布有助于把汽车品牌扩展成生活方式品牌。","影石可考虑把相机周边、穿戴或软件服务纳入统一生态叙事。"),
    mk("Li Auto","P0","China","China","理想线下门店查询入口","store_experience","2026/06/09","official store page","https://www.lixiang.com/support/store/findus","offline","showroom / service","family buyers","门店查询与顾问入口",4,"门店查询页是标准的线上导流线下基础设施。","影石可加强门店和体验点的聚合入口。"),
    mk("Li Auto","P0","China","China","理想社区内容与车友活动入口","community_operation","2026/06/09","official community page","https://www.lixiang.com/community/list","online","community / owner operations","existing owners; potential buyers","社区内容与车友活动聚合",4,"社区页适合作为内容、活动和用户关系运营阵地。","影石可把用户作品和线下活动放进统一社区频道。",member_only="yes"),

    mk("XPeng","P0","China","China","小鹏汽车 AI Day 2025","conference","2025/11/05","official newsroom listing","https://www.xpeng.com/newsroom","offline","smart EV / AI ecosystem","technology-minded users","AI 技术大会",4,"技术大会加强科技品牌心智并向试驾转化。","影石可做影像 AI 能力开放日。"),
    mk("XPeng","P0","China","Global","XPENG 亮相 Goodwood Festival of Speed","city_activation","2025/07/10","official news article","https://www.xpeng.com/news/0197f776723197e8d9368a02811e0074","offline","smart EV / global brand","performance EV users","动态展示与强场景体验",4,"强场景活动更能让技术卖点被感知。","影石可在户外、运动或极限场景里做深度体验。",end_date="2025/07/13",city="Goodwood"),
    mk("XPeng","P0","China","Global","XPENG 亮相 IAA Mobility 2025","conference","2025/09/08","official news article","https://www.xpeng.com/pressroom/news/01992787505898ee96718a028110008c","offline","smart EV / AI ecosystem","global media; tech users","国际展会与 AI 生态展示",4,"国际展会适合做技术品牌和生态展示。","影石可在国际展会中用完整内容工作流展示产品能力。",city="Munich"),
    mk("XPeng","P0","China","China","小鹏活动中心","community_operation","2026/06/09","official events page","https://www.xpeng.com/events","online","brand events / community","technology-minded users","活动聚合与报名入口",4,"活动中心能让零散活动形成体系感。","影石可做活动中心页面，汇总试拍、课程和挑战赛。"),
    mk("XPeng","P0","China","China","小鹏服务与用户运营入口","member_service_activity","2026/06/09","official service page","https://www.xpeng.com/service","hybrid","after-sales / owner operations","existing users; owners","服务入口与复访",3,"售后支持对复购和口碑非常重要。","影石可做会员服务中心。",member_only="yes"),
    mk("XPeng","P0","China","China","小鹏门店与试驾中心入口","store_experience","2026/06/09","official store page","https://store.xpeng.com","offline","showroom / test drive","tech-savvy prospects","门店与试驾中心入口",5,"这是线索转化最清晰的场景之一。","影石可做试拍中心页和顾问分配。"),

    mk("AITO","P0","China","China","问界 M8 亮相粤港澳大湾区车展","city_activation","2025/06/01","public auto media coverage","https://auto.sina.com.cn/newcar/2025-06-01/detail-ineypvcm3774190.shtml","offline","premium family EV","family EV buyers","车展亮相与线下咨询收口",4,"车展活动非常适合收口线索和意向试驾。","影石可参考大型展会做内容互动和线索收集。",end_date="2025/06/08",city="Shenzhen",venue="粤港澳大湾区车展"),
    mk("AITO","P0","China","China","问界 M8 累计交付突破 17 万辆","community_milestone","2026/04/16","public finance media coverage","https://finance.sina.com.cn/stock/estate/integration/2026-04-16/doc-inhuskun1670373.shtml","online","premium family EV","existing owners; prospective buyers","里程碑增强社会证明",3,"交付里程碑对高单价产品的信任转化很关键。","影石可把用户参与里程碑转成传播事件。"),
    mk("AITO","P0","China","China","鸿蒙智行预约试驾入口","test_drive_booking","2026/06/09","official test-drive page","https://hima.auto/test-drive/","online","vehicle test drive conversion","family EV buyers","预约试驾与顾问收口",5,"试驾预约是最适合参考给影石的线索收口方式之一。","影石可做预约试拍、预约讲解、预约门店体验。"),
    mk("AITO","P0","China","China","鸿蒙智行门店查询入口","store_experience","2026/06/09","official store page","https://hima.auto/store-finder/","offline","showroom / store network","family EV buyers","门店查询与到店转化",4,"到店体验页是最基础但非常有效的转化工具。","影石可做城市体验地图。"),
    mk("AITO","P0","China","China","鸿蒙智行品牌社区与小程序入口","community_operation","2026/06/09","official homepage","https://hima.auto/","online","community / private traffic","existing users; prospects","首页前置小程序与社群入口",4,"私域入口越前置，转化效率通常越高。","影石可把企微、会员和小程序入口前置到首页。",member_only="yes"),

    mk("ZEEKR","P0","China","China","极氪 9X 正式上市","product_launch","2025/09/29","public auto media coverage","https://auto.sina.com.cn/newcar/x/2025-09-29/detail-infseqei1595177.shtml","hybrid","premium SUV / smart EV","premium EV buyers","高端技术旗舰发布",4,"高端定位和技术包装值得参考。","影石可对旗舰产品线建立更清晰的高端话语体系。"),
    mk("ZEEKR","P0","China","China","极氪 9X 在广州车展交付破万","city_activation","2025/11/21","public auto media coverage","https://auto.sina.com.cn/news/2025-11-21/detail-infyekye6960670.shtml","offline","premium SUV / delivery milestone","premium EV buyers","车展里程碑与交付证明",3,"车展+交付里程碑是典型的信任增强打法。","影石可把用户作品数、社群人数等节点做成展会传播点。",city="Guangzhou",venue="广州车展"),
    mk("ZEEKR","P0","China","China","极氪 007 GT 试驾预约","test_drive_booking","2025/06/10","public auto media coverage","https://www.pcauto.com.cn/aichat/133970.html","online","vehicle test drive conversion","performance EV buyers","试驾预约与官方小程序引导",4,"线上引流到店动作非常直接。","影石可做看内容-立即预约试拍结构。"),
    mk("ZEEKR","P0","China","China","极氪直营体验店体系扩张","store_experience","2025/06/22","public auto media coverage","https://baike.pcauto.com.cn/792058/1550401.html","offline","direct retail / service network","premium EV buyers","直营体验店与交付体系",3,"门店体系本身也是品牌信任感的一部分。","影石可把门店、交付、售后和活动空间做联动。"),
    mk("ZEEKR","P0","China","China","极氪上门试驾服务","test_drive_booking","2025/06/23","public auto media coverage","https://www.pcauto.com.cn/hq/140905.html","offline","home test drive / lead conversion","premium EV buyers","上门试驾与深度体验",4,"上门体验会显著提高高客单产品的成交效率。","影石可给重点客户做上门试拍服务。"),

    mk("Xiaomi EV","P0","China","China","小米 YU7 正式发布","product_launch","2025/06/26","official discover article","https://www.mi.com/global/discover/article?id=5173","hybrid","electric vehicle / launch conversion","technology users; Xiaomi fans","汽车新品发售与销售开启",5,"发售开启节奏适合参考到新品上线当天的转化设计。","影石可在发售日同步开放会员权益、预约试拍和礼包。",city="Beijing"),
    mk("Xiaomi EV","P0","China","Germany","Xiaomi EV opens Munich R&D center","brand_collab_offline_activation","2025/09/25","official discover article","https://www.mi.com/global/discover/article?id=5474","offline","EV / global expansion","global media; EV community","研发中心开业与技术背书",3,"这类活动偏品牌势能，但对国际化和技术信任有价值。","影石可把海外体验中心开业做成传播点。",city="Munich"),
    mk("Xiaomi EV","P0","China","China","小米汽车销售中心网络扩张","store_experience","2025/08/19","official discover article","https://www.mi.com/global/discover/article?id=4969","offline","EV retail network","EV buyers; Xiaomi fans","销售中心扩张与到店转化",4,"门店网络扩张说明流量最终还是要回到线下成交。","影石可优先建设高价值城市触点。"),
    mk("Xiaomi EV","P0","China","China","小米汽车累计交付突破 30 万辆","community_milestone","2025/11/18","official discover article","https://www.mi.com/global/discover/article?id=5369","online","EV social proof / brand trust","existing owners; prospective buyers","交付里程碑与信任转化",3,"交付和用户里程碑能显著提升品牌信任感。","影石可把重要用户量级做成传播节点。"),
    mk("Xiaomi EV","P0","China","China","小米汽车人车家生态联动发布","product_launch","2025/06/26","official global event page","https://www.mi.com/global/discover/","hybrid","EV / ecosystem","ecosystem shoppers; EV users","人车家生态联动",4,"生态用户池可以直接导入汽车新品。","影石可参考老用户池导入新产品线的发布链路。",city="Beijing"),

    mk("lululemon","P1","China","China","lululemon 2025 夏日乐挑战","community_operation","2025/06/30","media coverage referencing store challenge","https://www.vogue.com.cn/fashion/brand_news/news_19257a0029a3476b.html","offline","women's activewear / community","young women; urban white-collar users","线上报名 + 门店挑战赛",5,"这是非常标准的线上引流到店活动结构。","影石可做城市门店拍摄挑战赛。",end_date="2025/08/31",city="China",venue="161 家门店",signup="store challenge participation",ugc="check-in and social content"),
    mk("lululemon","P1","China","China","lululemon 一起好状态 2025","community_operation","2025/10/29","media coverage on city community activation","https://www.vogue.com.cn/fashion/brand_news/news_125158e7dd2109d1.html","offline","women's activewear / lifestyle","community fitness users","城市社群活动与门店复访",5,"这类活动不仅拉新，也适合老用户复访和复购。","影石可做城市主题体验周。",end_date="2025/11/30",city="China",venue="35 座城市门店与社区空间"),
    mk("lululemon","P1","China","China","lululemon Scuba 天猫超级品牌日","brand_collab_offline_activation","2025/09/16","marketing media report","https://www.brandstar.com.cn/news/7771","online","women's activewear / youth lifestyle","Gen Z users; fashion-lifestyle buyers","品牌日与商品复购转化",4,"品牌日很适合做销量拉升和会员运营。","影石可以围绕年度爆款做品牌日。",member_only="yes",member_benefit="brand-day offers",offer="shopping incentives"),
    mk("lululemon","P1","China","China","lululemon 热汗课程入口","community_operation","2026/06/09","official content page","https://www.lululemon.cn/article-l-43.html","offline","women's activewear / community","yoga users; urban women","门店社群课与复访",5,"课程型活动对复访和社区沉淀特别有效。","影石可做固定频次的创作工作坊。"),
    mk("lululemon","P1","China","China","lululemon 礼品卡","member_benefit","2026/06/09","official giftcard page","https://www.lululemon.cn/giftcard","online","gift card / repeat purchase","gifting buyers; repeat customers","礼品卡与送礼转化",3,"礼品卡属于基础复购工具，但很实用。","影石可做品牌礼卡、体验卡和课程卡。",member_only="yes"),

    mk("Salomon","P1","China","China","Salomon TsaiGu Trail 2025","community_run","2025/11/12","PR Newswire race release","https://www.prnewswire.com/news-releases/salomons-decade-long-investment-in-chinese-trail-running-culminates-in-dominant-tsaigu-trail-2025-victory-302612908.html","offline","trail running / outdoor community","trail runners; outdoor enthusiasts","垂类赛事与社群复购",5,"这是非常典型的垂类人群深耕型活动。","影石可在高重合运动圈层做年度赛事合作。",end_date="2025/11/16"),
    mk("Salomon","P1","China","China","Salomon 成都太古里旗舰店重开","store_experience","2025/12/09","Hypebeast retail coverage","https://hypebeast.cn/2025/12/salomon-chengdu-flagship-store-reopening","offline","outdoor lifestyle / footwear","young urban outdoor users","旗舰店重开与到店体验",4,"旗舰店重开很适合做内容传播和门店引流。","影石可对核心城市体验点做升级开业活动。",city="Chengdu",venue="太古里旗舰店"),
    mk("Salomon","P1","China","China","Salomon 安福路概念店","store_experience","2026/06/09","SGB retail coverage","https://sgbonline.com/salomon-shanghai-anfu-road/","offline","outdoor lifestyle / footwear retail","young urban outdoor users","概念店与城市社群",4,"概念店是年轻人和户外用户交汇的好场景。","影石可做主题店或联名店。",city="Shanghai",venue="安福路概念店"),
    mk("Salomon","P1","China","China","Salomon XT-Whisper × XSneaker 联名活动","brand_collab_offline_activation","2025/09/01","Hypebeast collaboration coverage","https://hypebeast.cn/2025/9/salomon-xsneaker-xt-whisper","offline","footwear collaboration / youth lifestyle","young sneaker users","联名限量发售与排队热度",4,"联名限量能快速制造社交热度与排队效应。","影石可做联名配件和限定体验空间。",end_date="2025/09/30"),
    mk("Salomon","P1","China","China","Salomon 101FF 独家发售活动","member_benefit","2025/10/15","Hypebeast release coverage","https://hypebeast.cn/2025/10/salomon-101ff-exclusive-release","online","footwear drop / repeat purchase","loyal Salomon followers","独家发售与老用户回流",4,"独家发售有利于制造稀缺和回访。","影石可为会员做限定发售。",end_date="2025/10/31",member_only="yes"),

    mk("HOKA","P1","China","China","HOKA MAFATE HOUSE 三里屯限时体验空间","brand_collab_offline_activation","2025/08/08","DoNews retail campaign coverage","https://www.donews.com/news/detail/8/5886769.html","offline","running footwear / fashion crossover","young runners; fashion-lifestyle users","快闪空间引流到店",5,"这种快闪空间非常适合引流、试用和社交传播。","影石可做运动记录主题快闪馆。",end_date="2025/08/17",city="Beijing",venue="三里屯"),
    mk("HOKA","P1","China","China","HOKA 飞跑嘉年华 2025","community_run","2025/09/14","Hypebeast event coverage","https://hypebeast.cn/2025/9/2025-hoka","offline","running footwear / community","runners; urban fitness users","跑者嘉年华与社群活动",4,"运动社群活动更能建立长期连接。","影石可加强与跑团、骑行俱乐部的固定合作。"),
    mk("HOKA","P1","China","China","HOKA 全球首家品牌体验中心","store_experience","2026/06/09","Hypebeast store coverage","https://hypebeast.cn/2025/5/hoka-one-one-shanghai-flagship-inside-look","offline","running footwear / premium retail","young runners; premium sports users","体验中心与试穿转化",5,"体验中心是线下转化效率最高的形态之一。","影石可设计一站式内容体验空间。",city="Shanghai"),
    mk("HOKA","P1","China","China","HOKA LAB 飞跑研究所","member_service_activity","2026/06/09","Hypebeast store coverage","https://hypebeast.cn/2025/5/hoka-one-one-shanghai-flagship-inside-look","offline","runner service / loyalty","runners; data-minded sports users","体测服务与会员粘性",4,"服务型空间更容易建立长期关系。","影石可把课程和售后服务嵌入门店。",member_only="yes"),
    mk("HOKA","P1","China","China","HOKA 中国限定与联名陈列","brand_collab_offline_activation","2026/06/09","Hypebeast store coverage","https://hypebeast.cn/2025/5/hoka-one-one-shanghai-flagship-inside-look","offline","retail drop / lifestyle","young runners; trend users","限定陈列与到店复购",4,"限定货盘能提高门店复访率。","影石可做城市限定壳、配件和作品卡。"),

    mk("On","P1","China","China","On 深圳首家旗舰店开业","store_experience","2026/03/05","PRNasia retail release","https://www.prnasia.com/story/524203-1.shtml","offline","running footwear / premium retail","urban runners; premium sports users","旗舰店开业与到店体验",4,"旗舰店是品牌形象和线下转化的双重抓手。","影石可在旗舰体验点加入内容创作空间。",city="Shenzhen",venue="深圳旗舰店"),
    mk("On","P1","China","China","On SquadRace 中国首发社区跑","community_run","2026/04/12","PRNasia community race release","https://www.prnasia.com/story/528722-1.shtml","offline","running footwear / community","running community; young professionals","团队赛制社群跑",4,"团队机制比单次报名更容易沉淀社群关系。","影石可尝试组队试拍赛。"),
    mk("On","P1","China","China","On 门店查询入口","store_experience","2026/06/09","official store locator","https://www.on.com/zh-cn/stores","offline","running footwear / retail","urban runners; premium sports users","门店查询与到店转化",4,"基础入口不花哨，但转化效率很高。","影石可强化城市体验地图。"),
    mk("On","P1","China","China","On 广州天环店开业跑","community_run","2025/11/21","PRNasia retail release","https://www.prnasia.com/story/513138-1.shtml","offline","running footwear / community","urban runners; premium sports users","门店开业跑与社群拉新",5,"这是非常典型的门店社群转化动作。","影石可把门店开业和社群活动做绑定。",city="Guangzhou",venue="天环店"),
    mk("On","P1","China","China","On 成都太古里中国首家旗舰店开幕","store_experience","2025/04/27","Hypebeast retail coverage","https://hypebeast.cn/2025/4/on-first-china-flaship-store-chengdu-opening","offline","running footwear / flagship retail","young premium runners","中国首家旗舰店开幕",4,"旗舰店是长期线下经营的重要抓手。","影石可做城市文化主题体验店。",city="Chengdu",venue="太古里旗舰店"),

    mk("Nike","P1","China","China","Nike Membership 官方会员计划","member_benefit","2025/06/09","official membership page","https://www.nike.com/membership","online","sportswear / membership","young sports users; sneaker users","会员专属权益与复购机制",5,"Nike Membership 的核心就是持续复购与专属感。","影石可把会员权益做得更具稀缺性。",member_only="yes"),
    mk("Nike","P1","China","China","Nike 会员店内专属服务","member_service_activity","2025/06/09","official in-store services page","https://www.nike.com/membership/in-store-services","offline","sportswear / store services","young sports users; sneaker members","店内专属服务与复访",4,"服务型权益可以显著提高老用户回访。","影石可做会员到店服务。",member_only="yes"),
    mk("Nike","P1","China","China","Nike 会员专属活动","member_service_activity","2025/06/09","official help article","https://www.nike.com/help/a/member-benefits","hybrid","sportswear / member retention","young sports users; runners","专属活动与长期留存",4,"这套权益结构对复购和留存非常实用。","影石可快速复制这类轻权益体系。",member_only="yes"),
    mk("Nike","P1","China","China","Nike Member Rewards & Offers","member_benefit","2026/06/09","official membership rewards page","https://www.nike.com/membership/member-rewards/","online","sportswear / member rewards","young sports users; sneaker members","奖励页与回访复购",4,"轻权益体系对日常复购很有帮助。","影石可从简单券包开始。",member_only="yes"),
    mk("Nike","P1","China","China","Nike By You 定制服务","member_service_activity","2026/06/09","official member benefits help page","https://www.nike.com/help/a/member-benefits","hybrid","customization / member retention","sneaker users; personalization-focused buyers","定制服务与会员专属",4,"定制服务兼顾复购和分享传播。","影石可把个性化服务做成会员权益。",member_only="yes"),

    mk("New Balance","P1","China","China","New Balance 204L 上海限时空间","brand_collab_offline_activation","2025/08/29","Hypebeast retail pop-up coverage","https://hypebeast.cn/2025/8/new-balance-204l-shanghai-pop-up","offline","lifestyle footwear / youth fashion","young fashion users; sneaker users","限时空间与年轻人打卡",4,"New Balance 的限时空间打法很适合品牌氛围营造。","影石可做年轻向城市快闪记录空间。",end_date="2025/09/07",city="Shanghai"),
    mk("New Balance","P1","China","China","New Balance Grey Days 2025","brand_collab_offline_activation","2025/05/02","Hypebeast campaign coverage","https://hypebeast.cn/2025/5/new-balance-grey-days-2025-release-info","hybrid","lifestyle footwear / youth campaign","young sneaker users; fashion-lifestyle users","年度主题活动与复购机制",4,"年度主题活动非常适合做内容和交易双收。","影石可做年度记录主题月。",end_date="2025/05/29"),
    mk("New Balance","P1","China","China","New Balance 1000 Grey Metallic 发售","brand_collab_offline_activation","2025/07/01","Hypebeast release coverage","https://hypebeast.cn/2025/7/new-balance-1000-grey-metallic-m1000f-release-info","online","lifestyle footwear / youth drop","young sneaker users; trend followers","新品发售与社交讨论",3,"这类发售更偏种草，但也能带动复购。","影石可做限定配件周。",end_date="2025/09/30"),
    mk("New Balance","P1","China","China","New Balance 中国官网入口","store_experience","2026/06/09","official homepage","https://www.newbalance.com.cn/","online","sportswear retail / homepage conversion","young sneaker users; lifestyle buyers","官网首页承接转化",3,"官网首页虽然基础，但对转化承接很关键。","影石可在首页前置活动和试拍入口。"),
    mk("New Balance","P1","China","China","New Balance 会员与复购活动入口","member_benefit","2026/06/09","official homepage","https://www.newbalance.com.cn/","online","sportswear membership","repeat buyers; lifestyle buyers","会员机制与品牌活动承接",3,"虽然入口不显性，但品牌首页是活动与复购的承接总入口。","影石可在会员入口聚合权益与活动。",member_only="yes"),

    mk("Arc'teryx","P1","China","China","始祖鸟北京 ARC’LOUNGE 出发地","store_experience","2025/08/18","business media coverage","https://www.eeo.com.cn/2025/0818/745382.shtml","offline","premium outdoor / retail experience","premium outdoor users","高端门店与身份认同",4,"这类门店不仅卖货，更在运营身份认同。","影石可把旗舰体验点做成内容与社群空间。",city="Beijing",venue="北京三里屯"),
    mk("Arc'teryx","P1","China","China","Arc'teryx 门店查询入口","store_experience","2026/06/09","official store locator","https://arcteryx.com/cn/zh/store-locator","offline","premium outdoor retail","premium outdoor users","门店查询与高客单转化",4,"这类入口是高客单产品线下转化的基础。","影石可在高端产品线里加强门店入口。"),
    mk("Arc'teryx","P1","China","China","Arc'teryx Explore 内容入口","community_operation","2026/06/09","official explore page","https://arcteryx.com/cn/zh/explore","online","outdoor content / community","outdoor enthusiasts; aspirational users","内容阵地与身份运营",3,"内容阵地更偏长期运营和品牌认同。","影石可打造品牌内容志。",member_only="yes"),
    mk("Arc'teryx","P1","China","China","始祖鸟蛇根洞世界级攀岩场地启用","city_activation","2026/06/09","SGB community climbing coverage","https://sgbonline.com/arcteryx-opens-chinas-first-world-class-climbing-site-at-shegeng-cave/","offline","outdoor climbing / community","climbers; outdoor enthusiasts","场地活动与专业社群",4,"这种场地级合作非常适合建立专业权威。","影石可做运动基地合作试拍。",city="China",venue="蛇根洞攀岩地"),
    mk("Arc'teryx","P1","China","China","始祖鸟山地课堂 × 小红书第二现场","community_operation","2026/06/09","award case coverage","https://winner.roifestival.com/cn/winners/detail/98aa5nij","online","community education / xiaohongshu","outdoor beginners; climbers","小红书放大线下专业课堂",5,"始祖鸟把小红书用成线下课堂的放大器，非常值得重点研究。","影石可把线下体验课和社媒内容阵地联动起来。"),
]


def main() -> None:
    base = Path("/Users/insta360/Documents/Codex/2026-06-09/new-chat")
    src = base / "brand-activity-material-library.csv"
    with src.open(newline="", encoding="utf-8") as handle:
        existing = list(csv.DictReader(handle))
    seen = {(row["brand"], row["activity_name"]) for row in existing}
    merged = existing[:]
    for row in RECOVERED_ROWS:
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
