# Plan: 品牌活动情报体系

**Generated**: 2026-06-09
**Estimated Complexity**: Medium

## Overview
目标不是“全网泛抓”，而是先建立一套能稳定发现、筛选、复盘品牌活动的情报体系，服务影石的活动策划参考。建议先做 2 周试点，验证品牌池、渠道池、字段口径和周报结构，再决定是否进入自动化抓取阶段。

## Prerequisites
- 明确本次参考的业务目标：新品发布、会员增长、门店到店、社群活跃，还是品牌破圈
- 一版初始品牌池与优先级
- 影石目标用户画像与重点产品线
- 需要覆盖的地域、语言和时间窗口
- 可接受的数据来源边界与合规要求

## Sprint 1: 定义范围与标准
**Goal**: 先统一“抓什么、为什么抓、怎么判断有价值”
**Demo/Validation**:
- 产出品牌池 V1、活动类型字典 V1、渠道地图 V1
- 团队能据此对同一活动做出一致判断

### Task 1.1: 定义品牌池
- **Location**: `brand-activity-intelligence-plan.md`
- **Description**: 按用户画像重合度拆成 4 类品牌池：
  1. 直接竞合：GoPro、DJI、Shokz、Garmin
  2. 户外运动：Arc'teryx、Salomon、Patagonia、DESCENTE
  3. 潮流生活方式：LEGO、Lululemon、On
  4. 科技影像周边：Sony、Canon、Bose
- **Dependencies**: None
- **Acceptance Criteria**:
  - 每个品牌有纳入理由
  - 每个品牌有优先级 `P0/P1/P2`
- **Validation**:
  - 业务方能在 15 分钟内完成增删改

### Task 1.2: 定义活动口径
- **Location**: `brand-activity-intelligence-plan.md`
- **Description**: 统一活动类型，至少包含：
  - 新品发布 / 预售 / 品鉴会
  - 会员活动 / 积分权益 / 会员日
  - 门店活动 / 快闪 / 城市巡展
  - 社群活动 / 训练营 / 跑团 / 影像挑战赛
  - 联名 / 展会 / 赛事赞助 / KOL 共创
- **Dependencies**: Task 1.1
- **Acceptance Criteria**:
  - 同类活动不会因命名差异被重复统计
  - 可以单独标记“是否值得影石复用”
- **Validation**:
  - 用 10 条历史样本试填，字段无明显歧义

### Task 1.3: 建立渠道地图
- **Location**: `brand-activity-intelligence-plan.md`
- **Description**: 为每个品牌列出主要公开信号源，优先级从高到低：
  - 官网 `News/Events/Brand` 页面
  - 门店活动页 / 会员页 / App / 小程序
  - 微信公众号 / 视频号
  - 抖音 / 小红书 / 微博
  - 天猫 / 京东旗舰店上新与会员活动页
  - 线下商场、展会、跑团或俱乐部报名页
- **Dependencies**: Task 1.1
- **Acceptance Criteria**:
  - 每个 P0 品牌至少有 5 个固定监控源
  - 标记每个源的抓取难度和更新频率
- **Validation**:
  - 随机抽查 3 个品牌，可在 5 分钟内找到最近活动记录

## Sprint 2: 两周试点采集
**Goal**: 用人工增强方式先跑通结果，不急着上全自动
**Demo/Validation**:
- 产出首版活动数据库和一份周报样稿
- 能回答“哪些玩法值得影石借鉴”

### Task 2.1: 采集样本
- **Location**: 建议输出到表格或 Airtable/Notion
- **Description**: 先抓 P0-P1 品牌最近 90-180 天活动，每个品牌至少采 10 条。
- **Dependencies**: Sprint 1
- **Acceptance Criteria**:
  - 总样本量达到 80-150 条
  - 每条样本包含来源链接和截图证据
- **Validation**:
  - 去重后有效样本占比大于 85%

### Task 2.2: 统一字段结构
- **Location**: 表格字段定义
- **Description**: 建议最少字段：
  - `brand`
  - `activity_name`
  - `activity_type`
  - `date`
  - `city_or_region`
  - `product_line`
  - `target_audience`
  - `entry_threshold`
  - `member_benefit`
  - `format_online_offline`
  - `channel_source`
  - `source_url`
  - `proof_screenshot`
  - `engagement_signal`
  - `reuse_score_for_insta360`
  - `notable_mechanic`
  - `visual_keyword`
- **Dependencies**: Task 2.1
- **Acceptance Criteria**:
  - 周报可直接从字段透视生成
  - 不需要二次人工解释就能看懂样本
- **Validation**:
  - 用 20 条样本复盘，缺失字段不超过 10%

### Task 2.3: 做第一版洞察周报
- **Location**: 周报模板
- **Description**: 周报只回答 4 个问题：
  - 哪些品牌最近活动最活跃
  - 哪些活动机制在重复出现
  - 哪些活动与影石用户画像最重合
  - 影石下周可直接借鉴的 3 个动作是什么
- **Dependencies**: Task 2.2
- **Acceptance Criteria**:
  - 周报控制在 1-2 页，管理层可快速读完
  - 每条建议都能回链到样本证据
- **Validation**:
  - 找一位非项目成员试读，10 分钟内能讲清结论

## Sprint 3: 自动化监控
**Goal**: 在试点验证后再自动化，避免先做复杂抓虫器
**Demo/Validation**:
- 跑通一版半自动监控清单
- 周更成本明显下降

### Task 3.1: 识别适合自动化的源
- **Location**: 渠道清单
- **Description**: 先自动化结构化程度高的源，例如官网新闻页、电商活动页、RSS/站点地图，再评估社媒。
- **Dependencies**: Sprint 2
- **Acceptance Criteria**:
  - 选出 10-20 个可稳定轮询的 URL
  - 标记反爬、登录、地区限制风险
- **Validation**:
  - 1 周内新增活动召回率可被人工复核

### Task 3.2: 建立采集与去重逻辑
- **Location**: 抓取脚本或自动化平台
- **Description**: 实现定时抓取、正文抽取、标题归一、URL 去重、时间解析和截图留档。
- **Dependencies**: Task 3.1
- **Acceptance Criteria**:
  - 同一活动跨平台不会重复入库
  - 失败源可追踪和重试
- **Validation**:
  - 连续跑 1 周，无大面积空采或重复爆炸

### Task 3.3: 建立评分与提醒
- **Location**: 周报或看板
- **Description**: 对活动做两类评分：
  - `relevance_score`: 与影石目标用户重合度
  - `replication_score`: 对影石活动可复用度
- **Dependencies**: Task 3.2
- **Acceptance Criteria**:
  - 新增活动能自动进入待研判列表
  - 高分活动可触发提醒
- **Validation**:
  - 团队每周能稳定收到有价值增量，而不是信息噪音

## Testing Strategy
- 先人工跑 2 周，验证字段和判断标准
- 每周抽样复核 20% 数据，检查误采、漏采、重复和误分类
- 用业务结论倒推字段是否足够支撑决策

## Potential Risks & Gotchas
- 过早追求“全网抓取”会导致源太散、噪音太大
- 会员活动大量存在于私域，公开网页未必完整
- 不同品牌活动命名风格差异大，去重和归类要先定义口径
- 中国市场很多信号在微信生态，小程序和公众号可能需要人工补充
- 如果不先定义“影石值得借鉴”的判断标准，最后只会堆活动清单

## Rollback Plan
- 如果自动化召回率低，回退到“P0 品牌人工 + P1 品牌半自动”的模式
- 如果品牌池过大，保留 8-12 个高价值品牌先做深
- 如果字段过多影响录入效率，压缩到“基础信息 + 借鉴点评”两层结构
