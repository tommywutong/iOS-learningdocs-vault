---
title: 借助 AI agent 调查 GPU 问题
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/investigating-gpu-issues-with-ai-agents
source_url: 'https://developer.apple.com/documentation/xcode/investigating-gpu-issues-with-ai-agents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/investigating-gpu-issues-with-ai-agents.json'
content_hash: 'sha256:b2b29f76341893f6'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 调试器](metal-debugger.md)

# 借助 AI agent 调查 GPU 问题

<sub>文章</sub>

将一份庞大的 GPU 跟踪记录交给 AI agent 自主调查，从而找出问题的根本原因。

## 概述

为了帮助你调查 GPU 跟踪记录中的问题，`gpudebug` 命令行工具提供了一个基于文本、可自我发现的接口，你可以以编程方式使用它，这使它非常适合 AI agent。

`list` 命令输出的每一行都显示节点名称和可用的操作，`go` 命令会打印目标节点的子节点。agent 可以通过跟随每个节点公开的操作来探索一份陌生的跟踪记录——而无需事先了解该跟踪记录的结构。

> [!tip] 提示
> 对于 AI agent，只需让它们查看 `man gpudebug` 并提供一个 `.gputrace` 文件。它们凭这些就能开始自主调查。

## 在多条命令间复用会话

对于涉及多条命令的调查，创建一次会话并复用它。加载跟踪记录和启动回放器可能需要数秒到数分钟不等，具体取决于跟踪记录的大小；复用会话可以避免在每次调用时都付出这个代价：

```shell
% gpudebug -t trace.gputrace -c "list"
Session 412 created.
...
% gpudebug -s 412 -c "go commands/cb0/re0/draw0" -c "info pipeline"
% gpudebug -s 412 -c "fetch color0"
% gpudebug -s 412 -c "next" -c "fetch color0"
% gpudebug --terminate 412
```

每次 `-s` 调用都会立即复用已经加载好的跟踪记录和回放器。

## 用 `--oneshot` 运行一次性查询

对于一次性的单条命令查询，如果管理会话显得繁琐，可以使用 `--oneshot`。这个选项会创建一个会话、运行命令，然后终止会话，但它会在每次调用时都付出完整的跟踪记录加载代价：

```shell
% gpudebug --oneshot -t trace.gputrace -c "go commands/cb0/re0/draw0" -c "info pipeline"
```

如需完整的命令参考，请参阅 `gpudebug(1)` 手册页（`man gpudebug`）。

## 另请参阅

### 基础

- [在 Xcode 中捕捉 Metal 工作负载](capturing-a-metal-workload-in-xcode.md) — 通过配置你的项目以使用 Metal 调试器，分析 App 的性能。
- [以编程方式捕捉 Metal 工作负载](capturing-a-metal-workload-programmatically.md) — 通过调用 Metal 的帧捕获功能，分析 App 的性能。
- [回放 GPU 跟踪文件](replaying-a-gpu-trace-file.md) — 在 Metal 调试器中使用 GPU 跟踪文件调试与分析 App 的性能。
- [调查视觉伪影](investigating-visual-artifacts.md) — 使用 Metal 调试器发现、诊断并修复 App 中的视觉伪影。
- [优化 GPU 性能](optimizing-gpu-performance.md) — 使用 Metal 调试器找到并解决性能瓶颈。
- [使用交互式命令行工具进行调试](debugging-with-interactive-command-line-tools.md) — 无需离开终端即可调查 GPU 跟踪记录中的渲染问题。
