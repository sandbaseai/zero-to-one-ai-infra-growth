# Day 5 — LinkedIn 公司主页：建立 B2B 可信度

日期: 2026-06-19

阶段: 第 1 周 — 账号和基础环境准备

状态: 已完成

![Day 5 图卡](../../assets/generated-images/day05-linkedin-trust.png)

## 背景

LinkedIn 和 X 的作用不一样。

X 是 build signal，LinkedIn 是 B2B trust surface。

当客户、投资人、合作伙伴或候选人搜索 SandBase 时，一个完整的 LinkedIn 公司主页能证明：这不是只有一个 landing page 的匿名项目。

## 目标

创建 SandBaseAI 公司主页，完善基础信息，并发布第一条公司动态。

公开主页：

https://www.linkedin.com/company/sandbaseai/

## 给小白的话

LinkedIn 对 B2B 产品来说不是“多一个社媒账号”。

它解决的是一个信任问题：

```text
别人搜索你时，会不会觉得这是一个真实公司？
```

所以公司主页、作者身份、管理员边界都要认真处理。

## 流程图

```mermaid
flowchart LR
  A["创建公司主页"] --> B["logo + 官网"]
  B --> C["About 文案"]
  C --> D["第一条公司动态"]
  D --> E{"公开作者是公司吗？"}
  E -- "是" --> F["形成 B2B 信任面"]
  E -- "否" --> G["调整发布身份"]
```

## 使用工具

| 工具 | 用途 |
|------|------|
| LinkedIn | 公司主页、B2B 信任、官方动态 |
| Browser | 页面创建、资料填写、发布确认 |
| Codex | 公司介绍、隐私判断、管理员操作建议 |

## 做了什么

- 创建公司主页
- 上传 logo
- 设置 tagline
- 设置官网链接
- 补 industry、company size、company type
- 写 About
- 设置 Message / Website CTA
- 发布第一条公司动态

## 第一条公司动态

主题不是硬推广，而是说明方向：

```text
SandBaseAI is building agent infrastructure for developers working on production AI agents.
```

重点表达：

- sandboxed runtime
- tool access
- model routing
- distributed compute
- helping agents move from demos to reliable systems

## 隐私和管理员边界

这一天有一个重要问题：公司需要公开身份，但个人管理员账号不应该被无意暴露。

我们确认：

- 普通访客看到的是 SandBaseAI 公司主页
- 公司动态显示作者是 SandBaseAI
- LinkedIn 内部会记录管理员权限
- 普通用户看不到后台管理员列表

添加运营账号做管理员时，因为搜索结果有同名歧义，我们没有冒险选择。

原则：

```text
品牌公开面优先。
管理员便利性第二。
身份不明确时不猜。
```

## 经验

LinkedIn 不是普通社媒账号，它是可信度资产。

对 SandBase 这种 B2B infra 产品来说，公司主页的作用是让外界看到一个清晰、稳定、专业的公司身份。
