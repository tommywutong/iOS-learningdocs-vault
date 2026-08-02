# C1：Swift API 与 Objective-C 类型系统试点

> 状态日期：2026-08-02
> 范围状态：已完成
> 执行边界：仅使用 Codex；不调用 DeepSeek，不恢复旧 `core` 分片

## 目标

暑期定向白名单及强相关 B 类均已完成（407 / 407）。用户于 2026-08-02 明确授权启动
下一阶段，但继续采用小批、可独立审查的方式控制用量。本试点只处理同一来源中与 Swift
语言设计、模块 API 和 Objective-C 互操作直接相关的四篇文章；不以目录或关键词匹配结果
批量扩张。

## 固定清单

| 英文原文 | 中文目标 | 原文字节 |
|---|---|---:|
| `blogs/en/nshipster/api-pollution-in-swift-modules.md` | `blogs/zh/nshipster/api-pollution-in-swift-modules.md` | 11,491 |
| `blogs/en/nshipster/swift-default-protocol-implementations.md` | `blogs/zh/nshipster/swift-default-protocol-implementations.md` | 7,861 |
| `blogs/en/nshipster/swift-property-observers.md` | `blogs/zh/nshipster/swift-property-observers.md` | 9,666 |
| `blogs/en/nshipster/type-encodings.md` | `blogs/zh/nshipster/type-encodings.md` | 7,432 |
| **合计** | **4 篇** | **36,450** |

这四篇均已有完整英文原文、没有现成中文配对，且没有命中已冻结的暑期 B 类白名单。它们
按 API 设计、协议默认实现、属性观察器、Objective-C 类型编码的顺序阅读，可复用术语并
覆盖 Swift 与 Objective-C 的边界。

## 完成记录

2026-08-02，四篇译文均已使用 Codex 完成人工翻译与逐篇复核，且没有调用 DeepSeek。
每篇均通过 `check_pair(..., strict_identifiers=True)`；批量还通过
`python3 tools/test_validate.py`、`python3 tools/test_segmented_markdown.py` 与
`python3 tools/check_links.py`（36,932 个本地链接，0 个错误）。

## 质量门

1. 只在对应 `blogs/zh/nshipster/` 路径新增译文；英文原文、frontmatter 的机器字段、
   代码、链接目标与图片路径保持不变。
2. 每篇先完成 Codex 人工翻译，再以英文原文逐段复核术语、条件、否定和代码上下文。
3. 每篇必须通过 `check_pair(..., strict_identifiers=True)`；全批再运行
   `python3 tools/validate.py`、`python3 tools/check_links.py`。
4. C1 完成并人工检查后才评估 C2；不得以 `tools/translate_plan.py next` 的目录聚合输出
   替代新的人工白名单。
