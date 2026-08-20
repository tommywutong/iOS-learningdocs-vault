---
title: 使用 Instruments 分析挂起
session_id: 10248
collection: wwdc2023
year: 2023
duration: '42:52'
topics: [Developer Tools]
group: D · 响应性、hang/hitch 与渲染循环（RunLoop 的现代替身）
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10248/'
content_hash: 'sha256:52c689fc88bbcd01'
translated: true
---

# 使用 Instruments 分析挂起

<sub>WWDC2023 · 42:52 · Developer Tools</sub>

用户界面元素通常会模拟真实世界的交互，包括实时响应。如果一个 App 在用户操作后出现明显延迟…

> [!note] 归档理由
> 用 Instruments 逐帧定位挂起（hang），方法论极强

## 章节

- [什么是挂起？](/videos/play/wwdc2023/10248/?time=116)
- [什么是瞬时？](/videos/play/wwdc2023/10248/?time=231)
- [事件处理与渲染循环](/videos/play/wwdc2023/10248/?time=279)
- [将主线程工作控制在 100ms 以下](/videos/play/wwdc2023/10248/?time=505)
- [主线程繁忙式挂起](/videos/play/wwdc2023/10248/?time=555)
- [过长还是过频？](/videos/play/wwdc2023/10248/?time=866)
- [LazyVGrid 在 iPad 上仍然挂起](/videos/play/wwdc2023/10248/?time=1306)
- [修复：使用 task 修饰符异步加载缩略图](/videos/play/wwdc2023/10248/?time=1471)
- [异步挂起](/videos/play/wwdc2023/10248/?time=1552)
- [修复：脱离主要 Actor](/videos/play/wwdc2023/10248/?time=1958)
- [主线程被阻塞式挂起](/videos/play/wwdc2023/10248/?time=2157)
- [修复：将共享属性设为 async](/videos/play/wwdc2023/10248/?time=2359)
- [线程被阻塞不等于 App 无响应](/videos/play/wwdc2023/10248/?time=2435)

## 相关资源

- [什么是挂起？](https://developer.apple.com/videos/play/wwdc2023/10248/?time=116)
- [什么是瞬时？](https://developer.apple.com/videos/play/wwdc2023/10248/?time=231)
- [事件处理与渲染循环](https://developer.apple.com/videos/play/wwdc2023/10248/?time=279)
- [将主线程工作控制在 100ms 以下](https://developer.apple.com/videos/play/wwdc2023/10248/?time=505)
- [主线程繁忙式挂起](https://developer.apple.com/videos/play/wwdc2023/10248/?time=555)
- [过长还是过频？](https://developer.apple.com/videos/play/wwdc2023/10248/?time=866)
- [LazyVGrid 在 iPad 上仍然挂起](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1306)
- [修复：使用 task 修饰符异步加载缩略图](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1471)
- [异步挂起](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1552)
- [修复：脱离主要 Actor](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1958)
- [主线程被阻塞式挂起](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2157)
- [修复：将共享属性设为 async](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2359)
- [线程被阻塞不等于 App 无响应](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2435)
- [分析已发布 App 中的响应性问题](https://developer.apple.com/documentation/Xcode/analyzing-responsiveness-issues-in-your-shipping-app)
- [提升 App 响应性](https://developer.apple.com/documentation/Xcode/improving-app-responsiveness)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10248/6/AB6FF62D-3A9D-4816-95E8-2E7B464CA1DF/downloads/wwdc2023-10248_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10248/6/AB6FF62D-3A9D-4816-95E8-2E7B464CA1DF/downloads/wwdc2023-10248_sd.mp4?dl=1)
- [揭秘 SwiftUI 性能](https://developer.apple.com/videos/play/wwdc2023/10160)
- [认识 RealityKit Trace](https://developer.apple.com/videos/play/wwdc2023/10099)
- [认识讲师：使用 Instruments 分析挂起](https://developer.apple.com/videos/play/wwdc2023/10299)
- [使用 Xcode 和设备端检测追踪挂起](https://developer.apple.com/videos/play/wwdc2022/10082)
- [可视化并优化 Swift 并发](https://developer.apple.com/videos/play/wwdc2022/110350)
- [Swift 并发：幕后探秘](https://developer.apple.com/videos/play/wwdc2021/10254)
- [了解并消除 App 中的挂起](https://developer.apple.com/videos/play/wwdc2021/10258)
- [探索 UI 动画卡顿与渲染循环](https://developer.apple.com/videos/play/tech-talks/10855)
- [SwiftUI 中的叠放、网格和大纲](https://developer.apple.com/videos/play/wwdc2020/10031)
- [Instruments 入门](https://developer.apple.com/videos/play/wwdc2019/411)
- [深入理解 System Trace](https://developer.apple.com/videos/play/wwdc2016/411)
- [BackgroundThumbnailView](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1178)
- [带 Grid 的 BackgroundSelectionView](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1198)
- [带 Grid 的 BackgroundSelectionView（简化版）](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1203)
- [LazyVGrid 变体](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1226)
- [BackgroundThumbnailView](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1445)
- [带进度指示（但无加载）的 BackgroundThumbnailView](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1499)
- [在主线程上进行异步加载的 BackgroundThumbnailView](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1526)
- [在主线程上进行异步加载的 BackgroundThumbnailView](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1799)
- [在主线程上进行异步加载的 BackgroundThumbnailView（简化版）](https://developer.apple.com/videos/play/wwdc2023/10248/?time=1901)
- [在主线程上进行异步加载的 BackgroundThumbnailView](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2020)
- [同步缩略图属性](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2039)
- [异步缩略图属性](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2043)
- [在后台进行异步加载的 BackgroundThumbnailView](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2048)
- [共享属性导致主线程阻塞](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2332)
- [共享属性导致主线程阻塞（简化版）](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2340)
- [共享属性导致主线程阻塞 + ColorizingService（简化版）](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2350)
- [await 关键字后的共享同步属性仍会导致主线程阻塞](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2365)
- [await 关键字后的共享同步属性仍会导致主线程阻塞（+colorize 函数）](https://developer.apple.com/videos/play/wwdc2023/10248/?time=2379)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Joachim Kurz：欢迎观看“使用 Instruments 分析挂起”。我是 Joachim，是 Instruments 团队的一名工程师。今天，我们将深入探讨挂起（hang）。首先，我会概述什么是挂起，为此我们需要聊聊人类感知。然后，我将简要介绍事件处理与渲染循环，这是理解挂起成因的基础。有了这些理论知识，我们将进入 Instruments，分析三个不同类型的挂起示例：主线程繁忙式挂起、异步挂起以及主线程被阻塞式挂起。针对每一种，我会展示如何识别它们，分析时要注意什么，以及如何知道何时需要向文档中添加其他仪器以获取更多信息。

在开始之前：本场讲座的某些部分需要你对 Instruments 有一定了解。如果你曾经用 Instruments 分析过 App，那就没问题。否则，请观看我们 2019 年的讲座“Instruments 入门”。处理挂起通常有三个步骤：发现挂起，分析挂起以了解其发生原因，然后修复它（并验证是否真正修复）。

今天，我们假设你已经发现了一个挂起，并将重点放在分析部分，同时也会讨论一些修复方法。

如果你想了解更多关于发现挂起的信息，请观看 WWDC22 的讲座“使用 Xcode 和设备端检测追踪挂起”。它涵盖了所有用于发现挂起的工具，包括：Instruments、可在 iOS 开发者设置中启用的设备端挂起检测，以及 Xcode Organizer。

今天，我们将使用 Instruments 来分析一个已经发现的挂起。为了更好地理解挂起，让我们谈谈人类感知，然后开灯。

我们需要一个灯泡和一根电线。嗯，好多了。就像台灯应有的样子，我插上电线它就亮了。当我拔掉电线时，它又立刻熄灭了。

但如果有延迟呢？我插上电线，它过了一会儿才亮。更奇怪的是，当我拔掉电线时，同样的事情发生了。从插上电线到灯亮起之间的延迟只有 500 毫秒。但这已经让你好奇这个盒子里发生了什么。感觉不太对劲，灯没有直接开关。

然而，在其他某些情况下，500 毫秒的延迟可能是可以接受的。什么样的延迟可以接受取决于具体情况。假设你无意中听到这样一段对话：“乌龟怎么交流？”“壳（Shell）电话（phones）。”这里，问题和答案之间有一秒的延迟。这感觉完全自然。但这个却不然：为什么呢？乌龟和独角兽之间的对话是一种请求-响应式的互动，但插上灯是直接操作一个真实物体。真实物体会瞬间反应。如果我们模拟真实事物，它也需要瞬间反应。如果不这样，就打破了模拟的假象。

当插上电线和灯亮起之间没有延迟时，你对我声称这里有一个真灯没有任何异议。但当有明显的延迟时，你的大脑会突然说：“等等，这东西不是这样工作的。”但多快才算瞬时？多大的延迟小到我们注意不到？这是没有延迟时的基准。

100 毫秒呢？对我来说，我感觉在开灯时注意到了一个微小的延迟，但关灯时没有，而且只有在我仔细看的时候才注意到。你的体验可能不同。100 毫秒算是一个阈值。明显更小的延迟几乎就无法感知了。

我们来试试 250 毫秒。

250 毫秒已经感觉不瞬时了。

虽然不算慢，但延迟绝对能注意到。

这类感知阈值也指导着我们的挂起报告。对于离散交互（例如点击按钮），低于约 100 毫秒的延迟通常会感觉是瞬时的。有些特殊情况你可能希望做得更快，但这是一个值得努力的好目标。超过这个阈值，就取决于具体情况了。直到 250 毫秒，你可能还可以接受。再长一些就会变得明显，至少是潜意识里。

这是一个连续的尺度，但超过 250 毫秒肯定就不再感觉瞬时了。因此，我们的大多数工具默认从 250 毫秒开始报告挂起，但我们称其为“微挂起”（micro hang），因为它们容易被忽略。根据上下文，这些可能是可以接受的，但通常并非如此。超过 500 毫秒的所有情况，我们都认为是真正的挂起。基于此，我们可以大致使用以下阈值：如果你想让某件事感觉瞬时，目标是延迟 100 毫秒或更少。如果你进行的是请求-响应式交互，没有额外反馈的情况下，500 毫秒的延迟可能可以接受。

但实际上，在一次交互中我们常常两者都有。让我们看一个例子。

我刚写完这封给所有帮助准备本次讲座的同事的邮件，准备发送。我把鼠标移到“发送”按钮上并点击它，片刻之后，邮件窗口动画飞出，表示正在发送。这里你实际上看到了两件事。首先，按钮高亮了，然后有一个 500 毫秒的小延迟，接着邮件窗口动画飞出。但这个延迟感觉还好，因为我们通过按钮高亮已经知道我们的请求已被接收。我们把按钮当作一个“真实”的东西，并期望它以“实时”的方式，瞬时更新。

因此，对于界面中的实际 UI 元素，我们通常要追求这种“瞬时”更新。

为了让我们的 UI 元素能够“瞬时”做出反应，保持主线程不被非 UI 工作占用至关重要。要明白为什么，让我们仔细看看事件处理与渲染循环，看看在 Apple 平台上事件是如何被处理的，以及用户输入是如何导致屏幕更新的。

在某个时刻，会有人与设备进行交互。我们无法控制何时发生。首先，通常会涉及一些硬件，比如鼠标或触摸屏。它检测到交互，创建一个事件，并将其发送给操作系统。操作系统找出哪个进程需要处理这个事件，并将其转发给该进程，例如你的 App。在 App 中，负责处理事件的是 App 的主线程。这是你大部分 UI 代码运行的地方。它决定如何更新 UI。然后这个 UI 更新会被发送到渲染服务器（render server），这是一个单独的进程，负责合成各个 UI 图层并渲染下一帧。最后，显示驱动程序（display driver）获取渲染服务器准备好的位图，并相应地更新屏幕上的像素。如果你想了解更多关于这是如何工作的，我们在“提升 App 响应性”文档中有介绍。对我们来说，这个粗略的概述就足够理解发生了什么了。现在，如果在这段时间内有另一个事件到来，它通常可以并行处理。但是，如果我们看单个事件如何在管道中传播，我们仍然需要按顺序查看所有步骤。在到达主线程之前的事件处理步骤，以及之后渲染和更新显示的步骤，它们的耗时通常相当可预测。当我们遇到交互显著延迟时，几乎总是因为主线程上的那部分耗时太长，或者当事件到来时，主线程上仍有其他东西正在执行，因此我们需要等待它完成，然后才能处理事件。

鉴于每次更新 UI 元素都需要在主线程上花费一些时间，并且我们希望这些更新在 100 毫秒内发生以感觉真实，理想情况下，主线程上没有工作应该超过 100 毫秒。如果你能更快，那就更好了。请注意，主线程上的长时间工作也可能导致卡顿（hitch），避免卡顿的阈值更低。

你可以在我们的技术讲座“探索 UI 动画卡顿与渲染循环”以及关于“提升 App 响应性”的文档中找到关于卡顿的更多详细信息。今天，我们专注于挂起。

我的一位同事在开发新功能时，在我们的一个 App“Backyard Birds”中发现了一个挂起。让我们用 Instruments 分析一下这个 App。

我这里有包含该 App 的 Xcode 项目。要在 Instruments 中分析 App，我只需点击“Product”菜单，然后选择“Profile”，Xcode 会构建 App 并将其安装到设备上，但不会启动它。

Xcode 还会打开 Instruments 并将其配置为针对 Xcode 中配置的同一个 App 和设备。在 Instruments 的模板选择器中，我会选择“Time Profiler”模板，当你还不知道在找什么，并想更好地了解你的 App 在做什么时，这通常是一个不错的起点。

这会在 Time Profiler 模板的基础上创建一个新的 Instruments 文档。这个新文档包含 Time Profiler 仪器和 Hangs 仪器，这两者对我们的分析都很有用。我点击工具栏左上角的“Record”按钮开始录制。Instruments 会启动配置好的 App 并开始捕获数据。

这里是 Backyard Birds App。我点击第一个花园进入详情视图。稍后当我点击“Choose Background”按钮时，应该会弹出一个底部表单（bottom sheet），显示一系列背景图片供我选择。我现在就这么做。按钮按下了，但似乎卡住了。表单花了很长时间才出现。这是一个严重的挂起。

Instruments 全程记录了这一切。我点击工具栏上的“Stop”按钮停止录制。Instruments 也已经检测到了挂起。它会测量挂起时长，并根据严重程度标记相应的间隔。在这种情况下，Instruments 显示发生了“严重挂起”（Severe Hang）。这和我们使用 App 时的体验也是一致的。

Instruments 检测到主线程无响应，并将相应的间隔标记为潜在的挂起。在我们的案例中，确实发生了挂起。主线程无响应主要有两种情况。最简单的情况是主线程还在忙着做其他工作。在这种情况下，主线程会显示大量 CPU 活动。另一种情况是主线程被阻塞了。这通常是因为主线程正在等待其他地方完成某些工作。当线程被阻塞时，主线程上的 CPU 活动会很少，甚至没有。你遇到的是哪种情况，决定了你应该采取哪些后续步骤来确定发生了什么。

回到 Instruments，我们需要找到主线程。文档中的最后一个轨道（track）显示了我们目标进程的轨道。它左侧有一个小的展开指示器，表示存在子轨道。我点击它来显示进程中每个线程的单独轨道。然后，我在这里选择“Main Thread”轨道。这也会更新详情区域，显示“Profile”视图，该视图向我们展示了在整段录制时间内，在主线程上执行的所有函数的调用树（call tree）。

但我们只对挂起期间发生的事情感兴趣，所以我右键点击时间线中的挂起间隔以显示上下文菜单。我可以在这里选择“Set Inspection Range”，但我还会按住 Option 键，以获得“Set Inspection Range and Zoom”。

这会放大到该间隔的范围，并将详情视图中显示的数据过滤到所选的时间范围。

虽然在整段挂起间隔内 CPU 使用率并非 100%，但仍然相当高，大部分时间在 60% 到 90% 之间。

这显然是主线程繁忙的情况。让我们找出所有这些 CPU 工作是什么。

我们现在可以仔细查看调用树中所有不同的节点。但右侧有一个很好的摘要：最重堆栈跟踪（heaviest stack trace）视图。

当我点击最重堆栈跟踪视图中的一个帧（frame）时，调用树视图会更新以显示这个节点。这也告诉我们，这个方法调用在调用树中已经相当深了。

默认情况下，最重堆栈跟踪会隐藏那些不是来自你的源代码的后续函数调用，以便更容易看到你的源代码在哪被涉及。我们可以对调用树视图应用类似的过滤器，方法是点击底部栏中的“Call Tree”按钮，并启用“Hide System Libraries”复选框。这将过滤掉来自系统库的所有函数，使我们更容易专注于我们自己的代码。

调用树视图显示，几乎所有我们的回溯（backtrace）都包含“BackgroundThumbnailView.body.getter”调用。看来我们应该让我们的 body getter 更快，对吧？不完全是！所以，我们知道我们有一个主线程繁忙的情况，意味着 CPU 正在做大量工作。我们也找到了一个花费了大量 CPU 时间的方法。但现在有两种不同的情况。我们可能在这个方法中花费了大量的 CPU 时间，因为它本身运行了很长时间。但也可能是因为它被调用了很多次，所以才会在这里显示出来。我们应如何减少主线程上的工作取决于我们遇到的是哪种情况。

一个典型的调用栈结构是这样的。从 main 函数开始调用，它调用一些 UI 框架和一堆其他东西，然后在某个时刻，你的代码被调用。如果这个函数只被调用一次，并且那一次调用花费了很长时间，就像这里的 Turtle 函数一样，那么我们需要看看它调用了什么。也许它做了很多工作。那么我们可以尝试少做一些工作。但也有可能我们正在调查的方法被调用了很多次，就像这里的 Unicorn。当然，它所做的工作也会被一遍又一遍地重复。这通常是因为某个调用者（例如来自一个循环）多次调用了 Unicorn 这个函数。与其优化焦点函数（这里是 Unicorn）做了什么，不如研究我们如何能减少它的调用次数可能更有益。

这意味着我们下一步需要看的方向取决于我们遇到的情况。

对于一个长时间运行的函数，比如我们的 Turtle 情况，我们需要查看它的实现及其被调用者（callee）。

我们需要往下看。然而，如果一个函数被调用了很多次，比如 Unicorn，那么看看是什么在调用它，并确定我们能否减少调用次数，会更有益处。我们需要往上看。但是 Time Profiler 不能告诉我们我们遇到的是哪种情况。

我们假设对 Unicorn 和 Turtle 的调用是紧接着发生的。Time Profiler 通过定期检查 CPU 上正在运行的内容来收集数据。对于每个样本，它检查当前在 CPU 上运行的函数。对于这个例子，我们会得到 Turtle 和 Unicorn 各四次。但也有可能这是一个非常快的 Turtle，而 Unicorn 花费的时间更长，或者其他组合。所有这些场景都会在 Time Profiler 中产生相同的数据。

要测量特定函数的执行时间，请使用 os_signposts。我们在 2019 年的讲座“Instruments 入门”中讨论过如何做到这一点。也有针对各种技术的专用仪器，它们可以精确地告诉你正在发生什么。其中之一就是 SwiftUI View Body 仪器。

要添加 SwiftUI View Body 仪器，我点击工具栏右上角的加号按钮。这会显示 Instruments 库。这是 Instruments 应用程序提供的所有仪器的列表。有很多。你甚至可以编写自己的自定义仪器。

我在过滤字段中输入“SwiftUI”，然后显示了两个仪器。我选择“View Body”仪器，并将其拖入文档窗口以添加它。现在，因为上次录制时这个仪器不在文档中，所以它没有数据可显示。但没问题。我们重新录制一次。

为了节省时间，我已经提前录制好了。

在文档中包含了 SwiftUI View Body 仪器后，录制完成后，“View Body”轨道现在也显示了一些数据。SwiftUI View Body 轨道中有很多间隔。有点拥挤，所以我按下 Ctrl+Plus 来增加它的高度。SwiftUI View Body 轨道按实现它们的库对间隔进行分组。每个间隔代表一次视图 body 的执行。让我们再次放大到我们的挂起。

在第二栏中，有很多标记为“BackgroundThumbnailView”的橙色间隔。这精确地告诉我们有多少次 body 执行以及每次花了多长时间。橙色表示该次 body 执行的运行时间比我们对 SwiftUI 的目标时间稍长。但更大的问题似乎是间隔的数量。在详情视图中，有所有 body 间隔的摘要。通过点击“Backyard Birds”旁边的展开指示器，我可以显示 Backyard Birds 中各个视图类型。这向我展示了 BackgroundThumbnailView 的 body 被执行了 70 次，平均每次约 50 毫秒，导致总时长超过 3 秒。这几乎解释了我们所有的挂起时长。但当我们只需要预先显示六张图片时，70 次就显得过多了。这是一个应该减少 body 调用次数的情况，因此我们需要查看我们 body getter 的调用者，找出为什么它被如此频繁地调用，并研究如何减少它。为了轻松导航到相关代码，我再次选择主线程轨道，右键点击调用树中的“BackgroundThumbnailView.body.getter”节点以显示上下文菜单，然后选择“Reveal in Xcode”。

这会在 Xcode 中直接打开我们的 body 实现。让我们通过右键点击该类型并选择“Find”、“Find Selected Symbol in Workspace”来找到这个视图是如何被使用的。Find 导航器中的第一个结果就是我们要找的。

这里，我们的“BackgroundThumbnailView”被用在了一个 ForEach 中，这个 ForEach 位于一个 GridRow 内，而 GridRow 又位于另一个 ForEach 内，这个外层的 ForEach 则是在一个 Grid 中。Grid 在创建时会急切地计算其全部内容，因此即使我们只需要前几个缩略图，它也会计算所有。但有一个替代方案：LazyVGrid。它只计算填满一屏所需的视图数量。SwiftUI 中有很多视图都有惰性变体，它们只计算必要数量的视图，这通常是一个减少工作的简单方法。然而，当需要渲染相同内容时，急切实体使用的内存要少得多。默认情况下使用常规的急切实体，当发现与预先做了过多工作相关的性能问题时，再切换到惰性变体。

我们来自 WWDC 2020 关于“SwiftUI 中的叠放、网格和大纲”的讲座介绍了这些惰性变体并进行了更详细的描述。

让我们分析一下更新后的代码。

我开始录制，并再次点击“Choose Background”按钮来重现我们的挂起。现在，这好多了。仍然有一个小延迟，但远没有之前那么糟糕。Instruments 证实了这一点。我们现在录制的挂起耗时不到 400 毫秒。这是一个微挂起。“View Body”轨道也显示，我们现在只进行了 8 次 BackgroundThumbnail body 执行，这符合我们的预期。也许这已经足够好了。微挂起不太明显。让我们通过在 iPad 上分析 Backyard Birds 来确保它在其他设备类型上也能良好运行。

这里，我在 iPad 上运行 Backyard Birds。我已经在详情视图了。我点击“Choose Background”按钮，表单花了很长时间才出现。一旦出现，我们就能知道原因了。现在有更多的缩略图，因为我们的屏幕更大、空间更多。Instruments 也记录了这次挂起。

将检查范围聚焦到我们的挂起间隔，我们再次看到了更多的 BackgroundThumbnailView body。这是有道理的。现在我们需要为整个屏幕渲染大约 40 个，因为屏幕上可以容纳更多。因此，同样的代码在 iPhone 上表现尚可，但在 iPad 上却很慢，仅仅是因为屏幕更大了。这也是你应该修复微挂起的原因之一。你在办公桌测试时认为的微挂起，在某些用户的不同条件下可能会成为一个严重的挂起。我们现在只渲染填充屏幕所需的视图数量，所以在减少调用次数方面的优化潜力已经用尽。让我们看看有什么办法可以让每一次执行更快。

我将检查范围设置为一个单独的 BackgroundThumbnailView 间隔，然后切换回“Main Thread”轨道。Instruments 在最重回溯视图中显示我们的视图 body getter，并显示它调用了“BackyardBackground.thumbnail”属性 getter。

这是提供要在视图中显示的缩略图图像的模型对象。这个缩略图 getter 调用“UIImage imageByPreparingThumbnailOfSize:”。所以我们似乎在运行时即时计算缩略图。这需要一些时间。在这种情况下，大约 150 毫秒。这项工作我们更应该放在后台进行，而不应让主线程忙于处理。

为了更好地理解我们可以做出什么改变，我想看看缩略图 getter 被调用的上下文。

我右键点击最重堆栈跟踪视图中的“BackgroundThumbnailView.body.getter”帧，选择“Open in Source Viewer”。这将把调用树视图替换为一个源代码查看器，显示我们的 body getter 的实现，并用 Time Profiler 的样本注释实现的代码行，以显示我们的代码在哪些地方花费了多少时间。

我们的 body 实现这里非常简单；它只是根据 background 返回的缩略图创建了一个新的 Image 视图。但这个缩略图调用花费了很长时间。我有个不同的写法。要跳转到 Xcode，我点击右上角的菜单按钮，然后选择“Open file in Xcode”。

和之前一样，这会在 Xcode 中显示我们的源代码，准备进行修改。

我现在想做的是在后台加载缩略图，并且在加载过程中显示一个进度指示符（progress indicator）。首先，我们需要一个状态（state）变量来保存加载后的缩略图。

然后，在 body 中，如果我们已经加载了图像，就在 Image 视图中使用它。否则，我们展示一个 ProgressView。

现在剩下的就是加载实际的缩略图。我们希望在视图出现时开始加载它。这就是“.task”修饰符的作用。

在出现时，SwiftUI 会为我们启动一个任务，该任务会调用“thumbnail” getter 并将结果赋值给我们的“image”，这将会更新我们的视图。让我们试试看！这里，在 Instruments 录制的情况下，我点击“Choose Background”按钮，表单立刻就出现了！太棒了！我们看到了进度指示，几秒钟后，缩略图就显示出来了。这有效。不错！但是等等，Instruments 仍然显示了一个将近两秒的挂起。这里发生的是，挂起现在稍微晚一点发生。让我在 Backyard Birds App 里展示它发生的位置。我已经在详情视图中了。稍等，我会再次点击“Choose Background”按钮，然后紧接着尝试通过点击“Done”按钮来关闭表单。好，“Choose Background”和“Done”。

我点击了多次，但在加载进行期间，我的点击被忽略了。这就是 Instruments 告诉我们的那个挂起。它发生在表单显示之后。

这是一种略有不同的挂起类型。我们已经讨论过主线程繁忙和被阻塞之间的区别。还有一种审视挂起的方式：它们是由什么引起的，以及它们何时发生。我们称之为同步挂起和异步挂起。

这里，主线程正在做一些工作。如果当一个事件到来时，处理该事件需要很长时间，那就是一个挂起。我们假设我们能控制好这一点，并确保事件能被快速处理。但也许我们只是将一些工作推迟到稍后在主线程上执行，或者发生了一些其他的主线程工作，然后一个事件到来了。那么该事件必须等待前面的工作完成才能被处理。那么即使每个单独事件处理的代码都很快完成，这仍然会导致挂起。我们平台上的挂起检测工作原理是，它查看主线程上的所有工作项，并检查它们是否太长。如果是，则将其标记为潜在的挂起。并且它这样做是不考虑是否有用户输入的，因为用户输入可能随时到来，然后我们就会遇到真正的挂起。这意味着挂起检测也检测这些异步或延迟的情况，但它只测量潜在的延迟，而不是实际体验到的延迟。

我们称这些挂起为异步挂起（asynchronous hang），因为它们通常是由“dispatch_async”到主队列的工作，或是在主要 Actor（main actor）上异步运行的 Swift 并发任务引起的。但它们也可能由任何导致主线程工作的事情引起。

我们看到的第一个挂起是同步挂起。我们点击了一个按钮，那次按钮点击引起了长时间运行的工作，所以结果显示得较晚。

最近的这个挂起是一个异步或延迟的挂起。点击“Done”按钮本身实际上不会导致任何耗时的工作。但主线程上仍有工作阻止了点击的处理。因此，虽然使用 App 的人如果在此期间不与 App 交互可能不会注意到，但我们仍然应该修复这些情况，以防他们交互。我们现在就来修复。

这里我回到了 Instruments，并且已经将选择范围设置到我们的异步挂起并放大了。在视图 body 轨道的摘要视图中，Instruments 显示现在对 BackgroundThumbnailView 的 body getter 有 75 次调用。

这是因为大多数缩略图 body getter 被执行了两次。SwiftUI 创建了 40 个带有进度指示的视图来填充网格。但只有 35 个最终被显示出来，对于这 35 个，我们开始加载图像，一旦图像加载完成，视图就会更新，body 再次被调用，总共给了我们 75 次 body getter 执行。

即使所有 75 个 body getter 总共也耗时不到一毫秒。所以现在我们的 body getter 很快了。那部分起作用了。但我们仍然有一个挂起。我将再次选择“Main Thread”轨道，在最重堆栈跟踪视图中，Instruments 显示仍然是需要很长时间的缩略图 getter 在主线程上占用时间。这次，它是由我们的“BackgroundThumbnailView.body.getter”内部的闭包调用的，而不是直接由 body getter 调用。我双击它，这是打开 Source Viewer 的快捷键。这正是我们期望由于在 task 修饰符闭包中而在后台执行的代码。这段代码应该在这个时候运行，但它不应该在主线程上运行。对于这种 Swift 并发任务没有按预期方式执行的问题，我们有另一个有用的仪器：Swift Concurrency Tasks 仪器。

我已经用添加了 Swift Concurrency Tasks 仪器录制了相同的行为。Swift Tasks 仪器向文档添加了一个摘要轨道，但对我们的案例更有趣的是它为每个线程轨道贡献的数据。这里，在主线程轨道中，有一个来自 Swift Tasks 仪器的新图形。单个轨道可以显示多个图形。通过点击线程轨道头中的小向下箭头，我可以配置要显示哪些图形。我可以选择另一个图形，比如 Time Profiler 的 CPU Usage 图形，或者在点击时按住 Command 键以选择多个。所以现在 Instruments 一起显示了这个线程的 CPU 使用率和 Swift Tasks 图形。我再次放大到我们的挂起间隔。“Swift Tasks”栏现在清楚地显示主线程上有一堆任务执行。将检查范围设置为其中一个，并在 Profile 视图中检查最重堆栈跟踪，证实了这个任务正在包装我们的缩略图计算工作。

所以这项工作按照我们的期望正确地被包装在一个任务里。但是该任务在主线程上执行，这出乎意料。

让我解释一下这里发生了什么。首先，body getter 从 SwiftUI 的 View 协议继承 `@MainActor` 注解。因为“body”在“View”协议中被注解为 `@MainActor`，所以当我们实现它时，body getter 也被隐式地注解为 `@MainActor`。其次，“.task”修饰符的闭包被注解为继承周围上下文的 Actor 隔离。因此，由于 body getter 被隔离到主要 Actor，task 闭包也会如此。所以在这个闭包中运行的所有代码默认将在主要 Actor 上运行，并且因为“thumbnail” getter 是同步的，它现在同步运行在主线程上。

默认情况下，Swift 并发任务会继承周围上下文的 Actor 隔离。SwiftUI 的 `.task` 修饰符也是同样的行为。有两种方法可以脱离主要 Actor。异步调用一个不绑定到主要 Actor 的函数，可以允许任务离开主要 Actor。在某些情况下这可能不可行。那么，你可以使用 `Task.detached` 显式地将任务从周围的 Actor 上下文中分离出来，但这是一种比较重的方法，创建单独的任务比简单挂起一个现有任务开销更大。当相应的视图消失时，SwiftUI 也会自动取消通过 task 修饰符创建的任务，但这种取消不会传播到新的非结构化任务（如 `Task.detached`）。要了解更多，请查看 WWDC22 的“可视化并优化 Swift 并发”以及关于提升 App 响应性的文档。

因为在我们的例子中，我们已经在异步上下文中，并且让缩略图函数变成非隔离（nonisolated）且异步的很容易，所以我们选择方案一。

这里，我们有缩略图加载代码。问题是，由于继承了 body getter 的主要 Actor 隔离，这个任务将在主要 Actor 上执行，并且由于 thumbnail getter 是同步的，它也将停留在主要 Actor 上。修复方法很简单。我们跳转到 thumbnail getter 的定义，将其改为 async，然后回到我们的视图结构体……

因为我们的 getter 现在是 async 的，我们需要在它前面加上 await。

这应该允许“thumbnail” getter 在 Swift 并发的并发线程池上执行，而不是主线程。让我们试试。我又回到了详情视图，点击“Choose Background”。哇。真快！不仅没有挂起，而且整体加载似乎也更快了。我几乎没看到进度视图。Instruments 证实现在没有挂起了。这里有一些高的 CPU 使用率。我放大来看看。这是缩略图加载现在发生的地方。检查主线程，我们可以确认主线程上的所有任务间隔现在都非常短。向下滚动到其他线程轨道，可以发现我们的 Swift 任务现在正在其他线程上并行执行，而不是串行执行，这更好地利用了我们的多核 CPU。这使我们能够在几百毫秒内计算完所有缩略图，而不是将近 1.5 秒。在这段时间里，主线程始终保持响应，所以我们现在一劳永逸地修复了这个问题。

我们已经调查并修复了一个主线程无响应的问题，该问题是由主线程繁忙引起的，我们通过挂起期间主线程使用大量 CPU 来识别这一点。我们还体验了挂起如何是同步的（当它直接作为用户交互的一部分发生时）或异步的（当先前安排在主线程上的工作导致传入事件被延迟处理时），以及 Instruments 如何检测这两种情况。我们已经通过减少工作量以及将无法减少的其他工作移至后台、只回到主线程更新 UI 这两种方式修复了挂起。但我们还有另一种情况没有研究：主线程被阻塞，在这种情况下主线程将使用非常少的 CPU。其他维度同样适用于主线程被阻塞的情况，但分析这种情况需要其他仪器。

现在我们来看一个例子。

我这里有一个来自另一个挂起的追踪文件。我已经放大了挂起。这是一个很长的挂起；持续了几秒钟。在“Main Thread”轨道中，CPU Usage 图表显示有一些初始的 CPU 使用率，但随后就没有了。这是一个明显的主线程被阻塞的案例。我们之前讨论过 Time Profiler 如何通过采样 CPU 上正在运行的内容来收集数据。

当我们放大时，CPU Usage 图表甚至显示了单个样本。所以这里的每个标记都是 Time Profiler 采集的一个样本。右边还有几个样本，但之后就没了。但是，当我选择一个没有样本的时间范围时，Time Profiler 无法告诉我们发生了什么，因为它在这段时间内没有记录任何数据。所以我们需要一个不同的工具：Thread States 仪器。像之前的其他仪器一样，你可以从 Instruments 库中添加它。我已经再次录制了同样的挂起，这次添加了“Thread State Trace”仪器。

现在这个仪器有了一个新的轨道。但和“Swift Concurrency”仪器一样，我们感兴趣的数据实际上在“线程”轨道里。所以主线程里有一个非常长的“blocked”间隔，超过 6 秒，这解释了我们大部分挂起的持续时间。当我点击它的中间时，Instruments 的时间光标会移动到那里，这也会更新详情区域中的“Narrative”视图，显示此阻塞状态的条目。Narrative 视图讲述了线程的故事；它在做什么、何时做以及为什么做。

对于选定的时间，它告诉我们线程被阻塞了 6.64 秒，因为它正在调用 mach_msg2_trap，这是一个系统调用。右边又是一个回溯视图。但这个回溯不是最重回溯——它不是某种聚合。它是导致线程被阻塞的 mach_msg2_trap 系统调用的精确回溯。函数调用显示为叶节点在底部，其调用栈显示在上面。调用栈告诉我们，系统调用是在分配 MLModel 的结果，而 MLModel 的分配又是因为分配了一个类型为“ColorizingService”的对象，这是作为该 colorizing service 上一个名为“shared”的单例属性的一部分被调用的，而这个属性又是由 body getter 中的一个闭包调用的。如果我们双击那个闭包，我们会再次跳转到 Source Viewer，并可以找到调用它的代码。这行代码看起来很无害，对吧？让我们仔细看看。

我们正在访问 ColorizingService 的 shared 属性，并将其存储到一个局部变量中。但它并不无害，因为 shared 属性在第一次访问时会创建共享的 ColorizingService 实例，而这又启动了整个模型加载机制，从而阻塞了线程。所以你可能会想说，“我们把它移到 await 之后的异步部分里吧。”然而，与直觉相反，这并不能解决问题。await 关键字只适用于后续代码中的异步函数调用。在我们的例子中，“colorize”函数是“async”的。但“shared”属性不是。因为它是一个静态 let 属性，它会在第一次被访问时惰性初始化，并且这个初始化是同步发生的。await 关键字并不能改变这一点，所以同步调用仍然会在主线程上发生。我们可以像修复之前那个例子一样来修复它，通过将 shared 属性也设为 async 来脱离主要 Actor。当你在线程上等待其他地方的工作取得进展时，这通常是可行的。然而，线程被阻塞的另一个常见原因是锁或信号量。关于在使用锁和信号量配合 Swift 并发时需要注意的最佳实践和应避免的事项，请观看我们 WWDC21 的讲座“Swift 并发：幕后探秘”。

在我们结束之前，我想谈谈另一个与主线程被阻塞相关的情况。这是我们刚才看到的追踪。右边是我们刚才调查的主线程被阻塞的挂起。但在它的左边，还有其他一些主线程被阻塞数秒的情况，但 Instruments 没有将其标记为潜在的挂起。这里，主线程只是处于休眠状态，因为没有用户输入。从操作系统的角度来看，它被阻塞了，但它只是在没有事情可做时不运行来节省资源。一旦有输入进来，它就会唤醒并处理它。因此，要判断一个被阻塞的线程是否是响应性问题，要看 Hangs 仪器，而不是线程状态仪器。

所以，主线程被阻塞并不等于主线程无响应。同样，高 CPU 使用率也不意味着主线程无响应。但如果主线程无响应，那就意味着它要么被阻塞了，要么是主线程繁忙。我们的挂起检测会综合考虑所有这些细节，只会标记主线程实际无响应的时间间隔，并将其显示为潜在的挂起。

如果你只从这场讲座中记住一件事，那就是：无论你在主线程上做什么工作，都应该在 100 毫秒内完成，以便将主线程释放出来处理事件。越短越好。要详细分析挂起，Instruments 是你最好的朋友。记住主线程繁忙和被阻塞之间的区别，并记住挂起也可能是由主线程上的异步工作引起的。要修复挂起，你要么减少工作量，要么将工作移到后台。有时，两者都需要。减少工作量通常只是意味着为工作选择正确的 API。一般来说，先进行测量，确认确实存在挂起，然后再进行优化。当然有一些最佳实践，但并发和异步代码也更难调试。你常常会惊讶于那些实际上非常快的功能，以及那些最终变慢的功能。

祝你发现、分析和修复所有挂起的过程愉快。谢谢观看。♪ ♪
