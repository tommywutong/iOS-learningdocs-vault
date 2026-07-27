---
title: 编写并运行性能测试
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/writing-and-running-performance-tests
source_url: 'https://developer.apple.com/documentation/xcode/writing-and-running-performance-tests'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/writing-and-running-performance-tests.json'
content_hash: 'sha256:92e744ca07abf3d0'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [测试](testing.md)

# 编写并运行性能测试

<sub>文章</sub>

反复采集你代码性能相关的指标。

## 概述

用户会把响应速度和效率视为对 App 体验有积极贡献的因素。使用性能测试来记录代码中性能关键部分的指标，并在性能衰退到可接受基线以下时及时发现。

### 创建一个测试目标

性能测试使用与验证代码行为相同的 [XCTest](../xctest.md) 框架。在你的 Xcode 项目中创建一个测试目标，以便向其中添加行为测试和性能测试。要了解如何向项目添加新目标，请参阅[在项目中配置新目标](configuring-a-new-target-in-your-project.md)。

### 添加测试用例类和性能测试方法

你需要将性能测试组织到测试用例类中，这些类是 [XCTestCase](../xctest/xctestcase.md) 的子类。有关创建测试用例类和测试方法的信息，请参阅[定义测试用例和测试方法](../xctest/defining-test-cases-and-test-methods.md)。

性能测试方法是测试用例类上的一个方法，其名称以 `test` 开头，没有参数，也没有返回值。性能测试会调用以下方法之一，指示 XCTest 记录你代码性能的相关指标：

- **[measure(_:)](<../xctest/xctestcase/measure(__).md>)** — 使用默认的测量选项，记录代码块参数执行期间的默认性能指标。
- **[measureMetrics(_:automaticallyStartMeasuring:for:)](<../xctest/xctestcase/measuremetrics(__automaticallystartmeasuring_for_).md>)** — 记录指定的性能指标，可以是代码块参数执行期间的指标；如果你为 `automaticallyStartMeasuring` 参数传入 `false`，则记录代码块参数内 [startMeasuring()](<../xctest/xctestcase/startmeasuring().md>) 和 [stopMeasuring()](<../xctest/xctestcase/stopmeasuring().md>) 调用之间的指标。
- **[measure(metrics:block:)](<../xctest/xctestcase/measure(metrics_block_).md>)** — 使用默认的测量选项，记录代码块参数执行期间指定指标的数据。
- **[measure(metrics:options:block:)](<../xctest/xctestcase/measure(metrics_options_block_).md>)** — 根据指定的测量选项，记录代码块参数执行期间指定指标的数据，或代码块参数内 [startMeasuring()](<../xctest/xctestcase/startmeasuring().md>) 和 [stopMeasuring()](<../xctest/xctestcase/stopmeasuring().md>) 调用之间指定指标的数据。
- **[measure(options:block:)](<../xctest/xctestcase/measure(options_block_).md>)** — 根据指定的测量选项，记录代码块参数执行期间的默认指标数据，或代码块参数内 [startMeasuring()](<../xctest/xctestcase/startmeasuring().md>) 和 [stopMeasuring()](<../xctest/xctestcase/stopmeasuring().md>) 调用之间的默认指标数据。

### 确定要记录的性能指标

[measure(_:)](<../xctest/xctestcase/measure(__).md>) 和 [measure(options:block:)](<../xctest/xctestcase/measure(options_block_).md>) 的默认行为是以秒为单位记录所测量代码所花费的时间。要更改测试用例类中性能测试方法所采集的默认指标集合，请重写 [defaultPerformanceMetrics](../xctest/xctestcase/defaultperformancemetrics.md) 和 [defaultMetrics](../xctest/xctestcase/defaultmetrics.md)。在特定测试中使用上方列表中不同的测量函数，以记录不同的指标。

有关可用指标以及如何实现你自己的指标的信息，请参阅 [XCTMetric](../xctest/xctmetric.md)。

### 配置你的 scheme 和测试计划以获得准确的性能测量结果

Xcode 使用你在 Xcode 项目中创建的测试计划，来确定针对某个 scheme 要运行哪些测试，以及如何配置这些测试。为确保你采集到的是 App 在真实场景下的行为指标，请配置性能测试计划，使其复现代码在设备上运行时的条件。将你的 scheme 配置为使用 Release 构建配置进行测试构建，并关闭“Debug executable”设置。

配置你的测试计划，以禁用代码覆盖率和运行时净化选项。有关配置测试计划的更多信息，请参阅[通过将测试组织到测试计划中来改进代码评估](organizing-tests-to-improve-feedback.md)。

### 运行你的性能测试方法

按照运行测试以验证代码行为的相同方式来运行你的性能测试，具体做法见[运行测试并解读结果](running-tests-and-interpreting-results.md)。除了源代码编辑器装订线中测试方法定义旁边的测试结果状态图标之外，Xcode 还会在编辑器装订线中，在上方列出的每个性能测量函数调用旁边显示一个图标。根据性能测量的结果，该图标会处于以下状态之一：

| 性能测量状态图标 | 说明 |
|---|---|
| ![一个灰色填充的圆角菱形图标，内含一个对勾。](../../../attachments/0419cbd83dc3329cf41ba12285d0b28c/check-gray@2x.png) | 带对勾的灰色图标表示，记录下来的指标已经与基线值进行了比较。 |
| ![一个灰色填充的圆角菱形图标，内含一个圆点。](../../../attachments/9d3b9995998afb2edbf4b33ceb32a7a8/dot-gray@2x.png) | 带圆点的灰色图标表示，没有为 XCTest 记录基线值，以便与记录下来的指标进行比较。 |

点按性能测量结果图标，即可查看测试中所记录指标最近数值的图表，以及每项已记录指标的平均值（均值），如下图所示。

![](../../../attachments/02845637cecf45c9156f839889c9b930/performance-tests-1@2x.png)

<sub>Xcode 中性能报告叠加层的屏幕截图。图中展示了所采集指标的最近数值，以及报告的平均值、基线值和可接受的最大标准差。</sub>

### 设置基线和容差

通过设置基线值和最大标准差，为性能测试中记录的指标定义阈值。如果记录的指标比基线值差出的幅度超过最大标准差，测试就会失败。

要为性能测试的指标设置基线值，请按照以下步骤操作：

1. 在 Xcode 中，点按测试中性能测量函数调用旁边的图标，打开性能报告叠加层。
2. 点按 Set Baseline。

之后，你可以通过以下方式更改基线值：

1. 在 Xcode 中，点按测试中性能测量函数调用旁边的图标，打开性能报告叠加层。
2. 点按 Edit。
3. 输入新的基线值，或者点按 Accept，将当前的平均记录值用作新的基线值。
4. 在 Max STDDEV 字段中输入一个值，以定义记录指标相对于基线的最大标准差。
5. 点按 Save。

### 诊断失败的性能测试

如果某项测试失败，你可以按住 Control 点按失败测试旁边编辑器装订线中的图标，并选择“Profile [测试名称]”，在 Instruments 中打开该测试，以了解测试失败的更多细节。或者，在 Xcode 测试导航器中定位到失败的测试，按住 Control 点按它，然后选择“Profile [测试名称]”。

有关性能测试如何融入提升你 App 性能整体生命周期的信息，请参阅[提升你 App 的性能](improving-your-app-s-performance.md)。
