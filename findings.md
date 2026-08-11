# Findings & Decisions

## Requirements
- 用户需要围绕影石 `luna ultra`、`X 系列全景相机`、`GO 系列`，跟踪与会员拉新、企微/私域导流、购买转化相关的品牌活动。
- 重点看中国存量市场，同时保留海外灵感补充。
- 当前优先品牌为 `DJI、Apple、OPPO、vivo、Samsung、LEGO、DESCENTE、POP MART、CHAGEE、GoPro、Garmin、Shokz`。
- 时间窗口为 `2025-01-01` 至今。
- 结果需要沉淀到本地 CSV，可用于每日更新和每周周报。

## Research Findings
- 这类活动信息高度分散在官方 `Events/News/Community/Membership/Store` 页面，以及中国市场的微信/小程序/门店渠道。
- Apple、LEGO、DJI 这类品牌存在明确的活动或会员入口，适合做首批稳定监控源。
- 手机品牌与运动品牌常把活动挂在社区、会员或新闻页，而不是统一的活动页。
- OPPO 中国官网存在可直接回链的发布会活动页 `find-x8-series-launch`，也有 ODC25、MWC25 等活动型新闻稿。
- vivo 中国官网新闻列表存在“人文影像馆”“开发者大会”“品牌联合”等活动型条目，但部分需要通过精确标题二次定位正文页。
- Samsung 全球/美国 Newsroom 对新品发布和体验活动覆盖较完整，中国官网更适合补会员入口和新品回顾页。
- Garmin 中国官网存在明确的 `Garmin Run Club` 活动页，可作为跑团/训练营活动的长期监控源。
- Shokz 官方存在 `2025 Events` 活动页和赛事/展会复盘博客，适合作为运动社群活动样本来源。
- LEGO 2025 年有 `World Play Day` 和 `Insiders Days` 两类很典型的品牌活动机制，前者偏城市/家庭参与，后者偏会员转化。
- 首批 12 条样本已覆盖 6 类关键活动机制：新品发布、城市或门店体验、会员或 App 预售、社群跑团、抽奖留资、IP/文化联名。
- 与影石转化目标最贴近的样本不是单纯发布会，而是 `vivo` 的零售体验、`DESCENTE` 的 App 先行权益、`Garmin` 的高频社群活动、`Shokz` 的留资抽奖、`CHAGEE` 的任务式联名活动。
- `POP MART` 和 `CHAGEE` 的活动公开信息更常出现在官方文件或官方媒体中心外链中，适合单独做“低结构化品牌”采集策略。
- 用户最新需求把看板目标收敛成两个方向：一是 `2025-06 至 2026-06` 年度总览，二是中文单语、建议前置、覆盖状态清晰的品牌情报看板。
- 第二张图中的“空白白卡”是样式继承问题：英雄区容器使用了白色文字，但卡片本身也是白底，导致指标文字视觉上接近消失。
- 首批扩充样本优先补入了中国消费电子和重点车企的官方活动，主库样本已从 `12` 条增至 `20` 条。
- 最近几轮刷新优先补 `官方活动页 / 官方会员权益页 / 官方转化入口页`，先解决“点进去没内容”与“链接和活动不符”的可用性问题。

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| 先以“代表性活动样本”入库，而不是一次性覆盖全部活动 | 在当前回合内可交付真实成果，并为自动化收集建立字段标准 |
| 只录入能回链到公开来源的活动 | 保障数据可复核 |
| 日后把中国私域线索作为人工增强层补进 CSV | 私域很多活动不一定有稳定可抓公开页 |
| 对官方源可见但字段不完整的活动，先用 `seeded_with_inference` 方式入库 | 让后续自动任务知道哪些条目需要优先补强 |
| 页面文案收敛为中文单语，保留英文仅在品牌英文名或源数据本体中出现 | 用户明确表示不需要中英双语界面 |
| 品牌覆盖状态表采用 `已采集 / 采集中 / 待采集` 三档 | 明确区分已入库品牌、当前扩展抓取品牌和未来待补品牌 |
| 对会返回反爬校验页但仍是官方购买/选配入口的链接，保留为 `entry` 类型而不是误标成 `detail` | 明确区分“活动详情页”和“转化入口页”，避免页面可用性误导 |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| `planning-with-files` 技能文档中的路径与当前环境不一致 | 通过实际目录检查后改用 `~/.codex/skills/planning-with-files` |

## Resources
- `/Users/insta360/Documents/Codex/2026-06-09/new-chat/brand-source-map-v1.md`
- `/Users/insta360/Documents/Codex/2026-06-09/new-chat/brand-activity-material-library.csv`
- `https://www.dji.com/cn/events`
- `https://www.dji.com/cn/newsroom`
- `https://www.apple.com/cn/today/`
- `https://www.lego.com/zh-cn/stores/events`
- `https://www.lego.com/zh-cn/insiders`
- `https://www.oppo.com/cn/events/find-x8-series-launch/`
- `https://www.oppo.com/cn/newsroom/press/539/`
- `https://www.vivo.com.cn/brand/news/list`
- `https://www.samsung.com/cn/offer/samsung-members/`
- `https://www.garmin.com.cn/minisite/grc/`
- `https://shokz.com/pages/2025-events`
- `https://shokz.com/blogs/news/boston-marathon-2025-recap`
- `https://www.lego.com/en-us/aboutus/news/2025/may/world-play-day-2025`
- `https://www.lego.com/en-us/stores/events/insiders-days-us`
- `https://www.apple.com/newsroom/2025/03/apples-worldwide-developers-conference-returns-the-week-of-june-9/`
- `https://www.vivo.com.cn/news/detail/513`
- `https://news.samsung.com/us/invitation-galaxy-unpacked-january-2025-next-big-leap-mobile-ai-experiences/`
- `https://allterrain.descente.com/story/mizusawa-down-new-modelmerge-trident/`
- `https://prod-out-res.popmart.com/cms/ANNUAL_RESULTS_ANNOUNCEMENT_FOR_THE_YEAR_ENDED_31_DECEMBER_2025_AND_CHANGE_IN_USE_OF_PROCEEDS_d210fe53f0.pdf`
- `https://mp.weixin.qq.com/s/Q029puDXc4Pk4wQcLBI0hg`
- `https://gopro.com/en/us/news/gopro-announces-updated-max-360-camera-and-quik-reframe-editing`
- `https://ca.shokz.com/pages/2025-shokz-brand-day-rewards-terms-conditions`

## Visual/Browser Findings
- OPPO 搜索结果直接返回了 `2025 全新 OPPO Find X8 系列暨移动智能生态旗舰新品发布会` 的官方活动页，适合作为“新品发布/预约直播”样本。
- OPPO 新闻稿中可见 `2025OPPO 开发者大会（ODC25）` 与 `OPPO AI Tech Summit during MWC25`，说明 OPPO 的活动信号兼有中国本地与海外大会两条线。
- vivo 中国官网新闻列表中可见 `vivo人文影像馆武汉启幕，以影像科技重塑零售体验`、`2025 VDC开发者大会`、`上海迪士尼度假区与vivo宣布达成战略联盟` 等条目，说明其活动线索可覆盖零售体验、开发者活动和品牌联名。
- 搜索结果显示 DJI 2025 年可直接采用 `DJI Flip` 官方发布稿作为“新品发布 + vlog 人群导向”样本。
- Apple 官方 Newsroom 可直接定位 `WWDC 2025` 预告页，适合作为“线上大会 + 线下特别活动”样本。
- LEGO 官方结果显示 `World Play Day` 包含上海在内的城市线下活动，`Insiders Days` 则是典型会员促转化机制。
- Garmin `Garmin Run Club` 页面直接露出 `2025 元旦迎新跑` 等条目，说明其活动库更适合做“社群跑团/报名活动”类型采集。
- Shokz `2025 Events` 页直接列出 `CES 2025`、各类 Marathon、Run Club 和 Pop-up Store，覆盖展会、赛事和社区活动三种玩法。
- 从 Apple 归档页源码中能直接定位 `WWDC 2025` 的正式新闻稿 URL，说明 Apple Newsroom 的归档页适合后续自动化提取。
- CHAGEE 官网媒体中心页面会直接挂出外部微信文章链接和活动摘要，例如 `霸王茶姬×乌镇戏剧节`，可作为品牌活动采集入口。
- DESCENTE 的 ALLTERRAIN Story 页面能拿到精确发布日期，并明确区分普通发售与 App 先行发售，适合追踪会员权益机制。
- POP MART 的活动信息在官方年度业绩文件中明确提到了 `POP LAND` 主题活动、`Wacky Mart` 展览和多城活动，但活动日期粒度不如新闻稿细。
- `OPPO 2026影像大赛` 官方活动页 `https://lumo.oppo.com/cn/` 可稳定访问，页面明确写出 `4月21日开启全球征稿` 与 `百万奖金池`，适合作为长期创作者征集模板。
- `vivo 618限时返场` 官方活动页 `https://cmsapi.vivo.com.cn/activity/link/618PC` 可稳定访问，适合作为大促返场和商城转化收口样本。
- `vivo 生日福利怎么领取？` 官方会员帮助页 `https://www.vivo.com.cn/service/questions/all?categoryId=148&questionId=960` 可稳定访问，适合作为轻量会员复购机制样本。
- `蔚来 ES8` 选配与订购入口会返回带反爬校验的页面，但作为官方转化入口仍可保留为 `entry` 类型，不应误标成完整活动详情页。
- `Apple 夏令营` 官方页 `https://www.apple.com/cn/retail/camp/` 可稳定访问，当前是通知登记阶段，适合作为 `暑期课程通知收集 -> 开放报名 -> 到店体验` 的教育型转化样本。
- `vivo黄韬：X Fold系列要做AI体验最好的移动终端` 官方新闻页 `https://www.vivo.com.cn/brand/news/detail?id=1365&type=0` 明确记录了 `2026年6月10日` 在广州未来社举办的 `AI时代终端想象` 专场体验活动，适合作为消费电子线下体验样本。
- 截至 `2026-07-01` 再次复核 `Apple / DJI / Xiaomi / OPPO / vivo / LEGO / 年轻人消费品牌` 的公开活动页后，未发现比当前主库更高质量、且仍落在 `2026-06-30` 窗口内的新增官方样本，适合按 `0 新增` 方式做一致性刷新。
