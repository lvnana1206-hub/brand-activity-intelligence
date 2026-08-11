# 品牌活动情报系统
## 主库下一版字段结构 + 四个页面字段映射

## 1. 这份方案解决什么问题

当前系统已经能稳定运行，但后续如果要继续升级，最大的瓶颈已经不是页面，而是数据模型。

现在主库已经能回答：
- 最近有哪些品牌在动
- 有哪些活动值得看
- 哪些活动更偏会员、门店、社群、联名、预约

但还不够支撑更深一层的问题：
- 哪些品牌是直接竞品，哪些是可合作品牌
- 哪些活动是为了拉新，哪些是为了复购
- 哪些节日窗口更适合做联合品牌活动
- 哪些样本更适合给领导看，哪些更适合给执行团队拆动作

所以这份文档的目标，是先把主库下一版字段结构和四个页面吃数逻辑定下来，再决定后续要不要真的改 CSV 表头或加自动分析层。

---

## 2. 设计原则

### 原则 1：不为了字段而加字段
新增字段必须直接服务以下至少一种能力：
- 更好筛选
- 更好比较
- 更好排序
- 更好生成建议
- 更好做节日/月份规划

### 原则 2：优先支持业务判断
字段设计优先服务：
- 会员拉新
- 私域承接
- 到店体验
- 购买转化
- 复购

### 原则 3：尽量把“主观判断”结构化
像“这个品牌是否值得合作”“这个活动是否适合联名”“这个活动更像拉新还是复购”，都应该尽量落成字段，而不是只写在备注里。

### 原则 4：允许字段分层
字段可以分成三层：
- 原始采集字段
- 人工判断字段
- 派生计算字段

---

## 3. 当前主库字段分层

当前主库核心字段可以粗分为 4 类：

### A. 基础识别字段
- `brand`
- `priority_tier`
- `region`
- `country`
- `activity_name`
- `activity_type`
- `activity_status`
- `start_date`
- `end_date`
- `discovery_date`

### B. 来源与证据字段
- `channel_source`
- `source_url`
- `proof_screenshot`
- `review_status`
- `last_updated`
- `link_type`
- `link_note`

### C. 活动机制字段
- `online_offline`
- `city_or_region`
- `venue`
- `product_line`
- `member_only`
- `member_benefit`
- `wecom_or_private_traffic_hook`
- `entry_threshold`
- `signup_flow`
- `target_audience`
- `core_mechanic`
- `ugc_or_creator_mechanic`
- `offer_or_incentive`
- `partnership_or_ip`
- `visual_keyword`
- `engagement_signal`
- `conversion_signal`

### D. 影石判断字段
- `reuse_score_for_insta360`
- `replication_difficulty`
- `insight_summary`
- `recommendation_for_insta360`
- `owner`

这些字段已经足够支撑当前四个页面，但如果要升级分类、领导视角和节日规划，建议新增下一层字段。

---

## 4. 建议新增字段（V2）

## 4.1 品牌角色字段

### `brand_role`
作用：区分这个品牌在影石视角里属于什么类型。

建议枚举值：
- `direct_competitor`
- `adjacent_competitor`
- `cooperation_candidate`
- `youth_traffic_brand`
- `offline_scene_brand`
- `lifestyle_inspiration_brand`

例子：
- `DJI` -> `direct_competitor`
- `GoPro` -> `direct_competitor`
- `Nike` -> `lifestyle_inspiration_brand`
- `霸王茶姬` -> `youth_traffic_brand`
- `问界` -> `offline_scene_brand`

### `cooperation_potential`
作用：判断是否适合未来异业合作或联合品牌。

建议枚举值：
- `high`
- `medium`
- `low`

判定逻辑示例：
- 受众高度重叠
- 城市线下活动能力强
- 节日联名适配度高
- 产品/场景有天然结合点

---

## 4.2 活动目标字段

### `campaign_goal_primary`
作用：定义这条活动最主要的业务目标。

建议枚举值：
- `member_acquisition`
- `private_traffic_capture`
- `store_visit`
- `purchase_conversion`
- `repurchase`
- `content_growth`
- `community_retention`

### `campaign_goal_secondary`
作用：定义这条活动的次级目标。

例子：
- 车企试驾页
  - `campaign_goal_primary = purchase_conversion`
  - `campaign_goal_secondary = store_visit`
- 奶茶小程序抽券
  - `campaign_goal_primary = store_visit`
  - `campaign_goal_secondary = repurchase`

### `conversion_stage`
作用：这条活动更偏哪个转化阶段。

建议枚举值：
- `seed`
- `engage`
- `visit`
- `join`
- `purchase`
- `repurchase`

含义：
- `seed`：种草
- `engage`：参与互动
- `visit`：到店
- `join`：入会/入群
- `purchase`：购买
- `repurchase`：复购

---

## 4.3 节日和时间字段

### `festival_tag`
作用：标记这条活动是否属于特定节日窗口。

建议格式：
多值字段，允许多个标签。

建议值：
- `new_year`
- `spring_festival`
- `valentines_day`
- `womens_day`
- `qingming`
- `labor_day`
- `mothers_day`
- `520`
- `childrens_day`
- `dragon_boat_festival`
- `fathers_day`
- `618`
- `graduation_season`
- `summer_holiday`
- `qixi`
- `back_to_school`
- `national_day`
- `double_11`
- `christmas`
- `new_year_eve`

### `seasonal_window`
作用：不只按节日，也按阶段性窗口标记。

建议值：
- `spring_launch`
- `summer_peak`
- `autumn_launch`
- `year_end_promo`
- `city_tour`
- `new_store_opening`

### `timeline_priority`
作用：在时间线页决定这条活动是否适合作为月份代表样本。

建议值：
- `high`
- `medium`
- `low`

---

## 4.4 联合品牌 / 异业合作字段

### `co_brand`
作用：记录这条活动是否有明确联合品牌对象。

示例：
- `麦兜`
- `乌镇戏剧节`
- `和平精英`
- `XSneaker`

### `cooperation_type`
作用：记录合作类型。

建议枚举值：
- `ip_collab`
- `festival_collab`
- `channel_collab`
- `venue_collab`
- `community_collab`
- `creator_collab`
- `media_collab`

### `joint_activation_strength`
作用：判断这条活动的联动强度。

建议值：
- `high`
- `medium`
- `low`

---

## 4.5 私域和会员承接字段

### `private_traffic_type`
作用：明确私域承接方式，不只写自由文本。

建议枚举值：
- `wecom_group`
- `wecom_1v1`
- `official_account`
- `mini_program`
- `app_membership`
- `sms_or_email`
- `store_consultant`
- `unknown`

### `membership_depth`
作用：判断会员体系参与深度。

建议值：
- `none`
- `light`
- `medium`
- `deep`

解释：
- `light`：只是会员可参加
- `medium`：会员专属权益明显
- `deep`：活动本身就是会员增长/升级/复购的一部分

---

## 4.6 领导视角字段

### `leadership_signal`
作用：标记这条活动是否适合给管理层展示。

建议值：
- `high`
- `medium`
- `low`

高的典型情况：
- 城市级大动作
- 联合品牌
- 明确门店转化
- 会员/私域闭环明显
- 季节性或节日性参考价值强

### `leadership_reason`
作用：一句话说明为什么这条值得管理层看。

示例：
- `能直接借鉴到影石门店试拍和社群承接`
- `适合做父亲节联合品牌活动`
- `适合做暑期创作者征集和城市巡回`

---

## 4.7 可计算派生字段

这些字段不一定需要直接录入，可以由脚本生成。

### `conversion_estimate_band`
建议值：
- `<1.5%`
- `1.5%-2.5%`
- `2.5%-4%`
- `4%-6%`
- `6%-8%`
- `8%-12%`

### `collab_score`
用于未来异业合作排序。

### `offline_value_score`
用于线下活动专项页排序。

### `festival_fit_score`
用于时间线页和节日活动推荐。

---

## 5. 推荐的 V2 主库字段清单

建议分成 3 层：

### 原始字段
- 保留当前 CSV 主字段不动

### 新增人工判断字段
- `brand_role`
- `cooperation_potential`
- `campaign_goal_primary`
- `campaign_goal_secondary`
- `conversion_stage`
- `festival_tag`
- `seasonal_window`
- `timeline_priority`
- `co_brand`
- `cooperation_type`
- `joint_activation_strength`
- `private_traffic_type`
- `membership_depth`
- `leadership_signal`
- `leadership_reason`

### 新增派生字段
- `conversion_estimate_band`
- `collab_score`
- `offline_value_score`
- `festival_fit_score`

---

## 6. 四个页面字段映射

## 6.1 品牌活动情报看板

### 页面目标
看最近有哪些动作最值得立刻参考。

### 核心字段
- `brand`
- `brand_role`
- `campaign_goal_primary`
- `conversion_stage`
- `activity_type`
- `discovery_date`
- `channel_source`
- `link_type`
- `evidence_level`
- `reuse_score_for_insta360`
- `conversion_estimate_band`
- `recommendation_for_insta360`

### 最适合新增的展示
- `品牌角色`
- `主要目标`
- `预估转化率区间`
- `证据等级`

### 适合的排序逻辑
- 最近发现
- 非发布会优先
- 高转化优先
- 高证据等级优先

---

## 6.2 年度优质品牌活动总览

### 页面目标
看全年活动结构、时间窗口和高质量案例分布。

### 核心字段
- `start_date`
- `festival_tag`
- `seasonal_window`
- `campaign_goal_primary`
- `activity_bucket`
- `co_brand`
- `brand_role`
- `conversion_estimate_band`
- `evidence_level`

### 最适合新增的展示
- `节日标签占比`
- `合作品牌出现频率`
- `高转化活动预估转化率`
- `品牌角色分布`

### 适合的筛选
- 只看直接竞品
- 只看可合作品牌
- 只看节日活动
- 只看高证据等级

---

## 6.3 线下活动专项页

### 页面目标
看哪些活动最适合直接转成影石线下活动 SOP。

### 核心字段
- `online_offline`
- `city_or_region`
- `venue`
- `store_visit`
- `private_traffic_type`
- `membership_depth`
- `co_brand`
- `cooperation_type`
- `offline_value_score`
- `evidence_level`

### 最适合新增的展示
- `私域承接方式`
- `会员参与深度`
- `是否适合联合品牌`
- `线下价值分`

### 适合的筛选
- 只看门店体验
- 只看联名快闪
- 只看社群活动
- 只看联合品牌

---

## 6.4 品牌活动学习时间线

### 页面目标
看月份节奏、节日窗口、品牌扎堆时间点和联动机会。

### 核心字段
- `start_date`
- `festival_tag`
- `seasonal_window`
- `brand_role`
- `cooperation_potential`
- `co_brand`
- `campaign_goal_primary`
- `timeline_priority`
- `festival_fit_score`

### 最适合新增的展示
- `适合联动品牌`
- `大疆 / 华为 / 车企 / 奶茶品牌` 的扎堆月份
- `重点节日`
- `品牌扎堆高峰`

### 适合的筛选
- 只看节日月份
- 只看大疆相关
- 只看可合作品牌
- 只看高节日适配度

---

## 7. 领导视角最爱看的数据

如果你后面要给领导看，最适合优先产出的不是页面，而是这些结构化结果：

### 1. 月度品牌活跃度
- 哪个月哪些品牌动作最多

### 2. 高转化机制分布
- 哪类活动最强：会员、联名、门店、小程序、社群、试用

### 3. 可合作品牌机会榜
- 哪些品牌更适合和影石联合做活动

### 4. 节日机会表
- 哪些节日最适合做哪种活动

### 5. 大疆时间点跟踪
- 大疆在哪些月份动作最密集
- 对应是什么类型活动

---

## 8. 推荐落地顺序

我建议按这个顺序走：

### 第一阶段：先不改 CSV 表头
先在脚本里做派生判断和页面排序逻辑验证。

### 第二阶段：新增人工判断字段
优先新增：
- `brand_role`
- `campaign_goal_primary`
- `festival_tag`
- `cooperation_potential`
- `private_traffic_type`

### 第三阶段：再做页面筛选升级
等字段稳定后，再把：
- 竞品
- 可合作品牌
- 节日活动
- 高证据等级

这些筛选加进四个页面。

---

## 9. 我最建议你先做的最小集

如果只能先加最少字段，我建议先加这 6 个：

- `brand_role`
- `campaign_goal_primary`
- `festival_tag`
- `cooperation_potential`
- `private_traffic_type`
- `conversion_estimate_band`

因为这 6 个字段已经足够把：
- 竞品 / 可合作品牌
- 拉新 / 复购 / 到店
- 节日 / 月份
- 私域承接
- 预估转化

这几条最关键的分析链先建立起来。

---

## 10. 一句话结论

下一版最该升级的，不是页面，而是主库的数据模型。  
只要把 `品牌角色 / 活动目标 / 节日标签 / 合作潜力 / 私域承接 / 预估转化` 这几层补齐，四个页面自然会从“展示页”升级成“真正的决策页”。
