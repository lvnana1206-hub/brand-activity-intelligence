# Task Plan: 品牌活动首批样本入库

## Goal
为影石品牌活动情报体系建立首批可用样本库，按 12 个优先品牌收集 `2025-01-01` 至今的代表性公开活动，并写入本地 CSV，便于后续日更、周报和建议清单生成。

## Current Phase
Phase 6

## Phases

### Phase 1: Requirements & Discovery
- [x] Understand user intent
- [x] Identify constraints and requirements
- [x] Document findings in findings.md
- **Status:** complete

### Phase 2: Planning & Structure
- [x] Define research and entry strategy
- [x] Confirm CSV write approach
- [x] Document decisions with rationale
- **Status:** complete

### Phase 3: Sample Collection & Entry
- [x] Collect official-source activities for 12 priority brands
- [x] Normalize sample fields
- [x] Write entries to `brand-activity-material-library.csv`
- **Status:** complete

### Phase 4: Verification
- [x] Verify CSV structure and row integrity
- [x] Check representative coverage by brand
- [x] Refresh summary files if needed
- **Status:** complete

### Phase 5: Delivery
- [x] Summarize what was entered
- [x] Note coverage gaps and next collection step
- [x] Deliver to user
- **Status:** complete

### Phase 6: Dashboard Revision & Coverage Expansion
- [x] Convert the pages to Chinese-only UI
- [x] Move Insta360 action sections ahead of the sample library
- [x] Add a brand coverage status table for China consumer electronics and key automotive brands
- [x] Seed the first batch of real official activity samples for expanded brands
- **Status:** complete

## Key Questions
1. Each brand should seed how many rows in the first batch while staying accurate and time-bounded?
2. Which official/public sources are stable enough to prioritize for repeatable monitoring?
3. How should incomplete fields be represented without introducing low-confidence guesses?

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| 先做 12 个优先品牌的代表性样本，而不是追求一次性铺满全年所有活动 | 先建立可用素材库和字段口径，后续日更再逐步扩量 |
| 优先使用官网、官方社区、官方会员/门店活动页 | 这些来源更稳定，适合后续持续监控 |
| CSV 中无法确认的字段留空，不做臆测 | 保证样本可信度，便于后续人工补录 |
| 对少数难以直达活动正文的品牌，允许使用官方年度文件或官方媒体中心落种子样本，并用 `seeded_with_inference` 标记 | 保证覆盖面，同时不把低置信信息伪装成高置信数据 |
| 页面界面改为中文单语，建议项全部采用“小标题：具体建议”格式 | 与用户最新使用习惯一致，可读性更高 |
| 扩展品牌优先批量补中国消费电子与重点车企 | 这些品牌与影石当前目标用户和市场竞争环境重合度最高 |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| 按技能文档中的 `~/.claude/plugins/...` 路径读取模板失败 | 1 | 改用实际存在的 `~/.codex/skills/planning-with-files/...` 路径 |

## Notes
- 每完成一轮检索就把关键发现写入 `findings.md`
- 写 CSV 前先统一字段口径，避免后续返工
- 当前已完成 12 条种子样本入库，剩余工作是刷新摘要并说明覆盖缺口
- 当前已完成 20 条样本入库，后续可按覆盖状态表继续推进第二批扩库
