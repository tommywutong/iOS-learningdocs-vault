---
title: 使用 XCTest 消除动画卡顿
session_id: 10077
collection: wwdc2020
year: 2020
duration: '13:45'
topics: [Developer Tools]
group: D · 响应性、hang/hitch 与渲染循环（RunLoop 的现代替身）
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10077/'
content_hash: 'sha256:a7baa8aee390a78f'
translated: true
---

# 使用 XCTest 消除动画卡顿

<sub>WWDC2020 · 13:45 · Developer Tools</sub>

动画可以显著提升 App 的用户体验，带来直接操作的感受，并帮助用户更好地……

> [!note] 归档理由
> 用 XCTest 把动画卡顿变成可回归的指标

## 相关资源

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10077/2/B3286370-EF32-46C5-AF96-8EF51A8EB971/wwdc2020_10077_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10077/2/B3286370-EF32-46C5-AF96-8EF51A8EB971/wwdc2020_10077_sd.mp4?dl=1)
- [Ultimate application performance survival guide](https://developer.apple.com/videos/play/wwdc2021/10181)
- [Diagnose performance issues with the Xcode Organizer](https://developer.apple.com/videos/play/wwdc2020/10076)
- [Handle interruptions and alerts in UI tests](https://developer.apple.com/videos/play/wwdc2020/10220)
- [Identify trends with the Power and Performance API](https://developer.apple.com/videos/play/wwdc2020/10057)
- [Triage test failures with XCTIssue](https://developer.apple.com/videos/play/wwdc2020/10687)
- [What's new in MetricKit](https://developer.apple.com/videos/play/wwdc2020/10081)
- [XCTSkip your tests](https://developer.apple.com/videos/play/wwdc2020/10164)
- [Create an animation os_signpost interval](https://developer.apple.com/videos/play/wwdc2020/10077/?time=395)
- [Use a UIKit instrumented animation os_signpost interval](https://developer.apple.com/videos/play/wwdc2020/10077/?time=415)
- [Measure scrolling animation performance using a Performance XCTest](https://developer.apple.com/videos/play/wwdc2020/10077/?time=432)
- [Reset the application state between runs](https://developer.apple.com/videos/play/wwdc2020/10077/?time=482)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。

大家好。我叫 Tanuja Mohan，是 Apple Power and Performance 团队的一名软件工程师。动画是我们 App 用户体验的重要组成部分。动画可以是微妙的，比如当我们点击返回按钮从一屏导航到另一屏时；也可以是手势的主要焦点，比如当我们在 App 中向上或向下滚动时。我们希望这些手势能产生平滑的响应，因为当导航耗时过长或滚动出现抖动时，用户会明显察觉。

我们将这些用户可感知的抖动称为“卡顿（hitch）”。任何一帧晚于预期时间出现在屏幕上，都属于卡顿。这会分散用户的注意力，并损害用户对你的 App 品质的感知。让我们放大观察 App 的各个帧，看看实际情况。前三帧都按预期显示。列表在逐渐移动，完美地跟随我们手指的移动。

但随后，第三帧停留在屏幕上。App 似乎不再跟踪你手指的移动。

然后，当第四帧显示到屏幕上时，列表突然大幅跳跃，回到了你手指的位置。这不是我们期望的，也是我们希望避免的。要理解这里发生了什么，我们首先需要了解帧是如何显示到屏幕上的。在 iPhone 和 iPad 上，帧通常预期以 60 Hz 的频率更新，每帧的节奏为 16.67 毫秒。在 iPad Pro 上，我们可以预期 120 Hz 的更新，节奏为 8.33 毫秒。这个节奏由 VSYNC 表示，即屏幕决定是否将帧交换到显示器上的时机。当帧错过了它预期的 VSYNC 时，我们就看到了卡顿。卡顿的严重程度由该帧延迟出现在屏幕上的时间量来衡量。

在这个例子中，第四帧延迟了 16.67 毫秒。

我们可以用两种方式来量化卡顿。

卡顿时长（hitch time）是指一帧延迟显示到屏幕上的时间，以毫秒为单位。我们更倾向于用卡顿率（hitch ratio），即每秒钟的毫秒数，它是总的卡顿时长（毫秒）除以某个其他时长（秒）。例如，除以一次测试的时长。这听起来很复杂。为什么我们不说“掉帧（dropped frames）”并测量“每秒帧数（frames per second）”呢？每秒帧数是一个绝对目标，很容易被扭曲。如果你的测试在动画执行期间包含任何静止时间，那么 fps 就没有意义了，因为我们在静止期间本来就不期望有任何帧被交换。

而且，我们常常有意不追求最高的 fps。也许一个游戏只想以 30 fps 运行，或者一个视频以 24 fps 运行。出于功耗和性能的考虑，时钟 App 图标上的指针只以 10 fps 运行。

即使考虑这些因素，卡顿时长的目标始终是零，并且是可靠的。但卡顿时长并不总是可比较的。一秒测试的总卡顿时长不能与十秒测试的总卡顿时长相比较。

通过将卡顿率归一化为每秒钟测试时长的卡顿时长毫秒数，我们得到了一个既可以在不同测试间进行比较，又可以作为最终用户影响近似值的指标。关于最终用户影响，以下是我们推荐并在工具中使用的目标卡顿率。

卡顿率低于每秒 5 毫秒是良好的用户体验。在每秒 5 到 10 毫秒的范围内，用户将开始注意到卡顿，这些卡顿需要被调查。

卡顿率达到每秒 10 毫秒或更高时，卡顿对用户来说相当分散注意力，我们应该立即采取措施来解决它们。在 iOS 14 中，你可以使用我们的一套工具在开发和发布工作流程中跟踪卡顿。XCTest 框架允许你直接在单元测试和 UI 测试中收集卡顿和动画数据，而 MetricKit 和 Xcode Organizer 则让你可以访问来自用户的性能指标。在本环节中，我们将重点介绍使用 Performance XCTest 捕捉卡顿的开发工作流程。如果你想了解如何在发布工作流程中查看卡顿，请查看今年 WWDC 2020 上我们关于 MetricKit 和 Xcode Organizer 的独立讲座。在 Xcode 11 中，我们引入了 XCTMetrics。这些指标指定了你想在测试中测量系统的哪个部分。我们今天可用的 XCTMetrics 允许你测试时钟时间、CPU 利用率、内存使用、os_signposts、存储，并且在 Xcode 12 中，我们有一个单独的指标来测量 App 启动时间。我们还有一个模板供你编写自己的自定义指标。

在本讲座中，我们将重点介绍 XCTOSSignpostMetric，它是用于执行动画性能测试的 XCTMetric。

从 Xcode 11 开始，你可以使用 XCTOSSignpostMetric 来测量 os_signpost 间隔的持续时间。现在，在 Xcode 12 中，当使用动画 os_signpost 间隔时，你不仅会收到持续时间，还会收到三个与卡顿相关的指标、帧率和帧数。

你可能已经熟悉帧率和帧数。这两个值分别测量显示到屏幕上的帧的频率和数量。

现在你也熟悉了卡顿。你现在可以跟踪在测试的代码块中发生了多少次卡顿、在测试中我们花费在卡顿上的总时长，以及这个总卡顿时长占被测量代码块时长的比率。

要收集这些指标，你首先需要检测你的代码以发出一个 os_signpost 间隔。有三种方法可以做到这一点，我们将它们称为非动画间隔——只返回持续时间的间隔，以及动画间隔——返回额外动画指标的间隔。在 Xcode 11 中，你只能使用“begin”和“end”接口来检测一个非动画 os_signpost 间隔。这只会返回持续时间。

现在，在 Xcode 12 中，要指定一个动画 os_signpost 间隔，你只需改用 animationBegin 接口即可。只需这一个更改，你就可以将你现有的任何检测转换为发出动画间隔，并接收前面提到的动画指标。

除了使用自定义间隔，你还可以使用 UIKit 预定义的检测间隔之一来测试导航过渡和滚动。这些是 XCTOSSignpostMetric 类上提供的子指标。让我们看一个使用这些子指标之一编写测试的例子。

这里我有一个 Performance XCTest，它将启动我的 App，点击“Meal Planner”单元格，并在 foodCollection 视图上向上滑动以向下滚动。

在这个测试中，我指定要测量 scrollDeceleration 子指标。

在 measure 块的主体中，我正在向上滑动，现在在 Xcode 12 中，你可以自定义滚动的速度。

这个测试到目前为止看起来不错，但我们可以做一些改进。请记住，默认情况下，measure 块会运行五次以收集性能测量值。这意味着在当前实现中，我们将连续向上滑动五次，并且很可能在每次迭代中滑动不同的内容。

为了避免这种情况，我们想要在每次运行之间重置 App 的状态。我们可以使用 XCTMeasureOptions 来让我们的 measure 块知道我们将手动停止测量收集。然后，将其传递到我们的 measure 块中，调用 stopMeasuring，然后重置我们的 App 状态。

现在我们编写好了测试，想要运行它。但在运行之前，我们首先想要修改测试 scheme 上的一些设置，以消除它们对我们性能测量的影响。我们首先想要确保为我们的 Performance XCTest 使用一个单独的测试 scheme。

然后，我们想要选择 release 构建配置并禁用调试器。

我们还想要禁用自动截图收集并关闭代码覆盖率。

最后，我们想要关闭所有诊断选项。这些是 Runtime Sanitization、Runtime API Checking 和 Memory Management 下列出的选项。

现在我们可以运行我们的 Performance XCTest 并在报告 UI 中查看结果。在下拉菜单中，我们可以看到我们新的动画指标。让我们选择卡顿率（Hitch Time Ratio）指标。

我们看到我们为五次迭代收集了测量值……

我们的卡顿率平均值为每秒 1.2 毫秒。

作为下一步，我们可以将这个平均值每秒 1.2 毫秒设置为我们的基线，这样将来任何运行这个测试的结果都会与这个基线值进行比较。

让我们看一个例子，看看你可能会如何在你的代码库中遇到卡顿，以及如何使用 Performance XCTest 防止它发布到用户手中。

假设我是一家支持在线点单和配送的膳食计划公司的 App 开发者。到目前为止，我已经实现了一个列出可用菜单项的视图。

作为下一步，我想通过包含不同菜肴样子的图片来使我的食物更具吸引力。在我开始编写这个新功能之前，我想测量我当前的动画性能，这样我就可以将其用作基线，以便在添加功能后进行对比。

我已经为我的性能测试设置了一个单独的测试 scheme，并按照我们之前讨论的配置好了设置。我现在可以编写我的测试了。

正如我们之前看到的，我将启动我的 App，点击“Meal Planner”单元格，并测量我的滚动动画性能。

我已经预先运行了这个测试，让我们看看我们的测量值。

看起来我们的卡顿为零，动画按预期执行。让我们继续添加我们的新功能。

首先，我将设置我的图像视图（image view）以包含我已预先包含在项目中的图片。

其次，我将缩放这些图片，使它们能很好地适应我的 App。

现在我们可以继续重新运行我们的性能测试。

请注意，当使用 XCTOSSignpostMetric 时，measure 块会监听你在代码块内何时发出检测的 os_signpost 间隔，并仅收集在此间隔内执行的代码的指标。另请注意，measure 块支持监听多个不同的 os_signpost 间隔。例如，你可以在同一段调用滑动手势的代码中同时监听 scrollDeceleration 和 scrollDragging 的 os_signpost 间隔。让我们快进到这个测试完成。

看起来我们的卡顿数量增加了，我们应该立即进行调查。

看来我们的问题出在这里的 scaleAspectFit 调用上。我们正在主线程（main thread）上重绘图像，而主线程负责渲染用户界面的其余部分。我们使用的是 CPU，它会创建新的像素并分配内存。

我们可以通过使用 Core Animation 的 setContentMode 来减少这种影响，它会将这些图像的重绘移交给 GPU。这使我们能够使用现有的图像像素，减少我们在主线程上的工作量。

我们可以再次运行我们的 Performance XCTest，看看这是否解决了问题。

我们可以确认，我们的动画指标现在报告回零卡顿，我们的性能恢复到了预期水平。

通过使用我们的 Performance XCTest，我们能够看到我们的新功能引起了性能衰退（regression），这给了我们修复它的机会，而现在我们的功能已经准备好交付给用户了。

让我们回顾一下我们讨论的内容。我们了解到，任何一帧晚于预期时间出现在屏幕上都属于卡顿。我们可以使用推荐的“良好”、“警告”和“严重”分类来量化这些卡顿。

然后我们了解到，我们可以在开发工作流程中使用 Performance XCTest 来捕捉卡顿。我们可以通过使用 UIKit 或自定义动画 os_signpost 间隔来做到这一点。我们还讨论了最佳实践，包括在迭代之间重置 App 内容以及配置 scheme 设置以防止不准确性。掌握了这些知识，你现在就可以在你的代码库中防止卡顿，为用户提供流畅的动画体验了。感谢聆听，希望你们接下来的会议一切顺利。
