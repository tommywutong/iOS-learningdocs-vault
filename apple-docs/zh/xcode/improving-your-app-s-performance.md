---
title: 提升 App 的性能
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/improving-your-app-s-performance
source_url: 'https://developer.apple.com/documentation/xcode/improving-your-app-s-performance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/improving-your-app-s-performance.json'
content_hash: 'sha256:4441e5c9fdfd1331'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [性能与指标](performance-and-metrics.md)

# 提升 App 的性能

<sub>文章</sub>

通过持续改进的循环来建模、衡量并提升 App 的性能。

## 概述

使用你 App 的人期望它能良好运行。如果一个 App 需要很长时间才能启动，或者对用户输入的响应很慢，可能会让人觉得它没有正常工作或运行卡顿。如果一个 App 发起大量的大型网络请求，可能会增加用户的流量费用并耗尽设备电量。同样地，一个占用大量磁盘空间的 App 会减少用户设备上其他内容或 App 的可用空间。这些行为中的任何一种都可能导致用户感到沮丧，并最终卸载你的 App。

通过科学的方法规划并实施性能改进：

1. 收集用户遇到的问题的相关信息。
2. 衡量你的 App 的行为以找出问题的原因。
3. 规划一项改进措施。
4. 实施该措施。
5. 观察 App 的性能是否有所提升。

这些活动形成了一个持续改进的循环，如下图所示：

![](../../../attachments/bebd5417a094f169e53eed1baac69c8c/improving-your-app-s-performance-1@2x.png)

<sub>一张展示性能改进工作循环的插图：收集 App 当前性能的数据，确定最需要改进的方面，分析你的 App，进行一次改动，然后回到数据收集阶段。</sub>

最小化资源消耗对你的用户有益，并能提升他们对 App 的印象。以下是一些具体好处：

- 减少 App 启动时间可以改善用户体验，并降低 iOS 看门狗定时器终止你的 App 的可能性。
- 减少总体内存使用量可以降低 iOS 在后台释放你 App 内存的可能性，并在用户切换回你的 App 时提高响应能力。
- 减少磁盘写入可以加快 App 的整体性能，使其响应更迅速，并减少用户设备存储的损耗。
- 降低挂起率（hang rate）和挂起时长可以改善用户对你 App 性能和响应能力的印象。
- 减少电池消耗以及高功耗设备功能的使用可以使你的 App 更可靠，并有助于确保用户设备的其他部分在需要时可用。
- 保持较低的磁盘空间占用可以让用户安装和使用更多 App，并在设备上保存更多内容。例如，将你的 App 可以重新生成的内容存储在 [cachesDirectory](../foundation/url/cachesdirectory.md) 中，以便系统在需要时可以将其清除。这样做可以加快 App 和系统的升级速度，并减少系统创建设备 iCloud 备份所需的 iCloud 存储空间。有关更多信息，请参阅[优化 App 的数据以供 iCloud 备份](../foundation/optimizing-your-app-s-data-for-icloud-backup.md)。

即使你的测量和观察没有发现迫在眉睫的性能问题，也建议你运行一遍性能改进循环并进行预防性工作，以防止 App 的性能出现衰退（regression）。

### 收集 App 当前性能的数据

为了全面了解 App 的性能，请结合来自多个来源的信息：

- 使用 [Xcode Organizer](https://developer.apple.com/videos/play/wwdc2020/10076) 查看启动时间、用户界面响应能力、存储写入、内存使用和能耗的指标，以及磁盘写入、崩溃和能耗的诊断报告。Organizer 允许你按设备型号、App 版本和用户百分位数细分测量结果。有关更多信息，请参阅[分析已发布 App 的性能](analyzing-the-performance-of-your-shipping-app.md)。
- 使用 [MetricKit](../metrickit.md) 收集指标并将其记录到你自己的工具中。这些指标以直方图（histogram）的形式记录一天内观测值的频率。MetricKit 超越了 Metrics Organizer 中的指标，涵盖了平均像素亮度、蜂窝网络条件以及与你的 App 中自定义 `OSSignpost` 事件相关的持续时间。
- 从 [TestFlight](https://developer.apple.com/testflight/) 测试人员那里获取关于你 App 测试版（beta）体验的反馈。填写你测试版的测试信息页面，并要求测试人员就你 App 的性能提供反馈。提供一个电子邮件地址，以便测试人员可以报告他们的发现。
- 调查你的用户关于已发布版本 App 使用体验的反馈。邀请用户通过电子邮件或 App 内的专用界面发送反馈。询问他们使用 App 的体验——包括哪些功能运行良好以及他们遇到的任何问题。

### 确定最需要改进的方面

利用你观察得到的信息以及对 App 目的和预期使用模式的理解，找出最大的改进机会。某些性能问题与所调查的 App 类型无关。一个启动时间很长，或者对用户操作界面的尝试无响应的 App，会让用户感觉无法控制该 App。

在 Metrics Organizer 或 MetricKit 中看到的某个指标的最大值，如果该值代表的是预期的 App 使用情况，那么它可能不表示最重要的问题。例如，对于播客播放器来说，与后台音频播放相关的能耗可能不是问题，因为用户期望它能在后台播放。然而，如果你的 App 是一个游戏，其玩法没有后台组件，那么看到该指标占据主导地位就会令人惊讶。

看到该值在指标报告中占据主导地位可能表明存在节能的可能性，但最有影响力的改动可能在于辅助服务的使用，这些服务不会影响 App 的主要功能。播客播放器可能很少需要使用粗粒度的定位服务来向听众推荐本地兴趣播客，但频繁追踪用户的精确位置所导致的高能耗可能表明有必要进行改动。

### 分析你的 App

使用 [Instruments](https://help.apple.com/instruments/mac/current/) 并选择一个与你正在考虑的指标相关的分析模板来分析你的 App：

- 无响应和挂起：使用[时间分析器](https://help.apple.com/instruments/mac/current/#/dev44b2b437)模板。
- 内存问题：使用[分配](https://help.apple.com/instruments/mac/10.0/#/dev7b8f6eb6)和[泄漏](https://help.apple.com/instruments/mac/current/#/dev022f987b)模板。
- 能耗问题：使用[能耗日志](https://help.apple.com/instruments/mac/current/#/deva0db8947)模板。
- I/O 问题：使用[文件活动](https://help.apple.com/instruments/mac/current/#/dev6983c7c4)模板。
- 网络相关问题：使用[网络模板](https://help.apple.com/instruments/mac/10.0/#/dev209edacf)。

在真机上分析比在模拟器上分析能获得更精确的测量结果。如果你收集到的信息显示你的 App 在某个特定类别或型号的设备上性能不佳，请在该设备上进行分析。

找到导致性能问题的代码，并制定改进计划。请记住，你的改动可能不局限于某一行代码甚至某个函数，你可能需要对 App 进行重大的架构更改。例如，为了减少因同步下载网络资源而导致的挂起，可以引入后台操作来处理网络请求（参见[在后台下载文件](../foundation/downloading-files-in-the-background.md)），并在下载完成时在主线程（main thread）上更新用户界面。

### 实施下一次改动

基于调查结果，实施你计划好的改动。在 Instruments 中创建一个“之后”的分析文件，以便与“之前”的分析文件进行比较，从而确认你的改动带来了改进。考虑在 [XCTest](../xctest.md) 中编写一个性能测试，以防止未来出现性能衰退，并作为问题存在且已修复的记录。

### 将修改后的行为与原始数据进行比较

在更改你的 App 以解决你观察到的最重要的性能问题之后，确认该改动达到了预期效果，并且改进程度足够。使用 Xcode Metrics Organizer 中每个 App 版本的性能指标图表，查看改动是带来了改进还是衰退。

最后，判断你正在处理的指标是否仍然是需要解决的最重要的方面，或者数据是否指向其他指标以进行性能改进循环的下一次迭代。

### 其他资源

以下文章、Xcode 帮助主题和 WWDC 会话视频包含有关使用 Xcode 和 Instruments 衡量和改进 App 性能的更多信息：

#### 性能工具与技术

- [使用 Xcode Organizer 诊断性能问题](https://developer.apple.com/videos/play/wwdc2020/10076/)
- [使用 XCTest 消除动画卡顿（hitch）](https://developer.apple.com/videos/play/wwdc2020/10077)
- [Instruments 帮助](https://help.apple.com/instruments/mac/current)
- [日志记录](../os/logging.md)
- [iOS 和 watchOS 上的性能](https://developer.apple.com/videos/play/wwdc2015/230/)
- [打造出色 App 性能的实用方法](https://developer.apple.com/videos/play/wwdc2018/407/)
- [分析你的 App 的性能](https://help.apple.com/instruments/mac/current/#/dev44b2b437)
- [使用 Xcode 进行可视化调试](https://developer.apple.com/videos/play/wwdc2016/410/)
- [MetricKit 新变化](https://developer.apple.com/videos/play/wwdc2020/10081)
- [编写和运行性能测试](writing-and-running-performance-tests.md)

#### 能耗

- [实现全天电池续航](https://developer.apple.com/videos/play/wwdc2015/707/)
- [调试能耗问题](https://developer.apple.com/videos/play/wwdc2015/708/)
- [能效与用户体验](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929-CH15)
- [iOS App 能效指南](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243)
- [Mac App 能效指南](https://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_11.html#//apple_ref/doc/uid/TP40016227-SW14)
- [使用 Power and Performance API 识别趋势](https://developer.apple.com/videos/play/wwdc2020/10057)
- [使用调试仪表监测正在运行的 App](https://help.apple.com/xcode/mac/current/index.html?localePath=en.lproj#/dev94c128b7b)
- [监测你的 App 的能耗](https://help.apple.com/xcode/mac/current/index.html?localePath=en.lproj#/devf7f7c5fcd)
- [分析你 App 的能耗](https://help.apple.com/instruments/mac/current/#/dev7b8f6eb6)
- [能耗调试新变化](https://developer.apple.com/videos/play/wwdc2018/228/)
- [编写节能 App](https://developer.apple.com/videos/play/wwdc2017/238/)
- [Xcode Energy Organizer](https://help.apple.com/xcode/mac/current/index.html?localePath=en.lproj#/dev36a5a9141)

## 另请参阅

### 相关文档

- [减少 App 的内存使用](reducing-your-app-s-memory-use.md) — 通过分析内存使用指标并进行更改以最大化内存效率来提升 App 的性能。
- [减少 App 的启动时间](reducing-your-app-s-launch-time.md) — 通过最小化启动时间，为你的 App 创造更流畅的体验。
- [减少磁盘写入](reducing-disk-writes.md) — 通过优化 App 将数据写入永久存储的方式来提升 App 的响应速度。

### 基础

- [使用 Instruments 分析 App](../tutorials/instruments.md) — 使用 Instruments 分析你的 App 的性能、资源使用情况和行为。学习如何提高响应能力、减少内存使用以及分析复杂的行为模式。
- [分析已发布 App 的性能](analyzing-the-performance-of-your-shipping-app.md) — 查看通过 App Store 分发的 App 的性能和能耗指标。
- [为你的 visionOS App 制定性能计划](../visionos/creating-a-performance-plan-for-visionos-app.md) — 确定你的 App 的性能和能耗目标，并制定衡量和评估这些目标的计划。
