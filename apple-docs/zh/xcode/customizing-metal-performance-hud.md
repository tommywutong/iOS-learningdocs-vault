---
title: 自定义 Metal Performance HUD
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/customizing-metal-performance-hud
source_url: 'https://developer.apple.com/documentation/xcode/customizing-metal-performance-hud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/customizing-metal-performance-hud.json'
content_hash: 'sha256:8c17db88506846af'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 开发者工作流](metal-developer-workflows.md)

# 自定义 Metal Performance HUD

<sub>文章</sub>

修改你的 Metal 平视显示器（HUD）的外观，以监控你的图形性能。

## 概述

你可以通过多种方式自定义 Metal Performance HUD 的外观，包括其大小和不透明度，或更改覆盖层中显示的指标。

在 macOS 中，你可以导出 HUD 设置，并在你的 App 启动时应用它们。

### 在 macOS 上自定义 Metal Performance HUD

当你在 App 中启用 Metal Performance HUD 时，HUD 会在菜单栏中添加一个新的 Metal HUD 菜单。

![显示 Metal HUD 菜单的截图。](../../../attachments/aefb76ac0076bfe3f4ab7b686e9ffaa8/metal-hud-menu@2x.png)

Metal HUD 菜单提供了一种快速配置 HUD、创建性能报告（参见[使用 Metal Performance HUD 生成性能报告](generating-performance-reports-with-metal-performance-hud.md)）以及访问配置面板的方法。

> [!note] 注意
> 你也可以通过三次点击 HUD 覆盖层来打开配置面板。

配置面板是你可以完全自定义 HUD 的地方。

你可以在“HUD”面板中启用或禁用各种功能，例如编码器 GPU 时间跟踪（参见[监控你的 Metal App 的图形性能](monitoring-your-metal-apps-graphics-performance.md)），或调整覆盖层的透明度、比例和位置。

![Metal HUD 配置面板的截图。](../../../attachments/ad3c03c0cad6e6f017d8473d7d081ec8/metal-hud-config-panel@2x.png)

在“指标”面板中，你可以看到覆盖层中可用指标的列表。要了解有关这些指标的更多信息，请参阅[了解 Metal Performance HUD 指标](understanding-metal-performance-hud-metrics.md)。

![Metal HUD 指标配置面板的截图。](../../../attachments/139a406f36beb0e99eaa893e693cc523/metal-hud-config-panel-metrics@2x.png)

在“洞察”面板中，启用性能洞察功能以帮助你发现潜在的性能问题。此功能跟踪 Metal API 的使用情况并突出显示潜在的瓶颈。要了解更多信息，请参阅[通过 Metal Performance HUD 获取性能洞察](gaining-performance-insights-with-metal-performance-hud.md)。

![Metal HUD 洞察配置面板的截图。](../../../attachments/67130492a96d630cbb1c505541a03d6b/metal-hud-config-insights@2x.png)

### 在设备上自定义 Metal Performance HUD

你可以通过以下步骤在 iOS 或 iPadOS 设备的“开发者”设置中自定义 Metal Performance HUD 和日志记录：

1. 打开“设置”App。
2. 选择“开发者”。
3. 在“Graphics HUD”下，点击“Graphics HUD”以访问设置。

以下截图显示了 iOS 中的选项：

![](../../../attachments/3b5dda94e18d8b289a8967c47620cba9/metal-hud-ios-config@2x.png)

<sub>iOS 中“开发者”设置的截图，突出显示了启用 Metal Performance HUD 覆盖层和日志记录的开关。</sub>

> [!important] 重要
> 这些设置适用于所有启用 Metal Performance HUD 的 App。在从 Xcode 调试时，你可以使用环境变量来覆盖这些设置。

### 以编程方式自定义 Metal Performance HUD

你可以通过配置 `CAMetalLayer` 实例的 `developerHUDProperties` 字典来以编程方式自定义 Metal Performance HUD：

```swift
myMetalLayer.developerHUDProperties = [
    "mode": "default",
    "logging": "default",
    "positionX": 0,
    "positionY": 0,
    // ...
]
```

| 键 | 值 | 说明 |
|---|---|---|
| mode | default, main, disabled | 为此图层启用或禁用 Metal HUD。如果你的 App 使用多个图层，你可以将此值设置为 `main` 以使其成为主图层。这一点很重要，因为系统会根据主图层的呈现间隔计算某些指标，例如 GPU 时间。默认情况下，主图层是 App 创建的第一个图层。 |
| logging | default, disabled | 启用或禁用 HUD 日志记录。 |
| positionX | 0 - drawable 宽度 | Metal HUD 以像素为单位的绝对 X 位置。 |
| positionY | 0 - drawable 高度 | Metal HUD 以像素为单位的绝对 Y 位置。 |

此外，你还可以通过在字典中设置 HUD 支持的环境变量来添加各种效果，包括：

- **`MTL_HUD_LOG_ENABLED=1`** — 打开每帧统计信息的日志记录。
- **`MTL_HUD_LOG_SHADER_ENABLED=1`** — 打开着色器编译活动的日志记录。
- **`MTL_HUD_CONFIG_FILE=<path>`** — 选择 Metal HUD 加载的配置文件，该文件需要是 App 可以访问的文件路径。
- **`MTL_HUD_OPACITY=1.0`** — 配置覆盖层的不透明度，范围 `[0.0, 1.0]`。默认值为 `1.0`。
- **`MTL_HUD_SCALE=0.2`** — 配置覆盖层的比例，作为可绘制宽度的百分比，范围 `[0.0, 1.0]`。默认比例为 `0.2`，最小宽度为 300 像素。
- **`MTL_HUD_ALIGNMENT=topright`** — 设置覆盖层的位置。默认位置是 `topright`。可用选项包括 `topleft`、`topcenter`、`topright`、`centerleft`、`centered`、`centerright`、`bottomright`、`bottomcenter` 和 `bottomleft`。
- **`MTL_HUD_POSITION_X`，`MTL_HUD_POSITION_Y`** — 设置覆盖层以像素为单位的绝对位置。覆盖 `MTL_HUD_ALIGNMENT`。
- **`MTL_HUD_ELEMENTS`** — 指定一个逗号分隔的指标列表，这些指标将显示在覆盖层中。可用的指标名称包括 `device`、`rosetta`、`layersize`、`layerscale`、`memory`、`fps`、`frameinterval`、`gputime`、`thermal`、`frameintervalgraph`、`presentdelay`、`frameintervalhistogram`、`metalcpu`、`gputimeline`、`shaders`、`framenumber`、`disk`、`fpsgraph`、`toplabeledcommandbuffers` 和 `toplabeledencoders`。有关更多信息，请参阅[了解 Metal Performance HUD 指标](understanding-metal-performance-hud-metrics.md)。
- **`MTL_HUD_ENCODER_TIMING_ENABLED=1`** — 打开基于编码器的 GPU 时间跟踪。有关更多信息，请参阅[了解编码器 GPU 时间跟踪](monitoring-your-metal-apps-graphics-performance.md#Understand-encoder-GPU-time-tracking)。
- **`MTL_HUD_ENCODER_GPU_TIMELINE_FRAME_COUNT=6`** — 设置 GPU 时间线中显示的最大帧数。
- **`MTL_HUD_ENCODER_GPU_TIMELINE_SWAP_DELTA=1`** — 设置 GPU 时间线的更新间隔（以秒为单位）。
- **`MTL_HUD_SHOW_ZERO_METRICS=1`** — 使覆盖层显示自 App 启动或上次重置以来值为 `0` 的指标。Metal Performance HUD 默认启用此变量，以隐藏当前上下文中可能不可用或未使用的指标。
- **`MTL_HUD_SHOW_METRICS_RANGE=1`** — 报告最近 1200 帧的指标范围。有关更多信息，请参阅[显示指标的值范围](monitoring-your-metal-apps-graphics-performance.md#Display-the-value-range-of-metrics)。
- **`MTL_HUD_INSIGHTS_ENABLED=1`** — 打开性能洞察功能。有关更多信息，请参阅[通过 Metal Performance HUD 获取性能洞察](gaining-performance-insights-with-metal-performance-hud.md)。
- **`MTL_HUD_INSIGHT_TIMEOUT=10`** — 设置性能洞察在消失前的超时时间。
- **`MTL_HUD_INSIGHT_REPORT_INTERVAL=5`** — 设置性能洞察的报告间隔（以秒为单位）。如果在此间隔内一半的帧显示特定模式，则 Metal Performance HUD 会报告性能洞察。
- **`MTL_HUD_RUSAGE_UPDATE_INTERVAL=3`** — 设置系统资源使用情况更新间隔（以秒为单位）。
- **`MTL_HUD_METRIC_TIMEOUT=5`** — 设置瞬时指标的超时时间（以秒为单位）。当你在禁用 MetalFX 时，Metal Performance HUD 会自动隐藏瞬时指标，例如 MetalFX 指标。
- **`MTL_HUD_REPORT_URL=\<path>`** — 设置一个 App 可写的路径，系统将性能报告写入该路径。有关更多信息，请参阅[使用 Metal Performance HUD 生成性能报告](generating-performance-reports-with-metal-performance-hud.md)。
- **`MTL_HUD_DISABLE_MENU_BAR=1`** — 禁用 Metal Performance HUD 菜单项。

### 保存和加载 Metal Performance HUD 配置

你可以通过单击配置面板中的“Export HUD Configuration”按钮来保存自定义的 Metal Performance HUD 配置。

![Metal HUD 菜单的截图，突出显示了配置面板中的“Export HUD Configuration”选项。](../../../attachments/20518018e71533e705311708a50cadd9/metal-hud-config-export@2x.png)

配置文件是一个属性列表文件，包含环境变量的键值对。你可以通过设置 `MTL_HUD_CONFIG_FILE` 环境变量将其传递给 HUD。

```
export MTL_HUD_CONFIG_FILE=<path>
```

或者，你也可以使用 Metal HUD 菜单中的“Copy HUD Configuration”选项，该选项会导出描述 HUD 当前状态的一组环境变量，你可以在 App 启动时将其传递给 App。

![Metal HUD 菜单的截图，突出显示了 Metal HUD 菜单中的“Copy HUD Configuration”选项。](../../../attachments/e3f3e9cee939be7048013b5b69945513/metal-hud-menu-config@2x.png)

## 另请参阅

### 运行时诊断

- [在运行时检查实时资源](inspecting-live-resources-at-runtime.md) — 在调试你的 Metal App 时，通过查看纹理和缓冲区的内容来验证你的资源。
- [验证你的 App 的 Metal API 使用情况](validating-your-apps-metal-api-usage.md) — 使用 API 验证捕获你的 Metal App 中的运行时问题。
- [验证你的 App 的 Metal 着色器使用情况](validating-your-apps-metal-shader-usage.md) — 使用着色器验证捕获常见的着色器运行时问题。
- [监控你的 Metal App 的图形性能](monitoring-your-metal-apps-graphics-performance.md) — 在你的 App 运行时使用 Metal Performance HUD 捕获性能问题。
- [了解 Metal Performance HUD 指标](understanding-metal-performance-hud-metrics.md) — 了解 Metal Performance HUD 报告的每个指标的含义。
- [通过 Metal Performance HUD 获取性能洞察](gaining-performance-insights-with-metal-performance-hud.md) — 在你的 App 运行时使用 Metal Performance HUD 捕获潜在的性能问题。
- [使用 Metal Performance HUD 生成性能报告](generating-performance-reports-with-metal-performance-hud.md) — 使用 Metal Performance HUD 记录你的 App 的性能。
