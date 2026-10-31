---
title: 设计流体界面
session_id: 803
collection: wwdc2018
year: 2018
duration: '64:41'
topics: [Design]
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2018/803/'
content_hash: 'sha256:7bcce8408dc551a3'
translated: true
---

# 设计流体界面

<sub>WWDC2018 · 64:41 · Design</sub>

探索用于创建 iPhone X 流体手势界面的技术。了解如何设计手势与动效，让它们感觉……

> [!note] 归档理由
> 流体界面背后的交互物理与响应性哲学，长期有效

## 相关资源

- [探索人机界面指南](https://developer.apple.com/design/human-interface-guidelines/)
- [相对于安全区放置内容](https://developer.apple.com/documentation/UIKit/positioning-content-relative-to-the-safe-area)
- [UIView](https://developer.apple.com/documentation/UIKit/UIView)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2018/803lpnlacvg2jsndx/803/803_hd_designing_fluid_interfaces.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2018/803lpnlacvg2jsndx/803/803_sd_designing_fluid_interfaces.mp4?dl=1)
- [演示文稿（PDF）](https://devstreaming-cdn.apple.com/videos/wwdc/2018/803lpnlacvg2jsndx/803/803_designing_fluid_interfaces.pdf?dl=1)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好。感谢各位光临。

谢谢大家过来，各位。

欢迎来到设计流体界面。我叫 Chan，我在 Apple 的人机界面团队工作。最近，我主要参与了这个项目，也就是 iPhone X 的流体手势界面。

所以，我和 Marcos、Nathan 想和大家分��一下我们在这个项目以及过去类似项目中学到的东西。

我们经常问自己一个问题：到底是什么让一个界面感觉流体？我们注意到，很多人对此的描述其实不一样。你知道，有时候，当人们真正试用这些东西时，我们给他们演示，他们试用并拿在手里，他们有时说这感觉快。或者其他人有时说这感觉顺滑。而当它感觉真的很好时，人们甚至会说它感觉自然，或者神奇。

但归根结底，这真的就像那种你知道一感觉到就知道的东西。它就感觉对了。

你可以有一个手势 UI，而且我们见过很多手势 UI，但如果没做对，总感觉有什么不对劲。而且往往很难指出为什么。

这不仅仅是帧率的问题，你知道。你可以让东西以每秒 60 帧的不错速率运行，但它就是感觉不对。那么，是什么给了我们这种感觉呢？我们认为，它归结为工具感觉像是你思想的延伸。思想的延伸。

那么，这为什么重要？你看，iPhone 是一个工具，对吧？它是用于信息和通信的手持工具。它通过把我们的触觉和视觉结合在一起工作。

但如果你想想，它实际上是一条可追溯到数千年前的手持工具长链的一部分。

左边的这个工具被用于 15 万年前提取骨髓，扩展了我们手指所能达到的锋利程度。所以我们已经制造手持工具有一段时间了。而最了不起的是，我们的手实际上与工具共同演化和适应。我们演化出了大量集中分布的肌肉、神经、血管，能够执行最精细的手势，并感知最轻的触碰。

所以我们对所居住的这个触觉世界极为适应。

但是，如果你看看计算机的历史，我们是从一个地方开始的，你和界面之间有很多层抽象。你需要知道很多东西才能操作它。这使它对很多人来说遥不可及。

但在过去几十年左右，你其实一直在剥离这些层，你知道，从间接操控开始，事情稍微更一对一一点。稍微更直接，一直到如今，我们终于把所有这些层都剥离了，到你直接与内容交互。对我们来说，这就是神奇的元素。当它不再感觉像计算机，而开始感觉更像自然世界的延伸。这意味着界面现在正在以比以往任何界面都更古老、更深层的层面与我们沟通。而我们对它的标准真的很高。你知道，如果 slightest 的东西感觉不对，砰，幻觉就破灭了。但当它感觉对时，它感觉像是你自己、你的身体的延伸。它是与你的思想同步的工具。使用起来感觉愉悦，感觉摩擦很低，甚至有趣。

那么，是什么给了我们这种感觉？当它感觉不对时，我们如何让它感觉对？这就是这场演示的全部内容。

我们今天要谈四件事。我们先从设计一些原则开始，谈如何构建感觉像我们延伸的界面。

如何设计动效，让它们与我们自身身体以及周围世界的动效保持一致。

以及如何设计优雅且智能的手势。我们还要谈，既然我们已经构建了这类东西，如何在其之上构建感觉原生于触觉这一媒介的交互。让我们开始。我们如何设计一个真正扩展我们思想的界面？我们如何做到这一点？我们认为，方法是把界面与我们思考的方式和移动的方式对齐。

所以，其中最重要的是，我们的思想在不断响应变化和刺激与思想，你知道？我们的思想和身体永远处于动态变化的状态。所以，不是界面应该是流体，而是我们是流体，而我们的界面需要能够响应这一点。

所以，这从响应开始。

你知道，我们的工具依赖于延迟。想想如果使用任何工具、演奏任何乐器，或者在物理世界做任何事时有延迟，会有多难？我们发现人们真的、真的对延迟很敏感。你知道？如果你引入任何程度的滞后，事情会突然在响应性上跌下悬崖。会有所有额外的心理负担。感觉完全脱节。不再感觉像是你的延伸。

所以我们努力降低延迟。事实上，我们实际设计了最新的 iPhone，让它对你的手指响应更快，以便我们能尽可能即时地检测到你所有手势的细微差别。

所以我们真的在乎这些，我们认为你也应该在乎。这意味着到处寻找延迟。不只是滑动。还有点击、按压、与对象的每次交互。一切都需要即时响应。

而在设计这些东西的过程中，你知道，延迟往往会稍微渗入一点。你知道？所以真正重要的是留意延迟。保持警惕， mindful of 所有我们可能引入到界面中的延迟或计时器，以便它始终感觉响应迅速。

所以，那就是响应这个话题。它很简单，但让界面感觉生动、动态。接下来，我们想允许持续的重定向与中断。这个很重要。

就像我们说的，我们的身体和思想在响应思想变化时永远处于重定向的状态。

所以，如果我走到这个舞台的末端，意识到我忘了那边的东西，我可以立即转身回去。我不必等到身体到达末端才做这件事，对吧？所以，我们的界面能够反映这种持续重定向的能力很重要。这让它感觉与你相连。

这就是为什么对于 iPhone 10，我们构建了一个完全可重定向的界面。

那是什么？所以 iPhone 10 其实——它是一个相当简单的双轴手势。你横向在 App 之间切换。你纵向回到主屏幕。但你也可以混合两个轴，所以你可以在回家的路上，偷看多任务，决定是否去那里。或者，你可以去多任务，然后决定，其实不，我想回家。

所以这可能看起来不太重要，但如果我们不做这个会怎样？如果它不可重定向呢？如果你能做的唯一手势是 App 之间的横向手势，以及回家的纵向手势，仅此而已。你不能做我刚才提到的任何中间操作。

那会发生什么？那就是，你必须在执行手势之前先思考，执行手势之前，你必须思考你想做什么。

会非常线性，对吧？所以你必须想，我想回家吗？我想去多任务吗？然后你做决定，然后执行手势，然后释放。

但酷的是，当它可重定向时，思考和手势并行发生。你 sort of 与手势一起思考，事实证明这比先想再做快得多。你知道？因为这是一个多轴手势空间。不是单独的手势。而是一个做所有这些事情的手势。Home、多任务、快速 App 切换，所以你不必把它当作单独的手势来思考。

这有助于发现。因为你可以在现有手势的路径上发现新手势。

它允许你在思想的速度下叠加手势。那么，最后一句是什么意思？让我展示一些示例。我们把模拟中的物理放慢了，以便你能实际看到我正在说的内容。

我可以滑动回家，然后在回家时滑动到下一页或 Springboard。一旦我内化了这些手势，就可以把这两个手势叠加起来。

另一个示例是，我可以启动一个 App 并意识到，哦，其实我需要去多任务，我可以在 App 启动时中断它并直接去多任务。

或者，我可以启动一个 App 并意识到，哦，那是错误的 App。我可以在启动时把它射回家。现在还有另一个，我实际上可以启动一个 App，如果我赶时间，我可以在它启动时开始与 App 交互。

所以这些可能看起来不那么重要，但我们发现这对界面始终响应、始终理解你非常重要。它始终感觉活着。这对于你对界面的期望和理解、感到舒适、意识到它总会在你需要时响应你，都非常重要。这也适用于运动的变化，不只是交互的开始，而是在交互的中途，你正在改变。对我们来说，对中断的响应也很重要。所以，一个很好的例子是 iPhone 10 上的多任务。

我们有一个暂停手势，你把手指向上滑到屏幕一半的位置，然后暂停，所以我们需要弄清楚如何检测这种运动变化。我们如何做到？如何检测这种运动变化？我们应该用计时器吗？我们应该等到你的手指低于某个速度一段时间，然后 bring in 多任务卡片吗？事实证明这太慢了。人们期望能够瞬间进入多任务。我们需要一种能像他们一样快速响应的方式。所以相反，我们看你的手指的加速度。

事实证明，当你暂停时，你的手指加速度有一个巨大的尖峰。而且，实际上你停得越快，我们检测得越快。所以它实际上是在响应运动变化，以我们所知最快的速度，而不是等待某个计时器。

所以这是响应重定向的最快方式的一个很好的例子。所以这就是中断与重定向的概念。这些东西让界面感觉真的、真的与你相连。

接下来，我们想谈一点界面的架构。你如何在概念上布局它。

我们认为，做这件事时，重要的是在整个运动过程中保持空间一致性。

这是什么意思？这有点像模拟我们在现实世界中的对象持久性记忆的工作方式。所以东西平滑地离开和进入我们的感知，走对称的路径。

所以，如果某样东西以某种方式消失，我们期望它从它来的地方出现？对吧？所以，如果我这样走出这个舞台，然后那样出现，你们会相当惊讶，对吧？因为那是不可能的。所以我们想利用我们所有人对世界的一致空间感。所以这意味着，如果你界面中的某样东西从视图中消失，然后重新回到视图中，它应该以对称的路径这样做。进入和离开时应该有 offscreen 的一致路径。iOS 导航实际上是一个很好的例子。当我点击这里的列表中的一个元素时，它从右侧滑入。

当我点击返回按钮时，它回到右侧。这是一条对称的路径。每个元素在两种状态下都有一个一致的所在位置。这也强化了手势。如果我选择向右滑动它，因为我知道它住在那里，我可以这样做。这是预期的。

那如果我们不做这个会怎样。这里有一个例子，当我点击某样东西时，它滑入，然后当我点返回时它向下走。而且感觉脱节和困惑，对吧？感觉像是我把它送到了某处。事实上，如果我想传达我正在把它送某处，这就是我该怎么做的，对吧？所以，那就是空间一致性的主题。

它帮助手势感觉与我们对世界的空间理解对齐。现在，下一个是在手势方向上进行提示。

你知道，我们人类总是 kind of 预测我们体验的接下来几步。我们总是使用世界上所有正在发生的事情的 kind of 轨迹来预测接下来几步的情感。

所以，我们认为当一个界面利用这种预测时很棒。所以，如果你这里有两种状态，初始状态和最终状态。对象——并且你有一个中间过渡。对象应该在两种状态之间平滑过渡，无论通过手势还是动画，都从初始状态增长到最终状态。

所以，一个很好的例子是控制中心。我们这里有控制中心中的这些模块，当你按压时，它们向上并向外朝向你的手指增长，朝向最终状态，最终只是弹开。所以，那就是提示。它让手势感觉预期且可预测。现在，下一个重要原则是保持触控交互轻量。

你知道，多点触控的轻盈性是我认为被最低估的方面之一。它实现了轻盈的滑动和滚动，以及我们所有习惯的点击等等。所有都非常轻量。但我们也想放大它们的运动。你想取一个小输入并产生大输出，以获得那种移动或投掷某物并获得被放大的结果的满足感。这如何应用于我们的界面？它从一个短暂的交互开始。

一个短暂、轻量的交互。

我们使用我们所有的传感器、所有技术，来尽可能多地理解它。Sort of 生成一个包含手势中能量和动量的 profile。

使用我们所知的一切，包括位置、速度、速率、力度、我们对它所知的一切，来生成这种手势的惯性 profile。然后我们取那个，并生成你运动的放大延伸。它仍然感觉像是你的延伸。所以，你用轻量的交互获得那种满足的结果。

所以，滚动实际上是一个很好的例子。你的手指只在屏幕上短暂时间，但系统在保留你所有的能量和动量，并优雅地把它们转移到界面中。

那如果它没有这个会怎样？同样的滑动，嗯，它们不会带你走很远。

为了滚动，你将不得不做这些长而费力的滑动，需要更多的手动输入。使用起来会非常痛苦。

另一个很好的例子是滑动回家。

你的手指在屏幕上的时间非常轻。它 ended up 使它成为一个更液体、更轻量的手势，仍然感觉原生于多点触控的媒介。

同时仍然能够重用很多你从按钮获得的肌肉记忆，因为你把手指在屏幕上向下移动，然后回到 Springboard。而且不只是滑动，点击也是。让界面对每次交互都做出满足的响应很重要。界面在向你发出信号，表示它理解了你。这对于界面感觉活着、与你相连非常重要。

所以，那就是轻量性与放大的主题。

下一个叫做橡皮筋（rubberbanding）。

它意味着我们正在柔和地指示界面的边界。在这个例子中，界面逐步、柔和地让你知道那里什么都没有。并且它在整个过程中跟踪你。它始终让你知道它正在理解你。

如果你不做这个会怎样？嗯，它会感觉像这样。会感觉非常生硬和令人不安。你 kind of 在那里撞墙。它会感觉坏了，对吧？而且你实际上无法区分一部冻结的手机和一部只是在屏幕边缘顶部的手机，对吧？所以，始终告诉用户你已到达边缘真的很重要。这同样适用于过渡。不只是当你撞到边缘时，也是当你从一个东西移交给另一个东西时。跟踪。所以一个很好的例子是，当你从向上滑动 Dock 过渡到向上滑动 App 时。它不只是撞墙，一个东西停止跟踪，然后另一个东西接管。它们都平滑地在平滑的曲线中交接，这样你就不会感觉有一个生硬的时刻，从一个东西切换到另一个东西。下一个是设计平滑的运动帧。

所以，想象我这里有一个小对象上下移动。非常简单。但我们都知道这个对象实际上并没有在动，对吧？我们都有它在动的感知。因为我们同时在屏幕上看到一堆帧，这给了我们它在动的幻觉。所以，如果我们把所有这些运动帧 kind of 展开在这里。我们看到球在时间中的运动，我们关心的是就在这里，相邻帧之间有太多视觉变化。这是界面的感知变得有点卡顿的时候。你会得到这种视觉频闪。

这是因为两帧之间的差异太大了。

它在你的视觉上频闪，所以。这里有一个例子，你有两个东西都以每秒 30 帧移动。但左边的那个看起来比右边的稍微顺滑一点，因为右边的那个移动太快了，以至于它在频闪。我对视觉的感知 kind of 崩溃了。我不再相信它在平滑移动了。

所以，重要的 takeaway 是，这不只是帧率的问题。而在帧中有什么。

所以我们 kind of 受帧率限制，以及我们能以多快的速度移动同时仍保留平滑运动。

这个是每秒 30 帧。如果我们把它提高到每秒 60 帧，你可以看到我们实际上可以 go a little bit faster，同时仍保留平滑运动。我们可以在不频闪的情况下做更快的运动。

而且，我们还可以做额外的技巧，比如运动模糊。运动模糊基本上在每一帧中烘焙了更多关于运动的信息，像你的眼睛工作方式和相机工作方式一样。

你还可以——从二维动画和视频游戏中借鉴一页，通过拉伸，这种叫做运动拉伸的技术在每一帧中拉伸内容，以提供这种弹性外观，因为它以速度移动。所以，在运动中，它 kind of 看起来像这样。所以，每种不同的技术 kind of 试图在视觉上编码更多关于运动中正在发生的事情的信息。我想稍微关注一下最后一个，运动拉伸，因为我们实际上在 iPhone 10 上做了这个。你知道，当你启动一个 App 时，图标弹性地向下拉伸，变成 App，因为它打开。

当你关闭 App 时，它在相反方向上向上拉伸。给你每帧运动之间那一点额外信息，让它看起来稍微更顺滑一点。最后，我们想与行为而非动画一起工作。你知道，现实世界中的东西永远处于动态运动状态，并且永远受到你的影响。它们并不真的像动画意义上的动画那样工作，对吧？现实生活中没有 prescribed 的动画曲线。所以我们想把动画和行为更多地看作是你与对象之间的对话。不是由界面 prescribed 的。所以，从静态东西过渡到动画东西，转而思考行为。所以，Nathan 即将深入探讨这一点。但这里有一个快速示例。所以，在 Photos 中，照片上有更少的质量，因为它在概念上更轻。但当你滑动 App 时，App 上有更多质量。它在概念上更重，所以我们给系统更多质量。

这就是关于如何设计像我们一样思考和工作的界面的一点。

在——它从响应开始。让东西感觉与你相连，并适应我们思想永远处于运动中的方式。

保持空间一致性，强化一致的空间感，以及该空间内的对称过渡。

并在手势方向上进行提示。利用我们对未来预测。并保持轻量的交互，但放大它们的输出。

获得那种满足的响应，同时仍保持交互 airy 和轻量。并拥有柔和的边界和边缘的界面。界面始终优雅地响应你，即使你撞到边缘，或从跟踪一个东西过渡到跟踪另一个东西。并设计与你协同工作的平滑动态行为。所以，那就是关于如何接近构建感觉像我们思想延伸的界面的一些原则。

所以，让我们再深入一点。我将把它交给我的同事 Nathan de Vries，设计动效——谈如何设计动效，让它们与运动、与你和自然世界的运动相连。谢谢，Chan。

大家好。我叫 Nathan，我今天超级兴奋能在这里和大家谈设计动态动效。

正如 Chan 提到的，我们的思想和身体永远处于变化状态。我们周围的世界处于变化状态。而这引入了这种期望，即我们的界面也以相同方式表现，随着它们变得更 tactile，它把我们的期望转移到更高的保真度。

我们使用动效在界面中的一种方式是通过定时动画。屏幕上点按一个按钮，然后 sort of 把控制权交给设计师。

他们的工作是通过时间来制作这些完美的动画帧。一旦动画完成，控制权就交还给使用界面的人，以便他们继续交互。

所以，你可以 kind of 把动画和交互看作是——随着时间线性地移动，这种 kind of 呼叫与响应模式。在流体界面中，使用界面的人的动态性质 kind of 把随时间的控制从我们作为设计师身上移开。

相反，我们的角色是设计动效如何与交互协同工作。我们通过这些始终运行、始终活跃的连续动态行为来做这件事。所以，这些动态行为就是我今天真正要 focus 的。首先，我们要谈无缝运动。而它是动效中那个让它感觉像是你自己延伸的元素。

然后，我们要看一下特性。如何即使没有定时曲线和定时动画，我们也可以给界面中的动效引入趣味、特性或质感的概念。

最后，我们将看动效本身如何给我们一些关于人们打算用你的界面做什么的线索。我们如何通过真正看手势的动效来解决关于手势试图做什么的一些不确定性。所以，为了开始，让我们看无缝运动。我所说的无缝运动是什么？让我们看一个我认为我们都能熟悉的例子。

我们这里有一辆汽车，它以恒定速度巡航。然后，刹车被应用，把它完全停住。让我们再看一次，但这次我们绘制汽车随时间的位置。所以在曲线的最开始，它 kind of 是直的，指向右上。这表明汽车的位置以恒定速率移动，kind of 不变。

但然后，你会注意到曲线开始弯曲，平滑地弯曲离开这条直线。这就是刹车被应用。汽车因引入的摩擦而减速。

到了曲线的末尾，曲线完全平坦、水平，显示位置现在不变。汽车停了。所以，这个位置曲线本质上可视化了我们所说的无缝运动。这条线完全不中断，并且方向没有突然变化。

所以它是平滑且无缝的。甚至当，实际上，新的动态行为被引入到汽车的运动中时，比如刹车，它对汽车应用摩擦。

甚至当汽车完全停下时，你会注意到曲线完全平滑。它有一种难以察觉的品质。你无法判断汽车精确何时停下。那我为什么谈汽车？这是关于流体界面的讲座，对吧？我们认为物理世界的特性为 great behaviors 造就了基础。

这个房间里的每个人发现汽车例子如此简单，因为我们对像汽车这样的对象如何在世界中移动有 shared understanding，或 shared intuition。

这使它们成为 great reference point。现在，我并不是说我们需要构建完美的汽车物理模拟，让它们 literally 驱动我们的界面。但我们可以借鉴汽车的运动、我们投掷或在周围物理世界中移动的对象的运动，并在我们自己的动态行为中使用它们，让它们的运动感觉熟悉、相关，甚至可信，这是最重要的。现在，这种在动态行为中引用物理世界的想法，从一开始就在 iPhone 中通过滚动存在。

一个孩子可以拿起 iPhone 并滚动到主屏幕上的 favorite App，就像他们可以把玩具车推过地板一样容易。那么，我们拥有的这个滚动动态行为的一些关键 kind of 特性是什么？嗯，首先是利用这种直觉，我们所有人对对象在世界中移动的 shared understanding。以及我们对那些对象的影响。

内容的运动是完美无缝的，所以当我与它交互时，当我拖动内容时，我的身体提供了运动的流体性，因为我的身体是流体。

但一旦我放开内容，它无缝地滑行到停止。所以，我们 kind of 保留了投入界面的努力的动量。

滚动使用的摩擦量是一致的，这使它可预测，并且非常容易掌握。

最后，内容来到一个难以察觉的停止，有点像汽车，不太知道它精确何时停下。

我们觉得这种 distinct 缺乏结尾 kind of 强化了内容始终在移动、始终能够移动的想法，所以当内容滚动时，它让你感觉可以再次把手指放下，继续滚动。你不必等待任何东西完成。所以，物理世界有无数特性会造就 great behaviors。

我们没有时间谈完所有，但我想 focus on 下一个，因为我们 personally 发现它在我们自己的设计工作中极为不可或缺。

所以，像这朵美丽的花这样的材料，这朵花的天然纤维有这种叫做弹性的有机特性。

弹性是材料在移除应力或应变后优雅地回到静止状态的倾向。

我们自己的身体极为有弹性。

我们能够跑非常长的距离，不是因为肌肉的力量，而是因为它们放松的能力。

是它们的弹性在做这件事。

所以，我们的肌肉在移除应力和应变后收缩和放松。这就是我们如何保存能量。让我们感觉自然和有机。同样的弹性用于 iPhone 10。

点按主屏幕上的一个图标，一个弹性行为把 App 拉向你。

把它放到你想要的精确位置。当你从底部滑动时，App 被放回主屏幕的完美位置。我们也在滚动中使用弹性。所以，如果我滚动太远并橡皮筋，就像 Chan 谈到的，当你放开时，内容使用弹性拉回边界内，帮助你进入这个静止位置，为下一次你想滚动做好准备。所以，让我们再深入一点，看看这个弹性背后如何工作。你可以把滚动内容看作是一个附在弹簧上的球。弹簧的一端是当前值。这是内容在显示屏上的位置。

弹簧的另一端是内容因为弹性想要去的位置。所以，你有这个弹簧把当前值拉向目标。它的行为正在影响内容的位置。

现在，弹簧本质上把当前值拉向目标。

弹簧有趣的地方在于，它 seamless 地做这件事。这种 seamless 性 kind of 内置在行为中。

这就是它们成为做流体界面设计的如此多功能工具的原因。

因为你可以 kind of 免费获得这些东西。它 baked in 到行为本身。所以我们 love 这个值向目标移动的行为。我们只需告诉球去哪里，就会得到球向目标移动的 seamless 运动。但我们想要对它移动多快、是否过冲有更多控制。我们如何做到？嗯，我们可以给球更多质量，比如让它更大，或更重。

如果我们这样做，那它会改变球的惯性，或它开始移动的意愿。或者它不愿停止移动的不愿。你 ended up 有这个 little 过冲。我们可以改变的另一个属性是弹簧的刚度，或弹簧的抗拉强度。这影响施加到球上的力，改变它向目标移动的速度。最后，就像汽车和汽车的刹车，我们可以改变球所在表面的阻尼，或摩擦。这会充当 kind of 刹车，随时间减慢球的速度，也影响我们过冲的能力。所以，球和弹簧的物理属性 kind of 是物理课材料，对吧？在科学上下文中 extremely useful，但我们发现，在我们自己的设计工作中，它们可能有点压倒性或笨重，用于控制屏幕上对象的行为。

所以我们认为我们的设计工具应该有一点人机界面。它们需要反映使用工具的设计师的需求。

我们如何做？我们如何简化这些属性，使其更设计友好？所以质量、刚度和阻尼将保留在幕后，它们是我们使用的弹簧系统的基本属性。但我们可以把界面简化为两个简单属性。

第一个是阻尼，它控制过冲多少或多少，从 100% 阻尼（不会有过冲）到 0% 阻尼（弹簧会无限振荡）。

第二个属性是响应。

这控制值尝试到达目标的速度。

你可能会注意到我 haven't 用 duration 这个词。我们实际上喜欢在描述弹性行为时避免使用 duration，因为它强化了这种持续动态变化的概念。弹簧始终在移动，并准备好移动到别处。

这些两个属性的技术术语是阻尼比和频率响应。所以，如果你想在自己的设计工作中使用它们，你可以查找这些术语，你会找到容易转换它们的方法。我们现在有了这两个用于控制弹性行为的简单属性。但有了这些曲线，我们仍然有无限的可能性。就像，有成百上千、数百万种不同的方式可以配置这两个简单属性并获得非常不同的行为。

我们如何使用这些来塑造 App 的特性？控制 App 的感觉？嗯，首先，我们必须记住，我们的设备是工具。

我们 need to respect that 工具在有目的使用时，需要我们不碍事，不通过引入不必要的运动来碍事。

所以我们认为你应该从简单开始。

弹簧不必过冲。你不需要使用 springy springs。

所以我们建议在调优弹性行为时从 100% 阻尼，或无过冲开始。

这样你就会得到平滑、优雅、无缝的运动，不会分散手头任务的注意力。就像快速发一封邮件。

那么，什么时候适合使用 bounciness？肯定有 sometime 适合，对吧？我们觉得，如果驱动运动的手势本身有动量，那你 should reward that 动量 with a little bit of 过冲。

换句话说，如果一个手势有动量，而没有过冲，运动跟随那个手势常常感觉坏了或不满足。我们使用这个的例子是在 Music App 中。

Music App 底部有一个小 minibar 代表 Now Playing，你可以点按该栏来显示 Now Playing。因为点按在 Now Playing 呈现方向上没有动量，我们使用 100% 阻尼来确保它不过冲。但如果你滑动以关闭 Now Playing，dismissal 方向上有动量，所以我们使用 80% 阻尼来有一点 bounce 和 squish，使手势更满足。

Bounciness 也可以作为 utility，作为功能手段。

它可以作为有更多内容在表面之下的 helpful hint。在 iPhone 10 中，我们向 Cover Sheet 引入了两个按钮，用于打开手电筒和启动相机。

为了避免误开手电筒，我们要求更 intentional 的手势来激活手电筒。

但如果你不知道激活它需要更 intentional 的手势，当你点按按钮时，它以 bounciness 响应。有一种 kind of playful feel。

而那个 hint 在教你，不仅按钮在工作，而且它在响应你。但它 kind of 在教你，如果你按得更 firm 一点，它就会激活。就像在教你。它在手势方向上进行提示。所以，bounciness 可以用来指示这类东西。现在，到目前为止，我们一直在谈使用动效来移动东西，或改变它们的缩放、改变它们在屏幕上的视觉表示。

但我们以多种方式感知运动。

通过光和颜色的变化，或质感和感觉。

甚至声音。许多其他我们的感官可以检测的 sensations。我们觉得这是一个机会，去 even further，超越动效，当你调优 App 的特性时。

通过把动效的动态行为与声音和触感的动态行为结合，你真的可以从根本上改变界面的感觉。

所以，当你看到、听到并感受到手势的结果时，它可以把原本只是滚动行为的东西变成感觉像非常 tactile 的界面。现在，当你要塑造 App 的特性时，有一个 final note 我希望你记住。

那就是它感觉 cohesive，保持 in character。这是什么意思？所以，即使在你的 App 内，或整个系统，重要的是把行为视为行为的 family。

所以，例如在滚动中，当我使用滚动行为向下滚动一页，然后点按状态栏滚动到页面顶部，使用弹性行为。

在这两种情况下，页面本身感觉像是以相同方式移动，它有相同的行为，即使两种不同类型的行为在驱动它的运动、影响它的运动。

现在，这 extend beyond 单个交互，如滚动。

它适用于你的整个 App。如果你有一个 playful 的 App，那么你应该 embrace that character，并让整个 App 感觉相同。这样人们——一旦他们学会 App 的一种行为，就可以很容易地 picked up 另一种行为，因为我们通过重复学习。我们学到的东西会 bleed over 到其他行为。

所以下一个，我想谈一点对齐动效，或动态动效，与意图。

所以，对于像按钮这样的离散交互，手势的意图相当清楚。对吧？你这里有三个 distinct 的视觉表示。

当我点按其中一个时，结果是清楚的。

但像滑动这样的手势，意图不那么立即清楚。你可以说是意图 almost encoded in 手势的运动，所以我们的角色是解释运动意味着什么，决定我们该对它做什么。让我们看一个例子。

所以，假设我打了一个 FaceTime 通话，一对一的 FaceTime 通话，在 FaceTime 中，我们有一个小视频表示你在屏幕角落。这是为了让我看到对方看到的内容。

我们把这个浮动视频叫做 PIP，picture in picture 的缩写。

现在，我们给 PIP 一个浮动外观，以明确它可以移动。

它可以被移动到屏幕的任何角落，只需一个 really lightweight flick。

所以，如果我们把这个与 Play、Pause 和 Skip 按钮比较，like，区别是什么？所以，在这种情况下，我们 actually 处理四个 invisible 区域。我们不再有屏幕上被点按的三个 distinct 的视觉表示。我们 kind of 必须看手势中发生的运动，并 intuit meant 了什么。我们 meant 去哪个角落？现在，我们把这些屏幕区域叫做手势的 endpoints。

当 PIP 被扔出时，我们的目标是找到正确的 endpoint，那个 meant 的。我们叫做把 endpoint 与手势的意图对齐。所以一种方法是在拖动 PIP 时跟踪最近的 endpoint。现在，这 kind of works。我可以把 PIP 移动到屏幕的另一个角落，但它一旦我再把 PIP 移动一点就 breakdown。现在，我 actually 需要把 PIP 拖动相当远，like past halfway over the screen。相当接近另一个角落。所以它并不是真正 magnifying 我的输入。它并不是真正为我工作。如果我 try to flick the PIP，它 kind of 回到最近的角落，这 not necessarily 是我 expected 的。所以，这里的问题是我们只看 position。我们完全忽略了 PIP 的动量，以及它被扔出时的速度。

那我们如何把动量纳入决定我们去哪个 endpoint？所以，为了思考这个，我想我们可以暂时把 endpoints 放一边，退一步。

just really simplify the problem。最终，我在这里试图做的是在屏幕上移动内容。

而我 actually 已经有大量肌肉记忆来 precisely 做这件事，通过滚动。所以我们为什么 not 在这里使用它？我们 all the time 使用滚动行为，所以我们对内容在我滚动时会走多远有 natural intuition。

所以，这里你可以看到，当我 instead 滚动 PIP 时，它 coast along，它 slowing down，使用我们从滚动熟悉的 deceleration。

基本上，通过在这里利用这一点，我们 reinforcing 人们 elsewhere 学到的东西。行为 just 是系统 expected 的。现在这个新的、hypothetical、imaginary 的 PIP 位置不是真实的。我们不会在界面中显示 PIP 去那里。我们叫做 projection。

所以，我们取了 PIP 被扔出时的速度。我们 kind of mixed in deceleration rate，我们 ended up with 这个 projected position，它 could go if 我们 scrolled it there。所以现在，不是找到我们扔出时 PIP 最近的 endpoint，我们可以计算它的 projected position 并移动到那里。所以现在，当我 just 用 lightweight flick 从屏幕的一个角落滑到另一个角落时，它去到了我 expected 的 endpoint。

所以，这个使用 projection 来找到 position 的 endpoint 的 idea，对于被拖动或滑动的东西 incredibly useful。我们觉得它 super important。我想与你分享一些 code for doing this，以便你可以在自己的 App 中做到。所以，这个 function 会 take 一个速度，像 PIP 的 position velocity，和 deceleration rate，它会给你一个你可以用作动态行为 endpoint 的值。

相当简单。如果我们看我的 FaceTime 示例中的 pan gesture 结束 code，你可以看到我 just 使用 UIScrollView.DecelerationRate。所以，我们 leaning on 人们对滚动的熟悉以及滚动时内容会走多远。

我用它与我的 projection。所以，我取 PIP 的 velocity 和 deceleration rate，我 create 那个 imaginary PIP position。而正是这个 imaginary、projected position，我 then use as 最近的 corner position。

我通过 retargeting 把 PIP 发送到那里。

所以，这个使用 projection 来找到 position 的 endpoint 的 idea，对于被拖动或滑动的东西 incredibly useful，你 really 需要 respect 手势的动量。

但这个 projection function 不只是对 positions useful，你也可以用它来处理 scales，甚至 rotations。

甚至两者的组合。

它是一个 really versatile tool，你 should really be using 它，以确保你 respect 手势的动量，并让 App 中的动态运动感觉像是你自己延伸。

那就是设计动效。动态动效。

行为 should continuously and seamlessly work in concert with 交互。

我们应该 leaning on 我们对周围物理世界的 shared intuition。我们作为孩子学到的关于对象在物理世界中如何表现和移动的东西，just as readily 适用于我们的动态界面。

你应该 remember bounciness 需要有目的。思考你为什么使用它，以及它是否 appropriate。并确保当你 add character 和 texture 时，你 balancing 它 with utility。

最后，remember to project momentum。不要 just 使用 position，使用所有 at your disposal 的信息，以确保 motion 与人们 actually 想要去的地方的意图对齐。然后，把他们带去那里。所以，为了谈一点如何流体地响应手势和交互，我想介绍我的同事 Marcos 上台。谢谢大家让我上台。那很棒。

谢谢，Nathan。

大家好。

我叫 Marcos。

到目前为止，我们已经看到流体性在设计界面时有多么重要。

其中很多来自你与设备的交互。

所以，在这个部分，我们将向你展示屏幕上触控如何在你的 App 中变成手势。以及如何设计这些手势，以捕获所有表达和意图进入你的界面。

所以，我们将从看一些核心手势的设计开始，比如点击和滑动。

然后，我们将看一些交互原则，你在为界面设计手势时 should follow。

然后，我们将看如何处理多个手势，以及如何把它们组合进你的 App。

我们将从看一个表面上看起来非常简单的手势开始，点击。

你可能会认为——你可能会认为点击是 something that doesn't have to be designed，但你会看到它的行为比看起来有更多的细微差别。

在我们的示例中，我们将看点击按钮，在这种情况下，是 Calculator App 上的按钮。

要记住的第一件事是，当我 touch down 按钮时，按钮 should immediately highlight。

这向我显示按钮在工作，系统正在响应我的手势。

但我们 shouldn't confirm the tap，直到我的 touch goes up。

要记住的下一件事是 around the tap area 创建一个 extra margin。这个 extra margin 会使我们的点击更舒适，并避免如果触控在交互过程中移动时的 accidental cancellations。就像我的同事 Chan 说的，我 should be able to change my mind after 我 touch down 按钮。所以，如果我拖动手指离开 tap area 并抬起，我可以 cancel the tap。同样，如果我 swipe it back on the button，按钮 should highlight again，并让我 confirm the tap。

我们要谈的下一个手势是滑动。

滑动是 iOS 的核心手势之一，它们用于多种动作，如滚动、拖动和分页。

但无论你用它做什么，或怎么称呼它，手势的核心原则始终相同。在这个示例中，我们要使用滑动把这张图像向右拖动。

所以，交互在我 touch down 图像 with intention to drag it 时开始。

但在我们能确定它是滑动之前，触控必须移动 certain distance。我们学会区分滑动和其他手势。这个距离叫做 hysteresis，iOS 中通常是 10 points。

所以一旦触控达到这个距离，滑动就开始。

这也是决定滑动方向的好时刻。例如，是水平还是垂直。在这个示例中我们 not really need it，但它在某些情况下非常有用。所以，现在滑动已被检测到，这是手势的初始位置。

在这一时刻之后，触控和图像应该 stay together 并作为 one thing 移动。我们应该 respect 相对位置，never use 图像的 center 作为拖动点。

在拖动过程中，我们还 should keep track of position 和 speed up the touch，这样当拖动结束时，我们 not use 最后一个位置。我们 use 触控的历史，以确保所有运动都被 fluidly transferred into 图像。

所以，正如我们所见，触控和内容应该 move together。一对一跟踪 extremely important。当滑动或拖动时，内容 should stay attached to 手势。

这是 iOS 的原则之一。你 enable scrolling，并使设备感觉 natural and intuitive。它如此 recognizable and expected，以至于 the moment 触控和内容 stop tracking one-to-one，我们 immediately notice it。而在滚动的情况下，它向我们显示我们已到达内容的末尾。但一对一跟踪 not limited to 触控屏。例如，在 Apple TV 上操控 UI 是围绕这个概念设计的。

所以，即使触控 not directly manipulating 内容，手势与界面之间的 direct connection 也让你控制动作，并使交互直观。

设计手势时的另一个核心原则是，在交互过程中提供 continuous feedback。这 not just limited to 滑动或拖动。它适用于所有交互。所以，如果你再次看 iPhone 10 上的手电筒按钮，按钮的大小基于我的触控压力变化。这给了我 action 的确认。它向我显示系统正在响应我的手势，但它 also teaches me 按得更 firm will eventually turn on the flashlight。continuous feedback 的另一个好例子是 Apple TV 上的 focus engine。

所以，Siri remote 上的移动 continuously represented on the screen。它们向我显示当前 selected 的 item，selection 即将改变的 moment，以及 selection 将要去的方向。所以，在手势过程中让我们的 UI 响应 critical to create a fluid experience。因此，当实现你的手势时，你应该 avoid 仅在手势结束时检测的方法，比如 UISwipeGestureRecognizer。并使用 ones like 实际的 touch，或其他 gestureRecognizers，它们提供关于手势的所有可能信息。

not just position，还有 velocity、pressure、触控的 size。然而，在大多数情况下，你的界面 must respond to more than one gesture。

随着你不断给 App 添加功能，复杂度和手势数量也会增加。例如，几乎所有使用 scroll view 的 UI 都会有 other gestures like taps 和 swipes 与之竞争。像在这个示例中，我可以滚动 Contacts 列表，或 free touch 其中一个来预览它。

所以，如果我们 had to wait for final gesture，before 我们 show any feedback，我们将 have to introduce a delay。而在等待期间，界面 wouldn't feel responsive。因此，我们应该从 action 的 beginning 就 detect all possible gestures。一旦我们 confident of intention，就 cancel all other gestures。

所以，如果我们回到示例，我开始按压那个联系人，但决定 instead 滚动。正是在 that moment，我们 cancel the 3D touch action，并 transition into right gesture。

然而，有时不可避免地要引入 delay。

例如，每次我们在 UI 中使用 double-tap 时，所有 normal taps 都会被 delayed。

系统 must wait after the tap，to see if it's a tap or a double-tap。在这个示例中，因为我可以 double-tap to zoom in and out of a photo，tapping to show app menu 被 delayed by about half a second。

所以，当为你的应用设计手势时，你应该 awareness of these situations，并尽可能避免 delay。

所以，to summarize，我们已经看到如何设计一些 core gestures，如 taps 和 swipes。我们已经看到内容和触控 should move one-to-one，并且这是 iOS 的 core concepts 之一。

你也 should provide continuous feedback during all interactions，并且当有 multiple gestures 时，从 beginning 就 parallel detect 它们。现在，我想把它交回给 Chan，他将谈与流体界面一起工作。谢谢大家。干得不错。

Alright，我回来了。

所以，我们 just learned about 如何 approach building interfaces that feel as fluid、as responsive、as lively as 我们 are。

所以，lets talk about 一些 considerations now that 我们're feeling a little bit more comfortable with this，for working within the medium of fluid interfaces。And that begins with teaching。

所以，手势界面的一个 downside 是 gestures 不是 immediately obvious。所以，我们必须 be friendly and clever about 如何 bring users along with us in a way that's friendly and inviting。

所以，一个方式是我们使用 visual cues。所以，世界充满了这些东西，对吧？你可以 learn them once，并 use them everywhere。它们是 portable。所以，当你 see this 时，你知道 how to use it。

所以，我们 tried to establish similar conventions in iOS。这里有几个例子。

所以，如果你有一个滚动的内容列表，你可以把内容从底部 clip off，以 indicate 有更多要 see，这 invites 我 try to reveal what's under there。如果我们处理内容 pages，你可以使用 paging indicator to indicate 有 multiple pages of content。

对于滑动的 panes of content，你可以使用 affordance，或 grabber handle like this，to indicate 它是 grabbable and slidable。

你可以使用的另一个技术是 elevate interactive elements to a separate plane。所以，如果你有一个 interactive element，把它 lift up to a separate plane 可以 help distinguish it from the content。

所以，我们的 on/off switch 是一个好例子。我们想 indicate switch 的 knob 是 grabbable，所以我们 elevate it to another plane。这 helps visually separate it，并 indicate 它的 draggable nature。

所以，floating elements，interactive elements like this，above the interface 可以 help indicate 它们是 grabbable。Next，我们可以使用 behavior，你知道，show rather than tell to use——如何使用界面。所以，我们可以 reinforce 一个 dynamic behavior with a static animation。

所以，Safari 是一个例子。在 Safari 中，我们有左上角的 x icon to close the tab，当你 hit that button 时，我们 slide the tab left to indicate 它是 deleted。

这 hints to me，我可以 slide it myself to the left。并 accomplish 相同的 action of deleting the tab through a gesture。

通过 keeping 离散动画和手势 aligned，我们可以 use one to teach the other。

还有另一个技术我们可以使用，就是 explanations。这是当你 explicitly tell users 如何使用 gesture。

所以，这 best when used sparingly，但它 best when 你有一个 gesture 在 bunch of places 被 repeatedly used，你 explain it once up front，然后 just keep using it，并 keep reinforcing it。

不要 use 它 for 只是 intermittently 使用的 gesture。人们不会 remember that。

现在，我想谈一点 fun 和 playfulness。因为这是流体界面最重要的方面之一。And, it only happens when you nail everything。

它是流体界面的 natural consequence。它是当界面 instant and satisfyingly 响应。当它 redirectable and forgiving。当 motion 和 gestures smooth。以及我们 just talked about 的一切。界面开始感觉 in sync with you。

然后，something magical happens where 你 don't feel like 你需要 learn the interface，你 feel like 你在 discovering the interface。

所以，我们认为 great when 我们 allow people to discover the interface through play。并且 it doesn't even feel like 他们在 learning it，it feels fun。

所以，人们 love playing with stuff。所以，我们认为 great to play into our natural fiddle factor。

你知道，play 是我们 mind's internalizing 界面的感觉。所以，great when 我们 build this stuff，when 我们 prototype it，just to build it。你知道，play with it yourself。See how you fiddle with it。Hand it to others see how they play with it。And，think about how 你可以 reinforce that with something like an animation，or behavior，an explanation。

并且 it's surprising how far play can go，以及 having interface teach itself to people。让我们谈一点 fluidity as a medium。我们 actually go about building this stuff。你知道，我们认为这样的界面是 unique medium，important that 我们 approach it right。

所以，第一件事是 design the interactions to be inseparable from the visuals，not an afterthought。交互设计应该 in concert with visuals 完成。你不应该 even be able to tell when one ends and another begins。

并且 really important that 我们 build demos of this stuff。interactive demo 我们 think really worth a million static designs。not just to show other people，but to also understand the true nature of the interface yourself。

并且 when 你 prototype this stuff，it's so valuable for you because 你 get to almost discover the interface as 你're building it。

你知道，this technique is actually how 我们 built the iPhone 10 interface。

并且 it's really important because 它 also sets a goal for the implementation。我们 so lucky here at Apple that 我们 have this amazing engineering team to build this stuff，because it's really hard to build。并且 it's so important also to have that kind of magical example that reminds yourself and the engineering teams，and yourselves that what it can feel like，你知道？And，it's really important to，kind of，remember，remind yourself of that。

并且 it makes——when 你 actually build it，it makes something that's hard to copy，and it gives your app a unique character。

所以，你知道，multitouch is such an amazing medium 我们 all get to play in。

我们 get to use technology to interface with people at an ancient，tactile level。It's actually really cool。

你知道，all those principles 我们 talked about today，它们 are at the core of the design of the iPhone 10 gestural interface，你知道，responsive，redirectable，interruptible gestures，dynamic motion，elegant gesture handling。

在很多 ways，it's kind of the embodiment of what 我们 think a fluid interface could be。

When 我们 align the interface to the way 我们 think and move，something kind of magical happens。

它真的不再感觉像一台计算机，而开始感觉像是我们无缝的延伸。

你知道，as 我们 design the future of interfaces，我们 think it's really important to try and capture our humanity in the technology like this。

这样，人类最重要的工具之一就不再是负担，而是一种愉悦与欣喜的使用体验。

非常感谢。[ 掌声 ]
filePath">
/Users/tommywu/Desktop/翻译/apple-developer-docs-vault/wwdc/zh/wwdc2018/803-designing-fluid-interfaces.md