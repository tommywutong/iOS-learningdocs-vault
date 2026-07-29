---
title: 使用 Instruments 优化 SwiftUI 性能
session_id: 306
collection: wwdc2025
year: 2025
duration: '35:36'
topics: [Swift, 'SwiftUI & UI Frameworks', Developer Tools]
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2025/306/'
content_hash: 'sha256:a935712cb497eda6'
translated: true
---

# 使用 Instruments 优化 SwiftUI 性能

<sub>WWDC2025 · 35:36 · Swift、SwiftUI & UI Frameworks、Developer Tools</sub>

了解全新的 SwiftUI instrument。我们将介绍 SwiftUI 如何更新视图，你 App 中的数据变化如何影响这些更新，以及如何……

> [!note] 归档理由
> SwiftUI 性能的 Instruments 实操

## 章节

- [介绍与议程](/videos/play/wwdc2025/306/?time=0)
- [探索 SwiftUI instrument](/videos/play/wwdc2025/306/?time=139)
- [诊断与修复过长的视图 body 更新](/videos/play/wwdc2025/306/?time=260)
- [理解 SwiftUI 更新的原因与影响](/videos/play/wwdc2025/306/?time=1194)
- [下一步](/videos/play/wwdc2025/306/?time=2101)

## 相关资源

- [介绍与议程](https://developer.apple.com/videos/play/wwdc2025/306/?time=0)
- [探索 SwiftUI instrument](https://developer.apple.com/videos/play/wwdc2025/306/?time=139)
- [诊断与修复过长的视图 body 更新](https://developer.apple.com/videos/play/wwdc2025/306/?time=260)
- [理解 SwiftUI 更新的原因与影响](https://developer.apple.com/videos/play/wwdc2025/306/?time=1194)
- [下一步](https://developer.apple.com/videos/play/wwdc2025/306/?time=2101)
- [性能与指标](https://developer.apple.com/documentation/Xcode/performance-and-metrics)
- [使用 Power Profiler 测量 App 的功耗](https://developer.apple.com/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler)
- [理解并改善 SwiftUI 性能](https://developer.apple.com/documentation/Xcode/understanding-and-improving-swiftui-performance)
- [分析 visionOS App 的性能](https://developer.apple.com/documentation/visionOS/analyzing-the-performance-of-your-visionOS-app)
- [改善 App 响应能力](https://developer.apple.com/documentation/Xcode/improving-app-responsiveness)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/306/4/cc55ba18-71e2-4481-8491-3473e650fdcc/downloads/wwdc2025-306_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/306/4/cc55ba18-71e2-4481-8491-3473e650fdcc/downloads/wwdc2025-306_sd.mp4?dl=1)
- [使用 Instruments 优化 CPU 性能](https://developer.apple.com/videos/play/wwdc2025/308)
- [使用 Instruments 分析挂起](https://developer.apple.com/videos/play/wwdc2023/10248)
- [揭开 SwiftUI 性能的神秘面纱](https://developer.apple.com/videos/play/wwdc2023/10160)
- [探索 SwiftUI 动画](https://developer.apple.com/videos/play/wwdc2023/10156)
- [使用 SwiftUI 构建自定义布局](https://developer.apple.com/videos/play/wwdc2022/10056)
- [揭开 SwiftUI 的神秘面纱](https://developer.apple.com/videos/play/wwdc2021/10022)
- [探索 UI 动画卡顿与渲染循环](https://developer.apple.com/videos/play/tech-talks/10855)
- [LandmarkListItemView](https://developer.apple.com/videos/play/wwdc2025/306/?time=527)
- [包含缓存距离字符串的 LocationFinder 类](https://developer.apple.com/videos/play/wwdc2025/306/?time=733)
- [包含收藏按钮的 LandmarkListItemView](https://developer.apple.com/videos/play/wwdc2025/306/?time=1011)
- [ModelData 类](https://developer.apple.com/videos/play/wwdc2025/306/?time=1040)
- [OnOffView](https://developer.apple.com/videos/play/wwdc2025/306/?time=1250)
- [Favorites View Model 类](https://developer.apple.com/videos/play/wwdc2025/306/?time=1761)
- [原因与影响：EnvironmentValues](https://developer.apple.com/videos/play/wwdc2025/306/?time=1894)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好！我是 Instruments 团队的 Jed。我是来自 Apple Music 团队的 Steven。优秀的 App 拥有卓越的性能。你的 App 中运行的任何代码都可能拖慢它的速度。分析你的 App 以找出代码中哪些区域可能是瓶颈，然后解决这些问题，让你的 App 尽可能流畅地运行，这一点很重要。在今天的讲座中，我们将重点关注如何识别你的 SwiftUI 代码成为瓶颈的情况，并向你展示如何帮助 SwiftUI 更高效地工作。首先，你如何知道自己存在性能问题？你可能会注意到的一个症状是你的 App 因为卡顿（hitch）或挂起（hang）而响应性变差。动画可能会暂停或跳跃，或者滚动可能会延迟。识别性能问题的最佳方法是使用 Instruments 对你的 App 进行性能分析。今天，我们将重点诊断使用 SwiftUI 的代码中的性能问题。首先，我们将介绍 Instruments 26 中附带的全新 SwiftUI instrument。接下来，我们将查看一个具有过长视图 body 更新的 App，讨论为什么它们是常见的性能问题，并使用该 instrument 来查找并修复它们。最后，我们将深入探讨 SwiftUI 更新的原因与影响。我们将使用该 instrument 来识别不必要的更新，并向你展示如何移除它们。性能问题的根本原因可能有很多，但今天我们将专注于由你使用 SwiftUI 所引起的问题。

如果你的 App 问题与 SwiftUI 代码无关，我们建议你首先查看“使用 Instruments 分析挂起”和“使用 Instruments 优化 CPU 性能”，以开始识别正在发生的事情。

Steven 和我一直在合作开发一个 App。Steven，你能展示一下我们目前构建的成果吗？谢谢，Jed！这个 App 叫做 Landmarks，它展示了来自世界各地的一些最令人惊叹的地点。每个地标都显示它离我当前所在位置的距离，这样我就可以畅想接下来要去哪里，无论是需要长途飞行才能到达的地方，还是只需一次短途自驾游即可到达的地方！这个 App 目前看起来相当不错，但在测试过程中，我注意到它并不总是像我希望的那样流畅滚动。我很想弄清楚原因。Jed，你提到了新的 SwiftUI instrument。能带我们参观一下吗？当然！在 Instruments 26 中，我们很高兴地介绍一种识别 SwiftUI App 中性能问题的新方法：下一代 SwiftUI instrument。

更新后的 SwiftUI 模板包含几个不同的 instrument，用于评估你的 App 的性能。首先，我们有新的 SwiftUI instrument，我稍后会详细说明。

接下来，我们包含了 Time Profiler，它显示了你的 App 在 CPU 上执行的工作随时间变化的样本。最后，我们有 Hangs and Hitches instruments，它记录你的 App 的响应能力。

调查你的 App 中潜在性能问题的第一步，是查看 SwiftUI instrument 提供的顶层信息。

SwiftUI instrument 轨道的第一条通道称为“Update Groups”，它显示 SwiftUI 何时在执行工作。

如果 CPU 使用率在这条通道为空时出现峰值，你就会知道你的问题很可能不在 SwiftUI 内部。SwiftUI instrument 轨道的其他通道允许你轻松识别长时间的 SwiftUI 更新及其发生时间。Long View Body Updates 会高亮显示视图的 `body` 属性运行时间过长的情况。Long Representable Updates 会识别可能耗时过长的视图和视图控制器可表示更新。最后，Other Long Updates 会显示所有其他类型的长时间 SwiftUI 工作。这 3 条通道为你提供了所有可能导致 App 性能不佳的长时间更新的高级视图。更新根据它们可能导致卡顿或挂起的可能性以橙色和红色显示。这些更新是否真的在你的 App 中导致任何挂起或卡顿可能取决于设备条件，但调查这些长时间更新，从红色的开始，通常是一个很好的起点。

要开始使用 SwiftUI instrument，请安装 Xcode 26。然后，在你要运行和分析 App 的设备上，更新到最新的操作系统版本，这些版本包含对记录 SwiftUI 跟踪的支持。我认为我们已经准备好首次对 Landmarks App 进行性能分析了。-Steven，交给你了！-谢谢，Jed！该项目已经在 Xcode 中打开。要开始性能分析，我将按下 Command-I，Xcode 会以 Release 模式编译 App，然后自动启动 Instruments。

从模板选择器中，我将选择 SwiftUI 模板，然后点击录制按钮开始录制。

我将开始滚动地标列表。每个大洲都有一个水平排列的搁架（shelf）。

我将水平滚动到北美搁架的末尾，以加载更多视图。

然后，我将点击停止录制。

录制停止后，Instruments 会将性能分析数据从我的设备复制过来并进行处理以进行分析。处理完成后，我将能够使用 SwiftUI Instrument 来确定是否存在任何需要我关注的潜在性能问题。我将最大化窗口以便更容易看到所有内容。

我将首先检查 SwiftUI instrument 轨道中的顶层长时间更新通道。

运行时间过长的视图 body 是 SwiftUI 中性能问题的常见原因，因此我将首先检查 Long View Body Updates 通道。

这个通道中有一些橙色和红色的长时间更新，因此我想调查一下它们。我将点击展开 SwiftUI 轨道。

这会显示出 3 个子轨道：View Body Updates、Representable Updates 和 Other Updates。每个子轨道都像顶层通道一样，用橙色和红色高亮显示长时间更新。其余的更新以灰色显示。我将选择 View Body Updates 轨道。

在下面的详情窗格中，有一个层次结构摘要，列出了在我的性能分析会话期间运行的所有视图 body。当我展开 App 进程的层次结构时，我会获得所有已运行视图 body 更新的模块列表。

我可以通过点击下拉菜单并选择 Long View Body Updates 摘要，将这些过滤为仅显示长时间更新。

从计数中我可以看出，有几个长时间更新需要调查。

我将点击展开我 App 的模块。LandmarkListItemView 有几个长时间更新，所以我将从那个视图开始。

将鼠标悬停在视图名称上会显示一个箭头。

点击箭头会显示一个上下文菜单。我将选择“Show Updates”，这会显示该视图 body 所有长时间更新的顺序列表。

我将右键单击其中一个长时间更新，然后点击“Set Inspection Range and Zoom”。

这会将我的跟踪中的选择设置为此视图 body 更新的时间间隔。然后，我将点击 Time Profiler instrument 轨道。

在这里我可以看到我的视图 body 运行时 CPU 上发生了什么。

Time Profiler 通过定期采样 CPU 上运行的内容来收集数据。对于每个样本，它会检查当前正在运行的函数，并将该信息保存到性能分析会话中。下方的 Profile 详情窗格显示了跟踪期间记录的样本的调用栈。在这种情况下，这些是视图 body 运行时记录的样本。

我将按住 Option 键并点击展开主线程调用栈。

SwiftUI 的工作由一个非常深的调用栈表示。我在这里最感兴趣的是 LandmarkListItemView。我将按下 Command-F 在调用栈中搜索，并在搜索字段中输入名称。

这是我的视图 body。在最左边的列中，Time Profiler 显示了调用栈中每个帧所花费的时间。

这一列显示，视图 body 中的大部分时间都花在一个名为 `distance` 的计算属性中。在 `distance` 内部，最重的两个帧是对两个不同格式化器的调用。

这个测量格式化器和这个数字格式化器。让我们切换回 Xcode 查看代码中发生了什么。

这是 LandmarkListItemView，它是列表中每个地标的视图。

这是我在 Time Profiler 中注意到的 `distance` 属性。此属性将我离地标的距离转换为格式化的字符串以在视图上显示。

这里是数字格式化器，Time Profiler 显示它的创建成本很高。

这里是测量格式化器创建字符串的地方，这也是视图 body 中耗时的主要贡献者。

在视图 body 中，我读取 `distance` 属性以构建标签的文本。这每次视图 body 运行时都会发生，并且由于视图 body 在主线程上运行，我的 App 必须等待距离文本被格式化后才能继续更新其 UI。但这为什么重要呢？运行视图 body 花费一毫秒可能看起来并不长，但总时间加起来可能会很多，尤其是当 SwiftUI 需要更新屏幕上的大量视图时。嘿，Jed，我应该如何看待 SwiftUI 运行视图 body 所花费的时间？这是一个很好的问题。我将首先描述渲染循环在 Apple 平台上是如何工作的。每一帧，你的 App 都会醒来处理事件，例如触摸或按键。然后，它更新 UI。这包括运行任何已更改的 SwiftUI 视图的 `body` 属性。所有这些工作都必须在每一帧的截止时间之前完成。然后，你的 App 将工作交给系统，系统在下一帧截止时间之前渲染你的视图。渲染后的输出最终在该截止时间之后变成可见的屏幕内容。这里的一切都在按应有的方式工作。更新在相应的帧截止时间之前完成，给系统足够的时间来渲染每一帧并使其在屏幕上可见。让我们将其与一个有因视图 body 执行时间过长而导致卡顿的 App 进行比较。

和之前一样，我们首先处理事件。然后我们运行 UI 更新。但在这里的第一帧，其中一个 UI 更新花费了太长时间。这导致 UI 更新部分超过了帧截止时间。这意味着下一次更新要等到一帧之后才能开始。而这一帧在截止时间时没有准备好将任何内容交给渲染器。结果，上一帧一直保持在屏幕上，直到系统完成渲染下一帧。我们将一帧在屏幕上停留时间过长，从而延迟后续帧的情况称为卡顿。卡顿会使动画看起来不流畅。有关卡顿的更多信息，请查看文章“理解你 App 中的卡顿”和这场 Tech Talk，它们更深入地探讨了渲染循环以及如何修复不同类型的卡顿。Steven，这有助于解释为什么视图 body 运行时间很重要吗？是的，非常有帮助！所以视图 body 更新运行时间比所需时间更长的风险是，这可能导致我的 App 错过帧截止时间，从而引起卡顿。所以我需要一种方法来计算每个地标的距离字符串，并在显示视图之前提前缓存它，而不是在 body 运行时进行。让我们回到代码中。

好的，这是每次视图 body 更新时都会运行的 `distance` 属性。我不在视图 body 运行时做这项工作，而是将它移到一个更集中的位置：我管理位置更新的类。

LocationFinder 类负责在我位置变化时接收更新。我不在视图 body 中计算格式化的距离字符串，而是可以提前创建这些字符串并在此处缓存它们，以便我的其中一个视图需要显示时，它们已经计算好了。

我将首先更新初始化方法以创建我之前在视图 body 中创建的格式化器。

我添加了一个名为 `formatter` 的属性来存储我的测量格式化器。

在初始化方法的顶部，我正在创建之前在我的视图中创建的数字格式化器。

以及测量格式化器，我将其存储在我添加的新属性中。因为格式永远不会改变，我可以在需要更新距离字符串时重用这些格式化器，并避免每次视图 body 运行时重新创建新格式化器的开销。接下来，我需要一种方法来保持字符串缓存，以便我的视图在需要时可以使用它们。我将添加一些代码来管理这些更新。

我有一个用于存储地标的数组，我将用它来计算距离。

我还有一个字典用于在计算后缓存距离字符串。

这个名为 `updateDistances` 的函数将在我的位置变化时重新计算字符串。

我在这里使用 `formatter` 来创建距离文本。

并在这里将文本存储到我的缓存中。

稍后，我将从我的视图中调用这最后一个函数来获取缓存的文本。这里还有最后一件事情要做。当我的位置更新时，我需要更新字符串的缓存。

我将点击跳转栏下拉菜单，然后跳转到 `didUpdateLocations` 函数，CoreLocation 会在我的位置变化时调用这个函数。

这就是我将调用我创建的 `updateDistances` 函数的地方。

现在，我将切换回我的视图。

我将更新视图以使用缓存的值。

这些变更应该能修复缓慢的视图 body 更新。

现在，让我们看一下实施这些修复后进行的 Instruments 跟踪，以验证情况是否已改善。在选择了 View Body Updates 轨道的情况下，详情窗格中的 Long View Body Updates 摘要显示，LandmarkListItemView 的长时间更新已经消失了。

摘要中仍然列出了两个较长的视图 body 更新，但需要注意的是，这些更新发生在跟踪的最开始，即 App 准备渲染其第一帧时。在 App 启动后立即进行更新花费更长时间并不罕见，因为系统正在构建 App 的初始视图层级结构（view hierarchy）。但这不会导致卡顿。重要的是，那些在滚动时可能导致卡顿的长时间 LandmarkListItemView 更新现在已经修复，并且从列表中消失了。这意味着我可以确信，在 SwiftUI 努力将所有视图显示到屏幕上的过程中，我并没有拖慢它。

修复长时间的视图 body 更新是提升 App 性能的好方法。然而，还有另一件事需要考虑；太多不必要的视图 body 更新也会导致性能问题。让我们探讨一下原因。

这是 Jed 之前展示的示意图。但这一次，并没有哪一个单一的更新比其他更新更长。相反，有一大堆相对较快的更新，都必须在同一帧内完成。

所有这些额外的工作导致了 App 错过了提交其帧的截止时间。又一次，下一次更新被延迟了一帧。并且因为没有任何内容可以交给渲染器，所以再次发生卡顿（hitch），因为上一帧在屏幕上停留了整整两帧。我提到不必要的视图更新可能带来的性能影响，是因为我正在为我们 App 开发一个新功能，我认为这在其中会很重要。浏览所有地标让我非常兴奋地探索新地方，但真的很难决定优先去哪里。所以我想出了一个主意来让它更容易。让我展示给你看。我给每个地标添加了一个新的心形按钮，我可以点击它来添加和移除收藏。

让我给你看看代码。

在 LandmarkListItemView 中，我添加了这个覆盖层来显示我的新心形按钮。

按钮的操作调用我的 model data 类上的 `toggleFavorite` 函数来收藏或取消收藏该地标。

如果地标被收藏，标签图标会显示一个实心心形，否则显示一个空心心形。

我将 Command-点击 `toggleFavorite` 跳转到该函数。

这是我添加收藏的方式。

模型存储了一个收藏地标的数组。当添加收藏时，我将地标附加到数组末尾。

要移除收藏，我执行相反的操作。

这就是我目前所做的。我确信我的功能还需要一些工作，但在开发过程中尽早并频繁地使用 Instruments 进行性能分析是一个好主意。那么，让我们看看我的新功能表现如何。我将按下 Command-I 来构建 App，切换回 Instruments，然后再次点击录制。

我想我会像之前一样向下滚动到 North America 列表并向右滚动，然后点击心形来收藏 Muir Woods。因为它离我住的地方不远，但不知何故我还没去过那里！好的，现在我将向上滚动。并收藏一个遥远的地方，比如 Mount Fuji 怎么样？那将是一次有趣的冒险。现在我将停止录制。

我想确保点击我的新收藏按钮不会导致任何额外的不必要更新。带着期望去分析一个跟踪，并寻找任何看起来异常的地方，是识别潜在问题的一个好方法。

我将点击展开 SwiftUI instrument 轨道，并选择 View Body Updates 子轨道。

因为我点击了两个收藏按钮，Muir Woods 和 Mount Fuji，所以我期望这两个视图已经更新了。我在跟踪的后半部分点击了按钮，在我向下滚动到底部之后。所以我会高亮跟踪的那一部分，以只关注我感兴趣的部分。

现在我将检查下面的详情窗格。我将展开层次结构以找到我的视图的更新列表。

我惊讶地发现 LandmarkListItemView 实际上更新了好几次。但为什么呢？在调试 UIKit App 中的视图更新时，我通常会在代码中设置一个断点，然后检查回溯来尝试找出视图更新的原因。但在我的 SwiftUI App 中，例如 Landmarks，这种方法对我来说并不奏效。SwiftUI 的调用栈似乎更难理解。Jed，为什么这种方法在 SwiftUI App 中不适用？让我解释一下。Xcode 通过在你触发断点时显示回溯，帮助你理解命令式代码（如在 UIKit App 中）的原因和影响。UIKit 是一个命令式框架，因此回溯通常对调试因果关系很有用。在这里，我可以看出我的标签正在被更新，因为我在 `viewDidLoad` 中设置了 `isOn` 属性。并且通过猜测回溯中某些系统帧的名称，这似乎发生在我 App 启动其第一个场景（scene）时。当我将其与执行相同操作的类似 SwiftUI App 进行比较时，我发现 SwiftUI 内部有几次递归更新，被 AttributeGraph 内部的帧分隔开来。这些信息都没有告诉我为什么我的视图特别需要更新。因为 SwiftUI 是声明式的，你不能使用回溯来理解为什么你的视图在更新。那么，我该如何理解是什么导致我的 SwiftUI 视图更新呢？首先，你需要理解 SwiftUI 是如何工作的。

我将通过一个小例子视图来说明 SwiftUI 的数据模型，即 AttributeGraph 如何定义视图之间的依赖关系，并在不必要时避免重新运行你的视图。今天我不会介绍所有细节，但这部分应该为你理解更新如何在你的 App 中流动奠定基础。

视图声明对 `View` 协议的遵循。然后，它们实现 `body` 属性，通过返回另一个 `View` 值来定义其外观和行为。

这里的 `OnOffView` 从其 `body` 返回一个 `Text` 视图，并传入一个根据其 `isOn` 状态变量值而变化的标签。

当这个视图首次被添加到视图层级结构时，SwiftUI 会从其父视图接收一个名为 attribute 的对象，该对象存储了视图结构体。视图结构体被频繁地重新创建，但 attribute 保持其身份，并在视图的整个生命周期内维护状态。因此，当父视图更新时，这个 attribute 的值会改变，但其身份不会改变。该视图被要求创建自己的 attribute 来存储其状态并定义其行为。它首先为 `isOn` 状态变量创建存储，以及一个跟踪该状态变量何时发生变化的 attribute。然后，该视图创建一个新的 attribute 来运行其 `body`，它依赖于这两个 attribute。每当视图 body attribute 被要求生成一个新值时，它会读取从父视图传递过来的当前视图值。接下来，该 attribute 使用你状态变量的当前值更新该视图结构体的一个副本。然后，它访问该视图临时副本上的 `body` 计算属性，并将其返回的值保存为 attribute 的更新值。然后，由于你的视图的 `body` 返回了一个 `Text` 视图，SwiftUI 会设置它显示文本所需的 attribute。

文本视图创建一个依赖于环境的 attribute，以访问当前的默认样式（如前景色和字体）来确定任何渲染文本的外观。此 attribute 添加了一个对你的视图 body 的依赖，以访问它将从你返回的 `Text` 结构体中渲染的字符串。最后，Text 创建另一个 attribute，该 attribute 基于带样式的文本构建一个要渲染内容的描述。

现在，让我们讨论一下当你改变一个状态变量时会发生什么。当你这样做时，SwiftUI 不会立即更新你的视图。相反，它会创建一个新的事务（transaction）。事务代表需要在下一帧之前对 SwiftUI 视图层级结构进行的更改。

此事务会将你的状态变量的信号 attribute 标记为过时。然后，当 SwiftUI 准备为下一帧更新时，它会运行该事务并应用已安排好的更新。既然一个 attribute 已被标记为过时，SwiftUI 会沿着依赖于这个现在已过时 attribute 的链向下走，通过设置一个标记来将每个 attribute 标记为过时。设置标记非常快，此时不会发生任何额外的工作。在处理完任何其他事务后，SwiftUI 现在需要弄清楚在这一帧要绘制什么到屏幕上。但它无法访问该信息，因为它被标记为过时了。

所以 SwiftUI 必须更新该信息的所有依赖项，以决定绘制什么。

从那些没有过时依赖项的 attribute 开始，比如 State 信号。现在你的视图 body attribute 已准备好更新。它再次运行，生成一个包含更新字符串的全新 `Text` 结构体值。这会传递给现有的 Apply styling attribute，然后更新继续，直到所有需要确定要绘制什么的 attribute 都已被更新。现在 SwiftUI 能够回答它最初的问题：它应该在屏幕上绘制什么？当我问“为什么我的视图 body 会运行？”时，真正的问题是“是什么将我的视图 body 标记为过时？”。你通常可以控制依赖项（例如其他视图）何时将你的视图 body 标记为过时，尤其是当这些视图是你自己的视图时。但是 SwiftUI 也会执行额外的工作来显示你的视图。虽然这些工作是必要的且通常是不可避免的，但了解它何时发生是很有价值的。将有关视图更新的原因和影响的信息提供给你，是新 SwiftUI instrument 的一大特色。原因与影响图记录了所有这些因果关系，并以如下所示的关系图形式展示给你。

我们从正在调查的视图 body 更新开始。该更新显示为一个节点，其图标标识它为视图 body 更新，标题告诉你它对应哪个视图类型。

有一个箭头从代表状态变化的节点指向它。该箭头标记为“update（更新）”，因为状态变化导致了视图更新。你还会注意到标记为“Creation（创建）”的边，它告诉你是什么使你的视图首次出现在视图层级结构中。

状态变化节点有一个标题，告诉你状态变量的名称以及它附加到的视图类型。当你选择状态变化时，你将看到值被更新的位置的回溯。

继续向左看原因与影响图，你可以看出状态变化是由于手势引起的，例如点击按钮。

Steven，Landmarks App 的原因图显示了什么？让我们检查一下原因与影响图，以弄清楚为什么发生了所有这些额外的视图 body 更新。这是原因与影响图视图。LandmarkListItemView.body 的节点被选中了。图中的蓝色节点代表我自己的代码部分，或者我在与 App 交互时执行的操作。该图从左到右显示原因和影响的链条。

“Gesture（手势）”节点代表我对收藏按钮的点击。

这导致了收藏地标数组的更新，这进而导致 LandmarkListItemView 的 `body` 更新了好多次。这比我预期的要多得多。

看起来点击单个收藏按钮可能会导致屏幕上很多项目视图都更新，而不是只有我点击的那个。因此，让我们通过回到代码来弄清楚这里发生了什么。

我将切换回 LandmarkListItemView。我检查一个地标是否被标记为收藏的方式是调用 `modelData.isFavorite` 并传入该地标。`ModelData` 是我的顶层模型对象，它使用 `@Observable` 宏来允许 SwiftUI 在其属性变化时更新我的视图。我将 Command-点击 `isFavorite` 跳转到该函数。

在这里，我访问 `favoritesCollection.landmarks` 数组来检查这个地标是否被收藏。这会导致 `@Observable` 在每个项目视图和整个收藏数组之间建立依赖关系。因此，每当我向数组添加一个收藏时，每个项目视图的 body 都会运行，因为数组发生了变化。让我向你展示这是如何工作的。

这里有一些我的 LandmarkListItemViews。这是我的 `ModelData` 类，其中包含 `favoritesCollection`，它跟踪我的收藏地标。目前，我唯一的收藏是地标编号二。`ModelData` 类有一个 `isFavorite` 函数。每个 `LandmarkListItemView` 都调用这个函数来确定图标是否应该高亮显示。`isFavorite` 函数检查集合是否包含该地标，每个视图渲染自己的按钮。因为每个视图都访问了收藏数组，即使是间接的，`@Observable` 宏已经为每个视图创建了对整个收藏数组的依赖。

那么，当我想通过点击另一个视图上的收藏按钮来添加一个新的收藏时会发生什么？视图调用 `toggleFavorite`，它向我的收藏中添加一个新地标。因为我所有的 `LandmarkListItemView` 都对 `favoritesCollection` 有依赖关系，所以所有视图都被标记为过时，并且它们的 body 会再次运行。

但这并不理想，因为我实际更改的只有视图编号三。我真正需要的是让我的视图的数据依赖关系更细化，这样当我的 App 数据发生变化时，只有必要的视图 body 会被更新。

那么，让我们重新思考一下这个问题。我知道我的每个视图都有一个带有其自身收藏状态的地标：已收藏或未收藏。因此，为了跟踪该状态，我将为我的视图创建一个 Observable 视图模型（Observable view model）。该模型有一个 `isFavorite` 属性来跟踪收藏状态，并且每个视图都将拥有自己的视图模型。

现在，我可以在 `ModelData` 类中存储我的视图模型。每个视图可以检索它自己的视图模型，并根据需要切换收藏的开启和关闭。因此，每个视图不再依赖于整个收藏数组，而只直接依赖于其自己地标的视图模型。那么，让我们再添加一个收藏！点击按钮调用 `toggleFavorite`，这会更新视图编号一的视图模型。并且由于视图编号一只依赖于它自己的视图模型，它是唯一会再次运行 body 的视图。让我们看看在 Landmarks 中实施这些更改后的效果。

这是在实施新的视图模型改进后我录制的一个跟踪。我将再次点击 View Body Updates 子轨道。我将像之前一样选择时间线的相同部分。

在详情窗格中，我将展开进程和 Landmarks 模块。

现在，只有两个更新。由于我更改了两个收藏，这看起来是正确的，但让我们再次检查一下图表。我将鼠标悬停在视图名称上，点击箭头并选择“Show Cause & Effect Graph”。

现在再次显示图表。

现在，从 `@Observable` 节点到我的视图 body 的箭头只显示了两个更新，每个按钮一个。通过将每个项目视图对整个收藏数组的依赖关系替换为紧密耦合的视图模型，我消除了大量不必要的视图 body 更新，这将有助于保持我的 App 流畅运行。在这个例子中，图表相对较小，因为导致我的视图 body 更新的原因非常有限。然而，当有更多不同的原因时，图表可能会变得大得多。发生这种情况的一种方式是当视图读取环境（Environment）时。Jed，你能给我们展示一个例子吗？当然！我将首先讨论环境是如何工作的。环境中的值存储在 `EnvironmentValues` 结构体中，它是一个值类型，类似于字典。这些视图中的每一个都对整个 `EnvironmentValues` 结构体有依赖关系，因为每个视图都使用 `@Environment` 属性包装器（property wrapper）访问环境。当环境中的任何值被更新时，每个依赖于该环境的视图都会收到通知，告知其 body 可能需要运行。然后，这些视图中的每一个都会检查它所读取的值是否发生了变化。如果值发生了变化，视图 body 需要再次运行。如果没有变化，SwiftUI 可以跳过运行视图 body，因为该视图已经是最新的了。让我们探讨一下这些更新在原因与影响图中是如何显示的。

图中有两种主要的节点类型代表对环境的更新。外部环境更新包括 App 级别的内容，例如从 SwiftUI 外部更新的颜色方案。环境写入更新代表在 SwiftUI 内部对环境中的值所做的更改。你在 App 中使用 `.environment` 修改器（modifier）所做的更新属于此类别。那么，假设由于设备切换到深色模式而更新了颜色方案环境值。这对于这些视图来说在原因与影响图中会是什么样子？该图将为 View1 显示一个“External Environment（外部环境）”节点，因为颜色方案是一个系统级的环境更新。该图还会显示一个节点指示 View1 的 body 已运行。因为 View2 也读取环境，所以图中也有一个外部环境更新作为其原因。但是 View2 不读取颜色方案值，所以它的 body 不会运行。在图中，视图 body 未运行的视图更新由一个暗淡的图标表示。在这种情况下，这两个外部环境节点代表同一个更新。如果你将鼠标悬停或点击用于同一个更新的任一节点，它们将同时高亮显示，以便更容易识别。这两个视图更新都显示在图中，因为即使在视图的 body 不需要因环境更新而运行的情况下，检查视图感兴趣的值是否更新仍然存在相关的成本。如果你有大量从环境读取的视图，所花费的时间可能会很快累积起来。这就是为什么避免在环境中存储更新非常频繁的值（例如几何值或定时器）很重要。这就是原因与影响图。这是一个很好的方式来可视化数据在你的 App 中如何流动，以帮助你确保你的视图不会进行超过其必要次数的更新。在本讲座中，我们介绍了一些在 SwiftUI App 中获得卓越性能的最佳实践。保持视图 body 快速运行很重要，这样 SwiftUI 才有足够的时间将你的 UI 无延迟地显示到屏幕上。不必要的视图 body 更新确实会累积起来。设计你的数据流，使其仅在必要时更新你的视图，并特别留意变化非常频繁的依赖项。最后，请记住在开发过程中尽早并频繁地使用 Instruments 来分析你的 App 的性能。我知道我们今天讲了很多内容。然而，最重要的收获是：确保你的视图 body 更新快速且仅在需要时进行，以实现卓越的 SwiftUI 性能。在此过程中，使用 SwiftUI instrument 来验证你的 App 的性能。

在今天的讲座中，我们向你展示了如何使用 SwiftUI instrument 来分析你的 App，但还有更多内容有待探索。请查看视频描述中链接的文档，以了解该 instrument 的一些其他功能。我们还添加了有关分析和改善 App 性能的更多视频和参考资料的链接。感谢你的参与！我们很高兴看到你使用新的 SwiftUI Instrument 让你的 App 发挥出最佳性能。
