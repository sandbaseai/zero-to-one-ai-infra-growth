# Uneed Launch 素材

状态：草稿

负责人：SandBase growth

相关草稿：Uneed waiting-line product draft，slug `sandbase`

## 目标

在给 SandBase 安排 Uneed launch 之前，先准备好发布素材。

这次 launch 不要写成普通 AI 工具提交，而是反复强化一个定位：

```text
SandBase is agent infrastructure for developers building production AI agents.
```

## 当前 Uneed 草稿

- Name: `SandBase`
- Slug: `sandbase`
- URL: `https://www.sandbase.ai`
- Category: `Development`
- Pricing: `Freemium`
- Tags: `API & Data`, `AI`, `Development`
- Tagline: `Agent infrastructure for developers building production AI agents.`

## 产品定位

### 短版本

```text
Agent infrastructure for developers building production AI agents.
```

### Launch 版本

```text
SandBase helps developers build production AI agents with infrastructure for sandboxed runtime, safe tool access, model routing, APIs, and distributed compute.
```

### 长版本

```text
SandBase is an agent infrastructure platform for developers building production AI agents.

It focuses on the runtime layer behind agent applications: sandboxed execution, safe tool access, model routing, APIs, and distributed compute for agent workloads.

The goal is to help agent builders move from demos to reliable systems that can run tools, use compute, and operate with clearer boundaries.
```

## 需要准备的截图

准备 3-5 张干净截图。不要出现私密数据、API key、邮箱、后台账号、billing 信息或未完成占位文案。

建议截图：

1. 首页首屏，展示核心定位。
2. Docs / quickstart，展示开发者如何开始。
3. Models / tools 页面，展示基础设施能力宽度。
4. Agent Ecosystem / registry 页面，如果已经上线。
5. Hackathon Support 页面，如果已经上线并且足够完整。

截图规则：

- 可以裁掉浏览器外框，除非 URL 本身有助于建立信任
- 如果浅色主题更清晰，优先使用浅色
- 小卡片尺寸下文字也要能看懂
- 不出现私密 workspace、账号、token、billing、email 信息
- 第一张截图要让人 3 秒内理解产品类别

已生成社媒图：

- [LinkedIn Uneed Agent Infrastructure Card](../../assets/generated-images/linkedin-uneed-agent-infra.png)
- 通过 `scripts/generate-images-sandbase.py --only linkedin-uneed-agent-infra` 生成
- 用途：LinkedIn 公司动态里配合 Uneed preparation update 使用

## 首条评论 / Launch Note

```text
Hi Uneed community,

We are building SandBase as agent infrastructure for developers working on production AI agents.

A lot of agent demos look impressive, but the hard part starts when agents need to run tools, access compute, route across models, and operate inside safer execution boundaries.

SandBase focuses on that infrastructure layer: sandboxed runtime, safe tool access, model routing, APIs, and distributed compute for agent workloads.

Would love feedback from builders working on agents, developer tools, or AI infrastructure:

- What breaks first when you move an agent from demo to production?
- Which tool/runtime boundary do you care about most?
- What would make an agent infrastructure layer trustworthy enough to adopt?
```

## X 支持文案

```text
We prepared SandBase on Uneed today.

SandBase is agent infrastructure for developers building production AI agents:

- sandboxed runtime
- safe tool access
- model routing
- APIs
- distributed compute for agent workloads

The question we care about:
what breaks first when AI agents move from demo to production?
```

## LinkedIn 支持文案

```text
We are preparing SandBase for a small launch on Uneed.

SandBase is an agent infrastructure platform for developers building production AI agents.

The product focuses on the runtime layer behind agent applications: sandboxed execution, safe tool access, model routing, APIs, and distributed compute for agent workloads.

Our view is simple: as agents move from demos to production systems, infrastructure becomes the product surface developers need to trust.

We are especially interested in feedback from teams building agent apps, developer tools, and AI infrastructure.
```

## Discord 更新

```text
Quick update: we prepared SandBase for a small Uneed launch.

We are positioning it as agent infrastructure for production AI agents, with focus on sandboxed runtime, safe tool access, model routing, APIs, and distributed compute.

Before we schedule the launch, I am collecting feedback:

When you move an agent from demo to production, what breaks first?
```

## 回复素材

### 如果有人问 SandBase 是什么

```text
SandBase is agent infrastructure for developers building production AI agents. The focus is the runtime layer: sandboxed execution, safe tool access, model routing, APIs, and compute for agent workloads.
```

### 如果有人问和 agent framework 有什么区别

```text
Agent frameworks help you define agent behavior. SandBase is focused on the infrastructure below that: where agents run, how they access tools, how model routing works, and how workloads execute with clearer boundaries.
```

### 如果有人问为什么 sandboxing 重要

```text
As soon as agents can use tools, browse, run code, or touch files, execution boundaries matter. Sandboxing is about giving agents useful capabilities without turning every tool call into an uncontrolled system action.
```

### 如果有人问是否只支持一个模型提供方

```text
No. The goal is to support agent workloads across models and tools, with routing and infrastructure designed around production agent apps rather than a single model API.
```

## 不要这样说

- "the best AI agent platform"
- "fully autonomous agents"
- "replace your engineering team"
- 没有具体文档支撑时，不说 "secure by default"
- 没有证据时，不说 "enterprise ready"
- 不编造 traction、客户、benchmark 或 integration

## 排期检查清单

只有这些准备好后再 schedule Uneed：

- 截图准备好
- 首条评论准备好
- X 支持文案准备好
- LinkedIn 支持文案准备好
- Discord 更新准备好
- launch 当天有人可以回复
- 没有未经明确确认选择付费升级
- 产品定位和官网、Docs、GitHub、LinkedIn、Peerlist、Uneed 草稿保持一致
