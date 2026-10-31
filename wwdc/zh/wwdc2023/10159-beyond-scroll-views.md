---
title: 超越滚动视图
session_id: 10159
collection: wwdc2023
year: 2023
duration: '14:46'
topics: ['SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10159/'
content_hash: 'sha256:a1493db1358d1fb2'
translated: true
---

# 超越滚动视图

<sub>WWDC2023 · 14:46 · SwiftUI & UI 框架</sub>

了解如何用 SwiftUI 最新的 API 把你的滚动视图提升到新的水平。我们将向你展示如何自定义滚动……

> [!note] 归档理由
> 滚动视图的底层行为与几何

## 章节

- [滚动视图简介](/videos/play/wwdc2023/10159/?time=0)
- [外边距与安全区](/videos/play/wwdc2023/10159/?time=121)
- [目标与位置](/videos/play/wwdc2023/10159/?time=254)
- [滚动过渡](/videos/play/wwdc2023/10159/?time=693)

## 相关资源

- [滚动视图简介](https://developer.apple.com/videos/play/wwdc2023/10159/?time=0)
- [外边距与安全区](https://developer.apple.com/videos/play/wwdc2023/10159/?time=121)
- [目标与位置](https://developer.apple.com/videos/play/wwdc2023/10159/?time=254)
- [滚动过渡](https://developer.apple.com/videos/play/wwdc2023/10159/?time=693)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10159/4/DCE1F4A7-9E0E-4F48-B70A-6C44D758769E/downloads/wwdc2023-10159_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10159/4/DCE1F4A7-9E0E-4F48-B70A-6C44D758769E/downloads/wwdc2023-10159_sd.mp4?dl=1)
- [探索 Swift Charts 中的饼图与交互性](https://developer.apple.com/videos/play/wwdc2023/10037)
- [SwiftUI 新变化](https://developer.apple.com/videos/play/wwdc2023/10148)
- [ScrollView](https://developer.apple.com/videos/play/wwdc2023/10159/?time=46)
- [基础精选分区](https://developer.apple.com/videos/play/wwdc2023/10159/?time=149)
- [带外边距的精选分区](https://developer.apple.com/videos/play/wwdc2023/10159/?time=240)
- [精选分区 + 容器相对框架](https://developer.apple.com/videos/play/wwdc2023/10159/?time=462)
- [精选分区 + 滚动位置](https://developer.apple.com/videos/play/wwdc2023/10159/?time=586)
- [精选分区 + 滚动过渡](https://developer.apple.com/videos/play/wwdc2023/10159/?time=754)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Harry：嗨，我是 Harry，SwiftUI 团队的一名工程师。欢迎收看「超越滚动视图」，我将谈谈 SwiftUI 中滚动视图的一些新改进。我们的设备想要做的事情，很少能被局限在它们固定的屏幕尺寸之内。它们处理这种复杂性的方式之一就是引入滚动。这让它们能够向我们展示所有放不进屏幕的内容。SwiftUI 提供了几种不同的组件，让你把滚动整合进你自己的 App。今天，我要谈的就是其中之一：ScrollView。ScrollView 是一个让你的内容可以滚动的基础构件。滚动视图具有轴（axes），定义了它们可滚动的方向。滚动视图有内容。当内容超出 ScrollView 的尺寸时，其中一部分内容会被裁剪，人们需要滚动才能看到它。滚动视图通过把安全区解析为其内容外侧的外边距，来确保内容被放置在安全区之内。默认情况下，ScrollView 会急切地求值其内容。你可以通过使用惰性叠放来改变这一行为。

ScrollView 在内容中滚动到的确切位置称为内容偏移（content offset）。SwiftUI 一直提供 ScrollViewReader API 作为控制内容偏移的方式。今年，SwiftUI 引入了更多方式，既可以影响 ScrollView 管理的内容偏移，也可以对它做出反应。在本次演讲中，我将首先讨论影响 ScrollView 外边距的各种方式，以及它们与安全区的关系。接着我会谈谈通过滚动目标和滚动位置来管理 ScrollView 的内容偏移。最后，我将展示如何用滚动过渡为你的 App 增添真正的亮点。自从我开始制作我的 Colors App 以来，用户们一直很喜欢向我展示他们最喜欢的一些配色组合。我想精选展示其中一些组合，让其他人也能欣赏。为此，我一直在为我的 Colors App 添加一个图库功能。我已经在实现图库方面取得了一些进展。在整个演讲中，我将不断打磨图库中精选分区的标头和内容。

在我的图库中，有一个包裹着惰性叠放的水平 ScrollView。我首先会用一些外边距让这个视图更好看一点。你的第一反应可能是给 ScrollView 添加一些 padding，这确实会让 ScrollView 内缩，但注意现在它的内容在滚动时会被裁剪。与其内缩 ScrollView 本身，我想扩展 ScrollView 的内容外边距。我可以用新的 safe area padding 修饰符来做到这一点。它的行为与普通的 padding 修饰符类似，但不是给内容加内边距，而是把内边距加到安全区上。现在我的 ScrollView 扩展到了整个宽度，让下一个条目能够探出头来。在继续之前，我想稍微谈谈安全区与 ScrollView 的关系。安全区最常来自于你的 App 所运行的设备。它们也可以来自诸如 safe area padding 或 safe area inset 修饰符之类的 API。ScrollView 会把安全区解析为它应用于其内容的外边距。这既包括由你负责的内容，也包括由 ScrollView 负责的其他内容，例如滚动指示器。这意味着无法通过修改安全区来为不同种类的内容配置不同的内边距。

如果你想应用不同的内边距，可以使用新的 contentMargins API。这个 API 让你可以把 ScrollView 的内容与滚动指示器分开设置内边距。或者让指示器与内容分开内缩。回到我的图库，我会把我的 safe area padding 修饰符更新为使用 content margin API。既然我的视图已经有了一些外边距，我想做的事情之一是控制当有人抬起手指后，ScrollView 会滚动到哪个内容偏移。

默认情况下，ScrollView 使用标准的减速率，加上滚动的速度，来计算滚动应当结束的目标内容偏移。它不会考虑诸如 ScrollView 的尺寸或其内容之类的东西。但有时这些因素很重要。SwiftUI 新增了 scrollTargetBehavior 修饰符，让你可以改变 ScrollView 计算这一目标内容偏移的方式。这个修饰符接受一个符合 scrollTargetBehavior 协议的类型。这里我指定了分页（paging）行为。现在我的 ScrollView 每次轻扫翻动一页。分页行为很特别。它有自定义的减速率，并根据 ScrollView 自身的包含尺寸来选择滚动到哪里。这在 iOS 上效果很好，但在 iPadOS 更大的屏幕上就有点过头了。我不想对齐 ScrollView 的包含尺寸，而是想对齐到单个视图。

视图对齐（view aligned）行为会把 ScrollView 对齐到视图，因此 ScrollView 需要知道它应当考虑哪些视图来进行对齐。这些视图称为滚动目标（scroll targets），有一族新的修饰符让我可以指定哪些视图是滚动目标。这里我会使用 scroll target layout 修饰符，让惰性叠放中的每个 hero 视图都被视为一个滚动目标。你也可以使用 scroll target 修饰符把单个视图标记为目标。但在使用惰性叠放时，使用 scroll target layout 修饰符很重要。可见区域之外的视图尚未创建。不过，布局知道它将会创建哪些视图，因此它可以确保 ScrollView 滚动到正确的位置。

现在我的 ScrollView 在 iPad 上看起来好多了。分页和视图对齐行为都构建在新的 ScrollTargetBehavior 协议之上。SwiftUI 在为你提供这些常见行为的同时，也允许你让自己的类型遵循这个协议并实现你自己的自定义行为，就像你采用之前介绍的 layout 协议那样。

通过实现唯一必需的方法 updateTarget，让你的类型遵循 ScrollTargetBehavior。SwiftUI 在计算一次滚动应当在哪里结束时调用这个方法，但也会在其他上下文中调用它，例如 ScrollView 改变尺寸时。自定义行为很容易。这里，如果目标接近 ScrollView 的顶部、且滚动是向上轻拂的，我会通过修改提供的目标，倾向于让滚动正好停在 ScrollView 的最顶端。这会让 ScrollView 选择一个不同的内容偏移作为滚动的终点。这就是插入你自己的自定义代码、影响 ScrollView 选择滚动位置所需的全部工作。

让我们回到我的图库视图。我想谈谈布局。注意我的 hero 视图的尺寸是相对于设备的整体宽度而言的。如果我们看看 iPad，两个视图正好平均填满设备的宽度。以前你必须使用 GeometryReader 才能做到这一点，但今年 SwiftUI 用一个名为 containerRelativeFrame 修饰符的新 API 让这一切容易得多。

我会向你展示我的 hero 视图是如何使用这个 API 的。我从一个颜色视图的叠放开始，加上一个指定固定高度的 frame 修饰符。我会把 containerRelativeFrame 修饰符添加到我的视图上。这里我指定了水平轴，这让视图直接采用其容器的宽度。在我的例子里，容器将是外围的 ScrollView，但它也可能是导航拆分视图的最近一栏，或你的 App 的窗口。

当我的容器宽度变化时，我的视图的尺寸会自动更新。我可以通过提供一个数量和间距，创建这些视图的类网格布局。我可以根据水平 sizeClass 条件化这个数量，让 iPad 上是两列、手机上是一列。更妙的是，我可以去掉那些操作系统条件判断，因为水平 sizeClass 环境属性现在在所有平台上都可用。最后，我会使用 aspectRatio 修饰符让高度相对于宽度，而不是硬编码一个固定高度。这样我就完成了图库的布局和滚动行为。还有一些我想做的改动。你会注意到的一件事是滚动指示器。我想把它们去掉。

我可以使用现有的 scrollIndicators API 来做到这一点。在 iPad 上用手指轻扫时这样看起来很棒，但我经常在 Mac 上使用我的图库。而在 Mac 上，使用鼠标或其他输入设备时，我可能无法轻松执行水平轻扫手势。而且当我连接鼠标时，即使我已经请求隐藏指示器，它们仍然可见。使用鼠标时，如果没有滚动指示器，滚动可能变得困难甚至不可能。出于这个原因，scrollIndicators 修饰符的默认行为是：在使用触控板这类更灵活的输入设备时隐藏指示器，而在连接鼠标时允许指示器显示。你可以给 scrollIndicators 修饰符提供 never 值，无论使用什么输入设备都始终隐藏指示器。但我的 App 仍需要支持使用鼠标的人。所以我需要为他们提供另一种滚动图库的方式。我会渲染一些视图来替代滚动指示器，让用户通过点击滚动到上一个或下一个视图。为了开始构建它，让我先把 ScrollView 整理一下。我会把我的 ScrollView 移入一个包含标头视图的 VStack 中。

现在我将专注于标头视图。

我会在标头视图中添加一些自定义的拨杆（paddle）视图。在 SwiftUI 的过去版本中，我会用一个 ScrollViewReader 传给我的拨杆并滚动到相应的视图。SwiftUI 的新特性是 scrollPosition 修饰符。这个修饰符把一个绑定关联到一个包装标识符的状态。我会把它传给我的 scrollPosition 修饰符（ScrollView 会从中读取）以及我的标头视图。在标头视图的拨杆中，我可以像写任何其他状态一样写入这个绑定。当绑定被写入时，ScrollView 会滚动到具有该 ID 的视图。正如视图对齐的 ScrollTargetBehavior 一样，scroll position 修饰符使用 scroll target layout 修饰符来知道应当考虑哪些视图来查询它们的身份值。

scroll position 修饰符还让我能够知道当前滚动到的视图的身份。所以我可以在标头视图中添加一些文本，显示当前滚动到的 hero 图像的值。当我的 ScrollView 中最靠前导的视图发生变化时，绑定会自动更新。现在我的鼠标用户也能滚动浏览我的图库了。我还想为这个视图添加最后一点润色。正如了解当前滚动到哪个视图很有用一样，有时我想根据某个视图在 ScrollView 中的位置在视觉上改变它。SwiftUI 中有一个名为 ScrollTransitions 的新 API，让这件事变得非常容易。ScrollTransition 与普通过渡（transition）非常相似。过渡描述的是一个视图在出现或消失时应当经历的变化。当一个视图已经出现后，它处于其身份（identity）阶段，不应施加任何自定义效果。ScrollTransition 描述的是与过渡类似的一组变化，但它是在视图进入 ScrollView 的可见区域、随后离开可见区域时应用的。

默认情况下，当视图位于可见区域的中心时，它处于 ScrollTransition 的身份阶段。让我们在我的 hero 视图的语境下看看这一点。我会稍微整理一下代码，把重点放在 ScrollTransitions 上。

当一个视图靠近 ScrollView 的边缘时，我希望它的尺寸略微缩小。我将从添加 scrollTransition 修饰符开始。这个 API 接受 content 和 phase，允许你根据阶段指定对内容的视觉更改。这里我会指定当视图不在其身份阶段时缩小比例。

看起来很棒！ScrollTransitions 与一个名为 VisualEffect 的新协议配合使用。这个协议提供了一组对视图内容的自定义，它们可以安全地用作布局（例如 ScrollView 的内容偏移）的函数。其中许多你可能看起来很眼熟。你已经认识 scaleEffect 了。你还可以自定义旋转或偏移，就像使用视图修饰符那样。然而，并非所有视图修饰符都可以安全地在 scrollTransition 内部使用。例如，自定义字体不受支持，将无法构建。任何会改变 ScrollView 整体内容尺寸的东西都不能用在 scrollTransition 修饰符中。哇，我们已经讲了很多，让我们快速回顾一下。

我们讨论了安全区与 contentMargins 之间的区别，以及它们与 ScrollView 的关系。我向你展示了如何使用分页和视图对齐的 scrollTargetBehavior 来影响 ScrollView 的行为，以及如何编写你自己对 scrollTargetBehavior 协议的实现。你了解了使用 containerRelativeFrame 修饰符创建相对于容器的布局有多么容易。我借助 scrollPosition 修饰符接入了 ScrollView 的状态，让我既能以编程方式滚动，又能得知当前滚动到的是哪个视图。最后，我使用 scrollTransition API，基于我的 ScrollView 的内容偏移创建了视觉效果。希望你喜欢了解这些 ScrollView 的改进。谢谢，祝你在 WWDC 度过美好时光。♪ ♪
