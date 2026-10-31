---
title: '深入探索 SwiftUI 中的惰性叠放与滚动'
session_id: 321
collection: wwdc2026
year: 2026
duration: '21:10'
topics: [Design, 'SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2026/321/'
content_hash: 'sha256:d390cec3f1e43452'
translated: true
---

# 深入探索 SwiftUI 中的惰性叠放与滚动

<sub>WWDC2026 · 21:10 · Design、SwiftUI & UI Frameworks</sub>

探索 SwiftUI 中惰性叠放的内部工作原理。我们将探讨 LazyVStack 和 LazyHStack 如何估算尺寸、惰性加载子视图……

> [!note] 归档理由
> 惰性栈与滚动的按需构建机制

## 章节

- [简介](/videos/play/wwdc2026/321/?time=0)
- [布局](/videos/play/wwdc2026/321/?time=84)
- [子视图加载](/videos/play/wwdc2026/321/?time=553)
- [预取](/videos/play/wwdc2026/321/?time=795)
- [编程式滚动](/videos/play/wwdc2026/321/?time=1060)
- [后续步骤](/videos/play/wwdc2026/321/?time=1195)

## 相关资源

- [简介](https://developer.apple.com/videos/play/wwdc2026/321/?time=0)
- [布局](https://developer.apple.com/videos/play/wwdc2026/321/?time=84)
- [子视图加载](https://developer.apple.com/videos/play/wwdc2026/321/?time=553)
- [预取](https://developer.apple.com/videos/play/wwdc2026/321/?time=795)
- [编程式滚动](https://developer.apple.com/videos/play/wwdc2026/321/?time=1060)
- [后续步骤](https://developer.apple.com/videos/play/wwdc2026/321/?time=1195)
- [使用惰性叠放视图分组数据](https://developer.apple.com/documentation/SwiftUI/Grouping-Data-with-Lazy-Stack-Views)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2026/321/5/78830752-d07d-4d89-aeab-94405c084de9/downloads/wwdc2026-321_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2026/321/5/78830752-d07d-4d89-aeab-94405c084de9/downloads/wwdc2026-321_sd.mp4?dl=1)
- [代码演练：在 SwiftUI 中构建强大的拖放](https://developer.apple.com/videos/play/wwdc2026/271)
- [使用 SwiftUI 组合自定义布局](https://developer.apple.com/videos/play/wwdc2022/10056)
- [SwiftUI 中的叠放、网格和大纲](https://developer.apple.com/videos/play/wwdc2020/10031)
- [Origami App](https://developer.apple.com/videos/play/wwdc2026/321/?time=83)
- [水平滚动展示](https://developer.apple.com/videos/play/wwdc2026/321/?time=311)
- [展示部分](https://developer.apple.com/videos/play/wwdc2026/321/?time=390)
- [滚动效果](https://developer.apple.com/videos/play/wwdc2026/321/?time=424)
- [滚动效果](https://developer.apple.com/videos/play/wwdc2026/321/?time=456)
- [滚动到展示按钮](https://developer.apple.com/videos/play/wwdc2026/321/?time=500)
- [滚动到展示按钮](https://developer.apple.com/videos/play/wwdc2026/321/?time=531)
- [一个已解析的子视图](https://developer.apple.com/videos/play/wwdc2026/321/?time=569)
- [多个已解析的子视图](https://developer.apple.com/videos/play/wwdc2026/321/?time=603)
- [动态数量的子视图](https://developer.apple.com/videos/play/wwdc2026/321/?time=652)
- [在视图层过滤](https://developer.apple.com/videos/play/wwdc2026/321/?time=706)
- [在数据层过滤](https://developer.apple.com/videos/play/wwdc2026/321/?time=735)
- [可选值解包](https://developer.apple.com/videos/play/wwdc2026/321/?time=755)
- [可选值解包](https://developer.apple.com/videos/play/wwdc2026/321/?time=768)
- [加载更多内容](https://developer.apple.com/videos/play/wwdc2026/321/?time=928)
- [在 onAppear 中设置惰性叠放子视图](https://developer.apple.com/videos/play/wwdc2026/321/?time=953)
- [惰性叠放子视图在 onAppear 之前就绪](https://developer.apple.com/videos/play/wwdc2026/321/?time=974)
- [使用 task 修饰符的加载图](https://developer.apple.com/videos/play/wwdc2026/321/?time=983)
- [在初始化方法中加载](https://developer.apple.com/videos/play/wwdc2026/321/?time=1000)
- [高亮 @State 变量](https://developer.apple.com/videos/play/wwdc2026/321/?time=1036)
- [高亮 @Binding](https://developer.apple.com/videos/play/wwdc2026/321/?time=1053)
- [编程式滚动到展示](https://developer.apple.com/videos/play/wwdc2026/321/?time=1078)
- [动态数量的视图](https://developer.apple.com/videos/play/wwdc2026/321/?time=1104)
- [在数据层过滤](https://developer.apple.com/videos/play/wwdc2026/321/?time=1133)
- [在惰性叠放子视图中使用 onGeometryChange](https://developer.apple.com/videos/play/wwdc2026/321/?time=1156)
- [在惰性叠放子视图中使用自定义布局](https://developer.apple.com/videos/play/wwdc2026/321/?time=1157)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我叫 Rens，我是一名 UI 框架工程师。

惰性叠放是任何显示长篇幅、自定义滚动内容的 SwiftUI App 的核心组件。它们早已是 SwiftUI 的一部分。与许多其他 SwiftUI 组件一样，惰性叠放的强大之处在于它们的简洁性。不同的 SwiftUI 组件可以与许多其他 SwiftUI 组件混合，以构建复杂的 App。例如，从 2027 年的版本开始，你可以使用 reorderable 来拖动并重新排序视图。你可以在《代码演练：在 SwiftUI 中构建强大的拖放》中了解更多。SwiftUI 还允许在列表之外的视图上添加滑动操作。当然，这两者与惰性叠放一起使用时都表现出色。我认为现在是时候进行一次刷新，深入探索惰性叠放与滚动了。我将解释它们如何工作、你能用它们做什么，以及你可能想要避免什么。之后，你将更好地理解惰性叠放的内部机制，能够将其应用到你自己 App 中的惰性叠放。

这个视频将假设你对使用叠放进行 SwiftUI 布局有基本了解。如果你刚接触 SwiftUI，我推荐《SwiftUI 中的叠放、网格和大纲》。

我一直在开发一个折纸 App，它展示制作一些流行折纸作品的步骤。

在这个早期版本中，它只显示制作天鹅的步骤。这里是主视图的设置。我有一个 ScrollView，里面有一个 LazyVStack，其中又包含每个步骤的 StepView。

惰性叠放允许滚动浏览大量步骤，而无需一次性立即加载所有视图。我现在将专注于 LazyVStack。

制作折纸天鹅的三个步骤完全可见。StepView 中步骤 4 的一小部分也可见。

现在，完整的 LazyVStack 比可见的视图大得多。但与 VStack 不同，LazyVStack 不会对不可见的视图进行求值或渲染。LazyVStack 只是从上到下布局其视图，并在可见矩形被填满时停止。如果你向下滚动，LazyVStack 会按需添加视图，以确保可见矩形保持填满；当视图滚动出屏幕时，它们会从惰性叠放中移除。

通过不一次性加载所有视图，LazyVStack 可以比 VStack 更高效。但代价是正确性。由于 LazyVStack 不加载所有视图，屏幕外子视图的高度会被估算。这个估算高度基于之前已放置视图的平均尺寸，以及剩余子视图的估算数量。惰性叠放也对屏幕外视图的变化不知情，因为它们并未加载。

类似地，由于并非所有视图都已加载，它无法找到所有视图的最大宽度。因此 LazyVStack 的理想宽度是其第一个子视图的宽度。在我的折纸 App 中，第一个视图是无限灵活的，所以 LazyVStack 的宽度等于屏幕宽度。

由于 LazyVStack 的高度是估算的而非精确的，它在滚动过程中随着惰性叠放对滚动到屏幕上的新视图布局了解更多而变化。例如，如果你一直滚动到底部，最后的视图比惰性叠放之前放置的其他视图略小，惰性叠放必须调整其最初估算的尺寸以反映这一点。

可见矩形上方的空间也不精确。滚动视图的滚动位置，或者说内容偏移，因此依赖于可见项的估算位置。可见区域上方空间不精确的一个例子，是 iPhone 上的方向变化之后。

StepView 在横屏下比竖屏下更矮。副标题文本通常在横屏下占更少的行。在方向变化期间，惰性叠放会保持步骤 4 的 StepView——最顶层的可见视图——锚定。LazyVStack 尚不知晓前几个 StepView 的确切布局变化，因为它们尚未加载。但当一直滚动回顶部时，惰性叠放必须与滚动视图的顶部对齐。这意味着它必须在途中修正可见区域上方的估算空间。它会以相同的量更新 ScrollView 的内容偏移，以便顶部的内容偏移也是零。

惰性叠放与嵌入的滚动视图协调位置和内容偏移。这样，当估算更新时，滚动视图中可见子视图的相对位置不会改变。

在同一惰性叠放中组合不同类型视图或内容很常见。对于我的折纸 App，我认为如果人们完成作品后能与他人分享照片会很酷。我想把这些照片显示在底部，放在一个水平滚动视图中。我添加了一个 Showcase 视图来显示这些照片。

Showcase 视图有一个水平滚动的 ScrollView，里面有一个 LazyHStack。

这意味着我的 App 现在在外部 LazyVStack 内嵌套了一个 LazyHStack。

像这样在 LazyVStack 中嵌套 LazyHStack 对性能也有好处，因为不是每个人都会滚动这个嵌套的滚动视图来查看额外的视图。

对于 LazyHStack，理想高度，因此它在垂直 ScrollView 中的高度，是其第一个子视图的高度。在我的折纸 App 中，所有照片使用相同高度。但如果每张照片都有一个行数可变的用户描述标签，更长的副标题会被截断。LazyHStack 无法提前知道所有视图中最大的副标题。它还没有加载它们。最佳解决方案是固定视图高度。例如，对于文本，你可以设置行数限制，并为较短的文本预留空间。

但我在想，我折纸 App 中的照片应该更大一点。也许我应该把它们垂直添加到步骤下方。如果我加到一个 section 中，我甚至可以固定 section 标题。

要固定 section 标题，使用 LazyVStack 上的 pinnedViews 参数。

我在 Showcase 视图中添加了新的 Section，并带有一个 header 视图。如果我向下滚动，Showcase 的 section 标题会贴在顶部。

我将讨论一些应避免的模式，以便惰性叠放发挥最佳性能。我将使用我刚添加的照片展示来做到这一点。给照片在滚动进出屏幕时添加滚动过渡效果可能会很酷。

这里，我使用 .scrollTransition 修饰符，给我的步骤在滚动进出屏幕时一个效果。然而，惰性叠放只根据它们的原始位置加载屏幕上的视图。而这里的变换把它们推到了原始 frame 之外。

这导致它们在应该可见时消失，因为惰性叠放认为它们在屏幕外。这里，当你向下滚动时，粉色天鹅过早消失了。

如果你对惰性叠放中的视图应用滚动过渡效果，确保那些通常不可见的视图不会被推入可见矩形。这里，我使用了不同的缩放效果。

这工作正常。一般来说，确保那些通常不可见的视图不会在变换中被推入可见矩形。惰性叠放不会知道这一点。

由于你需要向下滚动一点才能到达 Showcase，我还将添加一个按钮以便快速滚动到那里。

但按钮不应始终可见。我希望它只在滚动视图顶部附近可见。

当某人向下滚动时，它应该消失。

这里，我在滚动视图上使用 .onScrollGeometryChange 来获取绝对内容偏移。

当我滚动超过 100 点时，按钮消失。

这可以工作，但因为惰性叠放的内容偏移是估算的，按钮消失的确切位置在估算变化时可能改变。相反，最好使用滚动视图可见区域中子视图的相对位置。

一种方法是使用 .onScrollTargetVisibilityChange 修饰符。

该修饰符中的闭包在滚动视图可见区域中子视图的可见性变化时被调用。这里，"Scroll to Showcase" 按钮的可见性仅取决于哪些子视图可见，阈值为 80%。

我已经详细介绍了惰性叠放的布局。我说过惰性叠放会在子视图即将进入滚动视图的可见部分时添加它们。然而，惰性叠放单独加载的子视图，并不总是直接对应于你在代码中定义的视图结构体。让我们回到我的原始代码，再看看 ContentView。在这个简单的情况下，StepView 实例和 LazyVStack 看到的子视图之间是一对一的对应。

有一个 ScrollView，ScrollView 有一个 LazyVStack 作为子视图，LazyVStack 有 ForEach 作为子视图。但当然 ForEach 不只是单个视图。

它为每个步骤解析为一个 StepView。在大多数情况下，这些是 LazyVStack 加载的子视图。

但这里，StepView 略微复杂一些。这将很重要。body 包含两个视图，StepDiagram 和 StepInstructions，在 body 的顶层。它们也没有嵌入到另一个布局中，比如 VStack。

在这种情况下，LazyVStack 仍然有 ForEach，它为每个步骤解析为一个 StepView。但就像 ForEach 解析为多个 StepView 一样，每个 StepView 现在也解析为两个视图。LazyVStack 分别求值并加载 StepDiagram 和 StepInstructions。

当然，StepView 仍需要被求值，惰性叠放才能创建其中任何一个。视图也可以解析为动态数量的视图。但那是你需要注意的事情。在这种情况下，StepView 使用 detailLevel 环境值，来检查它是否应该可见。

ForEach 再次为每个步骤解析为一个 StepView。但每个 StepView 现在解析为一个子视图或零个子视图。在这种情况下，给定当前的 detail level，步骤 2 不可见，但第一和第三步骤可见。

这可以工作，惰性叠放的内容被惰性加载，但 StepView 本身可能比你预期的保留更久。

那是因为 LazyVStack 使用索引来寻址可见的子视图。

它现在必须保留较早的 StepView，以防 detailLevel 环境值发生变化，因为那会影响索引。

在 ForEach 中创建多次的叶级子视图，如 StepView，避免创建动态数量的子视图。

因此，使用 detailLevel 环境值来过滤步骤的例子并不是个好主意。

假设 StepView body 的内容中使用了不相关的环境值，如 writingStyle。这个环境值的变化现在可能导致滚动出屏幕的视图的 body 求值，造成不必要的视图更新。惰性叠放也不会释放为 StepView 分配的状态。相反，在数据层过滤。如果你使用 SwiftData，使用 Predicate 来过滤你的 Query。

这里，我在 Predicate 中使用 detailLevel。这使子视图的数量对 LazyVStack 立刻清晰。它不必构造视图来计算视图数量或索引。

注意，在视图 body 中解包可选值有相同的效果。这里，我可选解包一个 apiToken 环境变量。body 仅在 token 不为 nil 时才返回某些内容。

token 是可以由 NetworkClient 模型对象处理的东西。

如果某人未认证，层级中更高的视图可以显示 ContentUnavailableView，而不是首先显示惰性叠放。

由于惰性叠放只在内存中保留其数据的一小部分，它们不需要对其内容执行完整 diff。它们只对可见视图执行最小的更改检查。

惰性叠放并不总是一次性加载子视图。我将讨论预取（prefetching），这是惰性叠放用来提升 App 滚动性能的内部机制。

当你向特定方向滚动，并且惰性叠放的可见部分到达已放置内容的末尾时，惰性叠放已经在把视图添加到屏幕上之前预取视图。预取意味着惰性叠放会在视图可见之前执行显示该视图的部分工作。

滚动时，ScrollView 需要以恒定速率绘制帧。这意味着只有有限的时间可用于执行计算，直到帧截止期限。这项工作包括 ScrollView 更新内容偏移、你的视图在新位置渲染，以及你的 App 可能因内容偏移变化而做的工作。当 ScrollView 包含惰性叠放时，它包括对滚动到屏幕上的视图进行求值、执行布局并渲染它们的工作。但把新视图放到屏幕上可能代价高昂。

如果工作耗时过长，超过截止期限，那将导致掉帧。这在滚动时表现为卡顿，应避免。

预取用于防止这种掉帧。滚动时，惰性叠放已经检查是否有足够的时间在视图滚动到屏幕前执行渲染新子视图的部分工作。

例如，惰性叠放可能能够在即将出现在屏幕上的视图出现之前，求值其 body 并布局它。

当视图最终出现时，大部分工作已经完成，分散在多个帧中。

显示 LazyVStack 中嵌套的 LazyHStack 的工作也可以分散在多个帧中。当视图出现时，调用 onAppear。所以一般来说，视图的 body 在某个时刻被调用，onAppear 稍后——当视图被放置在屏幕上时——被调用。如果滚动方向反转，甚至可能视图的 body 作为预取的一部分被调用，而 onAppear 永远不会被调用。

在惰性叠放中使用 onAppear 对许多事情有用，甚至包括数据加载。一个这样的用例是无限滚动。这里，折纸 App 在你滚动到底部时从网络获取更多照片。最后一个视图，一个 ProgressView，有一个 .onAppear 修饰符。当该视图出现时，获取新页面。

但对每个视图在 onAppear 中加载所有内容并不是个好主意。

在这个例子中，onAppear 用于设置每个视图。视图的尺寸和大部分内容在被放置后完全改变。

预取之前完成的工作将被丢弃，并且必须在视图出现时重新完成。惰性叠放可能还会加载比需要更多的视图，并且滚动可能受到影响，正如我稍后将展示的。

相反，在初始化方法中设置视图，使其在出现前处于合理状态。

即使不是必需的，加载内容在视图出现之前也可能有用。

这里，我使用 task 修饰符在视图出现时从互联网远程加载图。但我实际上可以利用预取来稍微更早地加载它，以便在出现时加载的概率更高。

例如，我可以使用一个 DiagramLoader 可观察对象，连接到缓存。当缓存不包含特定 ID 的数据时，它可以在初始化时立即加载数据。由于它在初始化方法中开始加载图，图将稍微更早地被获取。滚动出屏幕的视图不再被渲染或更新。但它们不会立即从内存中移除。惰性叠放会把这些保留几个更新，以防它们滚动回屏幕上。当视图最终从内存中删除时，状态变量会随之删除。

由于与滚动出屏幕的视图关联的数据将被删除，不要依赖视图状态来保存滚动后仍需保留的数据。这里，StepView 使用一个 isHighlighted 状态变量。但如果视图滚动离开，那个高亮状态将丢失。

相反，把重要状态移动到模型对象，或通过 binding 移动到外部视图，如这里。

你通常在滚动视图中使用惰性叠放。现在我想给你一些技巧，让滚动在惰性叠放中工作良好。早些时候，我给折纸 App 添加了一个按钮，滚动到用户照片的展示。

编程式滚动到该 section 的代码看起来像这样。我使用 ScrollPosition binding 来滚动到 showcase 的 section 标题。

编程式滚动在惰性叠放中工作，即使目标视图不在屏幕上。

滚动到屏幕外视图需要惰性叠放估算其位置。在动画滚动中，惰性叠放每帧更新这个估算位置。然而，有些事情会阻止滚动平滑且快速。例如，这里也有，StepView 中动态数量的视图有性能影响。编程式滚动到带 ID 的视图在每个 ForEach 中的视图总是解析为单个子视图时最高效。在这种情况下，惰性叠放可以查询 ForEach 来找到要滚动到的 ID，而无需构造任何视图。滚动到靠近末尾的子视图也更高效，如果惰性叠放能快速计数其子视图。

如前，与其在视图 body 中用条件过滤视图，你应该在数据层过滤，例如在 Query 上使用 predicate。

编程式滚动如果太多视图在出现在屏幕上后改变布局，也会变得不那么平滑。一个常见模式是使用 onGeometryChange 来设置一个随后在另一个布局过程中使用的 state 值。

这里，StepView 有一个 subtitleHeight 状态变量，通过 subtitle 上的 onGeometryChange 更新。

视图随后再次被求值，并使用 subtitleHeight 来计算图的 frame。这使滚动变得不可靠。惰性叠放测量视图的原始高度，但高度在视图出现后变化，把其他内容推下去。

在这种情况下，如果你不能使用 SwiftUI 的布局原语，使用自定义布局。这里，那个自定义布局是 StepLayout。要了解更多关于使用自定义布局的内容，查看《使用 SwiftUI 组合自定义布局》。

好的，我已经展示了惰性叠放的许多方面。我谈到了它们的布局、视图结构体并不总是解析为单个子视图以及这如何影响惰性叠放、惰性叠放如何预取视图以获得更好的滚动性能，以及它们如何允许编程式滚动到屏幕外视图。一路上，我给出了一些你可以用于自己 App 中惰性叠放的技巧和最佳实践。例如，避免对惰性叠放使用绝对内容尺寸或内容偏移，因为这些是估算的、不稳定的。

避免在叶级视图中使用条件视图内容来过滤数据，因为那可能导致 SwiftUI 视图比预期活得更久。

在可能的情况下，在 onAppear 被调用之前设置好惰性叠放的子视图，以确保预取工作最佳。并且不要在惰性叠放的子视图出现后改变它们的布局，因为那可能把惰性叠放推离目标滚动位置。

理解 SwiftUI 组件工作的某些机制，帮助你在使用它们时更出色。我想，在准备这个视频之后，我现在在制作天鹅方面也更出色了。
