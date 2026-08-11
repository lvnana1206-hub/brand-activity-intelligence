import csv
import subprocess
import tempfile
import unittest
from pathlib import Path


class GenerateBrandDashboardTest(unittest.TestCase):
    def test_generates_html_dashboard_from_csv_and_daily_summary(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            csv_path = base / "library.csv"
            daily_path = base / "daily.md"
            output_path = base / "dashboard.html"
            overview_path = base / "overview.html"
            timeline_path = base / "timeline.html"

            header = [
                "brand",
                "priority_tier",
                "region",
                "country",
                "activity_name",
                "activity_type",
                "activity_status",
                "start_date",
                "end_date",
                "discovery_date",
                "channel_source",
                "source_url",
                "proof_screenshot",
                "city_or_region",
                "venue",
                "online_offline",
                "product_line",
                "member_only",
                "member_benefit",
                "wecom_or_private_traffic_hook",
                "entry_threshold",
                "signup_flow",
                "target_audience",
                "core_mechanic",
                "ugc_or_creator_mechanic",
                "offer_or_incentive",
                "partnership_or_ip",
                "visual_keyword",
                "engagement_signal",
                "conversion_signal",
                "reuse_score_for_insta360",
                "replication_difficulty",
                "insight_summary",
                "recommendation_for_insta360",
                "owner",
                "review_status",
                "last_updated",
            ]

            rows = [
                [
                    "DJI",
                    "P0",
                    "China",
                    "China",
                    "DJI Flip Launch",
                    "product_launch",
                    "completed",
                    "2025-01-14",
                    "2025-01-14",
                    "2026-06-09",
                    "official newsroom",
                    "https://example.com/dji",
                    "",
                    "Shenzhen",
                    "",
                    "online",
                    "consumer drone / vlog",
                    "no",
                    "",
                    "",
                    "public",
                    "newsroom to product page",
                    "vlog creators",
                    "easy aerial vlog capture",
                    "",
                    "",
                    "",
                    "foldable drone",
                    "launch content and product page handoff",
                    "clear path to product consideration",
                    "5",
                    "medium",
                    "High overlap with Insta360 vlog users.",
                    "Create simple trial-to-membership flow.",
                    "tester",
                    "seeded",
                    "2026-06-09",
                ],
                [
                    "Shokz",
                    "P1",
                    "North America",
                    "Canada",
                    "Shokz Lucky Draw",
                    "email_signup_promo",
                    "completed",
                    "2025-10-16",
                    "2025-10-22",
                    "2026-06-09",
                    "official campaign terms page",
                    "https://example.com/shokz",
                    "",
                    "",
                    "",
                    "online",
                    "open-ear headphones",
                    "no",
                    "chance to win OpenRun Pro 2",
                    "",
                    "email submission",
                    "landing page to email capture",
                    "runners",
                    "lead capture giveaway",
                    "",
                    "lucky draw",
                    "",
                    "brand day",
                    "email acquisition",
                    "lead capture for conversion",
                    "5",
                    "low",
                    "Good for private traffic acquisition.",
                    "Use giveaway to collect enterprise WeChat leads.",
                    "tester",
                    "seeded_with_inference",
                    "2026-06-09",
                ],
            ]

            with csv_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(header)
                writer.writerows(rows)

            daily_path.write_text(
                "# 每日品牌活动刷新\n\n"
                "最近一次刷新时间：2026-06-09 22:00 CST\n\n"
                "## 今天最值得抄作业的 5 个机制\n"
                "- NIO：把交付中心做成内容场\n"
                "- NIO: Turn delivery centers into content spaces\n"
                "- Garmin：固定节奏社群活动\n\n"
                "## 对影石的即时建议\n"
                "- NIO：试驾与社群入群联动\n"
                "- NIO: Link test drives with community onboarding\n"
                "- 做会员优先试拍\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    "python3",
                    "/Users/insta360/Documents/Codex/2026-06-09/new-chat/generate_brand_dashboard.py",
                    "--csv",
                    str(csv_path),
                    "--daily",
                    str(daily_path),
                    "--output",
                    str(output_path),
                    "--overview-output",
                    str(overview_path),
                    "--timeline-output",
                    str(timeline_path),
                    "--window-start",
                    "2025-06-01",
                    "--window-end",
                    "2026-06-30",
                ],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            html = output_path.read_text(encoding="utf-8")

            self.assertIn("品牌活动情报看板", html)
            self.assertIn("#ff78d1", html)
            self.assertIn("#9a6bff", html)
            self.assertIn("总样本数", html)
            self.assertIn("2", html)
            self.assertIn("样本视角", html)
            self.assertIn("只看线下 / 混合型活动", html)
            self.assertIn("链接类型", html)
            self.assertIn("只看活动详情页", html)
            self.assertIn("只看转化入口页", html)
            self.assertIn("只看参考页", html)
            self.assertIn("只看失效链接", html)
            self.assertIn("证据等级", html)
            self.assertIn("官方直证", html)
            self.assertIn("id='scope-filter'", html)
            self.assertIn("seeded_with_inference", html)
            self.assertIn("做会员优先试拍", html)
            self.assertIn("影石行动建议", html)
            self.assertIn("线下活动总览", html)
            self.assertIn("线下活动重点分支", html)
            self.assertIn("线下垂类活动优先池", html)
            self.assertIn("可落地线下活动模板", html)
            self.assertIn("本月重点品牌", html)
            self.assertIn("本月重点渠道", html)
            self.assertIn("本月重点活动类型", html)
            self.assertIn("最近几天活动速览", html)
            self.assertIn("本周最值得抄作业 TOP 8", html)
            self.assertIn("高转化活动预估转化率", html)
            self.assertIn("预估转化率区间", html)
            self.assertIn("DJI Flip Launch", html)
            self.assertIn("大疆", html)
            self.assertIn("中国区转化重点", html)
            self.assertIn("近一年优势活动", html)
            self.assertIn("小红书", html)
            self.assertIn("大众点评", html)
            self.assertIn("微博", html)
            self.assertIn("华为", html)
            self.assertIn("中国消费电子", html)
            self.assertIn("车企", html)
            self.assertIn("比亚迪", html)
            self.assertIn("理想汽车", html)
            self.assertIn("品牌建议分是什么", html)
            self.assertIn("品牌建议分", html)
            self.assertIn("5 分：可以直接复用", html)
            self.assertIn("不是品牌真实成交转化率", html)
            self.assertIn("品牌活动类型", html)
            self.assertIn("brand-card-cover", html)
            self.assertEqual(html.count("NIO：把交付中心做成内容场"), 1)
            self.assertEqual(html.count("NIO: Turn delivery centers into content spaces"), 0)
            self.assertEqual(html.count("NIO：试驾与社群入群联动"), 1)
            self.assertEqual(html.count("NIO: Link test drives with community onboarding"), 0)
            self.assertNotIn("影石必做清单", html)
            self.assertIn("品牌覆盖状态表", html)
            self.assertIn("已采集", html)
            self.assertIn("采集中", html)
            self.assertIn("待采集", html)
            self.assertIn("蔚来", html)
            self.assertIn("比亚迪", html)
            self.assertNotIn("板块切换", html)
            self.assertNotIn("data-section-target", html)
            self.assertLess(html.index("影石行动建议"), html.index("品牌覆盖状态表"))
            self.assertGreater(html.index("品牌覆盖状态表"), html.index("品牌分组卡片"))

            overview_html = overview_path.read_text(encoding="utf-8")
            self.assertIn("年度优质品牌活动总览", overview_html)
            self.assertIn("#ff78d1", overview_html)
            self.assertIn("2025-06-01 - 2026-06-30", overview_html)
            self.assertIn("品牌活动情报看板", overview_html)
            self.assertIn("brand-offline-activity-monitor.html", overview_html)
            self.assertIn("高转化品牌榜", overview_html)
            self.assertIn("基于样本转化信号推算", overview_html)
            self.assertIn("渠道热度分布", overview_html)
            self.assertTrue("官方活动页" in overview_html or "官方新闻稿" in overview_html or "官方门店页" in overview_html)
            self.assertIn("id='window-start'", overview_html)
            self.assertIn("id='window-end'", overview_html)
            self.assertIn("各品牌预估活动转化率排名", overview_html)
            self.assertIn("各品牌优质活动比较排名", overview_html)
            self.assertIn("高转化优质活动分类分布", overview_html)
            self.assertIn("高转化活动预估转化率", overview_html)
            self.assertIn("预估转化率区间", overview_html)
            self.assertIn("年度节奏学习时间线", overview_html)
            self.assertIn("brand-offline-activity-monitor.html", html)
            self.assertIn("特殊节日", overview_html)
            self.assertIn("月度主题", overview_html)
            self.assertIn("代表品牌", overview_html)
            self.assertIn("代表活动", overview_html)
            self.assertIn("建议关注", overview_html)
            self.assertIn("可能会推", overview_html)
            self.assertNotIn("围绕 女性节 和 女性节点", overview_html)

            timeline_html = timeline_path.read_text(encoding="utf-8")
            self.assertIn("品牌活动学习时间线", timeline_html)
            self.assertIn("#ff78d1", timeline_html)
            self.assertIn("#5dc7ff", timeline_html)
            self.assertIn("年度节奏学习时间线", timeline_html)
            self.assertIn("月份时间轴导航", timeline_html)
            self.assertNotIn("横向月份时间轴", timeline_html)
            self.assertIn("timeline-strip", timeline_html)
            self.assertIn("timeline-month-chip", timeline_html)
            self.assertIn("timeline-node-date", timeline_html)
            self.assertIn("时间节点", timeline_html)
            self.assertIn("重点节日 / 时间点", timeline_html)
            self.assertIn("品牌扎堆高峰", timeline_html)
            self.assertNotIn("overflow-x:auto", timeline_html)
            self.assertIn("特殊节日", timeline_html)
            self.assertIn("月度主题", timeline_html)
            self.assertIn("重点品牌", timeline_html)
            self.assertIn("代表活动", timeline_html)
            self.assertIn("建议关注", timeline_html)
            self.assertIn("timeline-strip", timeline_html)
            self.assertIn("timeline-month-chip", timeline_html)
            self.assertIn("brand-activity-overview.html", timeline_html)
            self.assertIn("brand-activity-dashboard.html", timeline_html)
            self.assertIn("brand-offline-activity-monitor.html", timeline_html)

    def test_generates_offline_monitor_page_without_touching_existing_pages(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            csv_path = base / "library.csv"
            daily_path = base / "daily.md"
            output_path = base / "offline-monitor.html"

            header = [
                "brand",
                "priority_tier",
                "region",
                "country",
                "activity_name",
                "activity_type",
                "activity_status",
                "start_date",
                "end_date",
                "discovery_date",
                "channel_source",
                "source_url",
                "proof_screenshot",
                "city_or_region",
                "venue",
                "online_offline",
                "product_line",
                "member_only",
                "member_benefit",
                "wecom_or_private_traffic_hook",
                "entry_threshold",
                "signup_flow",
                "target_audience",
                "core_mechanic",
                "ugc_or_creator_mechanic",
                "offer_or_incentive",
                "partnership_or_ip",
                "visual_keyword",
                "engagement_signal",
                "conversion_signal",
                "reuse_score_for_insta360",
                "replication_difficulty",
                "insight_summary",
                "recommendation_for_insta360",
                "owner",
                "review_status",
                "last_updated",
                "link_type",
                "link_note",
            ]

            rows = [
                [
                    "Huawei",
                    "P0",
                    "China",
                    "China",
                    "华为旗舰店影像体验日",
                    "store_experience",
                    "active",
                    "2026-06-09",
                    "2026-06-09",
                    "2026-06-12",
                    "official store page",
                    "https://example.com/huawei-store-day",
                    "",
                    "上海",
                    "华为智能生活馆",
                    "offline",
                    "X series",
                    "yes",
                    "到店礼和会员积分",
                    "到店后引导企业微信入群",
                    "会员报名",
                    "官网报名后到店核销",
                    "vlog 记录者",
                    "试拍体验 + 会员入群",
                    "",
                    "到店赠品",
                    "",
                    "影像试拍",
                    "门店报名与体验",
                    "到店后加入社群",
                    "5",
                    "medium",
                    "门店体验与会员承接一体化。",
                    "小标题：把试拍报名和企业微信入群放在同一条动线。",
                    "tester",
                    "seeded",
                    "2026-06-12",
                    "detail",
                    "活动详情页",
                ],
                [
                    "NIO",
                    "P0",
                    "China",
                    "China",
                    "蔚来城市试驾周",
                    "test_drive_booking",
                    "active",
                    "2026-06-08",
                    "2026-06-20",
                    "2026-06-12",
                    "official test-drive page",
                    "https://example.com/nio-drive",
                    "",
                    "杭州",
                    "蔚来中心",
                    "hybrid",
                    "X series",
                    "no",
                    "试驾积分",
                    "预约后导流社群",
                    "预约试驾",
                    "填写表单后到店",
                    "户外运动记录者",
                    "预约试驾 + 进群运营",
                    "",
                    "试驾礼",
                    "",
                    "城市试驾",
                    "表单提交",
                    "预约到店",
                    "5",
                    "low",
                    "试驾预约和私域承接衔接紧。",
                    "小标题：复制车企的预约入口设计，做预约试拍和到店讲解。",
                    "tester",
                    "seeded",
                    "2026-06-12",
                    "entry",
                    "转化入口页",
                ],
                [
                    "Nike",
                    "P1",
                    "China",
                    "China",
                    "Nike Membership 城市跑",
                    "community_run",
                    "active",
                    "2026-06-06",
                    "2026-06-06",
                    "2026-06-12",
                    "weibo official post",
                    "https://example.com/nike-run",
                    "",
                    "成都",
                    "Nike 门店",
                    "offline",
                    "GO series",
                    "yes",
                    "会员优先报名",
                    "报名后进门店社群",
                    "会员报名",
                    "小程序报名",
                    "生活记录者",
                    "门店跑团 + 会员专属名额",
                    "用户晒图",
                    "完赛礼",
                    "",
                    "城市打卡",
                    "微博官宣",
                    "门店社群沉淀",
                    "4",
                    "low",
                    "社群跑团和会员权益结合紧密。",
                    "小标题：用门店跑团做城市创作者社群活动。",
                    "tester",
                    "seeded",
                    "2026-06-12",
                    "detail",
                    "微博官宣详情页",
                ],
            ]

            with csv_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(header)
                writer.writerows(rows)

            daily_path.write_text(
                "# 每日品牌活动刷新\n\n"
                "最近一次刷新时间：2026-06-12 22:00 CST\n\n"
                "## 今天最值得抄作业的 5 个机制\n"
                "- `到店报名`：把官网预约、门店核销和企微入群串起来。\n"
                "- `会员跑团`：用会员专属名额带动复购和社群。\n\n"
                "## 对影石的即时建议\n"
                "- `预约试拍`：把预约试拍、门店讲解和企微沉淀放在一条链路。\n"
                "- `会员社群`：用会员专属活动拉动城市社群复购。\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    "python3",
                    "/Users/insta360/Documents/Codex/2026-06-09/new-chat/generate_brand_offline_monitor.py",
                    "--csv",
                    str(csv_path),
                    "--daily",
                    str(daily_path),
                    "--output",
                    str(output_path),
                    "--window-start",
                    "2025-06-01",
                    "--window-end",
                    "2026-06-30",
                ],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            offline_html = output_path.read_text(encoding="utf-8")

            self.assertIn("线下活动专项监控", offline_html)
            self.assertIn("#ff78d1", offline_html)
            self.assertIn("brand-activity-dashboard.html", offline_html)
            self.assertIn("brand-activity-overview.html", offline_html)
            self.assertIn("影石线下行动建议", offline_html)
            self.assertIn("本月重点品牌", offline_html)
            self.assertIn("本月重点渠道", offline_html)
            self.assertIn("本月重点活动类型", offline_html)
            self.assertIn("最近几天线下活动速览", offline_html)
            self.assertIn("到店转化活动池", offline_html)
            self.assertIn("会员复购活动池", offline_html)
            self.assertIn("社群 / 联名 / 打卡活动池", offline_html)
            self.assertIn("可直接学习的线下模板", offline_html)
            self.assertIn("线下活动样本库", offline_html)
            self.assertIn("证据等级", offline_html)
            self.assertIn("只看参考页", offline_html)
            self.assertIn("官方门店页", offline_html)
            self.assertIn("门店 / 到店入口", offline_html)
            self.assertIn("华为旗舰店影像体验日", offline_html)
            self.assertIn("Nike Membership 城市跑", offline_html)
            self.assertIn("只看活动详情页", offline_html)
            self.assertIn("活动详情页可直接点击", offline_html)
            self.assertNotIn("不替代现有两个页面", offline_html)


if __name__ == "__main__":
    unittest.main()
