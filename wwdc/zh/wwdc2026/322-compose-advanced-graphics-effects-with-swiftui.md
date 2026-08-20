---
title: 用 SwiftUI 合成高级图形效果
session_id: 322
collection: wwdc2026
year: 2026
duration: '17:55'
topics: [Design, 'SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2026/322/'
content_hash: 'sha256:76248e0c1381d12a'
translated: true
---

# 用 SwiftUI 合成高级图形效果

<sub>WWDC2026 · 17:55 · Design、SwiftUI & UI Frameworks</sub>

了解如何通过创造性地组合 SwiftUI 布局和图形 API 来打造丰富、自定制的体验。我们将向你展示如何分解……

> [!note] 归档理由
> SwiftUI 图形效果与合成

## 章节

- [引言](/videos/play/wwdc2026/322/?time=0)
- [设计分解](/videos/play/wwdc2026/322/?time=100)
- [封面图与着色器效果](/videos/play/wwdc2026/322/?time=251)
- [用时间驱动动画](/videos/play/wwdc2026/322/?time=667)
- [时间同步的逐字稿视图](/videos/play/wwdc2026/322/?time=720)
- [使用对齐参考线的浮动时间戳](/videos/play/wwdc2026/322/?time=798)
- [创意管线](/videos/play/wwdc2026/322/?time=976)
- [下一步](/videos/play/wwdc2026/322/?time=1033)

## 相关资源

- [引言](https://developer.apple.com/videos/play/wwdc2026/322/?time=0)
- [设计分解](https://developer.apple.com/videos/play/wwdc2026/322/?time=100)
- [封面图与着色器效果](https://developer.apple.com/videos/play/wwdc2026/322/?time=251)
- [用时间驱动动画](https://developer.apple.com/videos/play/wwdc2026/322/?time=667)
- [时间同步的逐字稿视图](https://developer.apple.com/videos/play/wwdc2026/322/?time=720)
- [使用对齐参考线的浮动时间戳](https://developer.apple.com/videos/play/wwdc2026/322/?time=798)
- [创意管线](https://developer.apple.com/videos/play/wwdc2026/322/?time=976)
- [下一步](https://developer.apple.com/videos/play/wwdc2026/322/?time=1033)
- [对齐](https://developer.apple.com/documentation/SwiftUI/Alignment)
- [用 SwiftUI 合成高级图形效果](https://developer.apple.com/documentation/SwiftUI/Composing-advanced-graphics-effects-with-SwiftUI)
- [着色器](https://developer.apple.com/documentation/SwiftUI/Shader)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2026/322/4/db4c622a-2091-45ef-a024-df317a5b55a5/downloads/wwdc2026-322_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2026/322/4/db4c622a-2091-45ef-a024-df317a5b55a5/downloads/wwdc2026-322_sd.mp4?dl=1)
- [用 SwiftUI 创建自定视觉效果](https://developer.apple.com/videos/play/wwdc2024/10151)
- [封面图](https://developer.apple.com/videos/play/wwdc2026/322/?time=258)
- [模糊后的封面图](https://developer.apple.com/videos/play/wwdc2026/322/?time=264)
- [在 SwiftUI 中应用图层效果](https://developer.apple.com/videos/play/wwdc2026/322/?time=429)
- [在 Metal 中编写图层效果着色器](https://developer.apple.com/videos/play/wwdc2026/322/?time=441)
- [带偏移参数的 Metal 着色器](https://developer.apple.com/videos/play/wwdc2026/322/?time=459)
- [带偏移参数的 SwiftUI 图层效果](https://developer.apple.com/videos/play/wwdc2026/322/?time=475)
- [带全宽偏移的 SwiftUI 图层效果](https://developer.apple.com/videos/play/wwdc2026/322/?time=484)
- [带噪点采样的 SwiftUI 图层效果](https://developer.apple.com/videos/play/wwdc2026/322/?time=517)
- [带噪点采样的 Metal 着色器](https://developer.apple.com/videos/play/wwdc2026/322/?time=535)
- [带域扭曲的 Metal 着色器](https://developer.apple.com/videos/play/wwdc2026/322/?time=622)
- [带静态视觉效果的 SwiftUI 图层效果](https://developer.apple.com/videos/play/wwdc2026/322/?time=676)
- [带动画视觉效果的 SwiftUI 图层效果](https://developer.apple.com/videos/play/wwdc2026/322/?time=697)
- [基本的逐字稿视图](https://developer.apple.com/videos/play/wwdc2026/322/?time=735)
- [时间同步的逐字稿视图](https://developer.apple.com/videos/play/wwdc2026/322/?time=753)
- [居中对齐叠加](https://developer.apple.com/videos/play/wwdc2026/322/?time=833)
- [底部前导对齐叠加](https://developer.apple.com/videos/play/wwdc2026/322/?time=846)
- [覆盖对齐参考线的叠加](https://developer.apple.com/videos/play/wwdc2026/322/?time=872)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好！我是 Haotian，UI Frameworks 团队的一名工程师。自诞生以来，SwiftUI 在图形和布局方面的能力不断提升，使其成为那些希望在 Apple 设备上打造丰富、自定制体验的人们的选择。Apple 自身也在其各种 App 中使用 SwiftUI 构建高级效果。唔，“高级”这个词可能听起来有些吓人。但事实是，即使是高级效果，SwiftUI App 也共享着相同的基本元素。这就像一个管线。

数据流过一系列标准管道。它接收一些东西，进行变换，然后传递下去。SwiftUI 的渐进式揭示意味着每个管道本身已经能够独立工作。但你可以将它们连接起来，创建分支，或合并数据流。这正是发挥创意的时刻。“高级”之处在于构造，而非复杂性。这是路线图。首先，我会拿一个设计并把它分解开。然后我会构建高级效果。最后，我会分享如何用创意管线将那些技术融入你自己的 App。这是我正在构建的设计。

所以，我一直在构建我自己的播客 App。这是它目前的样子，一个简陋的逐字稿视图。我打算把它变漂亮，就像 Apple Music 中的实时歌词视图一样。带有动画封面图，以及随时间同步滚动的逐字稿。我该从何入手？我从已有的东西开始。我现有的用户界面已经包含了所有我需要的数据，包括封面图、播放信息和逐字稿文本。问题不在于我需要什么数据，而在于我如何使用管线来变换它。这里有几个例子。

从封面图开始，我需要一个管道把图像转换成可视化器，着色器管道正好适用。

可视化器需要动起来才能反映我们的播放状态。对于动态视觉效果，我把时间管道连接到管线，这是两个管道合并成了一个。

嗯，时间管道的作用不止于此。逐字稿管道被变换后有了时间戳叠加，但它不知道当前时间，因此无法正确滚动。

我可以连接同一个时间管道，形成时间同步滚动文本的管线。现在我就得到了背景的动态视觉效果，以及前景的滚动逐字稿。是时候把这两条并行的管道连接在一起了。如果你把视角拉远，你会意识到每个 modifier、每个 API，都是管线中的另一个阶段。它就这么流动着。

就像刚才展示的那样，我的播客 App 包含了高级布局和图形。我有一个全屏封面图，应用了着色器效果和时间驱动的动画。在另一边，我有一个时间同步的可滚动逐字稿视图，通过浮动视图附着（floating-view attachment）得到了精化！我会逐一讲解这些部分，并解释如何实现它们，先从封面图开始。

这是我们的原始素材。一张封面图。

封面图很美，但它会放在逐字稿的后面。我使用 `.blur` modifier 把它柔化，以免它抢眼。

现在我的封面图模糊了，接下来我会施展一些着色器魔法。你可能会问，着色器是什么？它和写 SwiftUI 代码有什么不同？让我来解释。

这个图标一开始是矢量，然后被 GPU 光栅化（rasterize）成像素。

这时，我可以在 GPU 上运行一个叫做着色器的程序，来决定在那些像素中填入什么颜色。

着色器函数是并行运行的。每个像素独立执行，不知道邻居的存在。了解这一点后，你就完全能理解 Metal 着色器如何从 SwiftUI 的着色器效果 API 中调用了。一共有三种类型的着色器效果。每种都有不同的方法签名，某些参数是必需的，尽管你也可以追加额外的参数来从 SwiftUI 向着色器传递你想要的信息。

`colorEffect` 通过将每个像素的颜色变换成新颜色来工作，其中每个像素都被提供了像素位置和原始视图在该位置的像素颜色。然后你基于这些信息返回新的颜色。这对于简单的效果很有用，比如把彩色图像变成黑白图像。

`distortionEffect` 工作方式不同。`distortionEffectFunction` 不是期望某个位置的颜色，而是为 SwiftUI 将要从原始图像采样的新位置提供一个现有位置。这里不涉及像素颜色，你告诉 SwiftUI：“我想要这个位置的颜色跟随那个位置的颜色”。这对于几何效果很有用，比如这里展示的剪切效果。

`layerEffect` 是最灵活的。`layerEffectFunction` 仍然是逐像素工作，但它提供了整个视图的图层（layer），这允许你采样相邻像素或整个区域。这对于像模糊（blur）这样的效果很有用，因为输出像素的颜色依赖于多个输入像素。

对于我的用例，`distortionEffect` 可以工作，但 `layerEffect` 提供了最大的灵活性。我会添加一个 `layerEffect` modifier，然后添加一个叫做 `backgroundWarp` 的着色器函数。

目前它只是在给定位置从原始图层采样，这给了我相同的图像。但现在我有一个可以在此基础上构建的着色器函数了。

使用 `layerEffect`，我可以从原始视图的任何位置采样。例如，我可以向着色器函数传递一个 `float2` 向量，并用它来偏移着色器中的采样位置。

为了匹配函数参数，我现在在 SwiftUI 侧放一个 `float2` 向量。

现在，当我增加偏移量时，每个像素都使用这个偏移值运行着色器，因此它们全都统一地、递增地从远处采样。

当我减小偏移量到零时，图像又会恢复。

不过，由于是统一偏移，我得到的只是按固定模式偏移的像素。我需要一些更有机的东西，一些随像素而变化的东西。

为了实现有机变化，我使用一个 `NoiseTexture`，这是一张预计算的平滑随机值图像。

这次，在 SwiftUI 侧，我除了传递 `NoiseTexture` 作为图像参数外，还传递了视图大小。

而在 Metal 侧，图像作为 `texture2d` 到达。

现在我要展示一些非常 Metal 的 Metal 代码了。

我首先使用当前像素位置和大小来获取 uv 值，它表示我相对于这张图像的位置，这让我可以在没有绝对位置的情况下采样纹理。

现在我来解包 `NoiseTexture`。

它有 RGB 通道，红色和绿色通道很有趣，因为每个通道都包含不同的噪点图案。

如果我移动 uv，我会得到不同的红色和绿色值。这对不断变化的值恰好非常适合用作 X 和 Y 方向的有机偏移，因为它随像素而异。

现在回到 Metal 着色器。

我创建一个重复模式的采样器，这样它可以平铺，然后我在每个像素的 UV 位置采样噪点。红色和绿色通道给了我一个二维偏移量，我缩放后加到位置上，用于从原始视图采样。现在，着色器轻微地扭曲了图像。

这是逐像素变化，但我想要更丰富的东西。

所以我做了个实验，如果我不只采样一次噪点，而是采样两次会怎样？第一次给我一个初始偏移。然后我再次采样噪点，但这次是在被初始偏移移动后的位置上进行采样，就这样，我得到了这些有机流动的斑点。

这种分层噪点方法是一种众所周知的技术，叫做域扭曲（domain warping）。要了解我是如何实现的，请下载示例 App，它甚至还有一个预览，你可以随意调整参数。

现在我有一个很酷的着色器效果，但它仍然是静止的。我需要让它动起来。这正是时间发挥作用的地方。

与 SwiftUI 基于事务的动画不同，着色器是无状态的。它们没有前一帧的记忆，输出仅依赖于参数。所以，如果我想要动画，我需要传入一个随时间变化的值。

`TimelineView` 正是我需要连接的管道。使用动画计划，它每帧都会触发，并附带一个时间戳。我把那个时间戳传入着色器，加到噪点采样的位置上，图案就开始流动了。

这就是由时间驱动的着色器动画。对于我的逐字稿视图，我也需要把时间加进来，才能让当前播放的逐字稿行高亮并居中显示在滚动视图（scroll view）中。

这是我的逐字稿。`ScrollView` 内的 `LazyVStack` 中放的是文本视图。每一行都是它自己的视图，标准的 SwiftUI。现在我需要让它跟随播放状态。

我使用播放时间戳来确定哪一行是当前行。当前行是粗体且清晰的，其余行淡出。通过 `onChange` modifier 来监听当前行的变化，我滚动以保持当前行居中。

我的时间同步滚动视图已经可以工作了。现在，我想把注意力放在当前行的小时间戳上。每一行在其叠加中都有一个时间戳，但只有当前行的时间戳是可见的。这样，它就不会干扰布局。它始终在那里，等着被显示出来。

让我们聚焦在这一行上，这是一个子视图，附着在其容器的边缘。我怎样才能把它放到那里？`offset` modifier 在不知道两个视图大小的情况下无法做到。

首先，我们来谈谈对齐（alignment）。每个视图都有对齐点。可以把它们看作布局系统用来定位视图的点，由两个轴共同定义。

当我将子视图放在叠加容器中时，布局系统使用默认的居中对齐来对齐它们。

可以想象成一个钉子同时穿过两个视图，所以它在每个视图的对齐点处把它们固定在一起。

我把叠加的对齐方式改为 `.bottomLeading`。

现在钉子穿过了每个视图的底部前导点，它们在那里锁在一起。

现在，布局系统要求底部前导对齐，所以子视图返回它的底部前导点来穿钉。

如果我要用代码显式表达这个意思，我会在这里写一个对齐参考线来表示底部就是底部。

好了，记住目标是让子视图的顶部边缘接触容器的底部边缘。

如果我告诉子视图，当布局系统询问底部对齐时，不要使用默认值。相反，我有一个自定覆盖，将底部对齐点移到了顶部边缘。

现在，当钉子要穿过来时，它会跟随那个点。

我只需写一个纯语义的覆盖，就得到了结果，无需手动偏移视图。这个 API 还有更多内容。我可以定义自己的自定对齐方式，闭包给我提供了 `ViewDimensions`，所以我可以根据视图的实际大小来计算点。请参阅关于“SwiftUI Alignment”的文档来了解全貌。

就是这样。我刚开始那简陋的逐字稿视图，现在有了由着色器和时间驱动的动画背景，一个与播放同步滚动的逐字稿，以及一个使用对齐参考线定位的浮动时间戳。

所有这些都是由简单的管道组合而成，并且它能在所有 Apple 设备上工作。

让我们退一步看看。我拿了一个设计，把它分解成多个图层，对每个图层找到了合适的 API，将原始数据转换成视图。每个阶段的输出都作为下一个阶段的输入。

像这样连接各个阶段，就是我所说的创意管线。但这些是我为这个播客 App 所做的选择。对于你自己的 App，管线可以更有创意。输入可能是陀螺仪数据而非音频。着色器可能是涟漪而非扭曲。前景可能是一个自由格式的画布而不是滚动视图。每种组合都会给你带来不同的东西。这就是创意的部分，API 是相同的。你投入什么以及如何连接它们，那才是属于你的。

所以，去创造属于你的东西吧。下载示例项目，实验着色器，改变噪点，调整速度，尝试不同的图像。在你自己的 App 中寻找那些小小视觉效果能带来巨大改变的机会。当你开始把这些管道连接在一起时，你会惊讶于简单的东西能如此迅速地变得高级。

感谢观看，再见！
