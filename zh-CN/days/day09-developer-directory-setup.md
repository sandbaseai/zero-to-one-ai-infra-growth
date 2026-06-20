# Day 9 — 日常运营、目录准备和 Agent Market

日期: 2026-06-20

阶段: 第 2 周 — 分发和日常运营

状态: 进行中

## 目标

今天 Day 9 先梳理三个工作流：

1. LinkedIn、X、Discord 日常运营不断线。
2. 外部目录 / profile 发布先做准备，不急着铺量。
3. 提高 SandBase agent market 的优先级，把它定义成 emerging agent infrastructure registry，而不是普通 AI 工具目录。

## 优先级

今天的优先级：

| 优先级 | 工作流 | 为什么重要 |
|--------|--------|------------|
| P0 | Emerging Agent Infrastructure Market | 可能成为 SandBase 的生态和发现层 |
| P1 | LinkedIn / X / Discord 日常运营 | 保持公开 build signal 不断线 |
| P2 | 外部目录准备 | 有价值，但不能变成泛 AI 工具提交 |

关键判断：

```text
不要做随机 AI 工具 marketplace。
要做新的、代表未来方向的、有技术价值的 agent infrastructure 项目库，并且这些项目未来可以和 SandBase 深度集成。
```

## 工作流 1 — 日常运营

日常运营保持轻量：

- LinkedIn：如果有真实进展，发一条公司或 founder 视角更新。
- X：围绕 agents、runtime、sandboxing、tools、distributed compute 发一条 build note 或高质量回复。
- Discord：发一个问题、更新或小 prompt，引导 builder 回应。

目标是稳定，不是刷量。

## 工作流 2 — 外部目录准备

目录工作先保持谨慎：

- 筛选可信渠道
- 准备技术描述
- 选择 infrastructure 相关分类
- 避免泛 AI 工具目录稀释定位
- 记录阻塞和审核状态

如果 market/registry 概念会改变公开叙事，目录提交可以先等。

## 工作流 3 — Emerging Agent Infrastructure Market

Market 想法应该当成战略资产。

工作名：

```text
Emerging Agent Infrastructure
```

目的：

```text
追踪围绕 AI agents 的新的、代表未来方向的、有技术价值的项目，并判断它们未来是否能和 SandBase 深度集成。
```

这不是普通 AI app marketplace。

第一版重点关注：

- agent runtimes
- tool and MCP infrastructure
- sandboxes and computer use
- agent memory
- observability and evals
- deployment and compute
- multi-agent systems
- agent workspaces
- vertical agent infrastructure

每个项目都要判断：

- 为什么重要
- 代表什么未来信号
- 技术分类
- 阶段：emerging / growing / established
- SandBase 集成潜力：runtime / sandbox / tooling / MCP / observability / compute / deployment / community

## 今日计划产出

- 确认 Day 9 优先级。
- 起草 market/registry 定位。
- 定义第一版项目筛选标准。
- 保持 LinkedIn / X / Discord 日常运营轻量不断线。
- 目录发布只做和产品叙事一致的准备。

## 使用工具

| 工具 | 作用 |
|------|------|
| Codex | 梳理策略、起草 market 定位、记录日常运营 |
| Browser | 操作 LinkedIn / X / Discord，检查外部渠道 |
| GitHub / Website / Blog | 公开资产和未来 registry 引用 |
| SandBase 产品上下文 | 判断哪些项目值得收录 |

## 执行记录

- Day 9 开始时重新调整优先级。
- 用户明确今天有三个方向：日常运营、外部目录发布准备、建立 agent market。
- agent market 被提高优先级，因为它可能成为 SandBase 的生态层，而不是一次性的目录提交动作。
- Peerlist profile 已使用公司信息创建：
  - 公开 profile：`https://peerlist.io/sandbase`
  - 名称：`SandBase AI`
  - bio：`Agent infrastructure for developers building production AI agents.`
  - website：`https://www.sandbase.ai`
  - X：`SandbaseAI`
- LinkedIn 公司主页没有填写，因为 Peerlist 的 LinkedIn 字段限定为 `linkedin.com/in/`，这是个人主页格式，不适合公司主页。
- 已打开 Peerlist Launchpad，但账号显示 `25% You can’t interact yet`，暂时无法提交项目 launch。
- 已从公司 logo 资产上传 SandBase logo。
- 添加了公司安全的 skills：`ai`、`Python`、`JavaScript`、`Machine Learning`。
- Peerlist profile 完成度提升到 `40%`，页面变成 `You can interact now!`。
- profile 可互动后重新尝试 Launchpad，但当前会话中 Launch 按钮仍未打开提交表单。
- 继续前查看了 Peerlist 官方 verification 帮助页，结论是：
  - verification 对创建和完善 Peerlist profile 来说是可选项
  - workplace、education、bootcamp verification 免费
  - identity verification 需要少量费用，并且需要政府 ID
  - 完成 verification 后，验证状态会显示在 profile 上，但用于验证的证件信息或工作邮箱不会公开展示
- 决策：这次目录动作不做 identity verification。今天的外部 profile / backlink 目标，用公开 Peerlist profile 已经足够。

## 创建或更新的链接

- Planning doc: [Emerging Agent Infrastructure Registry](../../playbooks/emerging-agent-infrastructure-registry.md)
- Submission kit: [外部目录提交素材包](../playbooks/directory-submission-kit.md)
- Directory batch: [外部目录批次 — 2026-06-20](../playbooks/directory-batch-2026-06-20.md)
- Peerlist profile: https://peerlist.io/sandbase

## 问题 / 阻塞

- 第一版应该放在 `Resources` 下面，还是未来升级成顶级 `Ecosystem`？
- 第一版数据格式用 Markdown、CSV、JSON，还是产品数据库？
- 项目提交先人工审核，还是做公开 submit form？
- 收录时是否必须有 SandBase compatibility，还是先判断 integration potential？
- Peerlist 和 DevHunt 在前面的内置浏览器尝试中都出现过超时，所以第一次提交已准备好，但还没有提交。
- 每个目录都必须记录费用状态。Uneed 有免费新产品排队和付费升级；Peerlist profile 免费，workplace 类 verification 免费，identity verification 付费；DevHunt 在提交前费用暂未确认。
- 新增预算规则：单个目录或 launch 动作不超过 30 美金，优先免费。任何付费仍需人工确认。
- Peerlist profile 已创建，并且已经可以作为公开品牌 profile 链接使用。
- 添加 logo 和 skills 后，Peerlist 已允许互动，但 Launch 表单仍没有打开。可能还需要更多 profile 信息、project/work entry、可选 verification，或是页面交互问题。

## 经验

Registry 有价值的前提是有判断力。

更强的角度不是“收录 agent 工具”，而是：

```text
追踪代表未来方向、未来可能和 SandBase 深度集成的 agent infrastructure 项目。
```

目录提交也是一样：不要为了完成度徽章去做所有动作。

对一个新 infrastructure 品牌来说，早期更好的判断是：

```text
用免费、可信的 profile 建立公开信任，但在没有明确业务价值前，跳过隐私成本高、ROI 不清晰的身份验证动作。
```

## 下一步

Peerlist 今天按外部 profile / backlink 目标先收口，然后继续做下一个目录目标：DevHunt 或 Uneed。
