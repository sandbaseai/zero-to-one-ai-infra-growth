# Day 15 — 开源机会挖掘

日期: 2026-06-22

阶段: 第 3 周 — 生态建设和可重复分发

状态: 进行中

## 目标

把每天的开源发现变成一个固定动作：找 3 个候选项目，打分，选 1 个，记录原因。

## 计划工作

- 快速检查搜索 / 网站健康。
- 找 3 个围绕 agent infrastructure 的新开源机会。
- 从 buildability 和 SandBase fit 两个角度打分。
- 选出 1 个后续开工。
- 围绕一个可信项目做 1 次真实社区互动。

## 使用工具

| 工具 | 作用 |
|------|------|
| GitHub | 候选项目来源 |
| Codex | 打分、记录和决策日志 |
| Peerlist / X / Discord | 社区上下文和反应信号 |
| Registry playbook | 过滤质量和未来信号 |

## 执行记录

- 明确了每日渠道巡检范围：
  - X
  - LinkedIn
  - Discord
  - Peerlist
  - DevHunt
  - 已注册过的外链 / profile 页面
  - 新外链和开源机会
- X 日常运营：
  - 回复了一条关于 Vercel `eve` 和 “agent as a directory of files” 模型的讨论。
  - 补充了 production runtime 视角：除了文件约定，agents 还需要可检查的 runtime assets，比如 permissions、environment config、tool traces、approvals、logs 和 replay data。
  - 回复了一条真实基础设施问题：一个 15 人团队如何为 coding 和 agentic applications 搭建 compute cluster。
  - 建议把 compute 拆成两个 pool：
    - GPU-heavy inference
    - CPU / isolation-heavy sandbox execution
  - 用 SandBase 账号发布了一条观点动态：

```text
Production agents do not only need model inference.

They need two kinds of compute:

- GPU compute for reasoning
- isolated CPU/runtime compute for tools, browser sessions, shell commands, and files

The agent runtime is where those two worlds meet.
```
- X 通知检查：
  - 暂时没有需要回复的评论或 mention。
  - 昨天关于 agent runtime 的回复收到点赞，这是一个早期信号：有技术观点的回复可以带来轻量曝光，不需要硬推广。
- LinkedIn 公司主页检查：
  - 公司页状态正常，外部可见。
  - 当前看到 3 个关注者、8 次搜索展示、1 个新增关注者。
  - 没有需要回复的评论。
  - 后续可以补充两个资料项：公司地址、公司域名邮箱验证。
- Discord 检查：
  - 检查了 `#agent-runtime` 和 `#builder-chat`。
  - 没有新的成员问题或回复需要处理。
  - 清理了输入框里旧的草稿，避免误发。
  - 今日决策：没有真实产品更新或社区问题时，不强行发 Discord 动态。
- Peerlist 检查：
  - 在通知里发现 Lil.Jr2.0 关于 permission boundaries、memory lifecycle、scoped agent capabilities 的真实回复。
  - 回复了一条产品相关的观点：

```text
That would be a strong demo. Showing when memory is created, scoped, updated, or denied would make the permission model much easier to evaluate.
```

  - 这是早期分发更合适的方式：贡献一个有用视角，而不是直接贴链接。
- DevHunt 检查：
  - 提交工具页面可以访问。
  - 当前 launch 周期仍然是 $49。
  - 因为今天目录预算不超过 $30，DevHunt 暂时只观察，不提交。
- 外链推进：
  - 复查了 Uneed 草稿。
  - 当前草稿内容仍然完整：
    - name: `SandBase`
    - URL: `https://www.sandbase.ai`
    - category: `Development`
    - pricing: `Freemium`
    - tags: `API & Data`, `AI`, `Development`
    - tagline: `Agent infrastructure for developers building production AI agents.`
  - Uneed 现在显示 `Schedule your launch`，这属于公开排期动作，需要确认后再点。
  - 确认后，已把 SandBase 加入 Uneed 免费等待队列。
  - Uneed 公开页已上线：
    - URL：`https://www.uneed.best/tool/sandbase`
    - launch 日期：2026-11-09
    - 费用：免费
    - 已跳过付费 upsell：`Auto-Submit to 100+ directories ($249)`
  - 复查了 Peerlist Launchpad。本周页面可以访问，但 `Launch` 按钮在当前浏览器里仍然没有打开可用提交表单。
  - AlternativeTo 和 SaaSHub 的提交页都进入 bot-protection / `Just a moment` 状态，因此不计为完成动作。
  - Product Hunt 提交页也出现 bot-protection / `Just a moment` 状态，因此今天不计入完成。
  - 创建了一个公开 GitHub 组织 profile 资产：
    - 仓库：`https://github.com/sandbaseai/.github`
    - profile README：`https://github.com/sandbaseai/.github/tree/main/profile`
    - 组织主页：`https://github.com/sandbaseai`
  - GitHub 组织 README 现在已经链接官网、Docs、Blog、X、LinkedIn、Discord、Uneed launch page 和几个开源资源仓库。
  - 这个动作比再投一个泛目录更像开发者信任资产。
- 追加外链候选扫描：
  - BetaList：
    - 检查 URL：`https://betalist.com/submit`
    - 结果：跳转到登录页
    - 状态：登录后可作为候选
    - 适配度：startup discovery 还可以，但不如 Peerlist 那么开发者垂直
  - Indie Hackers：
    - 检查 URL：`https://www.indiehackers.com/products/new`
    - 结果：跳转到登录页
    - 状态：登录后可作为候选
    - 适配度：适合做产品 / founder story 页，但文案要保持产品视角，不能像 SEO 投放
  - Fazier：
    - 检查 URL：`https://fazier.com/launch`
    - 结果：可访问
    - 状态：后续登录后可以尝试提交
    - 适配度：产品发现平台，有 AI-agent 相关产品，但整体质量混杂
  - Product Hunt：
    - 检查 URL：`https://www.producthunt.com/posts/new`
    - 结果：bot-protection 页面
    - 状态：等待，不硬做
  - TAIFT：
    - 检查 URL：`https://theresanaiforthat.com/submit/`
    - 结果：bot-protection 页面
    - 状态：等待；这是泛 AI 目录，需要谨慎使用
  - AlternativeTo、SaaSHub、OpenHub、Launching Next、Startup Buffer：
    - 结果：被 bot-protection 拦住或当前会话不可用
    - 状态：不计入今天完成
  - Microlaunch：
    - 结果：跳到 premium / pricing
    - 状态：今天不优先
  - StackShare：
    - 结果：`/submit` 路径不像稳定的产品提交流程
    - 状态：不计入
  - GitHub 组织主页：
    - 结果：确认新公开 README 已展示
    - 已在组织主页 pin 公开仓库：
      - `awesome-native-agent-platforms`
      - `agent-sandbox-cookbook`
      - `.github`
      - `zero-to-one-ai-infra-growth`
    - 结果：GitHub 组织页现在更像一个开发者信任资产，而不是空组织壳。
  - DEV Community：
    - 已创建并验证公开 profile：`https://dev.to/sandbaseai`
    - 展示名：`SandBase AI`
    - 官网：`https://www.sandbase.ai`
    - bio：`Agent infrastructure for developers building production AI agents.`
    - location：`Remote`
    - work：`Agent infrastructure at SandBase AI`
    - 关注了相关技术 tags：
      - `ai`
      - `python`
      - `opensource`
      - `devops`
      - `machinelearning`
      - `security`
      - `typescript`
      - `go`
      - `docker`
      - `kubernetes`
      - `rag`
      - `langchain`
    - 已拒绝 newsletter 订阅。
    - 结果：这是一个有价值的开发者社区 profile，也可以作为后续技术文章发布阵地。
  - DEV Community 技术文章发布：
    - 基于官网文章 `Why Production AI Agents Need a Runtime Layer` 做了 DEV.to 平台化改写。
    - 改写策略：
      - 保留 `agent runtime`、`durable state`、`sandboxed execution`、`resource limits`、`lifecycle` 等技术主线。
      - 减少站内 SEO 文结构和产品广告感。
      - 把 SandBase 放在结尾作为建设背景，而不是开头硬推广。
    - DEV.to 草稿标题：`Production AI Agents Need a Runtime Layer`
    - 标签：`ai`、`architecture`、`security`
    - canonical URL 已设置为官网原文：
      - `https://www.sandbase.ai/blog/production-ai-agents-need-a-runtime-layer/`
    - 状态：已发布。
    - 正式链接：
      - `https://dev.to/sandbaseai/production-ai-agents-need-a-runtime-layer-2o2a`
    - 本地草稿文件：
      - `30-day-growth-diary/drafts/devto-production-ai-agents-runtime-layer.md`
  - DEV.to 发布后二次分发：
    - X：
      - 用 SandBaseAI 账号发布短观点贴，强调 production agents 不只是 framework，而是需要 runtime layer。
      - 内容重点：durable state、sandboxed tool execution、resource limits、lifecycle control。
      - 链接：`https://x.com/SandbaseAI/status/2068948735107994092`
    - LinkedIn：
      - 用 SandBaseAI 公司页发布更完整版本。
      - 语气保持 B2B / infra 风格，强调 framework 和 runtime 的区别。
    - Discord：
      - 在 `#agent-runtime` 发轻量社区更新。
      - 不是公告式硬推广，而是邀请对 long-running / tool-using agents 有经验的人反馈。
  - Fazier：
    - 检查 URL：`https://fazier.com/submit`
    - 结果：已查看价格和提交规则
    - Basic：免费，但要求在 SandBase 官网首页或 footer 放 Fazier backlink badge
    - Lite：$19，不要求反链，符合 $30 预算
    - Premium：$39，超过当前预算
    - 决策：暂时跳过；渠道质量混杂，也不够开发者 / infra 垂直，不值得今天做小额付费实验
  - BetaList：
    - 已创建提交草稿：`https://betalist.com/submissions/172251`
    - 已重写文案，避免过度承诺，保持 agent infrastructure 定位
    - topics 调整到 `Infrastructure`、`API Integration`、`Observability`
    - 已走到 package 页面
    - 最低套餐：Lite $39
    - 决策：超过 $30 单渠道预算，不提交
  - Indie Hackers：
    - 已创建 profile：`https://www.indiehackers.com/sandbaseai`
    - 尝试添加 product section，但编辑器没有稳定把产品字段保存到公开 profile
    - 决策：作为已创建 profile / 后续候选保留，但暂时不计为完成外链
- 开源机会挖掘：
  - GitHub 精确搜索 `agent runtime sandbox tool calling` 没有仓库结果，但有大量代码结果。这说明机会点更可能在 examples / adapters，而不是成熟品类名。
  - 放宽到 `AI agent sandbox` 后，找到一批今天刚更新的新项目。
  - 今日 shortlist 3 个候选：
    - `jeremylongshore/agent-governance-plane`：面向 AI coding agents 的 Slack-native governance，包含 sandboxed execution、每次 tool call approval、signed audit logs。
    - `runseal-labs/runseal`：面向 AI agents 的 OS-native sandbox layer 和 stable execution protocol。
    - `blissito/sandbox-host`：自托管 Firecracker microVM 平台，用于 AI agent sandboxes 和 MCP 风格 sandbox tools。
  - 建议后续优先选 `runseal-labs/runseal` 方向，因为它最贴近 SandBase 的 sandbox / runtime 定位，而且可以拆成小型 checklist 或 probe 项目，不会一开始就变成大工程。

## 创建或更新的链接

- X 观点动态：https://x.com/SandbaseAI/status/2068866907579847023
- Peerlist 讨论回复：https://peerlist.io/scroll/post/ACTHKKD9EGGK77GDN1LQ6KJNBPMPRB
- Uneed 草稿编辑页：https://www.uneed.best/edit/waiting-line/37893?new=true
- Uneed 公开 launch 页：https://www.uneed.best/tool/sandbase
- GitHub 组织主页：https://github.com/sandbaseai
- GitHub 组织 README 仓库：https://github.com/sandbaseai/.github
- DEV Community profile：https://dev.to/sandbaseai
- DEV Community published article：https://dev.to/sandbaseai/production-ai-agents-need-a-runtime-layer-2o2a
- X distribution post：https://x.com/SandbaseAI/status/2068948735107994092
- Discord channel used for distribution：https://discord.com/channels/1516741633310199818/1516742589913632891
- 候选：BetaList 提交页：https://betalist.com/submit
- 候选：Indie Hackers 产品页：https://www.indiehackers.com/products/new
- 候选：Fazier launch 页：https://fazier.com/launch
- Indie Hackers profile 已创建：https://www.indiehackers.com/sandbaseai
- BetaList 草稿：https://betalist.com/submissions/172251
- GitHub 候选搜索：https://github.com/search?q=AI+agent+sandbox&type=repositories&s=updated&o=desc
- 候选项目：https://github.com/jeremylongshore/agent-governance-plane
- 候选项目：https://github.com/runseal-labs/runseal
- 候选项目：https://github.com/blissito/sandbox-host

## 问题 / 阻塞

- Uneed 已加入免费等待队列。
- GitHub 组织 profile README 已上线。
- Peerlist Launchpad 仍然卡在 UI / 账号状态上。
- DevHunt 因为费用超过当前预算，今天不适合提交。

## 经验

早期社区分发不要追求“到处贴链接”，更应该优先做有技术含量的真实回复。Peerlist 上一次小但真实的互动，比在多个线程里机械推广 SandBase 更有价值。

目录提交不能硬做。如果提交页被拦、价格不合适，或者会把 SandBase 放进泛 AI 工具分类，就应该跳过，保护定位。GitHub 组织 README 这种开发者信任资产，有时比弱目录更有价值。

开源机会挖掘最有价值的结果不是“收藏很多项目”，而是形成一个可执行的小项目方向。今天最好的方向是围绕 agent runtime 做 sandbox capability checklist / probe。

## 下一步

准备一个围绕 agent runtime sandbox capability probes 的小型开源项目 brief。另外可以考虑把最重要的几个 GitHub 仓库 pin 到组织主页。

下一批外链优先级：

1. 登录后做 Indie Hackers product page。
2. 如果价格 / 审核路径可接受，再做 BetaList。
3. 如果提交流程免费或价格合理，再做 Fazier。
4. Product Hunt 等 launch assets 和回复计划准备好后再做。

今天追加执行后，下一步优先级调整为：

1. 后续再修复 / 重试 Indie Hackers 产品保存问题。
2. BetaList 只有在预算规则允许超过 $39 时再继续。
3. Fazier 只作为低优先级付费实验，不作为核心外链渠道。
4. 继续加强 GitHub 开发者资产，因为它和 SandBase 的信任定位更匹配。
5. 下一篇 agent runtime / sandbox 技术文章准备好后，可以同步发到 DEV Community。
