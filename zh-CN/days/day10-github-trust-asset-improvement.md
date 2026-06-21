# Day 10 — 早期品牌搜索反馈和持续分发

日期: 2026-06-21

阶段: 第 2 周 — 分发和日常运营

状态: 进行中

## 目标

利用 Google 里已经出现的第一批品牌搜索反馈，调整接下来的分发动作。

昨天的工作已经开始在外部出现信号：

- SandBase docs 页面已经在 Google 结果中出现。
- Peerlist 出现了 `Posts by SandBase AI` 结果，并且摘要里出现了我们的定位：

```text
SandBase AI. Agent infrastructure for developers building production AI agents.
```

这是外部 profile 策略开始生效的早期信号。

## 计划工作

- 保存 Google 结果截图，作为早期证据。
- 记录 Peerlist 被 Google 抓取 / 展示的信号。
- 观察错误第三方实体结果，并通过更强的正确实体信号压过去。
- 继续围绕 agent infrastructure 做轻量社媒互动。
- 继续推进一个高质量目录 / profile。
- 继续跟进技术 SEO 修复：blog sitemap、未来日期文章、品牌实体一致性。

## 使用工具

| 工具 | 作用 |
|------|------|
| Codex | 记录证据、梳理策略、准备当天计划 |
| Google Search | 观察品牌搜索结果 |
| Peerlist | 外部 profile 和可被索引的社交页面 |
| GitHub / Website / Blog | 正确实体信号和技术信任资产 |

## 执行记录

- Google 搜索截图显示 SandBase 相关结果开始出现：
  - SandBase Docs 结果：`JavaScript / TypeScript SDK | SandBase Docs`
  - Peerlist 结果：`Posts by SandBase AI`
  - Peerlist 摘要：`SandBase AI. Agent infrastructure for developers building production AI agents. 2 followers.`
- 这说明 Day 9 的 Peerlist profile 不只是目录动作，它已经成为可被 Google 抓取的品牌相关公开页面。
- 截图里同时出现了一个错误 / 无关的 Tracxn 结果，把另一个 "SandBase" 实体描述成 deadpooled company。
- 决策：不因为错误结果焦虑，而是用更多正确实体信号逐步压过去：
  - 官网页面
  - Docs
  - Blog articles
  - GitHub organization
  - LinkedIn company page
  - Peerlist profile
  - DevHunt / Uneed / Product Hunt profile
  - Agent Ecosystem
  - Hackathon Support
- 用户反馈 P0 SEO 问题已修复：blog sitemap、未来日期文章、品牌实体一致性。
- 已在线上验证 P0 SEO 修复：
  - `sitemap-blog.xml` 现在包含 85 个 URL，包括英文和中文的具体文章 URL。
  - 之前未来日期的 `n8n vs Dify` 文章现在显示为 `June 20, 2026`。
  - blog 列表没有发现 2026 年 6 月 21 日之后的未来日期。
  - 首页 title 已改为 `SandBase - Agent Infrastructure for Production AI Agents`。
  - 首页 description 已聚焦 production agents、sandboxed runtime、tool access、model routing、cloud sandboxes 和 unified APIs。
  - Organization JSON-LD 已使用正确实体链接：X、GitHub `sandbaseai`、LinkedIn 公司页、Peerlist、Discord。
  - `sitemap-pages.xml` 已包含 Agent Ecosystem 和各个项目详情页。
  - `Hackathon Support` 暂时还没有出现在生产环境 pages sitemap 里，等对应分支部署后需要再次检查。
- Google Search Console sitemap 跟进：
  - 已存在的不带 www sitemap index `https://sandbase.ai/sitemap-index.xml` 仍然有效，状态为 `成功`，上次读取时间是 2026 年 6 月 20 日，发现 954 个页面。
  - 2026 年 6 月 21 日提交 canonical www 版本 `https://www.sandbase.ai/sitemap-index.xml`。
  - GSC 弹窗确认已成功提交，但列表中新 www 记录初始状态显示 `无法抓取` / 未知，发现页面数为 0。
  - 决策：暂时保留两个 sitemap 记录，把 www 记录视为刚提交后的待处理状态，明天复查后再决定是否需要进一步处理。

## 创建或更新的链接

- 证据截图：[Google brand result with Peerlist](../../assets/google-brand-result-peerlist-2026-06-21.png)
- Peerlist profile/posts surface: https://peerlist.io/sandbase

## 问题 / 阻塞

- 错误的 Tracxn 实体结果可能还会存在一段时间，直到 Google 对新的 SandBase.ai 实体有更强信心。
- 明天需要在 Google Search Console 里复查新提交的 `https://www.sandbase.ai/sitemap-index.xml`。
- `Hackathon Support` 部署后需要再次检查，确认它出现在 `sitemap-pages.xml` 中。
- 需要继续做正确的第三方 profile 信号，不能只依赖官网内容。

## 经验

早期品牌搜索结果不只是排名问题，本质是实体识别问题。

今天最重要的信号是：

```text
Google 正在开始把 SandBase AI 和 "agent infrastructure for developers building production AI agents" 联系起来。
```

下一步要做的是让这个关联更强、更干净。

不要追求每个目录都提交。要做少量高信任页面，并且反复表达同一个定位。

## 下一步

今天：

- 明天复查 Google Search Console 里新提交的 www sitemap index。
- 在 X / Peerlist 做 2-3 次围绕 production agents 的轻互动。
- 推进一个新的可信外部 profile：DevHunt 或 Uneed。
- 准备一条围绕 Agent Ecosystem 或 Hackathon Support 的产品视角内容。
