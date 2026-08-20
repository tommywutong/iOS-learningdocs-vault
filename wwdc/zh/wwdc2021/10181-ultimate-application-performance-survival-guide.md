---
title: 终极 App 性能生存指南
session_id: 10181
collection: wwdc2021
year: 2021
duration: '24:00'
topics: [Developer Tools]
group: D · 响应性、hang/hitch 与渲染循环（RunLoop 的现代替身）
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10181/'
content_hash: 'sha256:8bea5880fb1bc718'
translated: true
---

# 终极 App 性能生存指南

<sub>WWDC2021 · 24:00 · Developer Tools</sub>

性能优化看起来可能是一项令人生畏的任务——有大量指标需要跟踪，有大量工具需要使用。别怕：我们的 App 性能生存指南……

> [!note] 归档理由
> 性能问题的总体分类与排查顺序（总纲）

## 相关资源

- [分析已发布 App 的性能](https://developer.apple.com/documentation/Xcode/analyzing-the-performance-of-your-shipping-app)
- [改善 App 响应性](https://developer.apple.com/documentation/Xcode/improving-app-responsiveness)
- [MetricKit](https://developer.apple.com/documentation/MetricKit)
- [App Store Connect API](https://developer.apple.com/documentation/AppStoreConnectAPI)
- [XCTest](https://developer.apple.com/documentation/XCTest)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10181/11/A69D2FCC-21C3-4392-B857-552EF73E7714/downloads/wwdc2021-10181_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10181/11/A69D2FCC-21C3-4392-B857-552EF73E7714/downloads/wwdc2021-10181_sd.mp4?dl=1)
- [优化空间计算 App 的功耗和性能](https://developer.apple.com/videos/play/wwdc2023/10100)
- [检测和诊断内存问题](https://developer.apple.com/videos/play/wwdc2021/10180)
- [诊断 App 中的功耗和性能衰退](https://developer.apple.com/videos/play/wwdc2021/10087)
- [在 Xcode Organizer 中分类 TestFlight 崩溃](https://developer.apple.com/videos/play/wwdc2021/10203)
- [了解和消除 App 中的挂起](https://developer.apple.com/videos/play/wwdc2021/10258)
- [使用 Xcode Organizer 诊断性能问题](https://developer.apple.com/videos/play/wwdc2020/10076)
- [使用 XCTest 消除动画卡顿](https://developer.apple.com/videos/play/wwdc2020/10077)
- [使用 Power and Performance API 识别趋势](https://developer.apple.com/videos/play/wwdc2020/10057)
- [MetricKit 新功能](https://developer.apple.com/videos/play/wwdc2020/10081)
- [探索 UI 动画卡顿和渲染循环](https://developer.apple.com/videos/play/tech-talks/10855)
- [Instruments 入门](https://developer.apple.com/videos/play/wwdc2019/411)
- [使用 MetricKit](https://developer.apple.com/videos/play/wwdc2021/10181/?time=346)
- [测试滚动性能](https://developer.apple.com/videos/play/wwdc2021/10181/?time=629)
- [使用 mxSignpostAnimationIntervalBegin](https://developer.apple.com/videos/play/wwdc2021/10181/?time=713)
- [使用 XCTest 测量磁盘使用量](https://developer.apple.com/videos/play/wwdc2021/10181/?time=831)
- [收集内存遥测数据](https://developer.apple.com/videos/play/wwdc2021/10181/?time=1279)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好。我是 Shefali Saboo，是 Apple 的一名性能工具工程师。

我将担任你的导游，一起探索应用性能的方方面面。今天的旅程将是一场激动人心的性能世界之旅。你的 App 在我们设备上的整体软件体验中扮演着重要角色。持续优化 App 并改善性能，意味着你的用户会更频繁地使用你的 App，参与度更高，并且使用时间也更长。为性能进行优化看起来可能是一项令人生畏的任务，因为要跟踪的指标和要使用的工具很多。但别怕。这份生存指南将让你快速了解工具、指标和范式，这些可以帮助你把开发提升到新水平，并确保最佳的用户体验。我非常兴奋能作为你的导游，一起走过我们的性能工具以及你可以用它们完成的出色工作。今天我们将介绍五大主要工具：Xcode Organizer、MetricKit、Instruments、XCTest 和 App Store Connect API。我们将从关键指标的快速介绍开始。

然后逐步讨论各领域中的一些常见问题以及解决和预防它们的方法。

最后，我们将以一些后续步骤结束。性能优化就像一条长河，有很多中途站。需要几种不同的工具来导览（navigation），在每个站点都有新东西要学习。让我们顺着河流走一趟。首先，快速介绍。让我们看看今天要讲的不同性能指标。目前，跟踪 App 性能有八个关键项：电池用量、启动时间、挂起率（Hang Rate）、内存、磁盘写入、滚动、终止和 MXSignposts。所有这些都可以通过我们的工具集进行跟踪。

我是一款名为 MealPlanner 的 App 的开发者，这款 App 允许用户跟踪他们一周的餐食并保存很棒的食谱。

下面是我的 App 中一个糟糕用户体验的例子，具体体现在滚动卡顿（scroll hitches）上。注意这种缓慢、跳跃和抖动的滚动？另一方面，这是同一款应用，但拥有无缝的用户体验，没有卡顿。

我们已经可以看到两种体验之间存在相当大的差异，而这种流畅的滚动正是我们希望通过性能优化来帮助你实现的。每个性能指标都有自己独特的范式集合和常用工具。让我们直接进入每个领域中的一些常见问题以及解决和预防它们的方法。沿着河流的第一站是电池用量。

如果你的 App 消耗了大量电量，用户在端上会看到这样的画面。这是电池用户界面（Battery UI）。它向用户展示了他们设备上的某个 App 对整个电池放电量贡献了多少，以及它的前台和后台活动。为什么你应该关心改善电池续航？很简单。用户优先使用那些能让他们全天使用设备而无需充电的 App。通过优化电池续航，用户可以更长时间地使用他们的设备和你的 App。这本身就是一项胜利。在优化电池续航方面，有许多不同的子系统需要注意。其中最重要的三个是 CPU、网络和定位。我可以在开发期间或版本发布后，使用几种不同的工具来跟踪和排查我的 App 的电池续航问题。当我在办公桌上开发和测试新功能时，我会通过 Xcode 构建和运行我的代码，然后点击调试导航器（Debug navigator），它看起来像一个带喷嘴的小瓶子，来查看 Xcode 提供的各种仪表（gauge）。我会密切关注的是能量仪表（Energy Gauge）。能量仪表允许我在测试 App 时跟踪我的 CPU 使用情况，并向我显示高 CPU 利用率和 CPU 唤醒开销（CPU Wake Overhead）的区域。高 CPU 利用率是指 CPU 使用率大于 20%，而 CPU 唤醒开销是指 CPU 从空闲状态唤醒的区域，这会产生能量成本。当我的 App 绘制用户界面、处理来自网络的数据或执行计算时，看到 CPU 出现峰值是很常见的，但是一旦这些任务完成，我的 App 正在等待用户执行下一个操作时，我应该看到 CPU 使用率接近或为零。从这里，我还可以点击 Time Profile 以在 Instruments 中分析我的 App，并查看分析时段内的热状态、CPU 使用率和活跃调用栈。我还可以使用位置能量模型（Location Energy Model）来测量 Core Location 的影响，并确保我的 App 在不该使用定位时没有在使用。有时，我的 App 的 beta 版或已发布版本中可能存在一个 bug，在办公桌上很难复现，或者需要更多的日志记录和上下文来调试。MetricKit 在设备上作为一个一体化的性能遥测框架运行，可以帮助我缩小根本原因的范围，并为我的客户遇到的问题提供宝贵的见解。要使用 MetricKit，我只需在我的 App 中添加并实现一个名为 AppMetrics 的自定义类，并使这个新类遵守 MXMetricManagerSubscriber 协议。

然后我可以将对自定义类的引用添加到管理器。并在 deinit 中移除对自定义类的引用，这是一个推荐的最佳实践。

我可以在相应的 didReceive 方法中处理这些数据。如果策略性地操作，我可以将许多在 Organizer 中找到的相同数据（如能量日志和 CPU 指标）与 MetricKit 中关于问题发生时可能出了什么差错的上下文数据相结合。感谢我们的设备端分析管道，你无需额外工作即可获得这些数据的简单版本。当用户使用你的 App 时，我们会收集来自同意用户的设备上的性能数据。这些数据随后在我们的服务器上聚合，并通过我们的众多工具之一（如 Xcode Organizer）发送回给你。访问 Xcode Organizer 以查看已在 App Store 中的 App 版本的性能数据非常简单，只需在 Xcode 打开时导航到菜单栏（menu bar），转到窗口，然后点击 Organizer 启动即可。

进入后，我可以点击电池用量指标，查看我的 App 在过去 16 个版本中的汇总数据，以及图表右侧按主要子组件的详细分类。

如果我的 App 最新版本出现重大性能衰退（regression），只要版本出现在 Organizer 中，我导航到回归（Regression）窗格（Xcode 13 中的新功能）后就能立即知道。这个新的回归窗格会隔离出我 App 最新版本中显著增加的所有指标，这样我就可以在一个地方看到所有需要关注的内容。为了确定我 App 的哪些区域导致了问题，我还可以使用报告（Reports）下的能量 Organizer（Energy Organizer）来查看从同意的用户设备收集的高 CPU 使用率和日志。这提供了对 App 内情况的更详细查看。我还可以通过查询 App Store Connect API 并对返回的 JSON 载荷运行我自己的分析来获取所有这些数据。所有这些工具都将使我能够轻松发现并解决 App 中的大部分电池用量衰退。要了解有关电池续航优化的更多信息，请查看 2019 年的“Improving Battery Life and Performance”讲座，要了解有关使用 Instruments 的更多信息，请查看今年的“Analyze HTTP Traffic in Instruments”讲座。我们的下一站是挂起率（Hang Rate）和滚动，这两个指标表明我的 App 没有响应。挂起（hang）是指 App 对用户输入或操作无响应至少 250 毫秒。App 中的挂起可能会导致用户从 App 切换器中强制退出应用，是用户在你的 App 中体验的主要障碍，应该优先处理。

滚动卡顿（stuttering scrolls）发生在下一帧屏幕刷新时新内容尚未准备好的情况下。这会导致不愉快的用户体验和整体的挫败感，导致用户在 App 上花费的时间减少。作为 App 开发者，目标是最大化用户参与度，所以这是一个开始优化的好地方。

还记得我们之前展示的流畅滚动吗？以此为目标是符合你用户最大利益的。我可以通过导航到 Xcode Organizer 中各自的视图来跟踪挂起和滚动指标。如果我发现任一图表呈上升趋势，或者就滚动而言，我发现图表显示的是更多黄色和红色条，而不是绿色条（就像这里的图表一样），这就是一个信号，表明我需要注意我的 App 在做什么。根据图表右侧的图例，红色条代表我们在之前的视频中看到的糟糕滚动体验，应该立即修复。这些数据现在也可以通过 App Store Connect API 获取。我可以使用 Instruments 通过线程状态（Thread State）或系统调用回溯（System Call Trace）来检测挂起的原因。线程状态回溯（Thread State Trace）仪器显示了线程状态的时间轴以及操作系统何时调度该线程运行。我可以在详细信息部分看到线程被阻塞了多长时间。

系统调用回溯（System Call Trace）显示了一个叙述，详细说明了进入的系统调用以及它们花费了多长时间。为了验证我没有发布带有影响用户滚动体验的 bug 的 App 版本，我可以使用 XCTest 编写一个性能测试，该测试启动并通过我的 App 进行滚动。在这个测试中，我指定我想测量 scrollDeceleration 子指标，并在 measure block 的主体中，以我期望的 App 内滚动速度向上滑动。由于这个 measure block 默认运行五次，我使用 XCTMeasureOptions 在运行之间重置应用状态。我可以将其传递给我的 measure block，停止测量，然后重置我的应用状态。有时，在强制测试用例中重现响应性问题可能并不容易。幸运的是，MetricKit 如果部署在我的生产应用中，可以让我在问题发生时收集遥测数据和诊断信息。对于挂起，在 iOS 14 中，MetricKit 会以 24 小时的节奏将这些诊断信息发送给我。在 iOS 15 和 macOS 12 的新特性中，我现在可以在问题发生后立即在我的 App 中收到所有诊断信息，包括挂起。将这些即时诊断与我自己的遥测数据结合使用，我可以快速找出根本原因并解决最紧迫的响应性问题。对于滚动卡顿，iOS 15 在 MetricKit 中引入了一个新 API，用于使用 MXSignpost 标记自定义动画。MXSignpost 是 MetricKit 附带的一个封装 API，允许我为遥测标记关键代码段。

使用 MXSignpostAnimation- IntervalBegin API，我将能够策略性地标记自定义动画的开始。使用 MXSignpost end API，我可以标记动画的结束，并在该间隔内收集卡顿率（hitch-rate）遥测数据。这两个函数不仅会捕获这个间隔的细粒度性能数据，还会捕获发生的任何卡顿。要了解更多关于如何理解和消除挂起的信息，我推荐查看今年的“Understand and Eliminate Hangs from your App”讲座。关于如何识别滚动卡顿问题的深入细节，我推荐查看 2020 年的“Eliminate Hitches Using XCTest”讲座和“Explore UI Animation Hitches and the Render Loop”技术讲座。我们现在接近中途了，接下来讨论磁盘写入。写入磁盘会磨损用户的 NAND，导致设备健康状况不佳。写入操作也很耗时，如果频繁进行，会导致糟糕的用户体验和慢速性能，因此批量处理这些写入操作很重要。

在发布我的 App 版本之前，我可以在 Instruments 中使用文件活动（File Activity）模板分析我的 App。这会以系统调用的形式记录文件系统使用情况，这样我就可以轻松地识别出我 App 代码中访问文件系统的位置。有许多方法可以成为系统的好公民并限制写入磁盘。一些常见做法包括批量进行写入操作、对频繁更改的数据使用 Core Data，以及避免快速创建和删除文件。除了分析我的 App，我还可以使用 XCTest 编写性能测试来衡量我的 App 的磁盘使用情况，以防止包含过多磁盘写入的代码在用户设备上运行。这就像将一个 XCTStorageMetric 实例传递给 measureWithMetric API，然后调用写入磁盘的代码一样简单。该测试测量 block 中代码写入磁盘的数据量，并在 Xcode 本身内向我显示结果。我可以设置期望写入磁盘的数据量的基线，以便如果 block 中的代码超过该值，测试就会失败。这将帮助我确保没有发布任何有 bug 的代码。

如果我已经发布了磁盘写入过高的 App 版本，我可以使用 Organizer 跟踪其在用户设备上的性能。磁盘写入指标向我显示了当前版本的 App 与之前发布的版本相比进行了多少次写入的趋势。图表中的峰值可能表明我的 App 存在导致大量写入的 bug。我应该确定这些写入的主要来源，理解它们，并寻找减少它们的方法。

我可以通过查看磁盘写入报告来寻找这些写入的来源。这些是在我的 App 在 24 小时内写入超过 1 GB 时生成的异常报告集合。堆栈回溯显示了我代码中在哪里进行了过多的写入，而 Xcode 13 中的新功能是，我还可以获得称为洞察（Insights）的额外详细信息，它可以指出一些简单的优化方法，让我成为系统的好公民，并减少 App 中的一些写入。所有这些数据现在也可以通过 App Store Connect API 获取。我还可以在它们发生时通过 MetricKit 在我的应用中获取这些报告。如果我正在使用 MetricKit 监控我的 App 的磁盘使用情况，我可以围绕关键的磁盘写入路径使用 MXSignpost 间隔来进行端点标记，以收集更细粒度的遥测数据，这有助于我发现优化的机会。要了解如何无缝识别和解决磁盘写入问题的更多信息，请务必收看今年的“Diagnose Power and Performance Regressions in your App”讲座。接近下一站时，我们将讨论启动时间和终止。启动时间是指从用户点击你的 App 图标到 App 中渲染出第一帧之间的时间。

如果你的用户花了很长时间等待你的 App 启动，这可能会给用户带来无意的挫败感，而过长的启动时间可能会导致系统终止你的 App。当系统终止你的 App 时，你的用户将从头开始体验整个启动流程，这比从后台运行状态恢复要花费更长的时间。

进程退出可能由多种不同的原因引起，例如达到并超过系统内存限制或启动超时。

每次你的 App 因这些原因之一而终止时，下次用户点击你的 App 图标时，它都会经历完整的启动流程，这不仅耗时，而且是一种令人沮丧的体验，尤其是当这种情况频繁发生时。

如果你没有恢复状态（state restoration），这也会增加用户的挫败感，因为他们必须重新找到自己的位置或重新创建丢失的工作。

我刚发布了一个新版本的 App，其中包含一项功能，允许用户为他们的餐食添加图片和详细的食谱。让我们看看有了这个新功能后我的 App 的启动时间是什么样，以及之前是什么样。

这就是用户现在尝试启动我拥有新功能 App 时会看到的情况。注意到尝试渲染第一帧花了多少时间吗？我的 App 在我们甚至有机会使用它之前就被挂起了。相比之下，这是添加该功能之前的启动情况。几乎就像我的 App 预见了启动并准备好了要显示的第一帧。从这两个例子中，我已经知道，我不希望用户想起我的 App 时记住的是第一个极其缓慢的启动。所以我需要尽快修复这个问题。由于启动问题已经在用户使用的 App 版本中，我可以从进入 Organizer 并查看启动时间和新的终止窗格开始。查看启动时间会让我了解我的 App 在过去 16 个版本中的平均“首次渲染时间”，这样我可以看到在添加新功能之前它的速度有多快。我还可以进入终止窗格，查看我的 App 因启动时间过长而被系统终止的频率。

在查看了 Organizer 之后，实际上看起来这是一个由我的新功能引入的相当糟糕的 bug，并且影响了很多用户。让我们看看如何着手修复它。我可以在办公桌上使用 Instruments 中的 App 启动（App Launch）模板来分析我的 App 的启动时间来测试这个问题。这个模板运行我的 App 五秒钟，在此期间它会收集时间分析（time profile）和线程状态回溯（Thread State Trace），记录 App 启动时发生的情况，这样我就可以找出线程被阻塞的原因并修复它。我还可以通过在使用类似我们之前看到的 measure block 中使用 XCTApplicationsLaunchMetric 来测量 XCT 性能测试中的启动时间。如果我想进行自己的分析，并且在我的 App 中实现了 MetricKit，我将默认收到作为每日指标载荷一部分的终止遥测数据。有关状态恢复（state restoration）的更多信息以避免 App 终止时数据丢失，请查看 2020 年的“Why is my App Getting Killed?”讲座。耶，我们做到了。在结束我们的旅程之前，我们到了最后一站。最后一站是内存。内存是 App、操作系统和内核之间的共享资源。如果你的 App 超过内存限制，它将被系统终止，下次用户启动它时，它将从头开始启动，这比从后台运行状态恢复要花费更长的时间。我的 App 中的新功能允许开发者为他们餐食添加图片和描述，这意味着内存使用可能会有点高。如果发生这种情况，我的 App 可能会因超过内存限制而被终止，所以我应该关注 Organizer 中的内存和终止指标，以确保不是这种情况。根据 Organizer 中的峰值内存和挂起时内存图表，它看起来并没有被终止，但在这个新版本的 App 中，内存使用出现了很大的峰值。

我可以通过在 Instruments 中使用泄漏（Leaks）、分配（Allocations）和 VM 跟踪器（VM Tracker）模板来分析我的 App 的内存使用情况。泄漏将检查我的进程的堆并检查泄漏的内存。分配将分析我的 App 的内存生命周期。而 VM 跟踪器将显示我的 App 随时间变化的虚拟内存空间。我还可以使用 MetricKit 获取相同的信息并对其进行自己的分析。除了使用包含终止和内存遥测数据的每日指标载荷外，我还可以围绕关键代码段使用 MXSignposts 进行检测，以捕获关于内存使用的更细粒度遥测数据。

要了解更多关于如何检测和理解如何在内存衰退进入你的应用之前解决它们的信息，请查看今年的“Detect and Diagnose Memory Issues”讲座。在让你离开之前，让我们总结一下今天看到的内容，并回顾一些后续步骤。我们理解识别性能优化有多么具有挑战性。在过去的几年里，开发者们使用了我们提供的这些相同工具来进行显著的性能优化。

一个很好的例子是 Snapchat，一款每天有数百万人使用的 App。Snapchat 长期致力于改善其 App 的启动体验并降低终止率。

在过去的一年里，我们看到 Snapchat 的不良终止减少了 99%。我们认为这非常了不起，使用我们今天讨论的性能工具和数据，你也可以做到这一点。

如果你对性能工具不熟悉，我推荐你花点时间看看 2020 年的“Diagnose Performance Issues with the Xcode Organizer”和“What's New in MetricKit”讲座，以及 2020 年的“Identify Trends with the Power and Performance API”讲座和 2019 年的“Getting Started with Instruments”讲座。在深入研究了所有这些指标和工具之后，我们希望你已经拥有了在 App Store 中发布性能最优 App 所需的所有资源。当你的用户享受无缝的用户体验时，他们会感谢你。这里涉及的材料很多，所以作为一个有趣的练习，我建议你使用 Xcode Organizer 查看你 App 性能的趋势数据。探索和尝试 Instruments 中提供的不同模板。挑战自己编写 XCTests 来在问题发布前捕获它们。并使用 MetricKit 扩展你的分析范围。

在优化性能方面，我们的工具提供了如此多的功能，所以不要犹豫，动手实践并探索它们附带的一切。感谢你加入我今天的旅程，希望你今年在大会上度过愉快的时光。[欢快的音乐]
