---
title: 认识全新的 MetricKit
session_id: 222
collection: wwdc2026
year: 2026
duration: '17:43'
topics: [Developer Tools, System Services]
group: G · 调试、崩溃与 Instruments
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2026/222/'
content_hash: 'sha256:ecfa1db58d08d573'
translated: true
---

# 认识全新的 MetricKit

<sub>WWDC2026 · 17:43 · Developer Tools、System Services</sub>

更快地发现并修复性能问题。来和我们一起探索 MetricKit 如何为你提供关键的性能指标以及……

> [!note] 归档理由
> MetricKit 最新形态

## 章节

- [简介](/videos/play/wwdc2026/222/?time=1)
- [指标](/videos/play/wwdc2026/222/?time=247)
- [诊断](/videos/play/wwdc2026/222/?time=433)
- [上下文](/videos/play/wwdc2026/222/?time=603)

## 相关资源

- [简介](https://developer.apple.com/videos/play/wwdc2026/222/?time=1)
- [指标](https://developer.apple.com/videos/play/wwdc2026/222/?time=247)
- [诊断](https://developer.apple.com/videos/play/wwdc2026/222/?time=433)
- [上下文](https://developer.apple.com/videos/play/wwdc2026/222/?time=603)
- [StateReporting 入门](https://developer.apple.com/documentation/StateReporting/getting-started-with-statereporting)
- [使用 MetricKit 分析 App 性能](https://developer.apple.com/documentation/MetricKit/analyzing-app-performance-with-metrickit)
- [使用 MetricKit 监控 App 性能](https://developer.apple.com/documentation/MetricKit/monitoring-app-performance-with-metrickit)
- [使用 MetricKit 按 App 状态追踪性能](https://developer.apple.com/documentation/MetricKit/track-performance-by-app-state-using-metrickit)
- [MetricKit](https://developer.apple.com/documentation/MetricKit)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2026/222/4/86b76599-f095-4bd8-8004-f1dbd1bacb84/downloads/wwdc2026-222_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2026/222/4/86b76599-f095-4bd8-8004-f1dbd1bacb84/downloads/wwdc2026-222_sd.mp4?dl=1)
- [查找并修复 Metal 游戏中的性能问题](https://developer.apple.com/videos/play/wwdc2026/388)
- [分析、修复和验证：使用 Instruments 改善 App 响应能力](https://developer.apple.com/videos/play/wwdc2026/268)
- [从 MetricKit 接收指标](https://developer.apple.com/videos/play/wwdc2026/222/?time=299)
- [将指标发送至服务器](https://developer.apple.com/videos/play/wwdc2026/222/?time=325)
- [访问你的性能指标](https://developer.apple.com/videos/play/wwdc2026/222/?time=344)
- [接收诊断](https://developer.apple.com/videos/play/wwdc2026/222/?time=539)
- [将诊断数据发送至服务器](https://developer.apple.com/videos/play/wwdc2026/222/?time=554)
- [访问诊断数据](https://developer.apple.com/videos/play/wwdc2026/222/?time=579)
- [接收带有状态的 MetricKit 数据](https://developer.apple.com/videos/play/wwdc2026/222/?time=837)
- [定义自定义结构化类型](https://developer.apple.com/videos/play/wwdc2026/222/?time=861)
- [将编码后的指标报告发送至服务器](https://developer.apple.com/videos/play/wwdc2026/222/?time=929)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我是 Yonni，MetricKit 团队的一名工程师。优秀的 App 和游戏会在真实世界、真实设备上监控和优化它们的性能。MetricKit 这个框架能够为你提供关于 App 用户体验质量的真实洞察。在本讲座中，我将首先介绍 MetricKit，包括 iOS 27 中的新功能。

然后，我会展示如何开始接收你的第一份指标报告。

你的第一份诊断报告。最后，我将探讨如何通过将性能问题关联到 App 的特定区域来获取更丰富的数据。

我先从框架的概述开始。

优化 App 性能是一个持续的过程。你从收集数据开始，分析它以识别问题。对于每个问题，你进行分类以找出根本原因，修复它，然后回到第一步来监控结果。MetricKit 在这个工作流程中承担收集的环节。

该框架提供两类数据：指标（metrics）和诊断（diagnostics）。指标让你了解某个性能领域整体是在改善还是恶化，而诊断则告诉你具体是哪个代码路径导致了性能问题。

在 iOS 27 中，该框架被完全重建，拥有一个上下文丰富且表现力强的新式现代 Swift 优先 API。

全新的 MetricKit API 是框架的未来。我今天要讨论的所有进步都专属于这套新的 API。指标是你 App 持续的健康信号。

启动时间、挂起（hang）时间和动画指标告诉你 App 的响应性和流畅度。缓慢的启动可能会让用户感到沮丧并离开你的 App，而快速启动则能让用户立即进入 App 的核心体验。

资源消耗指标，如 CPU、GPU、磁盘写入和网络传输，则告诉你 App 的工作强度以及对设备健康的影响。

例如，MetricKit 的启动时间（如首次绘制时间指标）提供了一个直方图，显示了落在特定时间范围桶内的启动次数。这个图表显示了每次用户在一天中打开 App 时，App 启动所需的时间。

大多数启动耗时在 510 到 540 毫秒之间，但也有一些离群值。

你也可以通过从 MetricKit 提供的数据中得出自己的见解来追踪持续的性能表现。

例如，MetricKit 报告显示，该 App 在使用 30 分钟期间，平均总挂起时间为 3 秒。这些信息可以用来推导出平均挂起率，即每小时 6 秒。

如果你将所有设备上的这些数据汇总，就能得到一个可衡量的信号，了解 App 性能的变化趋势。

在 iOS 27 中，MetricKit 可以提供作为 App 状态函数（function of the app's state）的每个指标。

例如，在测量一个有多个标签页的 App 中的挂起时间时，MetricKit 可以提供该指标与当前活跃标签页是标签 1、标签 2 还是标签 3 的交叉数据。稍后我将更详细地介绍这一点。在 iOS 27 中，MetricKit 现在也提供了一个新指标——Metal 帧率（Metal frame rate）。帧率是游戏开发者理解渲染性能的关键指标。要了解更多关于优化你的游戏以适配平台的信息，请观看讲座“查找并修复 Metal 游戏中的性能问题”。

除了指标，MetricKit 还提供诊断。诊断包含有用的信息，能帮你识别是哪个代码路径导致了性能问题，以便进行调查和修复。

在 iOS 27 中，MetricKit 提供了内存异常诊断。因此，当你的 App 或扩展因超出内存限制而被终止时，你可以更深入地了解发生了什么。

下面我将深入探讨你的 App 如何获取性能指标。

随着用户全天使用你的 App，MetricKit 会持续收集指标，如 App 启动、挂起、内存和 CPU 使用情况，并在每日报告中将其发送给你的 App。

在这份报告中，MetricKit 提供了一项覆盖 App 全天使用情况的条目。它还会为更小的时间段提供单独的条目，通常每个条目对应几个小时。这些较小的条目仅在存在与之相关的指标时才出现。以下是数据的组织结构。在每个时间间隔内，指标被组织成指标组（metric groups）。每个组代表系统的一个方面，比如 `.cpu`、`.memory`、`.display` 和 `.gpu`。在一个组内，你可以找到各个性能指标。

我将通过代码来讲解。

你的入口点是 MetricManager 类。要接收报告，你需要通过 metricReports 属性来等待它们。

这个设置应该在 App 启动时完成，以避免因延迟订阅而导致数据丢失。MetricManager 应该保持存活，这样当后续数据就绪时，数据流才能继续传递报告。

只需这几行代码，你的 App 现在就能接收结构化的指标数据了。

通常，你可能希望将这些指标发送到服务器，以便检查你的 App 在众多设备上的健康状况。MetricReports 是符合 Codable 协议的，这使得将它们编码成 JSON 等格式以便发送到服务器变得很容易。

只需创建一个 JSONEncoder 并编码整个报告即可。

如果你只想访问特定的指标组或特定的值，你也可以进一步检查指标报告。为此，请遍历你的 intervalEntries。这包括一个全天汇总的条目，以及在可用情况下的更小时间段窗口。然后，将指标过滤到你感兴趣的组。在这种情况下，memoryMetrics 只包含内存组中的指标。

最后，对 metric 的 case 进行切换，以访问你感兴趣的指标类型以及该指标在此报告中的值。在这个例子中，代码只处理了 peakMemory 值。请在 App 启动后立即在一个 detached task 或专用的 service 类中执行此工作。

回到工作流程。现在你已经完成了收集阶段，准备好进入分析了。

跨所有设备分析指标是一个数据科学问题。为了实现这种分析，你需要建立一个服务器来接收这些报告，并按照你关心的维度进行聚合。

你需要为想要生成的数据和想要发现的见解确定最佳的统计分析方案。

使用你的自定义聚合分析，你可以获得一个基线，了解你的 App 目前的性能表现。然后，监控你的聚合指标，以检测情况是在变好还是变坏。

我已经展示了如何使用指标来发现 App 中的问题。现在，我将介绍如何使用诊断来解决这些问题。

指标是监控 App 的好方法。在你随着时间的推移收集指标并监控性能时，你可以进入工作流程中的分类阶段。诊断在这个阶段尤其有帮助。

当出现问题时，比如崩溃或挂起，系统会在设备上捕获一个诊断。诊断报告会打包详细信息，并通过 MetricKit 立即将其传递给你的 App。

在里面，你可以获得有用的信息来对问题进行分类。例如，许多诊断包括回溯（backtrace），它们会显示事件发生时的确切调用栈。

最重要的诊断之一是针对崩溃的。崩溃诊断不仅提供回溯，还会指出你的 App 被终止的原因以及一个异常类型，告诉你是什么类型的失败。

在 iOS 27 中，终止类别（termination category）现在表明了每个崩溃在指标中是如何被记录的。

这样，如果异常终止的趋势上升，你可以直接将它们与各个诊断关联起来。

在这个例子中，符号化后的回溯从系统的线程（thread）开始。随着执行流向下，它会进入 App 的代码。要找到崩溃点，你可以一直沿着调用往下追。这里，执行到达了 App 的 `submitReport()` 函数并停止了。这表明这是执行路径中的失败点。

现在，你可以使用这个信息来定位该函数的修复。

要获取诊断报告，你需要等待你的 MetricManager 实例上的 diagnosticReports。像 MetricReports 一样，在 App 启动后立即在一个 detached task 或专用的 service 类中开始监听这个数据流。

就像 MetricReports 一样，DiagnosticReports 也是符合 Codable 的。这段代码等待传入的 diagnosticReports，然后使用 JSONEncoder 将它们编码成 JSON。

现在，你可以将所有诊断信息发送到你的分析服务器。

诊断报告也是结构化的，所以你可以选择接收什么。例如，这段代码等待 diagnosticReports，并对不同类型的诊断进行 case 切换。在遇到崩溃诊断时，它会提取回溯、原因和类别。现在，这些信息可以被 App 处理，比如发送到服务器。在遇到挂起诊断时，它可以使用 hang case 来以不同方式处理该报告。

我已经介绍了如何为你的 App 获取指标和诊断报告。接下来，我将向你展示如何将这些数据上下文化。

到目前为止，MetricKit 提供的指标和诊断代表了 App 性能的整体情况。但是，为了调查个别问题，你可能需要更丰富、更细粒度的数据，以了解 App 的更多状态信息，比如用户流程是什么，或者 App 是如何配置的。MetricKit 可以为你提供与你自己定义的关于 App 的重要信息相关联的上下文数据。

这里有一个例子。我有一个费用报告 App，允许员工扫描收据、提交费用，并通过分类（categories）和预算（budgets）追踪他们的支出。这些功能被组织在“报告”标签页和“支出”标签页中。

我对滚动卡顿（scroll hitch）指标感兴趣。它表明在这一天中，App 在滚动 5 分钟的时间里，总卡顿时长为 4.5秒。这意味着卡顿率为每秒 15 毫秒。但这只是所有 App 使用情况下的平均滚动卡顿率，即使有人在“报告”标签页和“支出”标签页之间来回切换也是如此。要知道这个指标是在 App 的什么条件下被收集的，你可以通过 StateReporting 框架来报告 App 状态。我现在就探讨这一点。

状态是你定义的描述 App 配置或行为的信息，这样 MetricKit 就可以根据这些特征来聚合指标。当人们使用你的 App 时，参数可能会根据他们的使用方式而变化。

在费用 App 中，人们可能会在使用过程中在不同的标签页之间移动。他们可能先进入“报告”标签页添加一个新费用，然后离开 App，回来时又到了“支出”标签页检查每日餐食预算。当 App 在这些状态之间过渡时，它会报告这些过渡。然后，MetricKit 可以将它们与指标和诊断数据交叉关联。

你还可以通过添加自定义结构化类型来为每个状态添加更多细节。对于费用 App，这可能是视图中项目的详细信息，比如交易列表被视为小、中还是大列表，以及该列表上的交易是否已排序。

现在，你不会得到一个跨越所有这些状态的单一混合指标（例如总的滚动卡顿率 15 ms/s），而是会为每个独立状态报告指标。在这个费用 App 中，每个标签页都有各自的指标。在这个例子中，在“支出”标签页上滚动非常流畅，卡顿率仅为 1 ms/s。但是，当在“报告”标签页上滚动时，卡顿率飙升到了 71 ms/s。有了这种粒度，你可以得出一个更有针对性的结论：“支出”标签页表现非常好！但“报告”标签页正经历严重的卡顿，而这正是你优化工作应该聚焦的地方。

你提供的每个状态都限定在一个域（domain）中。域描述了 App 的一个功能或区域。在给定时间内，一个域只能有一个活跃状态。

独立的域允许多个状态同时进行。在费用 App 中，我正测试一个实验性的变更，想知道它是否对性能有帮助。当实验打开时，费用会从数据库中以小批量获取。关闭时，则使用更大的批量。通过将标签页状态和批量大小状态放在不同的域中，MetricKit 将为每个标签页和每个批量大小分别提供指标。

状态遵循一个过渡模型。你的 App 报告它正在转向的状态，MetricKit 会追踪它在该状态下停留了多长时间。没有开始或结束配对——App 在任何给定时间报告它所处的状况。

要在你的 App 中报告状态，首先导入 StateReporting 框架。然后，创建一个域（通常是一个反向 DNS 字符串），并在设置 MetricManager 实例时注册它。

最后，当你的 App 进入你定义的状态时，报告这些过渡。在这个例子中，App 过渡到由字符串 "Reports" 标识的状态。

如果你想进一步细化你的数据，可以通过使用 ReportableMetadata 宏定义你自己的结构体，来为这些状态提供额外的结构化信息。然后，使用这个元数据类型创建一个新的 StateReporter。

最后，通过包含标签和你的自定义类型来报告过渡。这个例子过渡到了 "Reports" 状态，并提供了一个 ViewConfiguration 结构体，其中包含 listSize 的值以及该列表中的项目是否已排序。

在向你的 App 添加状态之前，你的指标报告会提供跨所有 App 使用的宽泛指标。stateEntries 属性包含感知状态的指标。当没有报告任何状态时，该属性为空。添加状态后，你的 MetricReport 现在将拥有 StateEntry 值。状态条目提供了另一种理解 App 指标的方式。每个状态都有自己的 StateEntry，其指标值是在该状态所持续的时间段内聚合的。当你准备将此数据发送到分析服务器时，你可以选择按状态报告域对 MetricReport 数据进行分组。配置你的 JSONEncoder，使状态条目按每个域分组。将编码器的 userInfo 属性上的 key `encodingFormatKey` 设置为值 `byStateReportingDomain`。现在，当报告被编码时，状态条目和间隔条目都将包含你的 App 的性能指标，并按报告中存在的每个域和状态进行分组。

以下是定义状态时需要注意的一些最佳实践。

域的范围应该狭窄，这样每个 App 区域都可以有自己的状态，并能够理解这些状态的数据。

状态过渡应该代表稳定、有意义的阶段，而不是短暂的 UI 事件。

仔细考虑每个状态的含义，这样如果出现性能衰退（regression），该状态将提供足够的信息来定位修复。仔细规划 App 中的状态转换数量以及你打算如何解释每个状态和域生成的数据。过多的状态可能会导致数据过于细粒度，实际上可能使解释整体情况变得更加困难。为了最小化开销，状态数量也有上限。

最后，在发布之前，使用兴趣点（Points of Interest）工具来验证你报告的状态是否符合预期。

MetricKit 让你比以往更快地发现和修复性能问题。持续监控数据，以定位和规划你的性能工作。

使用 MetricManager 开始收集性能指标，以监控 App 的健康状况。

分析诊断以找出具体的改进机会。

通过报告 App 的重要状态来将你获得的数据上下文化。

探索 MetricKit 提供的新数据类型，如内存诊断和 Metal 帧率指标。

最后，如果你正在使用 MXMetricManager API，请迁移到新的 MetricManager API，以利用所有这些新能力。谢谢，祝你 WWDC 愉快！
