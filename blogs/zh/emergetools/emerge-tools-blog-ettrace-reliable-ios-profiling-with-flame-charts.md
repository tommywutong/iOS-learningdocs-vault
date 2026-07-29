---
title: 'Emerge Tools 博客 | ETTrace：基于火焰图的可靠 iOS 性能分析'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/ettrace-reliable-ios-profiling-with-flamecharts'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:7104c3cd072392bc'
translated: true
---

> 原文：[Emerge Tools 博客 | ETTrace: Reliable iOS Profiling With Flame Charts](https://www.emergetools.com/blog/posts/ettrace-reliable-ios-profiling-with-flamecharts)　·　Emerge Tools 博客

# ETTrace：基于火焰图的可靠 iOS 性能分析

2023 年 4 月 27 日，作者 [Noah Martin](https://twitter.com/sond813)

iOS 性能

![ETTrace 的宣传图徽标](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog14.2dec7363.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

测量 iOS App 的性能通常是通过性能分析来计算每个函数消耗的时间。通常你会使用 Xcode Instruments 中的 Time Profiler 来完成，但众所周知，它既慢又不可靠。

Emerge 提供了一款性能分析工具，作为[CI 中的性能测试](https://www.emergetools.com/product/performanceanalysis?utm_medium=blog&utm_source=emerge-tools&utm_campaign=ettrace)功能的一部分。该分析以火焰图（flame graph）的形式可视化，并且已被[证明](https://doordash.engineering/2023/01/31/how-we-reduced-our-ios-app-launch-time-by-60?utm_medium=blog&utm_source=emerge-tools&utm_campaign=ettrace)是一种了解 App 性能瓶颈并找到解决方案的简便方法。今天，我们推出一项新的使用方法，让你可以**完全在本地且以开源方式**使用同样出色的分析可视化效果。

![用于性能测试的 Emerge Tools 性能分析界面](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog14%2F1.gif&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

[ETTrace](https://github.com/emergeTools/ettrace?utm_medium=blog&utm_source=emerge-tools&utm_campaign=ettrace) 是一个用 Objective-C 编写的开源框架，并包含一个用 Swift 编写的 CLI，可完全在本地进行性能分析和可视化。它的设计目标是既简单又快速——只需将 framework 链接到你的 App，运行 `ettrace` 开始分析，然后停止即可立即看到你的火焰图。无需重启 App 或点击冗长的菜单来查看结果。

## [为什么我们需要一个新的分析器](https://www.emergetools.com/blog/posts/ettrace-reliable-ios-profiling-with-flamecharts#why-we-need-a-new-profiler)

Emerge 的性能分析旨在防止性能衰退（regression）被合并到你的代码库中。对于在 CI 中配置的特定场景，它能提供一致的结果。然而，在调试时，推到 CI 并不理想。你需要一种快速且本地化的工具。

ETTrace 让你能够轻松调试性能问题。如果你在使用 Emerge，那么当你准备好时，可以通过推送到 CI 来验证你的修复。此外，你可以探索 App 中的所有代码路径，而无需编写特定的测试。如果你使用 ETTrace 识别出性能关键路径，就可以将它们设置为在 CI 中进行监控。

你可能会想，为什么不直接用 Instruments 呢？虽然 Time Profiler 是 iOS 性能分析的当前最佳实践，但如果不具备性能方面的专业知识，使用起来会很困难（甚至对于性能专家也是如此）。部分原因在于其不够直观的可视化方式，同样也在于该工具本身笨重的特性。

在 Emerge，我和许多从事大型 App 的工程师交流过，反馈都如出一辙：Time Profiler 可能不稳定且缓慢。即使是为本文截图时，我也遇到了多次卡死，需要强制退出。符号化（symbolication）也经常出现问题，生成的跟踪信息只显示地址而不显示函数名。

ETTrace 以两种方式支持符号化。首先，如果你有 dSYM 文件，可以通过 `--dsyms` 参数直接提供给工具。其次，对于模拟器构建，ETTrace 会自动使用 App 二进制文件中的符号表进行符号化。由于该工具是开源的，如果你在符号化方面遇到任何问题，调试起来也很容易——这与 Instruments 形成对比。

![Instruments 与 ETTrace 对比](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog14%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [采样是如何工作的](https://www.emergetools.com/blog/posts/ettrace-reliable-ios-profiling-with-flamecharts#how-sampling-works)

ETTrace 是一个基于采样的分析器，意味着它以固定的时间间隔记录堆栈（stack）来构建可视化。采样仅针对主线程（main thread），而这正是用户通常会遇到性能问题（例如挂起（hang））的地方。采样在一个后台线程上大致像这样进行：

```objectivec
sStackRecordingThread = [[NSThread alloc] initWithBlock:^{
  NSThread *thread = [NSThread currentThread];
  while (!thread.cancelled) {
      [self recordStack];
      usleep(4500);
  }
}];
```

每次记录包含堆栈中观察到的地址列表以及当前时间戳。地址在跟踪记录完成后进行符号化，然后聚合符号化后的版本。任何两个堆栈之间的最大时间间隔应为 5ms（考虑到 `usleep` 可能比我们指定的时间多出 0.5ms）。为确保跟踪的准确性，任何超出此时间的额外时间都会被累积并报告为 `<unattributed>`。

这种可视化在技术上称为火焰图表（flame chart），意味着节点按时间在 x 轴上排序。它遵循以下数据结构：

```swift
struct FlameChartNode {
let name: String
let duration: Double
let children: [FlameChartNode]
}
```

由 Emerge 性能测试生成的可视化是火焰图，其中堆栈在每个层级按名称聚合。每个节点没有特定的开始/结束时间，因为它们没有排序，只在 x 轴上有一个持续时间。数据结构如下所示：

```swift
struct FlameGraphNode {
let duration: Double
// Children is keyed by node name
let children: [String: FlameGraphNode]
}
```

由于 ETTrace 只可视化 App 的一次单独的跟踪记录（而非多次跟踪的平均值），因此数据是火焰图表，这可能更易于调试。ETTrace 还有一个差异性分析（diffing）功能，你可以上传两次跟踪记录并比较它们，以查看某个函数是改进了还是衰退了。当使用此功能时，可视化将是一个火焰图。

## [理解协议一致性](https://www.emergetools.com/blog/posts/ettrace-reliable-ios-profiling-with-flamecharts#understanding-protocol-conformances)

作为一个使用 ETTrace 的案例研究，让我们看看如何分析协议一致性（protocol conformance）对 App 启动的影响。我们将以开源的 Mastodon App 为例，但会进行修改以包含更多的协议一致性。通常你会先启动 App 再使用 ETTrace，但为了直接从启动开始分析，我们需要在 Info.plist 中添加键 `ETTraceRunAtStartup` 并将其值设为 `YES`。

现在，我们可以启动与 ETTrace.framework 链接的 App，并开始性能分析！在通过 Xcode 安装之前，请确保从手机上删除该 App。然后，安装但不启动 App。最后，在命令行运行 `ettrace` 并根据提示操作，包括从主屏幕手动启动 App。生成的火焰图显示，在协议一致性上花费了大量时间：超过 60ms！

![ETTrace 中缓慢的协议一致性](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog14%2F3.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

接下来，尝试第二次启动同一个 App，并运行 `ettrace` 来获取跟踪记录。这一次，一致性查找非常快，ETTrace 甚至没有采样到它们！通过选择这两次跟踪记录，你可以使用差异性火焰图来确认速度变慢的原因。

![差异火焰图显示首次启动与后续启动的差异](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog14%2F4.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

这表明，在 iOS 16 中，协议一致性在 App 首次启动时（包括安装更新后）仍然使用慢路径，而在后续启动中则非常快。然而，其他类型的协议一致性检查，例如当 `as?` 操作的结果为 `nil` 时，仍然可能[非常慢](https://www.emergetools.com/blog/posts/how-order-files-speed-up-protocols?utm_medium=blog&utm_source=emerge-tools&utm_campaign=ettrace)。在你的 App 本地运行 ETTrace 可以帮助识别是否存在这些情况。

## [在 CI 中自动化](https://www.emergetools.com/blog/posts/ettrace-reliable-ios-profiling-with-flamecharts#automate-in-ci)

使用 ETTrace 进行本地性能调试只是性能优化工作流程的一部分。你需要一个快速的迭代周期来评估新想法，而持续的测试和告警则提供了额外的安全网，以防止问题被引入生产环境，并确认你在本地测量的结果。Emerge 提供了[性能测试功能](https://www.emergetools.com/product/performanceanalysis?utm_medium=blog&utm_source=emerge-tools&utm_campaign=ettrace)来完成这项工作。将 ETTrace 的本地性能调试与 Emerge 的性能分析结合使用，为开发者带来了统一的性能工作流程，并使 App 性能持续改善。如果你对这些工具有更多兴趣，欢迎[联系我们](https://www.emergetools.com/cdn-cgi/l/email-protection#97e4e2e7e7f8e5e3d7f2faf2e5f0f2e3f8f8fbe4b9f4f8faa8e2e3fac8faf2f3fee2faaaf5fbf8f0b1f6fae7ace2e3fac8e4f8e2e5f4f2aaf2faf2e5f0f2bae3f8f8fbe4b1f6fae7ace2e3fac8f4f6fae7f6fef0f9aaf2e3e3e5f6f4f2)，如果你对 ETTrace 有任何反馈，请[在 Github 上提交 issue](https://github.com/EmergeTools/ETTrace/issues?utm_medium=blog&utm_source=emerge-tools&utm_campaign=ettrace)！

---

感谢 [Itay Brenner](https://github.com/Itaybre?utm_medium=blog&utm_source=emerge-tools&utm_campaign=ettrace) 在这个项目上的工作，以及 [Filip Busic](https://twitter.com/__unused?utm_medium=blog&utm_source=emerge-tools&utm_campaign=ettrace)、[Miguel Jimenez](https://twitter.com/miguel_jimemigu?utm_medium=blog&utm_source=emerge-tools&utm_campaign=ettrace) 和 [Keith Smiley](https://github.com/keith?utm_medium=blog&utm_source=emerge-tools&utm_campaign=ettrace) 在早期对工具进行测试并提供反馈！
