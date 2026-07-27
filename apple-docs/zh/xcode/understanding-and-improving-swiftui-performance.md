---
title: 了解并提升 SwiftUI 性能
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/understanding-and-improving-swiftui-performance
source_url: 'https://developer.apple.com/documentation/xcode/understanding-and-improving-swiftui-performance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/understanding-and-improving-swiftui-performance.json'
content_hash: 'sha256:b0a9e31daa5c0754'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [性能与指标](performance-and-metrics.md)

# 了解并提升 SwiftUI 性能

<sub>文章</sub>

识别并解决耗时过长的视图更新，并降低更新频率。

## 概述

[SwiftUI](../swiftui.md) 实现了一种构建用户界面的声明式方法。你描述你 App 的 UI，以及它如何依赖于 App 的数据和环境。SwiftUI 会计算代表 UI 的视图，并根据用户的操作以及视图依赖项的变化来更新 UI，例如：

- 视图的状态
- 环境
- [Observable](../observation/observable.md) 模型数据

为了让使用你 App 的用户获得响应灵敏的体验，你的 App 需要快速计算其视图主体。运行耗时过长的视图主体，或者更新过于频繁的视图，会消耗系统原本可以用于其他地方的资源，从而降低整体系统效率。系统要求视图在系统渲染屏幕上下一个显示帧之前完成更新。如果视图未能及时完成更新，就会在你 App 的 UI 中造成卡顿，让用户在使用你的 App 时体验不佳。有关更多信息，请参阅[提升 App 响应速度](improving-app-responsiveness.md)。

使用 Instruments 检测你 App 中耗时过长的视图主体计算和频繁的视图更新，并识别出你 App 中导致这些问题的代码。使用常见的 SwiftUI 模式来解决你发现的问题。

### 了解你 App 如何使用 SwiftUI

按照以下步骤追踪你 App 对 SwiftUI 的使用情况：

1. 在 Xcode 中，选择 Product \> Profile，以构建并在 Instruments 中打开你的 App。
2. 选择 SwiftUI 模板。
3. 点按 Record（红色圆点）以开始一次延迟录制。
4. 与你想测试的 App 功能进行交互。
5. 在 Instruments 中，按下 Stop Recording。

Instruments 时间线会显示你 App 中代码的时间性能分析，并与一条 SwiftUI 轨道并列展示。

SwiftUI 轨道包含多条子轨道，用于显示你 App 引发的与 SwiftUI 工作相关的事件：

- **Update Groups** — 这条子轨道概览了 SwiftUI 为你的 App 计算更新所花费的时间。
- **Long View Body Updates** — 这条子轨道会为你 App 中运行时间超过 500 微秒的 SwiftUI 视图主体计算显示橙色线条，为运行时间超过 1000 微秒的计算显示红色线条。
- **Long Platform View Updates** — 这条子轨道显示的是绘制 AppKit 视图（你的 macOS App 在 SwiftUI 中承载的视图）或 UIKit 视图（你的 iOS、iPadOS 或 Mac Catalyst App 在 SwiftUI 中承载的视图）时耗时过长的计算。
- **Other Long Updates** — 这条子轨道显示 SwiftUI 为渲染你的视图而执行的其他耗时过长的操作，包括几何和文本布局计算。

Hitches 时间线报告的是你的 App 未能及时准备好视图更新、导致系统无法将更新后的 UI 渲染到屏幕上的情况。

当你选择 SwiftUI 时间线时，详情视图会显示你 App 中所有 SwiftUI 更新的摘要。Instruments 会按模块、视图名称和类别来组织这些更新。在你试用 App 各项功能的过程中，使用这些信息来了解你 App 中的视图与系统框架中的视图分别花费了多少时间进行更新。

### 改进耗时过长的视图主体计算

点按 SwiftUI instrument 时间线中的展开三角形，展开 SwiftUI 时间线子轨道。View Body Updates、Platform View Updates 和 Other Updates 这几条子轨道会为你 App 中的每个模块显示各自独立的时间线，这样你就能识别出更新耗时过长的视图究竟属于你 App 的代码、第三方 SDK，还是系统。

按住 Control 点按时间线中某次耗时过长的视图主体更新，选择 Set Inspection Range and Zoom，将时间线和详情视图聚焦到该次更新上。使用 Time Profiler instrument 来识别你的 App 在这次长时间更新期间运行了哪些代码。点按时间线中的 Time Profiler 子轨道，即可查看该次长时间更新期间运行的函数调用树。切换到 Flame Graph 视图，可获得另一种可视化方式。

单次长时间更新在 Time Profiler instrument 中可能没有足够的采样，不足以帮你确定 App 中正在运行的代码。在这种情况下，请在 Instruments 中录制你的 App 时重复触发这次长时间更新，并使用该更新的多个实例来识别导致这次更新运行时间过长的 App 代码。按照以下步骤，将调用树或火焰图筛选为同一次更新的所有实例：

1. 点按 Time Profile 子轨道时间线中所选范围之外的区域，清除已选定的范围。
2. 在详情视图中，按住 Control 点按 `MySwiftUIView.body`，选择 Show Calls Made by `MySwiftUIView.body`。

要重置该筛选条件，请点按 Instruments 底部栏中的 Callers/Callees，然后选择 Clear Selection。

导致视图主体更新耗时过长的一个常见原因，是在视图的 [body](../swiftui/view/body-8kl5o.md) 属性中执行开销较大的计算。正确的做法是，以异步方式执行该计算，并缓存结果，以避免每次视图需要使用该计算结果时都重复这项工作。

### 降低视图更新的频率

并非所有性能问题都是由耗时过长的更新引起的。有时，某个 App 会产生一连串更新，其中每次更新本身都很短暂，但序列中大量的更新会让 SwiftUI 做大量工作，并长时间保持活跃状态。使用 Update Groups 时间线来识别那些长时间保持活跃、但并非由耗时过长的更新引起的更新组。

按住 Control 点按某个更新组，选择 Set Inspection Range，将详情组聚焦到该组上。使用 Summary: All Updates 视图中的信息，来识别哪些视图是该组更新的一部分，以及更新的次数。

> [!note] 注意
> 你可能需要手动调整检查范围的起始位置，以纳入那些引发本次更新、且发生在该更新组开始之前的事件。

将指针悬停在某次更新上，然后点按出现的箭头，选择 Show Causes。详情视图会显示该组中的更新列表，以及一张图形化展示——展示导致每次更新的事件，以及每次更新所引发的后续效果。图中的节点代表产生或接收更新的对象；例如，视图主体、环境对象和事务。图中的边代表节点之间的因果关系；例如，从某个 [Observable()](<../observation/observable().md>) 对象，到在其 `body` 中读取该对象某个属性的视图之间的连接。

点按某个节点，即可在检查器中查看关于该节点的更多信息。蓝色节点代表由你 App 中的代码定义的对象。灰色节点代表由系统定义的对象。

点按某条边，即可在检查器中查看关于该边所代表更新的更多信息。检查器会显示 Instruments 采集到的关于该次更新的附加信息，例如你视图属性的变化情况。

> [!tip] 提示
> 为了简化因果关系图的呈现方式，Instruments 有时会在图中的多个位置表示同一批节点和边。当你点按某个节点或边、在检查器中查看更多信息时，Instruments 会高亮显示所有代表同一个对象或同一次更新的节点和边。

将因果关系图中发生的事件，与你对视图用途的理解进行比对，以识别不必要的更新，或者虽然确有必要、但发生得过于频繁的更新。导致更新过于频繁的常见原因包括：

- 你的视图观察了某个对象上的属性，而该对象还有其他可观察属性，并且只要其他属性中的任意一个发生变化，视图就会更新。将你的可观察对象迁移为使用 [Observable()](<../observation/observable().md>) 宏，该宏只会追踪视图实际读取的属性，并且只在这些属性发生更新时才发出变化事件。有关更多信息，请参阅[从 Observable Object 协议迁移到 Observable 宏](../swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro.md)。
- 响应某次更新的视图，会以并不构成 UI 有意义变化的方式，导致其所包含的视图发生更新；例如，某个使用 [GeometryReader](../swiftui/geometryreader.md) 的自定布局，会为其所包含的视图重新计算滚动几何信息，即便某些更新并未导致任何滚动变化，也照样如此。在你 App 的视图层级结构中，找到另一个可以接收该更新、且只对其所包含视图做出相关变化的视图。

对于需要响应频繁更新而进行更新的视图，请按照上文[改进耗时过长的视图主体计算](#Improve-long-running-view-body-computations)中的步骤，提升这些更新的效率。

Instruments 中的因果关系图针对每条边只显示一个变化的属性。在你做出改动以降低视图更新频率后，请在 Instruments 中录制一次新的记录，以确定更新频率是否已经降低，或者是否还有另一个属性更新或事件同样会导致相同的视图更新。

识别出最频繁导致你视图更新的事件类型，并优先开展性能工程工作，先降低该事件的发生频率。

### 移除不必要的更新

如果一张因果关系图，起点是代表你 App 中代码的节点（蓝色节点），产生的事件影响了框架代码（灰色节点），终点又落回你 App 中的某个节点（另一个蓝色节点），这就表明：你的 App 产生了一个事件，而这个事件本应由你的 App 自行响应，却由 SwiftUI 框架进行了中转。

通过降低引发这些更新的事件发生频率，来修改你的代码以降低更新频率。例如，如果你使用 [onGeometryChange(for:of:action:)](<../swiftui/view/ongeometrychange(for_of_action_).md>) 在视图大小发生变化时更新子视图的布局，可以先测试变化幅度是否超过某个阈值，再决定是否更新布局。

### 采用高效的 SwiftUI 设计模式

保持你的视图主体运行迅速。视图主体中的代码需要高效，并且只依赖有限的依赖项，包括状态和环境对象。

将业务逻辑和其他与 UI 无关的工作从视图中移到模型类型里，因为 SwiftUI 会频繁重新创建视图，并重新计算视图主体。因此，避免在你的 [View](../swiftui/view.md) 初始化方法以及以下方法中执行复杂、耗时较长的任务：

- [body](../swiftui/view/body-8kl5o.md)
- [onAppear(perform:)](<../swiftui/view/onappear(perform_).md>)
- [onChanged(_:)](<../swiftui/gesture/onchanged(__).md>)
- 任何其他可以修改视图状态的修饰符

考虑复杂布局对性能的影响。布局读取器，例如 [GeometryReader](../swiftui/geometryreader.md) 和 [ScrollViewReader](../swiftui/scrollviewreader.md)，会观察其父视图中的布局变化，以重新计算自身的布局。将不影响布局的、带有状态依赖的视图移动到单独的视图层级结构中，以缩小同时进行布局和状态更新的范围。

避免在视图中存储闭包。闭包可能会从你的父视图中捕获额外的状态，从而使该视图更新得更频繁。每当闭包所捕获的任何状态发生变化时，SwiftUI 都需要重新计算该闭包的结果。如果闭包捕获了 `self`——无论是显式捕获，还是因为它引用了该视图的某个属性——那么每当该视图的任何属性发生变化时，SwiftUI 都会重新计算该闭包的结果。当你的视图初始化方法接受一个用于为该视图构建子视图的闭包时，请在初始化方法中直接调用该闭包，这样你只需存储其返回值。不要将该闭包标记为 [@escaping](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/#Escaping-Closures)。

对于操作闭包——例如你传给 [Button](../swiftui/button.md) 的闭包——或者需要参数的闭包——例如你传给 [ForEach](../swiftui/foreach.md) 的闭包——你不需要这样做。不过，这类闭包仍然可能导致过多的更新，因此请按照上文[降低视图更新的频率](#Reduce-the-frequency-of-view-updates)中的步骤操作，确保你的 App 高效地调用其闭包。

## 另请参阅

### 响应速度

- [分析你已发布 App 中的响应速度问题](analyzing-responsiveness-issues-in-your-shipping-app.md) — 识别用户遇到的响应速度问题，并使用 Xcode Organizer 中的挂起和卡顿数据，确定哪些问题最需要优先修复。
- [提升 App 响应速度](improving-app-responsiveness.md) — 通过消除 App 中的挂起和卡顿，打造响应灵敏的用户体验。
- [了解用户界面响应速度](understanding-user-interface-responsiveness.md) — 通过检查事件处理和渲染循环，让你的 App 更具响应性。
- [了解你 App 中的挂起](understanding-hangs-in-your-app.md) — 通过检查主线程和主运行循环，确定用户交互延迟的原因。
- [了解你 App 中的卡顿](understanding-hitches-in-your-app.md) — 通过检查渲染循环，确定动作中断的原因。
- [及早诊断性能问题](diagnosing-performance-issues-early.md) — 在开发和测试期间，使用 Xcode 中的 Thread Performance Checker 工具，诊断你 App 中潜在的性能问题。
- [缩短你 App 的启动时间](reducing-your-app-s-launch-time.md) — 通过最大限度减少启动所花费的时间，为你的 App 打造更具响应性的体验。
- [减少你 App 中的终止次数](reduce-terminations-in-your-app.md) — 通过解决常见的终止原因，尽量降低系统停止你 App 的频率。
