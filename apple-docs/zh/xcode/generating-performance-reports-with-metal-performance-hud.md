---
title: 使用 Metal Performance HUD 生成性能报告
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/generating-performance-reports-with-metal-performance-hud
source_url: 'https://developer.apple.com/documentation/xcode/generating-performance-reports-with-metal-performance-hud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/generating-performance-reports-with-metal-performance-hud.json'
content_hash: 'sha256:22be4e3745705452'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 开发者工作流](metal-developer-workflows.md)

# 使用 Metal Performance HUD 生成性能报告

<sub>文章</sub>

使用平视显示器（Heads‑up Display）记录你的 App 的性能。

## 概述

借助 Metal Performance HUD，你可以生成指定时长的性能报告，用于分析你的 App 在该时间区间内的性能。生成报告开始时，系统会重置所有现有指标，HUD 会自动启用性能洞察（Performance Insights）功能。你还可以启用其他可选 HUD 功能，例如编码器 GPU 时间追踪（Encoder GPU Time Tracking）（参见[了解编码器 GPU 时间追踪](monitoring-your-metal-apps-graphics-performance.md#Understand-encoder-GPU-time-tracking)），以便向报告中添加更多指标。

### 生成性能报告

你可以从全局菜单中触发性能报告的生成，并选择所需的时长。报告时长范围从 5 秒到 30 分钟不等。

![一张显示“生成性能报告”菜单的屏幕截图。](../../../attachments/2faf7af21776b3bfaeb1529d99c699aa/metal-hud-menu-perf-report@2x.png)

在 Metal Performance HUD 重置所有指标、启用性能洞察并开始数据收集之前，有 3 秒的延迟。

![一张显示在性能报告生成开始前 Metal Performance HUD 等待 3 秒的屏幕截图。](../../../attachments/3e92384110374a35dbd4542998dec479/metal-hud-app-generate-perf-report@2x.png)

时长结束后，HUD 会将报告保存到你的 App 的临时文件夹。系统还会在菜单和洞察配置面板中列出报告，并提供在访达中显示报告或直接打开的选项。

![一张显示 Metal Performance HUD 生成性能报告菜单的屏幕截图。](../../../attachments/4798461e4bb5511115536bf7c246bf27/metal-hud-menu-generated-perf-report@2x.png)

你也可以使用 `MTL_HUD_REPORT_URL` 环境变量来指定保存性能报告的路径。

```
export MTL_HUD_REPORT_URL=<path>
```

![一张显示性能报告的屏幕截图。](../../../attachments/ffa7ddc4143cbf0c48b7280d85037a82/metal-hud-report@2x.png)

### 分析与解读性能报告

每份性能报告都包含一系列可折叠的部分。完整列表如下：

- **报告信息（Report info）**——详细说明报告的基本元数据，例如数据收集的时长、起始帧和结束帧、收集的总帧数，以及收集期开始和结束时的内存用量。
- **帧间隔分布（Frame interval distribution）**——包含一个帧间隔分布表和帧率统计信息，例如 99% 上限和 1% 下限。
- **性能洞察（Performance insights）**——如果 HUD 在数据收集期间检测到性能洞察，则提供详细信息。某些洞察还会添加额外的表格，例如如果 HUD 检测到频繁的渲染目标更改，则会添加帧编码表格。
- **带有标签的顶层命令缓冲区和编码器（Top labeled command buffers and encoders）**——包含一个表格，列出最消耗 GPU 且带有标签的命令缓冲区和编码器。
- **指标（Metrics）**——包含一个由 HUD 报告的性能指标表格，包括平均值、最小值和最大值。
- **帧时序（Frame timing）**——包含报告最后一帧的所有命令缓冲区和编码器的 CPU 和 GPU 时间的表格。
- **帧编码（Frame encoding）**——包含报告最后一帧的 CPU 编码序列的表格。颜色附件会按照颜色编码，以帮助你发现规律并找到合并渲染通道（Render Pass）的机会。
- **着色器编译（Shader compilation）**——包含在报告期间编译的着色器和后端编译时间的表格，以及自 App 启动以来编译的所有着色器的附加表格。

## 另请参阅

### 运行时诊断

- [在运行时检查实时资源](inspecting-live-resources-at-runtime.md)——在调试 Metal App 时，通过查看纹理和缓冲区的内容来验证你的资源。
- [验证你的 App 的 Metal API 使用情况](validating-your-apps-metal-api-usage.md)——使用 API 验证（API Validation）捕获 Metal App 中的运行时问题。
- [验证你的 App 的 Metal 着色器使用情况](validating-your-apps-metal-shader-usage.md)——使用着色器验证（Shader Validation）捕获常见的着色器运行时问题。
- [监控你的 Metal App 的图形性能](monitoring-your-metal-apps-graphics-performance.md)——在你的 App 运行时，使用 Metal Performance HUD 捕获性能问题。
- [自定 Metal Performance HUD](customizing-metal-performance-hud.md)——修改你的 Metal 平视显示器的外观，以监控你的图形性能。
- [了解 Metal Performance HUD 指标](understanding-metal-performance-hud-metrics.md)——了解平视显示器报告的每个指标的含义。
- [使用 Metal Performance HUD 获取性能洞察](gaining-performance-insights-with-metal-performance-hud.md)——在你的 App 运行时，使用 Metal 平视显示器捕获潜在的性能问题。
