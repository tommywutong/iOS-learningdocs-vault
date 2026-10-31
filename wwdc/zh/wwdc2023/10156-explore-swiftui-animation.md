---
title: 探索 SwiftUI 动画
session_id: 10156
collection: wwdc2023
year: 2023
duration: '30:01'
topics: ['SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10156/'
content_hash: 'sha256:b49180b9966c6ffb'
translated: true
---

# 探索 SwiftUI 动画

<sub>WWDC2023 · 30:01 · SwiftUI & UI Frameworks</sub>

探索 SwiftUI 强大的动画能力，了解这些特性如何协同产生令人印象深刻的视觉效果……
> [!note] 归档理由
> SwiftUI 动画的插值与事务模型

## 章节

- [Anatomy of an update](/videos/play/wwdc2023/10156/?time=63)
- [Animatable](/videos/play/wwdc2023/10156/?time=400)
- [Animation](/videos/play/wwdc2023/10156/?time=696)
- [Transaction](/videos/play/wwdc2023/10156/?time=1200)

## 相关资源

- [Anatomy of an update](https://developer.apple.com/videos/play/wwdc2023/10156/?time=63)
- [Animatable](https://developer.apple.com/videos/play/wwdc2023/10156/?time=400)
- [Animation](https://developer.apple.com/videos/play/wwdc2023/10156/?time=696)
- [Transaction](https://developer.apple.com/videos/play/wwdc2023/10156/?time=1200)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10156/4/9C42B457-119B-4939-B635-598E91D22BD6/downloads/wwdc2023-10156_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10156/4/9C42B457-119B-4939-B635-598E91D22BD6/downloads/wwdc2023-10156_sd.mp4?dl=1)
- [Animate with springs](https://developer.apple.com/videos/play/wwdc2023/10158)
- [Demystify SwiftUI performance](https://developer.apple.com/videos/play/wwdc2023/10160)
- [Meet MapKit for SwiftUI](https://developer.apple.com/videos/play/wwdc2023/10043)
- [What’s new in SwiftUI](https://developer.apple.com/videos/play/wwdc2023/10148)
- [Wind your way through advanced animations in SwiftUI](https://developer.apple.com/videos/play/wwdc2023/10157)
- [Pet Avatar - Unanimated](https://developer.apple.com/videos/play/wwdc2023/10156/?time=134)
- [Pet Avatar - Animated](https://developer.apple.com/videos/play/wwdc2023/10156/?time=253)
- [Pet Avatar - Explicit Animation](https://developer.apple.com/videos/play/wwdc2023/10156/?time=709)
- [UnitCurve Model](https://developer.apple.com/videos/play/wwdc2023/10156/?time=768)
- [Spring Model](https://developer.apple.com/videos/play/wwdc2023/10156/?time=836)
- [MyLinearAnimation](https://developer.apple.com/videos/play/wwdc2023/10156/?time=1045)
- [MyLinearAnimation with Velocity](https://developer.apple.com/videos/play/wwdc2023/10156/?time=1190)
- [Pet Avatar - Animation Modifier](https://developer.apple.com/videos/play/wwdc2023/10156/?time=1364)
- [Pet Avatar - Multiple Animation Modifiers](https://developer.apple.com/videos/play/wwdc2023/10156/?time=1424)
- [Generic Avatar - Scoped Animation Modifiers](https://developer.apple.com/videos/play/wwdc2023/10156/?time=1520)
- [Pet Avatar - Transaction Modifier](https://developer.apple.com/videos/play/wwdc2023/10156/?time=1725)
- [Generic Avatar - Scoped Transaction Modifier](https://developer.apple.com/videos/play/wwdc2023/10156/?time=1738)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Kyle：大家好，我是 Kyle，SwiftUI 团队的成员。动画是现代 App 设计的关键组成部分。恰当地应用时，它能为你的 UI 带来清晰与活力。让给 App 添加动画变得简单，是我们在开始开发 SwiftUI 时的核心动机之一。这也是 SwiftUI 被塑造成现在这样的重要原因。本场是 SwiftUI 强大动画能力的概览，以及它们如何协同产生令人印象深刻的视觉效果。我将介绍 SwiftUI 如何刷新视图的渲染、如何用 Animatable 决定动画什么、如何用 Animation 随时间插值数值，以及如何用 Transaction 传播当前更新的上下文。

近年来，我的同事之间一直在争论谁拥有最好的毛茸茸——或不那么毛茸茸——的伴侣。

我们很好奇能否达成共识，于是做了一个 App 来投票。

每个宠物都有投一票的按钮。当你点按，票数改变，头像滑动以反映当前排名。

在上次投票中，正如应当的，猫以微弱优势获得第一。风险太高，不能把下一次投票完全留给机遇，因此我添加新功能。点按后，我选择的头像会放大，以推动人们投票给正确的宠物。我可以再次点按把它缩小。这已经运行得相当好，但如果有动画会更好得多。

SwiftUI 跟踪视图的依赖，如这个 selected 状态变量。当事件如点按进来时，更新事务打开。

如果其任何依赖改变，视图失效，在事务关闭时，框架调用 body 生成新值以刷新渲染。

此视图的 body 由 tap gesture、scale effect 和 image 组成。

在幕后，SwiftUI 维护长期存活的依赖图，管理视图及其数据的生命周期。

图中的每个节点，称为 attribute，映射到 UI 的细粒度部分。当 selected 状态变为 true 时，这些下游 attribute 的值都变得 stale。它们通过逐层解包新视图值来刷新。

一旦对应的图 attribute 更新，视图的 body 值被丢弃。

最后，图代表你发出绘制命令以更新渲染。

我将只放大图，以便可视化 attribute 的生命周期。

attribute 以初始值诞生。事件进来，更新事务打开。上游依赖改变。框架调用 body。attribute 的值被更新。事务关闭。这样，图中每个 attribute 的当前值随时间演化。

这就是视图更新的剖析。现在我添加动画。

如果我用 withAnimation 包裹状态更改，当 tap gesture 闭包触发时，动画就为事务设置。然后 selected 切换，下游 attribute 失效。如前，body 被调用以提供新 attribute 值。

这里变得有趣。scaleEffect 是特殊 attribute，「可动画 attribute」。当可动画 attribute 的值改变时，它检查事务是否设置了动画。

如果有，它制作副本，并用动画随时间从旧值插值到新值。

我将放大 scaleEffect 可动画 attribute，检查这如何展开。首先要注意，可动画 attribute 概念上同时有 model 和 presentation 值。现在它们相同。然后事件进来，事务打开，这次带动画。状态改变，body 被调用以刷新 stale attribute 值。因为值已改变，attribute 制作动画的本地副本以计算当前 presentation 值。

SwiftUI 知道 attribute 图包含运行中的动画时，会调用适当的可动画 attribute 以产生下一帧。对于内置可动画 attribute 如 scaleEffect，SwiftUI 非常高效。它能离主线程工作，并且不调用任何你的视图代码。

这是动画实际运行。

不错。

当某人使用「动画」一词时，他们可能指视图随时间变化的整体视觉体验。

我到目前为止讲的是，在 SwiftUI 中，有两个正交方面共同构成整体视觉体验。可动画 attribute，如 scaleEffect，决定被动画的数据，而 Animation 决定这些数据如何随时间变化。

我将依次深入每个方面，从 Animatable 开始，它决定动画什么。SwiftUI 为任何符合 Animatable 协议的视图构建可动画 attribute。唯一要求是视图定义它想动画的数据的读写向量。数据必须符合 VectorArithmetic。

VectorArithmetic 匹配你在数学课上学到的向量教科书定义。它支持向量加法和标量乘法。

如果你生疏或不熟悉向量，别灰心。向量基本上只是固定长度的数字列表，而就 SwiftUI 动画而言，处理向量的目的大多只是抽象该列表的长度。

例如，CGFloat 和 Double 是一维向量，而 CGPoint 和 CGSize 定义二维向量，CGRect 定义四维向量。

通过处理向量，SwiftUI 能用单一泛型实现动画所有这些类型及更多。

到目前为止，为简化起见，我将 scaleEffect 表示为一维缩放因子。

一维 scaleEffect 的 Animatable 符合将是直接的。它的 animatableData 就是 CGFloat。

实际上，scaleEffect 允许你独立配置变换的宽度、高度和相对锚点——全部可动画。因此 scaleEffect 实际上为可动画数据定义四维向量：CGSize 的宽度和高度缩放，配对 UnitPoint 的相对锚点。

AnimatablePair 把两个向量融合成单个更大的向量。它是 public 类型，你也可以使用。如果你让自己的视图符合 Animatable，它可能派上用场。

scaleEffect 只是 SwiftUI 内置的众多可动画视觉效果之一，因此绝大多数时候，Animatable 不是你需要直接使用的 API。但在罕见情况下，高级用例可能要求让自己的视图符合 Animatable。

考虑宠物 Podium 视图，它使用自定义 RadialLayout 沿圆弧分布子视图。默认情况下，在动画中改变偏移角度会把宠物头像动画到新位置沿直线。注意宠物们如何 shortcut 并 trespass 圆的内部？这不是我想要的。

相反，我希望头像沿圆的周长动画。我可以把 Podium 符合 animatable 并使用偏移角度作为其可动画数据来获得此效果。

为什么这产生如此不同的效果？为解释，我将逐步过每个版本 Podium 视图的动画更新，从默认行为开始，它把头像沿直线动画。

Podium 的 body 由 RadialLayout 和三个头像组成。当事务打开时，如果偏移角度改变，body 被调用以刷新 stale 下游 attribute 值。然后运行 layout，更新每个子视图的位置。

这就是默认版本中的动画更新。活跃的可动画数据是视图位置 CGPoint，它在笛卡尔坐标空间插值，意味着每个头像沿直线移动。在自定义版本中，当我把 Podium 符合 Animatable 时，变化的是 body 成为活跃可动画 attribute，以偏移角度作为其可动画数据。这如何导致每个头像沿弧线移动？在这个自定义版本中，动画的每一帧，SwiftUI 都会用新的偏移角度调用 body，并重新运行 layout。

这非常强大，有时，如动画自定义布局或绘制代码时，它可能是实现你想要效果的唯一方式。

只需记住，自定义 Animatable 符合动画成本可能比内置效果高得多，因为它每帧都会运行 body。因此只有在无法用内置效果实现你想要的效果时才使用这个工具。

接下来，我介绍 Animation，随时间插值可动画数据的通用算法。

早先，我通过用 withAnimation 包裹状态更改给宠物头像视图添加动画。

你可以通过传递显式动画如 bouncy spring 来自定义。

SwiftUI 内置了大量强大动画。它们大致可分为三类：Timing curve animations、Spring animations 和 Higher order animations，后者修改基础动画。

Timing curve animations 可能是你最熟悉的动画类别。例如，easeInOut 是 timing curve animation。

所有 timing curve animations 都接受 curve，定义动画速度，以及 duration。

timing curve 可以用 bezier control points 创建。通过调整起始和结束 control points，你改变动画的初始和最终速度。

UnitCurve 类型可独立使用，计算 0 到 1 之间相对点的值和速度。

SwiftUI 内置若干 timing curve 预设：Linear、easeIn、easeOut 和 easeInOut。

所有 timing curve animations 也可以指定自定义 duration。

下一类动画，Springs，通过运行 spring simulation 决定给定时间点的值。

你可能熟悉传统指定 spring 的方式，例如 mass、stiffness 和 damping。但我们从未觉得这些方式特别直观，因此我们发明了新方式。你只需指定动画的 perceived duration 和你希望 spring 有多 bouncy。这更易上手。

类似 UnitCurve，Spring 类型可独立使用，计算给定时间 spring 的值和速度。

SwiftUI 内置三个 spring 预设：Smooth，无 bounce；snappy，少量 bounce；bouncy，较大 bounce。

如果你不习惯参数化 spring animation，这些预设是获得良好感觉的可靠方式。

每个预设也可以调整以调整 duration 或 tweak bounciness。

我们强烈推荐使用 spring animations，因为它们通过保留速度和自然归于静止给 UI 有机感觉。事实上，我们对 spring animations 的好处如此坚信，以至于在 iOS 17 和 aligned releases 中，当你使用 bare withAnimation 时，我们把 smooth spring 作为新的默认。

最后一类动画，Higher order，修改基础动画。它们可以减慢或加快它。可以在基础动画开始前添加 delay。可以重复基础动画任意次数，可选在正向和反向播放之间切换。

现在我们引入全新的动画类别：Custom animations。CustomAnimation 协议给你访问我们用来实现 SwiftUI 所有内置动画的相同低级泛型 entry points。

CustomAnimation 协议有三个要求：animate、shouldMerge 和 velocity。

我先聚焦 animate。shouldMerge 和 velocity 是可选要求。稍后回到它们。

animate 被传递要动画的向量、动画开始以来经过的时间量，以及 context，包含额外动画状态。

animate 返回动画的当前值，或 nil 如果动画已结束。

这个 value vector 来自哪里？它来自视图的 animatable data。在宠物头像视图中，那是 scale effect。

回想 scaleEffect 的 animatable data 是四维向量，包括二维 width 和 height scale。当头像被选中时，它从 1 by 1 的缩放因子动画到 1.5 by 1.5。

向量加法和标量乘法操作允许 SwiftUI 把这两个向量相减，计算它们之间的 delta。

这个 delta 实际上是被动画的对象。

这意味着，在实践中，运行在 scaleEffect 可动画 attribute 中的动画不是从 1 插值到 1.5，而是从 0 到 0.5。除其他外，这使实现 animate 方法更方便。让我展示。

我将实现由 duration 配置的线性 timing curve animation。

回想 animate 被传递要动画的 delta vector。我可以使用标量乘法把向量按已过 duration 比例缩放。一旦完整 duration 过去，我返回 nil 表示动画已结束，可以移除。就这样。而且因为此实现是泛型的，它与任意维度的 animatable data 都能工作。这就是 Animatable 和 Animation 如何协同产生 UI 中令人印象深刻的视觉效果。

接下来，我回到 CustomAnimation 的两个可选要求：shouldMerge 和 velocity。它们做什么？想象一会儿你是 scaleEffect 可动画 attribute。用户点按，事务打开，你的值改变，你制作动画的本地副本，并开始 happily 动画你的 delta vector。一切都很棒。直到 pesky 用户在动画结束前再次点按。你怎么办？你设置新动画，并在其上调用 shouldMerge。

默认实现返回 false——timing curve animations 这样做——在这种情况下两个动画将一起运行，系统会组合它们的结果。

这是 SwiftUI 动画处理 delta vector 的另一个原因。它使计算多个动画运行时的正确组合 presentation 值更容易。但如果我选了 spring animation 而非 timing curve animation 呢？Spring animations 覆盖 shouldMerge 以返回 true，并纳入前一个动画的状态。这允许它们保留速度并 retarget 到新值，可能比像 timing curve animations 那样加性组合更自然。

这就是最终 velocity 要求的用途。实现它允许在运行中的动画与新动画合并时保留速度。因此我将通过为 velocity 添加实现来完成线性 timing curve animation。

我在本场中用「transaction」一词指给定 UI 更新执行的一组工作。在 SwiftUI 代码中，Transaction 也指相关的强大数据流构造和 API 家族。你可能已经熟悉 Environment 和 Preferences，分别是 SwiftUI 隐式向下和向上传递的字典。Transaction 类似。它是 SwiftUI 用来隐式传播当前更新所有上下文的字典，最值得注意的是动画。

我早先对可动画 attribute 如何读取当前动画的解释有点模糊。因此我将追踪头像视图的另一个动画更新。这次我更具体。当 tap gesture 闭包触发时，withAnimation 在 root transaction 字典中设置动画。

body 被调用以更新 attribute 值。transaction 字典跨 attribute 图传播。当它到达可动画 attribute 时，attribute 检查是否设置了动画。如果有，它制作副本以驱动其 presentation 值。Transaction 只与特定更新相关，因此一旦 stale attribute 刷新，它被丢弃。

把动画沿视图层级在 transaction 字典中流动，使一系列强大 API 能控制动画何时以及如何应用于你的视图。

现在，宠物头像视图只能通过 tap 选择。我将把 selected State 变量改为 Binding。这样它也可以被 programmatically 选择。

但如何动画视图属性的 programmatic 更改？我可以使用 transaction modifier 访问随 transaction 字典沿视图层级流动的动画。

如果我从这个 modifier 内设置动画，那么无论 body 何时被调用，即使事务中没有动画或不同动画，attribute 都会覆盖动画。当它到达 scale effect 时，这个动画将被用于插值缩放因子。

相当酷。

但这个模式有问题。在 SwiftUI 刷新视图时 indiscriminately 覆盖所有后代的动画，可能导致意外动画。相反，对于这样的用例，SwiftUI 提供 animation view modifier。它接受额外的 value 参数，允许你更精确地限定效果。它只在值改变时才把动画写入事务。

现在那已接好，这个 withAnimation 没有 accomplishing 任何事，因此我们可以移除它。

animation view modifier 也是强大工具，用于你想对视图不同部分应用不同动画的情况。

例如，宠物头像有阴影，我为简化起见到目前为止在示例中省略。阴影半径在头像被选中时增加，以 accentuate 它抬高于背景的错觉。

试玩后，我决定想要阴影的动画比 scale effect 的更 subdued。为实现，我可以在 scaleEffect 和 shadow 之间插入另一个 animation view modifier。现在事务为动画 scale effect 拾取 bouncy spring。

并为动画阴影半径拾取更 subtle 的 smooth spring。

因为 animation modifiers 只在它们的值改变时活跃，意外动画的几率大大降低。但如果头像的 image 恰好在同一事务中与 selected 一起改变，它会继承阴影的 smooth spring animation 用于其 content transition。

这值得 linger。这个 animation view modifier 对 leaf 组件很好，其中整个子层级都在你控制下。但对于 non-leaf 组件，包含任意子内容，意外动画更可能发生。

例如，如果我想在与宠物无关的另一个 App 中复用头像，我可以让它更 generic，接受任意子内容。在这种场景下，我更少保证当 selected 改变时，子内容不会也改变。

这可能导致意外动画。好消息。我们有一个新版本的 animation view modifier，专门设计用于此类用例。它 narrow scopes 动画到 body closure 中指定的可动画 attribute。工作方式如下。想象事务中没有动画。当事务到达 animation view modifier 的 attribute 时，制作一个 populated with specified animation 的副本。副本向下游传播，但只到 scoped 可动画 attribute。一旦完成工作，副本被丢弃，原始事务从离开处继续。

因此当事务到达子内容时，因为原始事务不受任何中间 animation view modifiers 影响，没有意外动画的风险。有限的 transaction API 自 SwiftUI 第一版就可用。现在我们引入定义自定义 transaction keys 的能力，以便你可以利用 transaction 字典隐式传播你自己的更新特定数据。

如果你曾经声明过自定义 environment key，声明自定义 transaction key 会很熟悉。模式是创建符合 TransactionKey 协议的独特类型。唯一要求是提供 defaultValue。然后在 Transaction 上声明 computed property 作为 extension，使用你的 key 从 transaction 字典读写。这里我定义了 boolean key 以跟踪给定更新中头像是否被 tapped。我将基于其值决定使用哪个动画。

如果头像被交互式选择，我用更 lively spring 放大或缩小它。但如果头像被 programmatically 选择，我用更 subdued spring 缩放它。我可以通过用 withTransaction 包裹状态更改，在 transaction 字典中为给定更新设置值。这应该感觉熟悉。withAnimation 只是 withTransaction 的 thin wrapper。

传递给 withTransaction 的参数是 Transaction 上 computed property 的 keypath 和要设置的值。

Transaction 在 SwiftUI 的隐式数据流构造中独特，因为它在每次更新结束时被丢弃。这意味着，除非为当前更新显式设置，transaction 字典中的每个值都恢复为其 key 的默认值。

在头像视图中，当 tap gesture 闭包触发时，avatarTapped 为当前更新设置为 true。

transaction 还包含 animation key 的默认值，即 nil。

transaction 跨视图层级传播，直到到达 transaction modifier。

这里，头像视图读取 avatarTapped，并基于其值设置适当的动画……

它向下传播。

这运行得相当好，但就像早先一样，可能导致意外动画。

为了给你更细粒度的控制来修改事务，我们引入 transaction modifier 的两个新变体。一个允许用 value 参数限定。另一个允许限定到 body closure 中定义的子层级。这些变体镜像早先介绍的 scoped animation view modifiers。

本场中，我解释了 SwiftUI 强大的动画原语 Animatable、Animation 和 Transaction。

作为下一步，我推荐查看两个相关场次。「Animate with springs」提供更多关于为何以及如何在 App 中有效使用 spring animations 的指导。「Wind your way through advanced animations in SwiftUI」介绍用于构建多步动画的强大新工具。我希望这些内容给你更好地理解 SwiftUI 动画如何工作，并赋能你更 skillfully 在 App 中利用动画。谢谢。♪ ♪
