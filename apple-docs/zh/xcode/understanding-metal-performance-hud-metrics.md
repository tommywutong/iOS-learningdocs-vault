---
title: 了解 Metal Performance HUD 指标
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/understanding-metal-performance-hud-metrics
source_url: 'https://developer.apple.com/documentation/xcode/understanding-metal-performance-hud-metrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/understanding-metal-performance-hud-metrics.json'
content_hash: 'sha256:64fb1fc35981db94'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 开发者工作流程](metal-developer-workflows.md)

# 了解 Metal Performance HUD 指标

<sub>文章</sub>

了解抬头显示所报告的每项指标分别代表什么含义。

## 概述

Metal Performance HUD 提供了各种性能指标，帮助你发现性能问题，或找到在 Xcode 中（参阅[在 Xcode 中捕获 Metal 工作负载](capturing-a-metal-workload-in-xcode.md)）或在 Instruments 中（参阅[分析你 Metal App 的性能](analyzing-the-performance-of-your-metal-app.md)）进行捕获的最佳范围。

> [!note] 注意
> 要详细了解如何自定 Metal Performance HUD 并启用各种指标，请参阅[自定 Metal Performance HUD](customizing-metal-performance-hud.md)。

以下是 Metal Performance HUD 指标的完整列表：

- **Metal Device** — 显示 [MTLDevice](../metal/mtldevice.md) 的名称。
- **Rosetta Info** — 如果 App 是通过 Rosetta 转译层运行的，则显示活跃的架构（x86_64）。
- **Layer Size and Composition** — 显示图层的大小和呈现模式（直接呈现或合成呈现）。
- **Layer Scale and Pixel Format** — 显示图层的内容缩放系数和像素格式。
- **Memory** — 显示该进程当前使用的内存量，以及 `MTLDevice` 的 [currentAllocatedSize](../metal/mtldevice/currentallocatedsize.md)。
- **Thermal State** — 显示设备当前的 [thermalState](../foundation/processinfo/thermalstate-swift.property.md)。
- **Screen Refresh Rate** — 显示你 App 所在显示屏当前的刷新率。
- **Game Mode** — 显示游戏模式的状态（开启或关闭）。
- **FPS** — 显示过去 120 帧内每秒帧数的滚动平均值。FPS 是通过用 1 秒除以帧间隔计算得出的。
- **FPS Graph** — 显示一张绘制过去 120 帧 FPS 的图表。
- **Frame Number** — 显示当前的帧编号。在大多数情况下，这是自 App 启动或上次指标重置以来可绘制内容呈现的次数。当你启用帧插值时，此值会计入插值帧。
- **GPU Time** — 显示过去 120 帧内 GPU 时间的滚动平均值。GPU 时间是使用 Metal 为每一帧调度的命令缓冲区的 [gpuStartTime](../metal/mtlcommandbuffer/gpustarttime.md) 和 [gpuEndTime](../metal/mtlcommandbuffer/gpuendtime.md) 计算得出的。
- **Present Delay** — 显示过去 120 帧内呈现延迟的滚动平均值。呈现延迟是指从你调用 `presentDrawable` 到该可绘制内容出现在显示屏上之间的时间间隔。
- **Frame Interval** — 显示过去 120 帧内，两个连续 `MTLDrawables` 之间实际显示时间差的滚动平均值。
- **Frame Interval Graph** — 显示一张绘制过去 120 帧帧间隔的图表。
- **Frame Interval Histogram** — 以柱状图显示分桶后的帧间隔。桶的大小即为显示屏的刷新率。
- **Command Buffer and Encoder Count** — 显示已调度的命令缓冲区和编码器的数量，以及它们在最后一帧中的 CPU 编码时间。编码器的 CPU 时间是指从分配命令编码器到编码结束之间的时间间隔。
- **Shader Compiler** — 显示着色器编译器的活动情况，包括管线状态数量、已缓存着色器数量、已编译着色器数量和编译时间。在已编译着色器数量下方，是一张显示过去 120 帧编译时间的图表。
- **Disk Usage** — 显示系统使用情况所报告的磁盘读取字节数、写入字节数和逻辑写入次数。要了解更多信息，请参阅 [rusage_info_current](../kernel/rusage_info_current.md)。

> [!important] 重要
> 以下指标要求你启用编码器 GPU 时间追踪功能。要了解更多信息，请参阅[自定 Metal Performance HUD](customizing-metal-performance-hud.md)。

- **Encoder Time and GPU Timeline** — 显示每种编码器类型的编码器 GPU 时间，以及一张 GPU 时间线图。该 GPU 时间线每秒显示过去三帧中各编码器在 GPU 上的持续时间。
- **Top Labeled Command Buffers** — 显示带有 [label](../metal/mtlcommandbuffer/label.md) 的、GPU 占用最高的命令缓冲区，不包含没有标签的命令缓冲区。
- **Top Labeled Encoders** — 显示带有 [label](../metal/mtlcommandencoder/label.md) 的、GPU 占用最高的编码器，不包含没有标签的命令编码器。

> [!important] 重要
> 以下指标仅在你的 App 中使用了特定的 MetalFX 效果时才会出现。要详细了解 MetalFX，请参阅 [MetalFX](../metalfx.md)。

- **MetalFX Scaling** — 显示 MetalFX 的缩放方法（时间性、空间性或降噪）。
- **MetalFX Scaling Input Resolution** — 显示 MetalFX 缩放的输入分辨率。
- **MetalFX Scaling Target Resolution** — 显示 MetalFX 缩放的目标分辨率。
- **MetalFX Exposure** — 显示 MetalFX 效果的曝光度。
- **MetalFX Frame Interpolator** — 显示 MetalFX 帧插值的状态（开启或关闭）。

> [!important] 重要
> 以下指标仅在你通过 Game Porting Toolkit 评估环境评估你的游戏时才会出现。要了解更多信息，请参阅 [Game Porting Toolkit](https://developer.apple.com/games/game-porting-toolkit/)。

- **GPTk Draw (GSTS)** — 显示带有几何阶段和曲面细分阶段的绘制调用数量（`DrawInstanced`、`DrawIndexedInstanced`、`DrawInstancedIndirect` 和 `DrawIndexedInstandedIndirect`）。
- **GPTk Draw (TS)** — 显示带有曲面细分阶段的绘制调用数量（`DrawInstanced`、`DrawIndexedInstanced`、`DrawInstancedIndirect` 和 `DrawIndexedInstandedIndirect`）。
- **GPTk Draw (GS)** — 显示带有几何阶段的绘制调用数量（`DrawInstanced`、`DrawIndexedInstanced`、`DrawInstancedIndirect` 和 `DrawIndexedInstandedIndirect`）。
- **GPTk Draw** — 显示不使用几何阶段或曲面细分阶段的绘制调用数量（`DrawInstanced`、`DrawIndexedInstanced`、`DrawInstancedIndirect` 和 `DrawIndexedInstandedIndirect`）。
- **GPTk Execute Indirect** — 显示间接绘制调用或调度的数量（`DrawInstancedIndirect`、`DrawIndexedInstandedIndirect` 和 `DispatchIndirect`）。
- **GPTk Dispatch** — 显示调度的数量（`Dispatch`）。
- **GPTk Dispatch Mesh** — 显示带有网格阶段的绘制调用或调度数量（`DrawInstanced`、`DrawIndexedInstanced`、`DrawInstancedIndirect`、`DrawIndexedInstandedIndirect`、`Dispatch` 和 `DispatchIndirect`）。
- **GPTk Copy Resource** — 显示资源复制的数量（`CopyResource`、`CopyBufferRegion`、`UpdateSubResource`、`CopySubResourceRegion` 和 `CopyTextureRegion`）。
- **GPTk Clear Resource** — 显示清除命令的数量（`ClearRenderTargetView`、`ClearDepthStencilView` 和 `ClearUnorderedAccessView`）。
- **GPTk Refit BVH** — 显示 BVH 重新拟合的次数。
- **GPTk Build BVH** — 显示 BVH 构建的次数。
- **GPTk Display Rays** — 显示光线调度的数量。
- **GPTk Ray Query** — 显示光线查询的数量。

## 另请参阅

### 运行时诊断

- [在运行时检查实时资源](inspecting-live-resources-at-runtime.md) — 在调试你的 Metal App 时，通过查看纹理和缓冲区的内容来验证你的资源。
- [验证你 App 的 Metal API 用法](validating-your-apps-metal-api-usage.md) — 使用 API Validation 捕获你 Metal App 中的运行时问题。
- [验证你 App 的 Metal 着色器用法](validating-your-apps-metal-shader-usage.md) — 使用 Shader Validation 捕获常见的着色器运行时问题。
- [监测你 Metal App 的图形性能](monitoring-your-metal-apps-graphics-performance.md) — 在你的 App 运行时，使用 Metal Performance HUD 捕获性能问题。
- [自定 Metal Performance HUD](customizing-metal-performance-hud.md) — 修改你 Metal 抬头显示的外观，以监测你的图形性能。
- [利用 Metal Performance HUD 获得性能洞察](gaining-performance-insights-with-metal-performance-hud.md) — 在你的 App 运行时，使用 Metal 抬头显示捕获潜在的性能问题。
- [使用 Metal Performance HUD 生成性能报告](generating-performance-reports-with-metal-performance-hud.md) — 使用抬头显示记录你 App 的性能。
