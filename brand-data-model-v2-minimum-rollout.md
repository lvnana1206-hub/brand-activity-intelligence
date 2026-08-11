# 品牌活动情报系统
## 主库 V2 最小字段集落地方案

## 1. 目标

这份方案不直接修改现有主库表头，而是先定义一版最小可落地字段集，方便后续低风险升级。

目标是先补齐最影响判断的 6 个字段，让系统优先具备这 4 种能力：

1. 区分 `竞品 / 可合作品牌 / 年轻流量品牌`
2. 区分活动主要目标：`拉新 / 私域 / 到店 / 购买 / 复购`
3. 标记节日窗口：`618 / 父亲节 / 七夕 / 毕业季 / 暑期`
4. 把主观判断变成结构化字段，支持页面筛选和排序

---

## 2. 第一阶段只加的 6 个字段

## 字段 1：`brand_role`

### 作用
定义品牌在影石视角里的角色。

### 建议枚举值
- `direct_competitor`
- `adjacent_competitor`
- `cooperation_candidate`
- `youth_traffic_brand`
- `offline_scene_brand`
- `lifestyle_inspiration_brand`

### 示例
- `DJI` -> `direct_competitor`
- `GoPro` -> `direct_competitor`
- `Nike` -> `lifestyle_inspiration_brand`
- `霸王茶姬` -> `youth_traffic_brand`
- `蔚来` -> `offline_scene_brand`

---

## 字段 2：`campaign_goal_primary`

### 作用
定义活动最核心的业务目标。

### 建议枚举值
- `member_acquisition`
- `private_traffic_capture`
- `store_visit`
- `purchase_conversion`
- `repurchase`
- `content_growth`
- `community_retention`

### 示例
- `三星14天无忧试用服务` -> `purchase_conversion`
- `NIO App 活动报名与车友社群入口` -> `community_retention`
- `沪上阿姨10万份0.01元尝新券` -> `store_visit`

---

## 字段 3：`festival_tag`

### 作用
标记活动属于哪个节日或节奏窗口。

### 建议格式
多值字段，先用英文标签，值之间用 `|` 分隔。

### 建议值
- `womens_day`
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
- `national_day`
- `double_11`
- `christmas`

### 示例
- `三星以旧换新夏季档` -> `618|summer_holiday`
- `奈雪 × 麦兜联名：198家门店主题店` -> `childrens_day`

---

## 字段 4：`cooperation_potential`

### 作用
判断这个品牌未来是否适合和影石联合做活动。

### 建议枚举值
- `high`
- `medium`
- `low`

### 判断标准
- 用户画像重合度
- 节日联名适配度
- 线下场景适配度
- 内容共创适配度

### 示例
- `Nike` -> `high`
- `lululemon` -> `high`
- `霸王茶姬` -> `medium`
- `华为` -> `low`

---

## 字段 5：`private_traffic_type`

### 作用
明确这条活动的私域承接方式。

### 建议枚举值
- `wecom_group`
- `wecom_1v1`
- `official_account`
- `mini_program`
- `app_membership`
- `store_consultant`
- `sms_or_email`
- `none`

### 示例
- `NIO App 活动报名与车友社群入口` -> `app_membership`
- `茶百道猜拳赢好礼` -> `wecom_group`
- `预约试驾-NIO 蔚来官网` -> `store_consultant`

---

## 字段 6：`conversion_estimate_band`

### 作用
把当前页面里的预估转化率区间正式结构化。

### 建议枚举值
- `<1.5%`
- `1.5%-2.5%`
- `2.5%-4%`
- `4%-6%`
- `6%-8%`
- `8%-12%`

### 说明
这是 `派生字段`，不建议手填，建议由脚本根据现有公开信号自动生成。

---

## 3. 第一阶段字段填写规则

## 3.1 手填字段
建议手填：
- `brand_role`
- `campaign_goal_primary`
- `festival_tag`
- `cooperation_potential`
- `private_traffic_type`

## 3.2 自动派生字段
建议自动生成：
- `conversion_estimate_band`

---

## 4. 和现有字段的映射关系

## `brand_role`
来源：
- 当前 `brand`
- 当前人工品牌分组经验

## `campaign_goal_primary`
主要参考：
- `activity_type`
- `member_benefit`
- `wecom_or_private_traffic_hook`
- `signup_flow`
- `conversion_signal`

## `festival_tag`
主要参考：
- `start_date`
- `activity_name`
- `partnership_or_ip`

## `cooperation_potential`
主要参考：
- `brand`
- `target_audience`
- `partnership_or_ip`
- `online_offline`

## `private_traffic_type`
主要参考：
- `wecom_or_private_traffic_hook`
- `member_benefit`
- `channel_source`
- `signup_flow`

## `conversion_estimate_band`
主要参考：
- `conversion_index`
- `overall_index`

---

## 5. 示例：一条样本怎么升级

### 当前样本
`三星14天无忧试用服务`

### 新增字段建议
- `brand_role = adjacent_competitor`
- `campaign_goal_primary = purchase_conversion`
- `festival_tag = 618|summer_holiday`
- `cooperation_potential = low`
- `private_traffic_type = mini_program`
- `conversion_estimate_band = 8%-12%`

---

## 6. 四个页面怎么先吃这 6 个字段

## 6.1 品牌活动情报看板

优先使用：
- `brand_role`
- `campaign_goal_primary`
- `private_traffic_type`
- `conversion_estimate_band`

最适合新增的筛选：
- 只看直接竞品
- 只看可合作品牌
- 只看私域承接活动
- 只看高转化区间

---

## 6.2 年度优质品牌活动总览

优先使用：
- `festival_tag`
- `campaign_goal_primary`
- `brand_role`
- `conversion_estimate_band`

最适合新增的筛选：
- 只看节日活动
- 只看购买转化
- 只看可合作品牌

---

## 6.3 线下活动专项页

优先使用：
- `brand_role`
- `campaign_goal_primary`
- `private_traffic_type`
- `cooperation_potential`

最适合新增的筛选：
- 只看门店活动
- 只看社群活动
- 只看可合作品牌
- 只看高私域承接活动

---

## 6.4 品牌活动学习时间线

优先使用：
- `festival_tag`
- `brand_role`
- `cooperation_potential`

最适合新增的显示：
- 适合联动品牌
- 竞品扎堆月份
- 大疆重点月份

---

## 7. 最小落地步骤

### 第一步
先不改 CSV 表头，只写一份字段定义和判定规则。

### 第二步
挑 `20-30` 条高价值样本做试填，验证这 6 个字段是否够用。

### 第三步
如果试填稳定，再正式改主库表头或新增并行版本 CSV。

### 第四步
再把四个页面的筛选和排序接到这些字段上。

---

## 8. 我建议的执行顺序

如果你准备真正开始落地，我建议这样做：

1. 先选 `20` 条样本做试填
2. 再决定是否正式改主库
3. 优先改 `看板页` 和 `学习时间线页`
4. 最后再把所有字段推广到 `总览页` 和 `线下专项页`

---

## 9. 一句话结论

第一阶段不要一次把主库改得太重。  
先用 `brand_role / campaign_goal_primary / festival_tag / cooperation_potential / private_traffic_type / conversion_estimate_band` 这 6 个字段做最小闭环，就足够把四个页面从展示页推向真正的分析页。
