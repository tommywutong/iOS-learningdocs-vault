---
title: 分析 App 的电池使用情况
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/analyzing-your-app-s-battery-use
source_url: 'https://developer.apple.com/documentation/xcode/analyzing-your-app-s-battery-use'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/analyzing-your-app-s-battery-use.json'
content_hash: 'sha256:ee8de812c3bb2c45'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [性能与指标](performance-and-metrics.md)

# 分析 App 的电池使用情况

<sub>文章</sub>

通过降低 App 的功耗，延长一次充电后 App 的可用时间。

## 概述

当 App 不需要耗电的子系统时，用户的设备会减少这些子系统的使用，从而尽可能延长电池续航时间。例如，没有任何 App 发出网络请求时，设备可以关闭 Wi-Fi 和蜂窝网络组件。

当 App 使用这些功能时，会缩短设备两次充电之间的使用时间，并可能升高设备温度，这会导致设备为避免过热而限制其功能。用户可以打开设备上的“电池”设置，查看哪些 App 使用了大量电量。如果用户发现你的 App 耗电很多，并造成不佳的整体设备使用体验，他们可能会减少使用你的 App，或将其卸载。

![一张 iOS“电池”设置面板的截图，其中显示设备上耗能的 App 列表。](../../../attachments/e862697e584353c8704e7c57153f2212/battery-settings@2x.png)

从 Xcode、MetricKit 和 Instruments 收集信息，以了解 App 的电池使用情况，并识别和确定改善 App 性能的机会优先级。

### 在 Xcode 中查看 App 的能耗

Xcode 管理器中的 Battery Usage 面板按 App 版本细分 App 的前台和后台功耗，为优化功耗提供起点。该图仅包含 Xcode 拥有足够信息来显示指标的 App 版本。

顶部图表显示屏幕开启时的使用情况和电池使用百分比，数据标准化为 App 位于前台且设备未连接电源时的 24 小时周期。

![](../../../attachments/c6fc436ca3bc73b36edf1044071f39b6/analyzing-your-app-s-battery-use-1@2x.png)

<sub>Xcode 管理器中 Battery Usage 指标面板的截图。从左到右依次是指标和报告列表、用条形图显示最近 8 个 App 版本电池使用情况的指标 UI，以及右侧比较数据和电池使用类别细分的详细视图。</sub>

底部图表显示同一时期的后台电池使用情况。

点按先前版本对应的条形图，会在图表右侧显示电池使用情况比较，如上图所示。每个版本的百分比值后面是类别细分。为便于比较，图表以粗体显示较大的值。

功耗类别包括：

- 音频
- 网络
- 处理：CPU 和 GPU 使用情况
- 显示：屏幕使用情况
- 蓝牙
- 定位
- 相机
- 手电筒
- NFC
- 其他：上述类别中因功耗太小而未在列表中显示的功耗，加上这些类别之外的任何系统功耗。

### 查看能耗异常报告

当 App 在 24 小时内使用大量能量时，系统会生成能耗异常报告。在 Xcode 管理器的 Energy 面板中查看汇总的异常报告。

Report List 中的每份报告都会显示导致异常的函数，以及该函数占总能耗的百分比。点按报告会显示一个示例栈回溯（stack trace），以及检查器中的其他详细信息，包括操作系统版本、设备型号、收到的日志数量和 14 天报告趋势。

### 获取针对能耗问题的编程助理建议

选择能耗报告后，在检查器中点按 Generate Recommendations，以在 Xcode 中获得辅助诊断。选择工作区后，Xcode 会打开项目，并将栈回溯和能耗上下文粘贴到编程助理中，帮助你识别并修复能耗过高的根本原因。

### 在 Xcode 中测量正在运行的 App 的功耗

在 Xcode 中，将运行目的位置设置为设备，然后选择 Product \> Run。有关更多信息，请参阅[在模拟设备或实体设备上运行 App](running-your-app-on-simulated-or-physical-devices.md)。

在 Debug 导览器中，显示调试仪表并点按 Energy Impact，以查看 App 的能耗。仪表会显示 App 的平均能耗影响，饼图则显示各功耗类别对设备能耗的贡献。时间线会报告每个类别相关的瞬时能耗，以及 App 的生命周期状态和设备的热状态。

![](../../../attachments/68e23dc2f44eaf64684d58b741f506d0/xcode-energy-gauges@2x.png)

<sub>Xcode 中 Energy Impact 视图的截图。一个仪表显示正在运行的 App 的平均总体能耗影响，其他图表则报告哪些功耗类别处于活跃状态以及设备状态。</sub>

### 收集功耗指标

使用 [MetricKit](../metrickit.md) 接收有关 App 在用户设备上如何使用电池的指标。通过收集以下指标了解 App 的电池使用情况：

| 功耗类别 | 指标 |
|---|---|
| CPU | [CPUTimeMetric](../metrickit/cputimemetric.md)、[CPUInstructionsCountMetric](../metrickit/cpuinstructionscountmetric.md) |
| 显示 | [PixelLuminanceMetric](../metrickit/pixelluminancemetric.md) |
| GPU | [GPUTimeMetric](../metrickit/gputimemetric.md) |
| 定位活动 | [LocationActivityTimeMetric](../metrickit/locationactivitytimemetric.md) |
| 网络活动 | [TotalWiFiUploadMetric](../metrickit/totalwifiuploadmetric.md)、[TotalWiFiDownloadMetric](../metrickit/totalwifidownloadmetric.md)、[TotalCellularUploadMetric](../metrickit/totalcellularuploadmetric.md)、[TotalCellularDownloadMetric](../metrickit/totalcellulardownloadmetric.md) |

### 在 Instruments 中分析 App 的功耗

使用 Instruments 中的 Power Profiler 工具调查 App 的电池使用情况。你可以使用此工具分析开发期间收集的数据，以及他人从用于运行 App 的设备发送给你的数据。有关更多信息，请参阅[使用 Power Profiler 测量 App 的功耗](measuring-your-app-s-power-use-with-power-profiler.md)。

### 在性能测试中测量能耗

如果你发现代码的某个特定部分通过 CPU 密集型活动显著增加了 App 的整体能耗，请创建性能测试来测量该代码的 CPU 使用情况。定期运行测试，以检测 App CPU 使用情况的衰退（regression），这可能会导致能耗相应增加。

在性能测试中使用 [XCTCPUMetric](../xctest/xctcpumetric.md) 测量测试代码块的 CPU 使用情况。有关更多信息，请参阅[编写和运行性能测试](writing-and-running-performance-tests.md)。

### 采用推荐实践，尽量减少电池使用

减少 App 执行的工作，并以更高效的方式执行其余工作。有关更多信息，请参阅[降低 App 的电池使用量](reducing-your-app-s-battery-use.md)。

## 另请参阅

### 功耗

- [使用 Power Profiler 测量 App 的功耗](measuring-your-app-s-power-use-with-power-profiler.md) — 无论设备是否连接到 Xcode，都可以分析 App 的功耗影响。
- [降低 App 的电池使用量](reducing-your-app-s-battery-use.md) — 采用设计原则和推荐的 API 来减少功耗。
