---
title: 收集内存使用信息
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/gathering-information-about-memory-use
source_url: 'https://developer.apple.com/documentation/xcode/gathering-information-about-memory-use'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/gathering-information-about-memory-use.json'
content_hash: 'sha256:86a2afe741eb26d4'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [性能与指标](performance-and-metrics.md) · [减少 App 内存使用](reducing-your-app-s-memory-use.md)

# 收集内存使用信息

<sub>文章</sub>

通过测量和分析 App 来识别内存使用效率低下的问题。

## 概述

Xcode 和 Instruments 提供了多种工具，用于观察和探索 App 中的内存使用情况。

### 查看内存报告

当你的 App 在 Xcode 中运行时，可以通过 Xcode 的调试导航器（Debug navigator）中的内存报告查看 App 的当前内存使用量，以及观察到的最高值。内存仪表（memory gauge）的黄色区域表示内存使用量已高到足以触发警告。如果 App 的内存使用量进入红色区域，则存在被 iOS 终止的风险。

![](../../../attachments/aa40d4726bfc19940d796f766fb1aceb/gathering-information-about-memory-use-1.png)

<sub>图示为在调试 App 时可用的 Xcode 内存报告。折线图跟踪了内存使用量随时间的变化。</sub>

> [!tip] 提示
> 如果 iOS 因为你的 App 使用了过多内存而反复终止它，你可以在模拟器中调查其行为，模拟器中的 App 可以继续运行。在模拟器中运行 App 时，内存仪表始终停留在绿色（安全）区域，因为 macOS 不会发出内存警告或内存不足终止。这种行为有助于诊断与内存使用过高相关的问题。但请记住，模拟器中内存仪表处于绿色区域并不一定意味着 App 的内存使用处于安全范围内。

### 检查调试内存图

你可以通过点击 Xcode 工作区窗口底部调试区域中的“调试内存图”（Debug Memory Graph）按钮，生成 App 中对象和分配的内存图（memory graph）。

![图示为“调试内存图”按钮。](../../../attachments/d156982b0dad1dd581a8d8e0e866539d/gathering-information-about-memory-use-2.png)

内存图显示了你的 App 正在使用的内存区域以及每个区域的大小。图中的节点代表一个对象、堆分配或内存映射文件。节点之间的连接以箭头形式绘制，显示一个内存区域引用另一个内存区域的位置。

![图示为调试内存图，以及 App 中已分配内存区域之间的关系。](../../../attachments/b02db2b60e5ef7d88a9bd5d237a85d36/gathering-information-about-memory-use-3.png)

内存图显示了 App 在何处使用内存以及这些用途之间的关联。你可以通过分配堆栈回溯（allocation stack traces）来增强此图，从而使每个区域都与分配该区域时记录的一个调用堆栈回溯相关联。

要启用分配堆栈回溯，请在 Scheme 运行设置的诊断（Diagnostics）区域中勾选“Malloc Stack”复选框。启用分配堆栈回溯后，内存图中节点的检查器（inspector）将显示分配该节点时记录的堆栈回溯。利用此信息，可以将内存图中的内存分配与 App 源代码中的函数和方法关联起来。

要从 Xcode 导出内存图，请选择“文件（File）\> 导出内存图（Export Memory Graph）”。你可以与团队成员共享导出的内存图，或使用命令行工具（包括 `vmmap` 和 `leaks`) 进行探索。有关命令行工具的更多信息，请参阅 WWDC 2018 会话 416 的 [iOS 内存深度剖析](https://developer.apple.com/videos/play/wwdc2018/416/)。

### 使用 Allocations 工具分析 App

Allocations 工具会跟踪所有堆和匿名虚拟内存（VM）分配的大小和数量，并按分类（category）进行组织。使用 Allocations 工具的时间轴，调查当你操作 App 界面时，App 已分配的内存总量如何增减。使用统计视图查看进行了哪些分类的分配，每个分类已进行的分配数量，以及这些分配的大小。点击分类名称旁的箭头，可查看该分类下进行的各个分配，以及分配内存的时间和负责该分配的代码。

Allocations 工具中的“代”（Generations）视图对于调查 App 特定功能的内存使用情况很有用。启动你的 App，并准备使用正在调查的功能——例如，通过导航到包含某个特定控制的视图。接下来，点击 Allocations 工具中的“标记代”（Mark Generation）按钮。在你的 App 中激活该功能，然后再次点击“标记代”（Mark Generation）。Instruments 会按代来组织内存分配，这些代在你点击“标记代”的时刻被分隔开。你可以隔离出使用该功能期间发生的内存分配。并非在此时间段内记录的所有分配都与你正在研究的功能相关，但许多在两个代标记之间未发生的无关分配将被排除在考量之外。

## 另请参阅

### 相关文档

- [通过 jetsam 事件报告识别高内存使用](identifying-high-memory-use-with-jetsam-event-reports.md) — 了解当可用内存不足时操作系统为何终止你的 App。

### 任务

- [进行更改以减少内存使用](making-changes-to-reduce-memory-use.md) — 通过解决导致内存使用过高的常见原因来减少 App 的内存使用。
- [防止内存使用衰退](preventing-memory-use-regressions.md) — 测量 App 功能所使用的内存，并通过 XCTest 性能测试检测增长。
- [响应低内存警告](responding-to-low-memory-warnings.md) — 检测你的 App 何时使用了过多内存，并控制内存使用。
