---
title: 探索 SwiftUI 中的并发
session_id: 266
collection: wwdc2025
year: 2025
duration: '24:55'
topics: ['SwiftUI & UI Frameworks', Swift]
group: C · 并发、锁与线程
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2025/266/'
content_hash: 'sha256:31358015bca5cc6f'
translated: true
---

# 探索 SwiftUI 中的并发

<sub>WWDC2025 · 24:55 · SwiftUI & UI Frameworks、Swift</sub>

探索 SwiftUI 如何借助 Swift 并发构建安全且响应迅速的应用。深入了解 SwiftUI 如何默认使用主要 Actor（Main Actor）……

> [!note] 归档理由
> SwiftUI 中的并发与主要 Actor

## 章节

- [引言](/videos/play/wwdc2025/266/?time=0)
- [主要 Actor 草甸](/videos/play/wwdc2025/266/?time=133)
- [并发峭壁](/videos/play/wwdc2025/266/?time=437)
- [代码营地](/videos/play/wwdc2025/266/?time=1013)
- [后续步骤](/videos/play/wwdc2025/266/?time=1427)

## 相关资源

- [引言](https://developer.apple.com/videos/play/wwdc2025/266/?time=0)
- [主要 Actor 草甸](https://developer.apple.com/videos/play/wwdc2025/266/?time=133)
- [并发峭壁](https://developer.apple.com/videos/play/wwdc2025/266/?time=437)
- [代码营地](https://developer.apple.com/videos/play/wwdc2025/266/?time=1013)
- [后续步骤](https://developer.apple.com/videos/play/wwdc2025/266/?time=1427)
- [Mutex](https://developer.apple.com/documentation/Synchronization/Mutex)
- [Concurrency](https://developer.apple.com/documentation/Swift/concurrency)
- [将 App 更新为使用 Swift 并发](https://developer.apple.com/documentation/swift/updating_an_app_to_use_swift_concurrency)
- [Swift 编程语言：并发](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/266/7/c7837487-ed14-4560-8c2c-a583596027ca/downloads/wwdc2025-266_hd.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/266/7/c7837487-ed14-4560-8c2c-a583596027ca/downloads/wwdc2025-266_sd.mp4?dl=1)
- [动手实践：使用 Swift 并发提升 App](https://developer.apple.com/videos/play/wwdc2025/270)
- [拥抱 Swift 并发](https://developer.apple.com/videos/play/wwdc2025/268)
- [探索 SwiftUI 动画](https://developer.apple.com/videos/play/wwdc2023/10156)
- [提取颜色的 UI](https://developer.apple.com/videos/play/wwdc2025/266/?time=165)
- [AppKit 和 UIKit 需要 @MainActor：一个示例](https://developer.apple.com/videos/play/wwdc2025/266/?time=355)
- [提取颜色的 UI](https://developer.apple.com/videos/play/wwdc2025/266/?time=402)
- [动画圆圈，配色方案视图的一部分](https://developer.apple.com/videos/play/wwdc2025/266/?time=506)
- [提取颜色的 UI](https://developer.apple.com/videos/play/wwdc2025/266/?time=790)
- [配色方案视图的一部分](https://developer.apple.com/videos/play/wwdc2025/266/?time=827)
- [提取颜色的 UI](https://developer.apple.com/videos/play/wwdc2025/266/?time=1062)
- [当颜色通过滚动出现时为其添加动画](https://developer.apple.com/videos/play/wwdc2025/266/?time=1135)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎加入。我是你们的导游 Daniel，来自 SwiftUI 团队。我们将一起探索并发（concurrency）的天地，以及 SwiftUI App 的开发。

你们来到这里，是因为听说过那些叫做数据竞争（data-race bug）的危险生物的故事。过去你们自己可能也遇到过一些。我指的是意外的 App 状态、动画出现毛刺（glitchy animation），甚至永久性的数据丢失。但别担心，这次旅行 100% 安全。因为有了 Swift 和 SwiftUI，我们正把这些数据竞争动物远远甩在身后。SwiftUI 以多种方式并发运行你的代码。在这次旅程中，你将学会如何通过 SwiftUI API 中的并发标注（concurrency annotation）来识别它们。最后，我希望你们在未来的 SwiftUI App 冒险中更加自信，无所畏惧。

Swift 6.2 引入了一种新的语言模式，它会隐式地将模块中的所有类型用 `@MainActor` 标注。我们在此次旅程中看到的一切，无论是否使用这种新模式都适用。这次旅程包含三个景点。我们将从主要 Actor 的美丽草甸开始，欣赏 SwiftUI 如何将主要 Actor 作为应用程序的编译时和运行时默认值。

然后我们将访问并发峭壁，探索 SwiftUI 如何通过将工作从主线程（main thread）卸除来帮助 App 避免 UI 卡顿（hitch），同时保护我们免受真实场景中的数据竞争 bug 的侵扰。

最后，我们将抵达营地，安顿下来，并思考你的并发代码与 SwiftUI API 之间的关系。

让我们前往第一站，主要 Actor 草甸。在我们的旅程中，我想收集一些自然灵感的配色方案，所以我为此构建了一个 App。拍照后，我可以选择想要的颜色数量，然后按下“提取（Extract）”按钮。App 会从照片中挑选出互补色，并显示在屏幕上。

我可以向下滚动查看所有提取的配色方案，并选择我最喜欢的一个导出。

对于提取 UI，我创建了一个结构体 `ColorExtractorView`。它遵循 SwiftUI 的 `View` 协议，该协议声明了 `@MainActor` 隔离（isolation）。

Swift 使用数据隔离（data isolation）来理解并验证所有可变状态（mutable state）的安全性。在整个旅程中，我们会遇到许多类似的并发概念。如果你不熟悉 Swift 并发或只是需要复习，请观看“拥抱 Swift 并发”讲座。在 SwiftUI 中，`View` 在 `@MainActor` 上被隔离，而我让我的结构体遵循 `View`。因此，`ColorExtractorView` 变成了 `@MainActor` 隔离。这条虚线表示推断隔离（inferred isolation），意思是，这个标注在编译时是隐含的，但它实际上不是我写的代码的一部分。整个类型在 `@MainActor` 上被隔离，意味着它的所有成员也都被隐式隔离。

这包括实现 `View` 要求的 `body` 属性，以及我声明的其他成员，比如这个 `@State` 变量。

聚焦视图的 `body`，我正在引用其他成员属性，例如 `model` 的 `scheme`，或 `model` 的 `colorCount` 的绑定（binding）。编译器允许这样做，因为共享的 `@MainActor` 隔离保证了这些访问是安全的。这也感觉很直观。

`@MainActor` 是 SwiftUI 的编译时默认值。这意味着大部分时间，我可以专注于构建 App 功能，而不必过多考虑并发问题。我无需为了并发目的而标注代码。它自动就是安全的。

为了给更多代码腾出空间，我将隐藏这些推断隔离。

这种带有 `@MainActor` 的编译时默认值，扩展到了我视图中的同步代码之外。

我的数据模型的类型不需要任何 `@MainActor` 标注。

因为我在视图的声明内部实例化了模型，Swift 会确保模型实例被正确隔离。

这个 `SchemeContentView` 有一个点击手势（tap gesture），用于启动颜色提取的工作。颜色提取函数是异步的，所以我使用了一个 `Task` 来切换到异步上下文，以便调用它。

由于视图 body 是 `@MainActor` 隔离的，这也使我给这个 `Task` 的闭包（closure）在主线程上运行，这非常方便。`@MainActor` 隔离是 SwiftUI 的编译时默认值。它使得编写视图方便且易于上手。但是，还有另一个非常实际的原因。来自 AppKit 和 UIKit 的 API 都采用 `@MainActor` 隔离。SwiftUI 与这些框架（framework）无缝互操作。例如，`UIViewRepresentable` 协议细化了 `View` 协议。与结构体类似，这使 `UIViewRepresentable` 在 `@MainActor` 上隔离。

因此，遵循 `UIViewRepresentable` 的类型也是一个 `View`。因此，它是 `@MainActor` 隔离的。`UILabel` 的初始化方法要求 `@MainActor` 隔离。这在我的 `makeUIView` 中可行，因为 `makeUIView` 是我 `@MainActor` 隔离的 `Representable` 类型的成员。

无需用 `@MainActor` 标注它。SwiftUI 用 `@MainActor` 标注其 API，因为这反映了它实现的默认运行时行为。

这些标注是框架在运行时期望语义（semantics）的下游体现。SwiftUI 的并发标注表达了其运行时语义。这看起来与我们之前看到的编译时便利性似乎有细微差别，但这是根本性的。我们马上会看到另一个加强这个想法的例子。

好了各位，下一站将会很激动人心。请确保你系好安全带，并固定好电子设备。

随着你在 App 开发过程中引入更多功能，如果主线程有太多工作要做，App 可能会开始出现掉帧（frame drop）或卡顿的问题。你可以使用任务（task）和结构化并发（structured concurrency）将计算从主线程卸除。我们的讲座“使用 Swift 并发提升 App”提供了改善 App 性能的一系列实用技巧。请务必观看。

本次旅程的重点是 SwiftUI 如何利用 Swift 并发来让你的 App 获得更好的性能。

过去，SwiftUI 团队曾透露，内置动画会使用后台线程（background thread）来计算它们的中间状态。

让我们通过检查 `SchemeContentView` 中的这个圆圈来回顾一下。

当颜色提取工作开始和结束时，圆圈会变大，然后通过动画缩小回原来的大小。

为此，我使用了一个响应 `isLoading` 属性的 `scaleEffect`。

这个动画的每一帧都需要一个介于 1 和 1.5 之间的不同缩放值。像这样的缩放值，以及动画数值（animated value），都涉及复杂的数学运算。逐帧计算大量这样的值可能会很昂贵。因此，SwiftUI 会在后台线程上执行此计算，这样主线程就有更多容量处理其他事情。

这种优化也适用于你实现的 API。

没错。有时候，SwiftUI 会在主线程之外运行你的代码。但别担心，这并不复杂。SwiftUI 是声明式（declarative）的。与 UIView 不同，遵循 `View` 协议的结构体不是一个必须在内存中占据固定位置的对象。

在运行时，SwiftUI 会为该视图创建一个独立的表示（representation）。

这个表示为多种优化提供了机会。其中一个重要的优化是在后台线程上评估视图表示的部分内容。

SwiftUI 保留此技术用于代表你进行大量计算的场合。例如，大多数情况下，它涉及一些高频率的几何计算（geometry calculation）。`Shape` 协议就是一个例子。

`Shape` 协议要求一个返回路径（path）的方法。我做了一个自定义的楔形形状（wedge shape）来代表我色轮中提取的颜色。它实现了那个 `path` 方法。

每个楔形都有不同的方向。在这个楔形形状做动画时，我编写的 `path` 方法会从后台线程被调用。

另一种 SwiftUI 代表你运行的自定义逻辑是闭包参数。

圆圈中间是这些模糊（blur）的文字。为了实现这一点，我在 SwiftUI 的 `Text` 上使用了 `visualEffect`。

当 `pulse` 值在 `true` 和 `false` 之间切换时，它会改变两个值之间的模糊半径（blur radius）。视图修饰符 `visualEffect` 接受一个闭包，用于定义对目标视图（即文字）的效果。视觉效果可能变得花哨且渲染昂贵。因此，SwiftUI 可以选择从后台线程调用这个闭包。

所以这是两个可能从后台线程调用你代码的 API。让我们快速再看几个。

`Layout` 协议可能会在主线程之外调用其要求的方法。并且类似于 `visualEffect`，`onGeometryChange` 的第一个参数是一个可能从后台线程被调用的闭包。

这种使用后台线程的运行时优化已经存在了很长时间。SwiftUI 可以使用 `Sendable` 标注向编译器以及你表达这种运行时行为或语义。再次强调，SwiftUI 的并发标注表达了其运行时语义。

在单独的线程上运行你的代码可以解放主线程，从而使你的 App 响应更迅速。而 `Sendable` 关键字在这里是为了提醒你，当你需要从 `@MainActor` 共享数据时，可能存在的竞态条件（data-race condition）。

可以把 `Sendable` 想象成悬崖边小径上的警告牌，上面写着“危险！不要在这里竞速！”嗯，这个描述可能有点太夸张了。实际上，Swift 会可靠地发现代码中任何潜在的竞态条件，并通过编译器错误来提醒你。避免数据竞争条件的最佳策略是根本不在并发任务之间共享数据。

当 SwiftUI API 要求你编写一个可发送（sendable）的函数时，框架会将你需要的大部分变量作为函数参数提供给你。这里有一个简单的例子。

之前，`ColorExtractorView` 中有一个我没展示的细节。得益于这个 `EqualWidthVStack` 类型，色轮和滑块具有相同的宽度。

`EqualWidthVStack` 是一个自定义布局（layout）。它如何进行布局不是我们关注的重点。这里的关键是，我能够使用 SwiftUI 传入的参数进行所有这些复杂的计算，而无需触碰任何外部变量。

但是，如果我确实需要访问某个可发送函数外部的变量呢？在 `SchemeContentView` 中，我需要在 `visualEffect` 中使用状态 `pulse`。但是，Swift 表示存在潜在的数据竞争条件。

让我们拿出望远镜，放大看看编译器错误在告诉我们什么。

`pulse` 变量是 `self.pulse` 的简写。这是在可发送闭包中共享一个 `@MainActor` 隔离的变量时的常见情况。

`Self` 是一个视图。它在主要 Actor 上被隔离。这是我们的起点。从这里开始，我们的最终目标是访问可发送闭包中的 `pulse` 变量。要实现这一点，必须发生两件事。首先，值 `self` 必须跨越从主要 Actor 到后台线程代码区域的边界。

在 Swift 中，我们称之为将变量 `self` 发送（sending）到后台线程。这要求 `self` 的类型是 `Sendable` 的。

现在 `self` 已经出现在正确的位置，我们想在非隔离（nonisolated）区域读取它的属性 `pulse`。编译器不允许这样做，除非属性 `pulse` 没有被隔离到任何 Actor。

再看一下代码，由于 `self` 是一个 `View`，它受到 `@MainActor` 的保护。

所以编译器认为它是 `Sendable` 的。

因此，Swift 对于 `self` 的这个引用从其 `@MainActor` 隔离穿越到 `Sendable` 闭包这一事实没有意见。

所以，实际上，Swift 是在警告我们试图访问 `pulse` 属性。当然，我们知道作为 `View` 的成员，`pulse` 是 `@MainActor` 隔离的。

所以编译器告诉我，即使我可以把 `self` 发送进来，访问其 `@MainActor` 隔离的属性 `pulse` 也是不安全的。

要修复这个编译错误，我可以避免通过视图的引用来读取该属性。我正在编写的视觉效果不需要这个视图的整个值。它只想知道 `pulse` 是 `true` 还是 `false`。我可以在闭包的捕获列表（capture list）中创建 `pulse` 变量的一个副本，然后引用这个副本。这样，我就不再需要将 `self` 发送到闭包中了。

我发送的是 `pulse` 的一个副本，它是可发送的，因为 `Bool` 是一个简单的值类型。

这个副本只存在于这个函数的作用域内，所以在这里访问它不会引起任何数据竞争问题。

在那个例子中，我们无法在可发送闭包中访问 `pulse` 变量，因为它受全局 Actor（global actor）的保护。使这可行的另一个策略是将我们要读取的所有内容都设为非隔离的。

好了，各位，你们已经到达营地了。让我们坐下来谈谈如何组织你的并发代码。

有经验的 SwiftUI 开发者可能已经注意到，大多数 SwiftUI 的 API，比如按钮（`button`）的动作回调（action callback），是同步（synchronous）的。要调用你的并发代码，你首先需要使用 `Task` 切换到异步上下文。

但是为什么 `Button` 不接受异步闭包呢？同步更新对于良好的用户体验很重要。如果你的 App 有长时间运行的任务，而用户必须等待结果，这一点尤其重要。

在用一个异步函数启动一个长时间运行的任务之前，更新你的 UI 以指示任务正在进行中是很重要的。这个更新应该是同步的，特别是当它需要触发一些对时间敏感的动画时。

想象一下，如果我让一个语言模型帮我提取颜色。那个提取过程会需要一段时间。所以在我的 App 中，我使用 `withAnimation` 来同步触发各种加载状态。当任务完成时，我通过另一个同步的状态更改来逆转这些加载状态。

SwiftUI 的动作回调接受同步闭包，这对于设置 UI 更新（比如我的加载状态）是必需的。另一方面，异步函数需要额外的考虑，特别是当你在处理动画时。现在让我们来探讨一下。

在我的 App 中，我可以向上滚动以显示之前的配色方案历史。当每个方案出现在屏幕上时，我希望它们的颜色通过一些动画显现出来。视图修饰符 `onScrollVisibilityChange` 在配色方案出现在屏幕上时给我事件。一旦发生这种情况，我将一个状态变量设置为 `true` 来触发动画，这会导致每个颜色的 Y 偏移量通过动画更新。

作为一个 UI 框架，为了在每一帧都创造出丝滑流畅的交互，SwiftUI 需要面对设备要求特定屏幕刷新率这个现实。

当我希望我的代码对连续的像滚动这样的手势做出反应时，这是一个重要的背景信息。让我们把这些代码放在时间线上。

我将用这个绿色三角形来标记 SwiftUI 调用 `onScrollVisibilityChange` 的时刻。蓝色圆圈标记我通过状态变更触发动画的时刻。

在这种设置下，这种变更是否与手势回调发生在同一帧上，会对视觉效果产生很大影响。

假设我想在我动画变更之前添加一些异步工作。我将用一个橙色线标记异步工作开始的时刻，并对其执行 `await`。在 Swift 中，`await` 一个异步函数会创建一个挂起点（suspension point）。

`Task` 接受一个异步函数作为参数。

当编译器看到 `await` 时，它会将异步函数分成两部分。

执行完第一部分后，Swift 运行时可以暂停这个函数，并在 CPU 上做一些其他工作。这可以持续任意长的时间。然后运行时在原来的异步函数上恢复执行，并执行它的后半部分。

对于函数中的每个 `await` 出现，这个过程可以重复进行。

回到我们的时间线，这个暂停可能意味着我的任务闭包要过很久才能恢复执行，从而错过了设备规定的刷新截止时间（refresh deadline）。

对用户来说，这意味着我的动画看起来滞后且脱节。因此，异步函数中的变更可能无法帮助你实现目标。

SwiftUI 默认提供同步回调。这有助于避免异步代码的意外暂停。在同步动作闭包中更新 UI 很容易正确完成。你总是可以选择使用 `Task` 来进入异步上下文。

像动画这样对时间敏感的逻辑需要 SwiftUI 的输入和输出是同步的。可观察属性（observable property）的同步变更和同步回调是与框架交互最自然的方式。出色的用户体验不一定需要涉及大量自定义并发逻辑。同步代码是许多 App 很好的起点和终点。

另一方面，如果你的 App 做了很多并发工作，试着找到 UI 代码和非 UI 代码之间的边界。最好将异步工作的逻辑与视图逻辑分开。

你可以使用一段状态作为桥梁。这个状态将 UI 代码与异步代码解耦。

它可以启动异步任务。

当一些异步工作完成时，对状态执行同步变更，以便你的 UI 可以响应此更改而更新。这样，UI 逻辑主要是同步的。

作为额外的好处，你会发现为你的异步代码编写测试更容易，因为它现在独立于 UI 逻辑了。

你的视图仍然可以使用 `Task` 来切换到异步上下文。

但尽量保持这个异步上下文中的代码简单。它的作用是告知模型某个 UI 事件。找到需要大量时间敏感性更改的 UI 代码和长时间运行的异步逻辑之间的边界，是改善 App 结构的好方法。它可以帮助你保持视图的同步性和响应性。同样重要的是组织好非 UI 代码。有了我在这个营地展示给你的技巧，你将拥有更大的自由度来这样做。

Swift 6.2 提供了一个很好的默认 Actor 隔离设置。如果你有一个现有的 App，可以试试看。你将能够删除大部分 `@MainActor` 标注。

Mutex 是使类（class）可发送的重要工具。查阅其官方文档来了解如何使用。

挑战一下自己，为你 App 中的异步代码编写一些单元测试。看看你是否能在不导入 SwiftUI 的情况下做到。

好了，各位。这就是 SwiftUI 如何利用 Swift 并发来帮助你构建快速且无数据竞争的 App。当我们结束这次旅程时，我希望你已经为 SwiftUI 中的并发建立了一个扎实的心智模型。

感谢你们的参与，祝你们有无数精彩的冒险。
