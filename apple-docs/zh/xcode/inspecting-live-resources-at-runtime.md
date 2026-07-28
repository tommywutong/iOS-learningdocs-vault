---
title: 在运行时检查实时资源
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/inspecting-live-resources-at-runtime
source_url: 'https://developer.apple.com/documentation/xcode/inspecting-live-resources-at-runtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/inspecting-live-resources-at-runtime.json'
content_hash: 'sha256:1a5ff2831952819e'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 开发者工作流](metal-developer-workflows.md)

# 在运行时检查实时资源

<sub>文章</sub>

调试 Metal App 时，通过查看纹理和缓冲区的内容来验证资源。

## 概述

在 Xcode 中调试 App 时，可以暂停在断点处，检查引用资源的变量，然后点按 Preview 按钮来预览纹理和缓冲区的内容。这是在运行时调试期间快速验证资源内容是否正确的一种方式。

> [!important] 重要
> 如果停用 GPU Frame Capture，就无法在 App 运行时检查资源内容。请参阅[在 Xcode 中捕获 Metal 工作负载](capturing-a-metal-workload-in-xcode.md)，了解如何重新启用它。

### 检查纹理和缓冲区

首先，在包含资源引用变量的作用域内暂停 App。为此，可以在引用资源的代码行上设置断点。要设置断点，请点按源码编辑器左侧的行号。以下示例展示了 `_skyMap` 绑定到渲染编码器所在代码行的断点：

![Xcode 源码编辑器的截图，其中突出显示了带有断点的一行代码。](../../../attachments/f33f01dc549725c850875379bfa880f1/gputools-quick-look-set-breakpoint@2x.png)

然后，当 App 在断点处暂停时，将指针移到引用资源的变量上，以显示 Value 检查器。

![](../../../attachments/24adafad63942811b270bcf3df4145c2/gputools-quick-look-hit-breakpoint@2x.png)

<sub>源码编辑器在带有断点的一行代码处暂停的截图，其中下划线 sky map 变量被突出显示。</sub>

最后，点按 Preview 按钮以显示资源内容。

![Preview 弹出窗口的截图，其中显示了下划线 sky map 变量的内容。](../../../attachments/25eff4f8f589d29d1b0b63e375b2cf18/gputools-quick-look-preview@2x.png)

如果资源是具有多个切片的纹理（如上面的天空贴图），可以拖动 Preview 弹出窗口底部的滑块来查看每个切片。如果资源中存在任何意外值，可以使用 Metal 调试器进一步调查（请参阅[调查视觉瑕疵](investigating-visual-artifacts.md)）。

## 另请参阅

### 运行时诊断

- [验证 App 的 Metal API 使用情况](validating-your-apps-metal-api-usage.md) — 使用 API Validation 捕获 Metal App 中的运行时问题。
- [验证 App 的 Metal 着色器使用情况](validating-your-apps-metal-shader-usage.md) — 使用 Shader Validation 捕获常见的着色器运行时问题。
- [监控 Metal App 的图形性能](monitoring-your-metal-apps-graphics-performance.md) — 在 App 运行时使用 Metal Performance HUD 捕获性能问题。
- [自定义 Metal Performance HUD](customizing-metal-performance-hud.md) — 修改 Metal 抬头显示器的外观，以监控图形性能。
- [理解 Metal Performance HUD 指标](understanding-metal-performance-hud-metrics.md) — 了解抬头显示器报告的各项指标表示什么。
- [使用 Metal Performance HUD 获取性能洞察](gaining-performance-insights-with-metal-performance-hud.md) — 在 App 运行时使用 Metal 抬头显示器捕获潜在性能问题。
- [使用 Metal Performance HUD 生成性能报告](generating-performance-reports-with-metal-performance-hud.md) — 使用抬头显示器记录 App 的性能。
