---
title: UICollectionView 之旅
session_id: 225
collection: wwdc2018
year: 2018
duration: '40:22'
topics: ['SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2018/225/'
content_hash: 'sha256:d67b2cf145c2ce46'
translated: true
---

# UICollectionView 之旅

<sub>WWDC2018 · 40:22 · SwiftUI & UI Frameworks</sub>

UICollectionView 是一个灵活、强大的工具，能帮助你在应用程序中实现出色的用户体验。了解如何利用……

> [!note] 归档理由
> UICollectionView 结构与布局体系

## 相关资源

- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2018/225s90wcvt1fjg6b/225/225_hd_a_tour_of_uicollectionview.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2018/225s90wcvt1fjg6b/225/225_sd_a_tour_of_uicollectionview.mp4?dl=1)
- [演讲幻灯片（PDF）](https://devstreaming-cdn.apple.com/videos/wwdc/2018/225s90wcvt1fjg6b/225/225_a_tour_of_uicollectionview.pdf?dl=1)
- [集合视图布局的进展](https://developer.apple.com/videos/play/wwdc2019/215)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家下午好，欢迎来到 UICollectionView 之旅。

我叫 Steve Breen——我把这个放这边——我是 UIKit 团队的 frameworks 工程师。

今天台上还有我的同事 Mohammed Jisrawi，也是 UIKit 团队的。

所以今天我们打算做点稍微不同的事。我们要根据从设计师 Breanka 那里收到的规格，从零构建一个 App，这将利用 UICollectionView 的许多能力。在我们完成构建 App 所需的所有任务过程中，我们会涉及到关于 UICollectionView 的一系列主题，包括布局、更新与动画。

我们有很多内容要覆盖，所以让我们直接开始吧。

好的，这是从我们的设计师那里拿到的第一份规格。看起来像一个好友 feed，想象一下。一个很棒的列式布局。

看起来相当直白，好吧。好吧，这个看起来很棒。所以这里我们有一个看起来非常花哨的 mosaic 布局，那是我们好友 feed 的内容。

好的，那么 Mohammed，既然你将为我们写所有代码并带我们过这些特性是怎么用的，你对这些设计有什么看法？嗯，你知道的，我也是第一次看到这些，但它们看起来像是集合视图的绝佳候选。我觉得我们可以在这上面玩出很多花样，尤其是这个。对，这个看起来很棒。

好的。所以在我们深入代码、Mohammed 开始带我们过之前，我们需要覆盖三个核心概念，以便在深入代码前理解 CollectionView。我们现在就讲这些，我们会谈布局、数据源与代理。好的。所以首先，先聊一点关于布局的事。所以如果你第一次打开 UICollectionView 的定义，而且你熟悉 UITableView，你马上会注意到 API 中有很多熟悉之处。你有 delegate 和 data source。所有这些看起来都相当熟悉，但布局概念对 UICollectionView 来说是相当独特且Distinct的。你可以真的把它看作 UICollectionView 的超能力。

它允许 CollectionView 把视觉排列与内容本身分离开来。

布局全都是关于内容显示在哪里。

现在，每个单独的 item 由 UICollectionView layout attributes 指定，属性如 bound、center、frame 等等。你可以把它想成一组属性，用来定义显示的这些 item。你甚至可以通过打印你自己的 UICollectionView layout attributes 子类并把它们包含在你的设计中来定制它们。

好的。所以当用户在屏幕上滚动内容时，布局被认为是不可变的。

现在如果你需要改变它，比如你要改变布局的外观，你就会使用 invalidation 机制，Mohammed 稍后会带我们过一遍。好的。现在，布局作为独立抽象的一大好处是，我们可以从一个布局过渡到另一个布局，并在布局之间移动时得到很棒的动画效果，布局 A 不需要知道任何关于布局 B 的事。它们只是声明布局是什么，然后过渡发生。

好的。CollectionViewLayout 是一个抽象类，因此它并不是 meant to be 直接使用，而是 CollectionViewLayout 的子类 meant to be 使用。

幸运的是，我们提供了一个。

UICollectionViewFlowLayout，如果你之前用过 CollectionView，你可能熟悉这个类。

现在 CollectionViewLayout 上有很多定制点，包括我们稍后会谈的一些属性，但你也可以用 delegate 来定制它，我们稍后会谈 CollectionViewDelegate，但 UICollectionViewFlowLayout 会指定额外的东西，扩展那个 CollectionViewDelegate。

好的，那么 Flow 是怎么回事？嗯，它是一个基于行的布局系统，因此它可以覆盖你可能收到的多种不同设计。

好的，那么基于行意味着什么？嗯，让我们过一遍。所以解释基于行系统最好的方式是给个例子，我们来做。

好的。所以这里我们看到一个垂直滚动的集合视图，我们将模拟 flow layout 在布局内容时的行为。好的。

这是我们的第一个 item，我们从 top leading 边缘开始，沿着一行布局我们的 item。现在看这一行。这一行与滚动轴正交。我们垂直滚动，所以这一行是水平的。

好的，现在注意这里，我们填满了该行的可用空间，所以现在我们要下到下一行继续布局内容。最后，我们下到最后一行，bingo，我们得到所有内容。

现在如果我在这里放下一些指南，来突出显示那些水平线在哪里，让我们谈谈我们定义的一些定制方式。

首先是 line spacing 的概念。

如你所见这里的箭头，line spacing 将是这些水平线之间的空间。

类似地，inter-item spacing 是布局行上 item 之间的空间。flow layout 上有两个属性，让你为两者指定最小值。好的。让我们稍微巩固一下直觉，把整个东西旋转 pi over 2，然后从 top leading 边缘重新开始。

现在，这个是水平滚动的，对吧，所以我们将有一个垂直的布局行，当我们到达这个区域的底部时，我们就填满了那一行，回到顶部。

好的。这个模式现在相当熟悉了，对吧。

好了。那就是所有内容。

现在我们有了垂直布局行。

所以现在在这个方向上，我们的 line spacing 是这个。

我们的 inter-item spacing 是这个。

记住这一点在你使用 flow layout 时很重要。

好的，这就是布局。

让我们谈一点数据源，如果你用过 TableView，这应该看起来非常熟悉。这是非常相似的模式。

它们共享非常相似的 API。好的，所以如果布局全都是关于内容放在哪里，数据源就是是什么。内容本身。

这里要思考的三个核心方法。第一个是可选的，number of sections in CollectionView，如果你不提供，我们就会假设你意思是 one。

类似地，我们有 number of items in section，这会告诉你每个单独 section 中的 item 数量，因为它们都可以有不同的 item 数。最后一个是 sell for item index path，你在这里提供实际要显示给用户的内容。

好的。这就是数据源。好的，我们深入代码前要谈的三个主题中的最后一个，是代理。

好的。所以使用代理是可选的。

现在，CollectionView 是 UIScrollView 的子类。所以我们使用 ScrollView 超类提供的相同代理，但我们会扩展它。

所以如果你需要修改滚动行为，你也可以针对这个相同代理来做，并与一些 UICollectionViewDelegate 方法配合，提供用户与内容交互时关于高亮与选择的细粒度控制。我们还得到了一个 API，让你知道，嘿，某样东西上屏了。WillDisplayItem 和 DidEndDisplayingItem。好的。这些就是我们深入代码前需要谈的三个核心概念，以便开始使用 UICollectionView。所以让我们切到 Mohammed 的 dev box，让他向我们展示这是怎么工作的。Mohammed。好的，所以我们的两个屏幕中，那个列式布局是使用 CollectionViewFlowLayout 的绝佳用例。我们可能在那里完成所有需要的事，而且这是开始使用 UICollectionView 的好方法。

所以现在虽然我们可能用 flow layout 完成我们设计的整个目标，我实际上要子类化 CollectionViewFlowLayout，因为我们打算做一点额外的定制。所以我要从创建我的 ColumnFlowLayout 类的一个实例开始，我已经准备好了。

我要用那个实例创建我的 CollectionView。我要取那个 CollectionView，并设置一些视图属性，比如 auto resizing mask、background color，而且因为它是一个 ScrollView，我也可以设置它的一些 ScrollView 属性。所有这些只是为了让它在我们的 App 中看起来和感觉像我们想要的。在把 CollectionView 添加到我的视图层级之后，我要用它的唯一 identifier 向 CollectionView 注册我的 PersonCell 类，以便我们能把 cell 设计送到 App。然后我要把 view controller 设为 CollectionView 的 data source，以便我们能给它一些关于它将显示多少 cell 以及 cell 中显示什么数据的信息。然后我要把它设为 delegate，以便我们能处理 cell 选择。

所以现在我们已经设置好了，我们需要实际遵循这两个协议。

所以让我们从遵循 data source 开始，这里我们有两个需要实现的必需方法。第一个是 number of items in section，我们只需返回 people 数组中的 people 数量或 item 数量，以让我们的数据模型对象被显示。

第二个方法是 CellForItemAtIndexPath，我们将使用唯一 identifier 从 CollectionView dequeue 一个 cell，把我们从 people 数组中取出的 person 对象传给 cell 以实际显示数据，然后返回 cell。

然后为了把这里收尾，我们只需实现 Delegate 协议中的一个可选方法，以便处理选择。所以我就添加 DidSelectItemAtIndexPath，在其中我们将实例化我们的 FeedView controller，这将是我们的第二个 screen，如果还没有实例的话，然后我们将传给它一个 person 对象，以便我们知道显示谁的图片，然后我们会把它 push 到 navigation controller 上。

好的。所以让我们构建这个并切到模拟器看看。

好的。 okay。所以我们的 CollectionView 在屏幕上，我们有一些 cell。你可以看到它们，虽然它们有点被挤扁了。尺寸不对，所以我们要做一点我们之前想到的定制。所以让我们回到 Xcode，弹出我们的 column 类——我们的 ColumnFlowLayout 类，我们已经放在一起的——让我们看看这里需要做什么。所以我已经有一个 prepare 方法的 stub override。

现在，UICollectionViewLayoutsPrepare 方法在 layout 被 invalidated 时被调用，在 UICollectionViewFlowLayout 的情况下，我们的 layout 在 CollectionView 的 bounds of size 改变时被 invalidated。所以如果你的 App 在 phone 上旋转，或者你的 App 在 iPad 上被调整大小。

所以这是做任何考虑 CollectionView size 的定制的好地方。在我们的情况，我们想要我们的 cell 是 CollectionView width 的某个函数。我们可以通过说它的 item sized 属性来让 CollectionView 知道我们想要 item 有多大。所以我就在这里做。

所以我要把 CollectionView 的 item size 设为一个 CG size，宽度是 CollectionView 的 bounds 的宽度，inset by its layout margins，然后给它一个 70 点的高度，只是为了匹配我们的设计。

而且既然我们已经在这里了，我要做几件其他的小事，只是为了让东西看起来好看。我要应用一个 section inset，顶部有一些 padding，匹配我们的 inter-item spacing，并且我要把 layout section inset reference property 设为 from safe area，以便一切整齐地 tucked 在 CollectionView 的 safe area insets 内。

好的。所以让我们再回到模拟器一次，看看我们正确构造的布局看起来像什么。好的。

那看起来很棒。那看起来就像我们的 spec。我觉得我们的设计师会非常高兴。如果我们旋转到 landscape，我们看到我们的 cell 有很好的大小，所以我们知道我们的 invalidation 代码在 prepare 中被再次调用了。

现在虽然这样 okay，你可能在想，这不是我们能做的最好的。它看起来没有它能的那么好。我们可能想做更有趣的事，比如在有空间时显示多列。现在 flow layout 使得这很容易。如果你还记得 Steve 早前解释 flow layout 如何执行布局，flow layout 会自动尝试在一行里塞进尽可能多的 item，然后再 wrap 到下一行。所以利用这一点，我们 kind of 可以 figured out 一个 layout——我们可以通过改变 item size 来得到多列。

所以如果我们回到 Xcode，到我们的 layout 这里，如果我们只是改变我们在这里计算 item size 的方式。所以我要移除这个 fit，然后用做一点额外 math 的东西替换它。

所以我就从和之前相同的 available width 开始。这是 margins inset 后的 bounds，以及对 minimum column width 的某个 arbitrary definition，它是 300 点。然后用这两个值计算我 think 我能放进 available space 的最大 column 数，然后用 available width 除以它来计算 optimal cell width，这可能比我们的 300 点更多。

然后我把它传给 CT size，作为我的 item size。

好的。所以让我们再回到模拟器，看看我们更新后的布局看起来像什么。

好的。所以这里一切都一样。我们没破坏它。这是个好的开始，如果我们去 portrait，那里就是我们并排的多列，正是我们想要的。

你觉得怎么样，Steve？那看起来很棒。我们有了一个很棒的可适应的列式基础布局。没做多少工作。没有。我们设计的下一步是什么？嗯，现在我们用好友列表 easing 了进来，是时候开始思考那个 fancy mosaic 布局了。哦，对。那会很棒。对。让我们切回 slides，聊聊这个。好的。让我们看看这个 layout 或设计，看我们能做什么。所以我们的第一直觉，我不知道你的，但我的是：能用 Flow 吗？我有它，它 ready to go。让我们试试用它。

所以让我们 zoom in 一下这个设计，看 Flow 是否对我们有意义。

这个三个照片所在的特定区域，我要 zoom in 一下。

好的。

所以现在在这种情况下，我们左边有一张很大的照片，右边有一个垂直叠放。

所以在 flow 宇宙中，既然它是基于行的，我们将布局那个大的左边 item，移动到下一个 item，那里有空间，尝试布局另一个 item，然后跳到下一行。但我们还没完。我们还有那个垂直叠放要处理。所以这真的对 Flow 不起作用，因为事实证明我们的 fancy 布局并不是真正的基于行的布局。

但经历这个练习是有用的，所以，你知道，让我们先从 flow 开始。

好的。在这种情况下，我们要创建我们自己的 custom layout。

哦，不，我们害怕了，对吧。不，它不复杂。我们这里要处理四个基本方法，而且我还要介绍一个额外的、获得 honorable mention 的方法。

好的。四个方法。开始。

我想谈的第一个方法是 CollectionView Content Size。

现在，回想一下之前我们提到 CollectionView 是 UIScrollView 的子类，UIScrollView 的一个 feature 是你有一个 visible region with a large content area，你得到那个很棒的 iOS 体验，把内容在其中移动，所以 CollectionView 需要知道如何告诉 ScrollView：嘿，这是我的内容有多大。好的。我们怎么得到这个 size？嗯，如果你想象一个 encompass 了 layout 将为你的 CollectionView 定义的所有内容的矩形，我们想要那个的 size。好的，这就是 CollectionView Content Size。

接下来我们有两个负责提供 layout attributes 的方法。

第一个是 LayoutAttributesForElements (in Rect)。

现在 CollectionView 会在需要知道用户滚动内容或首次显示时需要显示什么时周期性地调用这个。所以这个查询是按几何区域的。

好的。它的 companion API，LayoutAttributesForItem AtIndexPath，如你所想，它只是在找一个 item。给我那个的 attributes。

好的，所以我们稍后会看到更多，当 Mohammed 带我们过一遍时，但对这两个 API 来说，重要的是性能 matters。

好的，我们四个核心 custom layout subclass item 中的第四个将是 Prepare 方法。Mohammed 早前已经聊过一点。每次 layout 被 invalidated 时它被调用。所以这是计算任何东西的好时机，比如你可能想缓存的 layout attributes，还有 content size，它很快就会被请求。

好的。我们 honorable mention API，让我们谈这个。这是 Should Invalidate Layout For Bounds Change。

所以每次 CollectionView 的 bounds 改变时它被调用。好的，所以 CollectionView 是 UIScrollView subclass。那么我们说的 bounds change 是什么意思？嗯，当 ScrollView bounds change 时，origin 可以在 scrolling 期间改变，size 也可以在 application size 改变或 CollectionView size 改变时改变。所以这会在 scrolling 期间被调用。

因此那个 oh yeah emoji。这被调用非常频繁。所以做正确的决定很重要。好的，所以 UICollectionViewLayout 中的默认实现返回 false。

所以如果你需要它做不同的事，这是你的机会。

举例来说，UICollectionViewLayout 会在 origin 改变时返回 false。好的，所以如果用户只是滚动内容，我们默认不会 invalidate。

但如果是 iPad 旋转、手机旋转、你的 App 改变到不同 size，它会返回 true。

这个的轻微例外是像 floating headers 和 footers 这样的东西，对吧。我们不得不在你滚动内容时重新计算那些。它会做 custom invalidation 来处理那些事。

好的。理论够了。

让我们切回我们的开发机器，让 Mohammed 带我们过一遍在代码中构建这个 fancy custom UICollectionViewLayout 是什么样的。

好的，让我们直接深入。所以我已经准备好了另一个 layout subclass，我们将用于这个 layout，你可能注意到它是直接 UICollectionViewLayout 的子类，不是 CollectionViewLayout 的子类，这是出于 Steve 早前解释的原因：UICollectionViewLayout 并不真正满足我们 custom mosaic design 的需求。

所以这里我先设置几个 instance variables，我将用来持有我稍后需要引用的一些关键信息。

第一个是一个 content bound CG rect，我将用它来保持 CollectionView 中所有 item 的一个 representative bounds。第二个是一个 cached attributes array，我将用它来持有我的 layout attributes，以便我能在性能 matters 时快速引用它们。

所以我们要从为这个 layout 实现 prepare 方法开始。

Prepare 是做大部分布局工作的理想位置，因为每个 invalidation 它被调用一次。

我们可以在那里设置 layout，然后避免在被调用更频繁的方法中做任何 heavy layout work 或 heavy layout math。

所以这里我们做了几件事。首先，我们重置 cached attributes 和 content bounds，只是为了清掉前一次 invalidation 的 stale information。

接下来，我们对 CollectionView 中的每个 item 做几件事。

第一是实际准备 attributes，现在我不会太深入我们特定 layout 这 entails 什么，因为这对你来说会不同。这是你计算 cell 的 sizes 和 positions 和 transforms 等等，以匹配你的设计需求的地方。

但有几件关键的事，我们在 attributes 完成后要做。第一，我们要缓存它们。我们要把它们放进 cached attributes array，以便稍后快速 grab。第二，我们要把它们的 frame union 到我们的 content bounds rect，以便我们的 content bounds 保持 up to date。

所以现在我们的 prepare 已经 up and running，我们需要实现 layout 中剩下的方法，以让一切工作。

第一个是 CollectionView Content Size，如果我们之前在 Prepare 中做好了工作，我们只需返回 Content Bounds as size。

接下来是 should invalidate layout for bounds change。

既然我们的 layout 没有任何 elements 需要我们在 scrolling 时 invalidate，所以没有 floating headers、没有 floating footers 之类。我们真的只想在 CollectionView 的 bounds of size 改变时 invalidate。所以如果 new bounds of size 不等于 CollectionView 的 bounds of size，我们当前的 bounds of size，我们只返回 true。

之后，我们将实现 LayoutAttributesForItem AtIndexPath，再次，既然我们在 Prepare 方法中准备了所有 attributes，我们只需从我们的 array 中 grab 对应于 RequestAtIndexPath 的特定 attributes。最后，我们要实现 LayoutAttributesForElements InRect。

现在这个方法被 CollectionView 周期性地以不同的 query rect 调用，这些可能比我们的 CollectionView 更大。我们的 CollectionView 只是在问一组 attributes，对应某个区域。

我们的工作是返回一个 array，包含对应于 CollectionView 中该 rect 内所有将要出现的 item 的所有 attributes。

所以我们可以在这里简单地通过 filtering 我们的 cached attributes array on attributes 的 frame 来回答这个问题。所以如果我们的 attributes 有一个 frame 与我们的 query rect 相交，我们就可以返回它们。好的。所以让我们切回 sim，看看我们的 layout 看起来像什么。

所以我要选择其中一个 feed，那里。我们有了我们的 layout。我们的 images nicely loaded in this fancy mosaic configuration，如果我们旋转到 landscape，你可以看到我们的 cell 已经 resized，所以我们正确地 updated 了一切，我们 invalidated，这很棒。

所以这看起来像我们的 spec，但那个 scrolling performance 不太好，是不是？不。不，它相当 bad， huh。

所以你可能已经对发生了什么有个 idea 了。让我们切回代码，看看可能发生了什么。

所以如果我们看看我们的 layout attributes 或 elements in rect 这里，记住这个方法在 scrolling 期间被频繁调用。

所以这个函数，它 filtering 我们的整个 array，你 might imagine 随着 CollectionView 中 item 数量的增加会变得 really expensive。所以我们的 App 中照片越多，scrolling performance 越慢。

所以如果你发现自己处于这种情况，帮助的是退一步，思考你 layout 的 nature，思考你是否能找到任何 optimization opportunities。

所以我们的 layout kind of 要求每个 cell apps next to or below 它的 preceding cell。

所以这意味着我们的 attributes 已经在 cached attributes array 中按它们 frame 的 minimum y value 排序了。

所以我们有一个 sorted array，所以我们可以加速搜索，做类似 binary search 的事，而不是我们现在的 linear filter。

所以让我们移除我们慢的实现，替换为应该快得多的东西。

所以我要逐步过一遍这个，别担心。

所以第一件事，我们调用一个我们已经准备好的 binary search 函数，它接受我们 array 中的 index 范围和我们的 query rect。

如果它找到一组 attributes，其 frame 坐在我们的 rect 内，它会把 attributes 作为 index 返回到我们的 array 中。

然后从那个 index 开始，我们可以 build up 我们 query rect 的其余 attributes 集合，只需在我们的 array 中 loop up 和 down，并 pick up attributes，直到我们 exit query rect，直到我们找到在 rect 外的 attributes。

你 array 中有成千上万个 item。你不会 thousands of times 遍历 array thousands of items。

好的，所以让我们再回到 sim，看看我们更快的 scrolling 算法看起来像什么。

让我们弹出这个并 flick 一下。它 way faster。

你觉得怎么样，Steve？Much better。好的，great。所以我们有了这两个 great layouts。下一步是什么？所以我们的两个 screens。那就只剩下我们好友列表的 update animations 了。哦，great。好的。嗯，让我们切回 slides，让我们过一遍那个 designer 称为 totally cool update animation 的东西。

好的，我们这里有一个 video。让我们跑一遍，看看这个 totally cool update animation 长什么样。好的。所以这里有一些 elements。我们看到 last item 正在被 refreshed。我猜有人 post 了一张图片，然后我们又 got another item there，看起来，对，那个 third item smears 不会在这里。好的。所以这里发生了三个基本操作，对吧。我们有 reload、move 和 delete。

为什么我们不切回 dev machine，Mohammed，你 why don't you show us 这是怎么工作的？Sure thing。好的，所以我们在同时做 multiple animated updates。

所以你可能知道 UICollectionView 和 UITableView 提供的一个 great tool，它是 Perform Batch Updates API，基本上允许我们把一组 updates 传给 collection view，可以在同一时间 with animation 执行。

所以我要添加一个对 CollectionView PerformBatchUpdates 的调用，并注意我是在 closure 里同时做我的 data source updates 和我的 CollectionView updates。这真的是我协调 updates 并保持 neat sync 并避免 inconsistencies 的 best way。

所以，首先我只是更新我的数据源中的 last item。我移除 second to last item，拿起 last item，把它 move 到 top，然后我让 CollectionView 执行我想要的 animations。

好的。让我们再回到 sim，看看我们的 update 长什么样。所以我已经通过右上角的 update 按钮 wired 我们的 update code，uh oh。发生了什么？哦，那很 embarrassing。发生了什么。你知道，我写 iOS 很久了。我 before 看过这个 movie。对， onstage 发生时 sucks。你知道，我们这里时间不多了，所以为什么我们不 just call reload data，然后我们可以在 V2 回来做 animations。真的吗？你知道，我们可以那样做，但那样我们就会失去那个 totally cool update animation，而且我们的用户期望这些 lively interfaces，对吧？对，对，你说得对。你知道吗？他们 deserve better。啊，我喜欢你这样想。好的，让我们 real quick 切回 slides，看看我们能不能 save 那个 totally cool update animation。

你've seen this before。好的。所以首先，让我们 dig into 这个 debug exception，看看它在 trying to tell us 什么。好的。

所以它在这里说我们正在尝试对同一个 index path 0-3 执行 delete 和 move。所以如果我记得 right，那是第四个 item。我们对它做了 reload 和 move。我们没 delete 它，我们 deleted 第三个 item，0-2，对吧。

我不记得 deleted 它们。所以，对，这是怎么回事？好的，但在我们做这个之前，让我们 go back 并 peek 一下 PerformBatchUpdates API，谈一些 high-level principles。好的。所以正如 Mohammed 早前介绍这个 API 时提到的，这个 API 的目的 是我们可以 commit multiple updates at the same time 并让 anything animate together 并得到那个 great experience。

正如他 also mentioned 的，把你的 data source updates 和 CollectionView updates 都放在 CollectionView update closure 内 perform 超级重要。

现在我所说的 CollectionView 也适用于 TableView。所以如果你的 apps 里有 TableViews，所有这些 information 都 going the same direction。

好的。让我们做些 observations。CollectionView updates，当你做 inserts、moves 和 deletes 时，这些在 update's closure 中的 ordering do not matter。

放哪里都行。

然而你的 data source updates，当你改变结构 offer 你的 data source，它 backing 那个 data source，或 does matter。

好的，这 best served by showing an example，所以我要取一个 two arrays 有 three elements 的 example，并加强我们的 intuition，展示一个 delete 和一个 insert，但第一轮我们做 delete first 和 second delete second。我们将 reverse the order，just to kind of strengthen our intuition。我 all the time 做这个，画 pictures，对吧。好的。所以 we deleted 第一个 item，现在我们要 insert at index one。

好的，在第二个 example 中，我们 reverse the order，先做 insert 然后做 delete。

所以我们的 intuition holds，indeed 我们得到不同的 result。这 probably 不是 good thing，对吧。

所以让我们 contrast 这个与 CollectionView updates。现在这里我有两组 CollectionView updates on a submit via batch updates，我 left out data source updates，just to keep the slide tidy。

但我第一个有 insert 和 delete，第二个有 delete 和 insert，order 是不同的。这会给你 exact same result。

我们都是 engineers。我们想 know why，why is that？嗯，让我们 talk about that。

这怎么发生的？为什么 ordering 对发送给 CollectionView 的 updates 不 important，当然对你的 data source 是 important。好的。让我们 operation by operation 走一遍。所以第一个 to delete，这是 process in descending index path order。现在让我们谈 index paths。所以首先，如果你能 think about what's happening on a PerformBatchUpdate，batch update 开始之前，你的 data source 在 before state。

现在一旦 batch updates 中 everything 都 done，你'll be an after state。好的。所以对于 delete，index paths always referred to the before stage。所以那就是 delete。所以 insert 是 process in ascending index path order paths。

所以 insert 中的 index paths always referring to the final state 或 after updates stage。

好的，move 是 two 的 mixture，对吧。你有一个 from 和一个 to index path，from 是 in the before state，对吧，to 是 in the after state。Reload。现在 reload 是 a little bit of a super command if you will，对吧。它 actually decomposes down into a delete 和一个 insert。并且 reload 中指定的 index path 是 speaking about the before state。

好的。这个 insight，现在我们理解了 reload 真正 what's doing，可以 kind of tell us a little bit of what's going on with our error in our app because of the delete on the reload on the last one is conflicting internally with the notion of moving that item，okay。所以我们可以 address this in a minute when we get back to code。好的，所以我不 going to go through 这些，但你可以 later reason about 这些。Just put it up here as reference that 这些是 things that'll cause CollectionView to go bonkers。Don't do it。以及我们如何 take all this knowledge 并 simplify it，distill it in such a way that 我们可以 always apply 我们的 data source updates from a given set of CollectionView or TableView updates 并 make sure everything is in sync。好的。这四个 basic rules。

所以首先你想要 decompose those moves and to delete and inserts。Easy。然后把 all your deletes and inserts combine into two separate lists，process the deletes first in descending order on the index paths，然后 finally apply those inserts in the ascending index path order。Do this，and you're good to go。What about reload data？我 and I know Mohammed said we could just hit that and we're done，everyone laughed so I'm pretty sure I yelled and that's the case，but the thing about reloaded data 是 you don't get those great animations，and this is really a sledge hammer approach。

所以，and we really prefer the apps to be lively and animated and feel great for our customers。所以，and this is used in special cases。

好的，Mohammed，让我们 real quick 切回来，see if we can get this fixed in code 并 save 那个 totally cool update animation。好的，time to redeem myself。对。所以让我们 use the guidelines that Steve just shared with us 来 fix 我们的 update animation。所以让我们 remove 我们的 existing implementation 这里。如果你 recall，我们的 update consisted of a reload、a delete 和一个 move，我们的 reload 和 the move 在 same index path。它们 started at the same one。所以那 really 是 where our conflict 是。所以我们要 start out by separating those two。所以让我们把 reload take out into its own call to perform batch updates，这里我 just updating 我的 data source，again，same as before，并 calling reload items on the CollectionView。我 just performing it in a UI view performed without animation closure，因为如果你 look closely at 我们的 spec，那就是 nonanimated，那个 initial reload。

好的。所以接下来，我们要 take care of 我们的 remaining updates，那个 delete 和 the move。让我们 reason about them for a second。我们在 index two 有一个 delete，然后我们 moving index three 的 item to index zero。

所以如果我们 break down 我们的 move using the guidelines 我们 just learned about，那 becomes a delete at index 2、a delete at index 3，以及一个 insertion of the item from index 3 at index 0。

所以现在我们有两组 operations。我们有 deletions 和 insertions。我们可以 accordingly process 它们。

首先，我们'll perform 我们的 deletions in descending order。所以我们将先 delete index 3，然后 hold onto the person from there so 我们可以 later insert 它们。

然后我们将 delete index 2 的 item。然后我们需要 process 我们的 insertions in ascending order。我们 just 有一个，所以我们可以 just go ahead and insert 它。最后，我们将 ask CollectionView to perform 我们想要的 animations。现在，注意，我 still calling move here。我 didn't break it down into its component actions，因为 we still want the collection view to play the right animations，而且 if 我们've done the right thing with 我们的 data source，the CollectionView will do the right thing in terms of animations。

好的。让我们 back to the simulator，see what 我们的 update 看起来像 when it works。

好的。Here goes nothing。

Wow。

Great! 我要 reload 并 take a slow-mo victory lap just to——there we go。That looks exactly like 我们的 spec，isn't it。That's great，awesome。好的。

嗯，让我们 wrap it up。我们 covered a ton of content。Can you switch it back to slides？我'd like to issue a bit of a call to action。所以如果你've been nervous 或 anxiety building that custom layout，take the stuff we just applied today 并 go back 并 dive in 并 create those custom layouts 并 build really great CollectionView solutions。如果你 got a lot of reload data sprinkled all throughout your apps 并 you're losing out on these gray animations。They'll inspect those things 并 see maybe why you didn't understand 或 something wasn't quite jived about why it was happening 并 fix those spots。好的，所以 more information，你可以 see the link on the slide here。

我们还有明天上午 9 点的 CollectionView lab。如果你对你的 CollectionViews 有任何 questions 或 comments，请 swing on by 并 chat。Mohammed 和我 both will be there。Thanks very much for coming out，and I hope you enjoy the rest of your conference。[ Applause ]
