---
title: 为可变刷新率显示器优化
session_id: 10147
collection: wwdc2021
year: 2021
duration: '23:20'
topics: ['Graphics & Games']
group: D · 响应性、hang/hitch 与渲染循环（RunLoop 的现代替身）
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10147/'
content_hash: 'sha256:05adf58ae27cf7db'
translated: true
---

# 为可变刷新率显示器优化

<sub>WWDC2021 · 23:20 · Graphics & Games</sub>

了解如何在所有支持动态显示时序的 Apple 平台上实现平滑的屏幕更新。学习 pacing……

> [!note] 归档理由
> 可变刷新率与帧预算，理解 ProMotion 下的时序

## 相关资源

- [Metal Feature Set Tables](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [Metal](https://developer.apple.com/documentation/Metal)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10147/5/B362C41F-D567-4137-8333-0B4FF56AD528/downloads/wwdc2021-10147_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10147/5/B362C41F-D567-4137-8333-0B4FF56AD528/downloads/wwdc2021-10147_sd.mp4?dl=1)
- [关机：改善电池消耗](https://developer.apple.com/videos/play/wwdc2022/10083)
- [交付优化的 Metal Apps 和游戏](https://developer.apple.com/videos/play/wwdc2019/606)
- [自适应同步调度是否启用](https://developer.apple.com/videos/play/wwdc2021/10147/?time=351)
- [利用 Drawable present 调用](https://developer.apple.com/videos/play/wwdc2021/10147/?time=409)
- [一个简单例子](https://developer.apple.com/videos/play/wwdc2021/10147/?time=431)
- [App 中的自适应同步 1](https://developer.apple.com/videos/play/wwdc2021/10147/?time=475)
- [App 中的自适应同步 2](https://developer.apple.com/videos/play/wwdc2021/10147/?time=523)
- [在运行时查询显示刷新率](https://developer.apple.com/videos/play/wwdc2021/10147/?time=936)
- [使用 CADisplayLink 的实际帧率](https://developer.apple.com/videos/play/wwdc2021/10147/?time=1026)
- [动态计算时间增量 1](https://developer.apple.com/videos/play/wwdc2021/10147/?time=1307)
- [动态计算时间增量 2](https://developer.apple.com/videos/play/wwdc2021/10147/?time=1317)
- [动态计算时间增量 3](https://developer.apple.com/videos/play/wwdc2021/10147/?time=1328)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

你好，我是 Kyle Sanner，来自 GPU 软件工程团队。和我的同事 Alex Li 一起，我们将讨论如何在可变刷新率显示器上让你的 App 获得最佳帧 pacing。我们把焦点放在 macOS 即将推出的一些新显示技术 Adaptive-Sync，以及如何在所有条件下在 iPad Pro 上平滑地驱动自定义绘制。我们将从 Apple 平台上支持的显示器类型快速概览开始。

我们将向你介绍 Mac 上的 Adaptive-Sync 显示器，以及 macOS Monterey 中的新工具，你可以用它们在这些显示器上为全屏 App 和游戏交付平滑的帧率。

然后，我们将深入探讨 iPad Pro 上的 ProMotion，并查看一些 CADisplayLink 最佳实践，帮助你的 App 在不同帧率下保持正确的帧 pacing。

让我们先回顾 Apple 设备支持的显示器类型。

Apple 系统上的大多数显示器以固定刷新率工作。也就是说，只要通电，它们就以一致的速率刷新自己。例外是 iPad 上的 ProMotion 显示器，现在还有 macOS 上的 Adaptive-Sync 显示器。让我们开始深入 macOS 上 Adaptive-Sync 显示器的新特性。

我们将从 Adaptive-Sync 显示器是什么，以及它们在 Mac 上如何工作开始。但首先，让我们先快速看看固定速率显示器如何工作。

这是向 60Hz 显示器交付帧的图。每个帧被呈现给显示器，在显示器刷新前停留 16ms。如果你的 Mac 在帧缓冲中有新绘制的帧准备好，那么那个新帧被呈现。否则，之前的帧再次显示。

看 120Hz 显示器，你会看到虽然我们把刷新率翻倍，从而把每个帧可以在屏幕上的间隔减半，它的行为方式相同，只是更快。

另一方面，看这个 Adaptive-Sync 显示器。每个帧不是静态时长，而是有一个可以在屏幕上停留的时间窗口。这个窗口取决于所连接的显示器。这个显示器可以在 40 到 120Hz 之间运行，这意味着一个帧可以在屏幕上停留 8 到 25ms 之间的任意时间。

注意一旦最大时间过去，系统必须刷新面板，显示器会短暂地无法接受新更新。好吧，那么你的游戏和 App 在 Adaptive-Sync 显示器上能获得什么好处？对于大多以显示器最大刷新率运行的应用，Adaptive-Sync 显示器免费提供巨大好处。让我们先看这个场景，你的 App 大多能在 8ms 内产生新帧，所以你相当可靠地运行在 120Hz。但由于场景复杂度瞬间增加，完成的帧在前一帧首次显示后 9ms 才到达帧缓冲。在固定帧率显示器上，前一帧会显示 16ms，而不是你预期的 8ms。这会在你的 App 中产生可感知的卡顿。

在 Adaptive-Sync 显示器上，你的帧在完成后立即呈现给显示器，所以你的 App 只承担 1ms 的惩罚。这么小的卡顿通常用户无法感知。对于无法达到显示器最大帧率的工作负载，你可以通过对你 App 呈现 drawables 的方式做小幅更改，提供平滑、均匀的帧。考虑这个场景：一个运行复杂场景的游戏可以以约 90Hz 产生更新。然而，一个间歇性效果导致复杂度大幅跃升，但不一致，造成突然跌落到 66Hz 的尖峰。通过监控你 App 的 GPU 工作，你可以响应这个复杂度尖峰，故意把帧呈现得更晚，直到场景复杂度持续降低。现在，让我们谈谈一些 Adaptive-Sync 最佳实践。在固定速率显示器上，当你的 App 的 GPU 工作持续超过显示器的 on-glass 间隔，我们之前建议你放慢渲染以命中显示器最快刷新率的下一个因数。

通常这意味着把目标帧率从 60 降低到 30，就像这里这个例子。

然而，向 Adaptive-Sync 显示器呈现时，我们正在改变该指导。你应该改为尝试以你的 App 能均匀做到的最高速率呈现帧。除了均匀呈现帧，记住如果你的帧以低于显示器支持的最低速率呈现，显示器可能变得无法接受新帧，这可能在你的 App 中引起抖动。但只要你处于支持范围内，你可以自由选择最适合你 App 的速率。现在你对今年 Mac 上新显示支持有了高层理解，让我们谈谈如何在游戏中启用 Adaptive Sync。

首先，你需要一台支持的 Mac。任何带有 Apple Silicon GPU 的 Mac 都能很好工作，我们也支持许多最近的基于 Intel 的 Mac。第二，你需要一台支持的 Adaptive-Sync 显示器，并启用 Adaptive-Sync 模式。这可以通过在显示器系统偏好设置中选择新的可变刷新率来完成。最后，你的 App 需要以全屏模式运行。让我们看看你可以在 App 中调用哪些 API 来检测它是否应该尝试做 Adaptive-Sync 调度。首先，你需要确定你运行的显示器是否支持 Adaptive-Sync 调度。为此，今年 NSScreen 上有一些新属性，minimumRefreshInterval 和 maximumRefreshInterval。这些值告诉你呈现给这个显示器的帧的有效 onscreen 时间范围。在固定帧显示器上，这些值相同，所以一个简单的不等比较就能告诉你这个屏幕是否处于 Adaptive-Sync 模式。接下来，你需要知道你的窗口当前是否全屏。你可以通过检查窗口的 styleMask 来确定。

记住，你需要把这两个检查结合起来，确保你的 App 能利用 Adaptive-Sync 调度。

好吧，很好。既然你已经掌握了 Adaptive-Sync 显示器和 macOS 提供的检测它们的新 API，让我们看看如何调整一些现有的 metal 呈现技术，以便在 Adaptive-Sync 显示器上均匀呈现。

你可以使用我们具有内建帧 pacing 的 MetalDrawable API，如 presentAfterMinimumDuration 或 presentAtTime，与 Adaptive-Sync 显示器配合得很好。或者，你可以用 present now 调用和你自己的自定义计时器自己实现一个解决方案。让我们看看几种不同实现如何工作。

我们从一个简单例子开始。这里，我们要获取一个 Drawable，设置 GPU 工作，并在屏幕上呈现它。我们依赖 Drawable 可用的背压来为我们设置帧率。在固定速率显示器上，我们知道这不是最好的想法，因为无法保证你的 GPU 工作与显示器的刷新率对齐。

但正如你在 Adaptive-Sync 显示器上拍摄的 instruments 捕获中看到的，当我们的场景一致时，这似乎还算可以。问题在于这个场景会遇到周期性卡顿。这些卡顿会转化为用户可见的停顿。让我们通过以固定、均匀的速率呈现来修复它。如果你想要为游戏的玩家实现可由用户调整的 FPS 滑块，也可以使用这个技术。这里，我们把想要的频率设置为 78Hz。我们不使用普通 present 调用，而是对这个 Drawable 使用 present afterMinimumDuration，并指定上面定义的间隔。这里，你可以看到以我们请求的速率平滑呈现的帧。我们没有像前一个例子那么快地呈现，但你的用户更不可能遇到停顿，你的 App 也会使用更少的 CPU 和 GPU 时间。好吧，这里事情变得更有趣一些。让我们尝试一种方法，无需设置单个固定速率就能产生均匀 pacing 的帧。一种方法是计算产生每个帧所需的 GPU 工作的滚动平均，并把那个时间送入我们的 present Drawable 调用。对于第一帧，我们需要用起始值加载我们的平均 GPU 时间。我选择乐观一点，目标是显示器能支持的最高速率。这只是我们平均值的起点，所以任何合理猜测都可以。现在，让我们附加一个 CommandBuffer 完成处理程序来测量 GPU 渲染这一帧所花费的时间，并把那个时间纳入我们的滚动平均。首先，我们可以获取 GPU 完成我们工作所花的时间。然后，我们把新时间纳入将用于呈现下一帧的滚动平均。这里是结果。如你所见，我们以类似前一个例子的速率呈现，但这个限制由我们之前生成的帧决定，并会在一系列 Mac GPU 上产生均匀帧率。这里，我们可以看到同一程序在性能较弱的 Mac 上平滑运行在 48Hz，无需任何额外代码更改。

好吧，现在你有了一些新工具和技术，可以在 Adaptive-Sync 显示器上优化你的 App。如果你想了解更多关于 macOS 上的 Adaptive-Sync 显示器，请查看 Apple 开发者网站上的新 Metal 示例项目。要了解更多关于在 Metal 中交付高性能体验，请查看前几年这些 WWDC 讲座。现在，我把话筒交给 Alex，你将了解更多关于 iPad Pro 上的帧 pacing。谢谢你，Kyle。接下来，让我们谈谈 ProMotion。自 2017 年以来，每台 iPad Pro 都配备了 ProMotion 显示器，提供高达 120Hz 的刷新率。然而，120Hz 在某些情况下可能不可用，包括当用户开启省电模式时，今年 iPadOS 15 已经把省电模式带到 iPad。正确的帧 pacing 将允许你的 App 正确且平滑地呈现运动内容，无论显示特性、用户偏好和系统状态如何。我们将查看 ProMotion 与固定速率显示器的差异，以及某些帧率可能不可用的情况。接下来，我们将讨论什么是 display link，以及你的 App 如何用它驱动自定义绘制。最后，我们将提供一些 display link 最佳实践。让我们深入。正如 Kyle 先前简要介绍的，固定 60Hz 显示器每 16ms 刷新一次，固定的节奏。它支持帧率是 60 因数的内容平滑呈现。例如 60Hz、30Hz、20Hz 等。然而，当内容比显示器刷新率更慢，比如 30Hz，显示器本身仍必须以相同节奏刷新，因此每其他帧是前一帧的重复，这会消耗一些电量。另一方面，ProMotion 通过高达 120Hz 的刷新率提供出色的响应性。它还适应屏幕内容，从而降低功耗。让我们看看它如何工作。当然，在其 120Hz 的最大刷新率下，显示器每 8ms 刷新一次。

因为 120 是 60 的倍数，ProMotion 支持所有现有帧率。它不仅提供 120Hz，还为你的 App 提供一些中间帧率。此外，ProMotion 可以动态调整其刷新率，所以对于平滑的 60Hz 内容，它可以仅每 16ms 刷新一次而无需重复，这在固定 120Hz 显示器上是必需的。这一直延伸到 24Hz。

现在，这些帧率可能并不总是可用。用户可以在辅助功能设置中开启限制帧率开关，把最大帧率限制在 60Hz。此外，当设备发热时，系统可能会对 120Hz 的可用性施加限制。随着 iPadOS 15，我们还将在省电模式中强制执行 60Hz 限制。那么这些场景如何影响你的 App？好消息是大多数 App 无需任何更改就能工作。但如果你的 App 执行逐帧自定义绘制，那么你需要关注这些帧率变化，我们将向你展示如何做到。驱动自定义绘制的推荐工具是 display link，它本质上是一个与显示刷新率同步的计时器。它帮助你的 App 驱动任何自定义动画或自定义渲染循环。有两种 display link。一种是 CoreVideo 在 macOS 提供的 CVDisplayLink，另一种是 CoreAnimation 在我们其他平台以及 macOS 上的 Catalyst 提供的 CADisplayLink，各有略微不同的特性和行为。今天我们将只讨论 CADisplayLink，但高层上，这些概念适用于两者。

CADisplayLink 在每个 vsync 醒来并调用回调。这给应用整个 8ms 来完成其工作。

常规计时器，如 NSTimer，很不可能与显示器完美同步。它可能相位失调或漂移，所以有时 App 可能没有足够时间完成工作，导致掉帧。现在你已经看到 CADisplayLink 提供一致的时序，这里还有它的一些额外好处。它可以以比显示器刷新率更慢的速率运行，为此，你的 App 通过 preferredFramesPerSecond 提供一个提示，我们会为你选择最接近的可用帧率。当帧率可用性变化时，如我们之前讨论的，CADisplayLink 会在底层自动调整其速率。当然，它还给你的 App 提供必要的时序信息，以便你的自定义绘制可以意识到这些变化。我们不会深入如何写自定义动画或自定义渲染循环，但我们将提供四条最佳实践，帮助你的自定义绘制与显示时序保持同步并避免一些常见陷阱。

首先，在运行时查询显示刷新率而不是硬编码它很重要。第二，通常情况下你应该使用 CADisplayLink 本身的帧率。接下来，使用 targetTimestamp 准备绘制将帮助减少卡顿。最后，动态计算时间增量始终是个好主意，以准备意外情况。让我们逐个介绍。最大显示刷新率可以通过 UIScreen 查询，它在 ProMotion 显示器上总是返回 120Hz，即使在省电模式开启等情况下。另一方面，CADisplayLink 实际上通过 duration 属性提供帧之间的最短间隔，并会基于当前设备状态动态更新。但几乎总是，你应该直接从 CADisplayLink 使用实际帧信息，因为 display link 可以以比最大显示刷新率更慢的速度运行。此外，帧率可用性取决于硬件，实际帧率可能由 display link 本身响应系统状态变化而动态更改。让我们看一个例子。假设我们请求 40Hz 的 display link。如你所见，在 ProMotion 显示器上，40Hz 是支持的。然而，在 60Hz 显示器上，或当 ProMotion 被限制到 60Hz 时，display link 会自动调整自己到 30Hz。这确保了良好的节奏，每次醒来都在可能的 vsync 上，试图给每帧相等的时间。如果我们使用普通的 40Hz NSTimer，它不具备帧率意识，它的醒来可能正好在 vsync 间隔中间，当然我们不能在那里呈现帧，所以你很可能会在自定义绘制中观察到卡顿。那么在代码中它看起来如何？这是你通常如何设置 display link。首先，你必须提供一个 target 和一个 selector，那是要调用的回调。接下来，通过 preferredFramesPerSecond 提示期望的 40Hz 帧率。然后你把 display link 添加到当前 runloop，回调将从那里被调用。所以在回调中，你可以通过从 targetTimestamp 减去 timestamp 来得到 display link 醒来之间预期的间隔。这个间隔不一定是总是 1/40，因为 display link 本身可能以不同频率运行。接下来，让我们谈谈这些时间戳。CADisplayLink 上主要有两个时间戳，Timestamp，表示回调被调度调用的时间，以及 targetTimestamp，是下一帧将被 CoreAnimation 合成的时间。我们将走一个例子，说明为什么你应该使用 targetTimestamp 来准备绘制。这里是一个动画，其归一化时间域从 0 到 1。假设我们目标最高可能帧率，当前是 120Hz。CADisplayLink 醒来，如果我们使用 timestamp 准备帧呈现，我们将直接在这里采样，它在下一个 vsync 呈现，这里是。

相同过程继续，我们看到它有良好的节奏，对于每个 120Hz 帧，我们的动画进度增加 0.05。现在，假设热状态变化，120Hz 不再可用。现在 display link 再次醒来，App 在进度 0.4 准备动画，它在下一个 vsync 正好这里呈现。

相同模式继续。过渡这里有点不对。我们看到进度增加 0.05，但一个是 8ms，另一个是 16ms。如果我们绘制进度 versus 时间，会清楚地看到过渡处的 hiccup，这会反映为用户可感知的卡顿，这不可取。

现在，让我们尝试 targetTimestamp。CADisplayLink 在这里醒来。进度在 targetTimestamp 采样，得到 0.15。相同模式继续，再次我们看到良好的节奏。在这个帧率过渡点，display link 醒来，在 targetTimestamp 采样，我们得到 0.50。它以相同方式继续。如果我们绘制相同的进度 versus 时间图，你会看到它是一条直线，因此即使帧率变化也能提供平滑内容。所以应该使用 targetTimestamp 而不是 timestamp 来准备你的绘制。在代码中，这通常像把任何 timestamp 使用替换为 targetTimestamp 一样简单。最后，让我们谈谈动态计算时间增量。targetTimestamp 和 timestamp 的差给你 display link 回调之间预期的时间量，但实际时间量不保证。更高优先级的线程可能在 CPU 上被调度，或 runloop 正忙于其他事情。在极端情况下，回调可能被完全跳过，所以这些情况下，为获得最佳用户体验，在自定义绘制中保持正确时序尤其关键。

当 CADisplayLink 回调被调用时，App 执行其工作，为下一帧准备更新或渲染。通常，回调会在调度的醒来时间正好被调用，但不总是这样。我们期望下一个回调在这里被调用。然而，display link 直到 vsync 间隔几毫秒后才有机会运行。因此你可能得不到完整的 8ms。在这种情况下，你可以查询 CACurrentMediaTime 并与 targetTimestamp 比较，以了解有多少时间可用。

现在，假设工作在这帧耗时过长。下一个回调直到 runloop 再次空闲时才会被调用。因为这个被延迟，随后的回调将被跳过，所以当你准备在本回调中推进自定义绘制的进度时，要注意你应该使用的时间增量不是 8ms，而是 16ms，如果你跟踪自定义绘制状态上次更新时的前一个 timestamp 的话。因此，如果你的 App 使用时间增量来推进自定义绘制的状态，每次 calback 被跳过时，这会把你的自定义绘制减慢一帧。你可以改为跟踪前一个 targetTimestamp，以便正确推进状态。如果你的自定义绘制有高工作负载，你可以查看 targetTimestamp 以按需潜在减少工作负载以满足截止时间。

回顾最佳实践，不要猜测显示刷新率。始终在运行时查询它。你的自定义绘制应该在支持的帧率上灵活，并准备好适应不同速率。使用 targetTimestamp 以确保无卡顿的帧率过渡，并留意任何意外情况，如错过 display link 回调。让我们总结。在本会议前半部分，我们讨论了如何在 macOS 的 Adaptive-Sync 显示器上运行时优化你 App 的帧 pacing。后半部分，我们描述了你的 App 在 iPad Pro 的 ProMotion 显示器上驱动自定义绘制并保持所有条件下平滑帧 pacing 的最佳实践。随着显示技术持续演进，我们希望本会议不仅为你提供了洞察，还提供了工具和最佳实践，以支持显示器日益动态的时序。非常感谢大家加入我们，享受 WWDC 2021 的其余部分。[music]
---

target file path: /Users/tommywu/Desktop/翻译/apple-developer-docs-vault/wwdc/zh/wwdc2021/10147-optimize-for-variable-refresh-rate-displays.md