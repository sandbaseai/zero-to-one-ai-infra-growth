# 每日开源机会挖掘 SOP

目的：每天找 3 个小型开源机会，帮助 SandBase 参与 agent infrastructure 生态。

这不是追热点、蹭 star，也不是复制热门项目。目标是围绕新兴 agent infrastructure 项目找到真实缺口，做小而可信、可维护的开源资产。

## 每日产出

每天：

1. 扫 GitHub、Peerlist、X 和相关 launch / community feed。
2. 找 3 个候选机会。
3. 给每个候选打分。
4. 选择 1 个推进。
5. 记录为什么选它。

## 筛选标准

好的候选通常满足：

- 和 agent infrastructure 相关
- 新、增长中、或者有技术势能
- 复杂度适合 1-2 天做出 first version
- 对原项目用户有帮助
- 可以作为小型独立 repo 长期维护
- 自然契合 SandBase 定位
- 不伪装成官方集成
- 能带来真实社区互动，而不是硬蹭

## 适合做的项目类型

- starter templates
- compatibility checkers
- examples
- adapters
- benchmark scripts
- security checklists
- comparison notes
- MCP / tool wrappers
- sandbox demos
- deployment recipes

## 避免

- 复制别人的产品
- 直接和原 maintainer 的核心工作竞争
- 为了曝光发低质量 issue
- 在项目没有独立价值前强塞 SandBase 品牌
- 选择复杂到短期做不完的东西
- 选择没有 infrastructure 角度的泛 AI app

## 每日打分

每个候选 1-5 分：

| 字段 | 问题 |
|------|------|
| Relevance | 是否明确属于 agent infrastructure？ |
| Buildability | 是否能在 1-2 天内做出有用 first version？ |
| Community fit | 原项目或用户是否可能需要？ |
| SandBase fit | 是否连接 runtime、sandbox、tools、compute、evals 或 deployment？ |
| Distribution value | 是否能形成可信公开信号，而不是 spam？ |

优先选择 buildability 和 ecosystem fit 综合最好的一项。

## 今日候选 — 2026-06-21

### 1. `emberd` Agent Tool Sandbox Examples

仓库：https://github.com/hdprajwal/emberd

它是什么：

基于 Firecracker 的 sandboxing runtime，用 isolated microVMs 运行 AI-agent tool calls。

机会：

做一个小仓库，提供 client examples 和 compatibility checklist，用来测试 agent tool calls 如何通过 emberd 风格的 HTTP sandbox API 执行。

可能仓库名：

```text
agent-tool-sandbox-examples
```

第一版：

- Python example：通过 HTTP 在 sandbox 中运行代码
- TypeScript example：同样流程
- checklist：timeout、stdout/stderr、exit code、file access、network access、cleanup
- notes：production agents 对 sandbox API 的要求

为什么好：

- 非常贴 SandBase 的 sandboxed tool execution 定位
- 复杂度低
- 即使 emberd 后续变化，这个资产也有独立价值
- 后续可以演变为 SandBase compatibility benchmark

打分：

- Relevance: 5
- Buildability: 5
- Community fit: 4
- SandBase fit: 5
- Distribution value: 4

建议：今日最高优先级。

### 2. `trytet` Wasm Agent Sandbox Proof Examples

仓库：https://github.com/bneb/trytet

它是什么：

面向 AI agent code execution 的 Wasm sandbox runtime，强调 deterministic traps、fuel-bounded execution 和 MCP-native 方向。

机会：

做一个小型 proof/example repo，围绕 fuel-bounded agent tasks，解释如何评估 agent sandbox 行为。

可能仓库名：

```text
agent-sandbox-fuel-tests
```

第一版：

- tiny infinite-loop test
- CPU-bound task test
- file access expectation checklist
- MCP-style tool-call safety notes
- README 解释为什么 fuel limits 对 production agents 重要

为什么好：

- 技术故事强
- 非常贴 sandbox safety
- 适合解释 agent runtime risk

风险：

- 项目本身已经比较完整、比较 opinionated
- 要先理解 CLI / build path 才能做出真正有用的 examples

打分：

- Relevance: 5
- Buildability: 3
- Community fit: 3
- SandBase fit: 5
- Distribution value: 4

建议：第二选择。

### 3. `funky` Agent Runtime Contract Examples

仓库：https://github.com/funkyhq/funky

它是什么：

面向 cloud-native AI agents 的 open protocol，把 pluggable sandboxes、session stores、runtimes 放在同一个 contract 后面。

机会：

做一个 “agent runtime contract checklist” 或 example implementation notes，帮助比较 sandbox runtime、session store、agent loop 的边界。

可能仓库名：

```text
agent-runtime-contract-checklist
```

第一版：

- README checklist
- 最小 JSON/YAML contract examples
- session lifecycle diagram
- sandbox / runtime / session-store 边界说明
- builder compatibility questions

为什么好：

- 和 SandBase 概念重叠很强
- 如果从文档/checklist 开始，复杂度很低
- 可以变成一个有传播价值的内容资产

风险：

- 比 runnable example 抽象
- 如果没有 demo，可能显得不够具体

打分：

- Relevance: 5
- Buildability: 4
- Community fit: 3
- SandBase fit: 5
- Distribution value: 3

建议：如果今天想做 documentation-first 开源资产，可以选它。

## 今日建议选择

推荐选：

```text
agent-tool-sandbox-examples
```

原因：

- 最容易快速做出 first version
- 最贴 SandBase 的 sandbox / runtime 定位
- 不绑定某一个 sandbox backend，长期价值更稳
- 可以先做 standalone examples，后续再加 SandBase、emberd、E2B、Modal 或 local adapters

## 第一版构建计划

仓库名：

```text
agent-tool-sandbox-examples
```

初始结构：

```text
README.md
examples/
  python-http-sandbox/
  typescript-http-sandbox/
checklists/
  sandbox-api-compatibility.md
  production-agent-tool-safety.md
```

README 定位：

```text
Examples and checklists for running AI-agent tool calls inside sandboxed runtimes.
```

第一版不要硬推广 SandBase。SandBase 可以作为维护方 / 生态背景出现，但不要作为唯一支持 backend。

## 每日原则

```text
找真正有技术势能的项目。
做让生态更容易使用的小资产。
让 SandBase 通过有用获得注意力。
```
