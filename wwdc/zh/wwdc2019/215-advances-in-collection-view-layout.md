---
title: 集合视图布局的进展
session_id: 215
collection: wwdc2019
year: 2019
duration: '50:13'
topics: ['SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2019/215/'
content_hash: 'sha256:5f0acbd393f39d80'
translated: true
---

# 集合视图布局的进展

<sub>WWDC2019 · 50:13 · SwiftUI & UI Frameworks</sub>

集合视图布局让你轻松构建丰富的交互式集合。了解如何制作动态且响应式的布局，范围……

> [!note] 归档理由
> Compositional Layout 的布局求值模型

## 相关资源

- [Implementing modern collection views](https://developer.apple.com/documentation/UIKit/implementing-modern-collection-views)
- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/215wh1hurdxwcctfc8/215/215_hd_advances_in_collection_view_layout.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/215wh1hurdxwcctfc8/215/215_sd_advances_in_collection_view_layout.mp4?dl=1)
- [演讲幻灯片（PDF）](https://devstreaming-cdn.apple.com/videos/wwdc/2019/215wh1hurdxwcctfc8/215/215_advances_in_collection_view_layout.pdf?dl=1)
- [Advances in UICollectionView](https://developer.apple.com/videos/play/wwdc2020/10097)
- [Build for iPad](https://developer.apple.com/videos/play/wwdc2020/10105)
- [Lists in UICollectionView](https://developer.apple.com/videos/play/wwdc2020/10026)
- [Advances in UI Data Sources](https://developer.apple.com/videos/play/wwdc2019/220)
- [What’s New in AppKit for macOS](https://developer.apple.com/videos/play/wwdc2019/210)
- [A Tour of UICollectionView](https://developer.apple.com/videos/play/wwdc2018/225)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

欢迎。我叫 Steve Breen，是 UIKit 团队的工程师。

今天和我一起的是来自 AppKit 团队的 Troy Stephens，以及来自 App Store 团队的 Dersu Abolfathi。

所以今天我们要聊聊集合视图布局的进展。现在，我们把讲座分成四大块。首先我们要回顾当前最先进的做法——我们今天是怎么做的？如何在应用中定义集合视图布局？然后我们要介绍今年为所有平台——iOS、tvOS 和 Mac——带来的全新方法。

一些动手演示，让你看到这个 API 的实际效果。

然后我们会 tour 一些更高级的功能，看看如何充分利用这个 API。

好了，我们有很多内容。那开始吧。

好了。首先让我们谈谈当前的 UI 状态。我们今天做什么？如何定义集合视图布局？现在，当集合视图在 iOS 6 中引入时，它有一个非常新颖的概念；它有一个单独的抽象来定义布局。

所以真的是两个类协同工作，一个负责渲染，一个负责东西放在哪里——集合视图布局。

现在，集合视图布局是一个抽象的东西。所以我们要子类化才能从中获益。我们随 iOS 6 提供了一个具体的布局类，叫集合视图流式布局。

现在，流式布局对于大量不同的设计非常有用，尤其是 iOS 6 那个年代，事情可能还比较简单。

它之所以做到这一点，是因为它使用基于行的布局系统。我们去年在《UICollectionView 入门》中讲过这个。但总结一下，基于行的系统允许你沿布局轴的正交轴进行布局，直到填满你可用的空间，然后我们放下下一行。

这真的很棒，简单、容易推理。你能很快上手并运行。

但今天的 App 呢？随着设备变得更异构、屏幕尺寸各异，今天 App 中的事情变得更复杂。这里我们看到的是 iOS 13 中我们出货的 App Store。

现在，如果设计师今天把这份设计交给你，你会怎么做？你会想，「好吧，我得选怎么设计这个东西。」而且选项比以往任何时候都多。

你可能会选集合视图。如果你这样做了，你会想，「嗯，流式布局真的能搞定这里吗？」你可能立刻就放弃它。

所以这时候你面对的是自定义布局。你知道，我看到你们在 Twitter 上对自定义布局的说法。它们可能很复杂。所以去年我们在《UICollectionView 入门》中谈过这个。

我们谈过构建自定义布局涉及什么。

现在，在你的具体布局类里需要提供一定的东西，我们 walkthrough 了那些东西。我们还 walkthrough 了设计自定义布局时需要考虑的性能注意事项，以确保当集合视图中有大量 item 时仍然快。但我们没覆盖所有内容，构建这些自定义布局还有额外的挑战。

其中有很多，但这里我只讲几个，比如 supplementaries 和 decoration views——集合视图可以管理的两种视图类型——在自定义布局中有点棘手。得你自己来。

自适应尺寸也有挑战需要 wrestle。我们稍后会更多地讲这个。所以今年我们为平台带来了一个全新的具体布局类，与 flow 并列作为对等。

我们称之为 compositional layout。

好吧。——还没见过它呢。

所以—— compositional layout 是什么？这个东西做什么？嗯，先来一点哲学。嘿，这是基于什么构建的？compositional layout 构建在三个基本 tent pole 上。第一，它是 composable——从简单事物构建复杂事物的理念。

它设计为灵活。你可以用 compositional layout 写任何布局。它极其灵活。它也默认快速。所以我们把所有性能优化都承担在框架里，你不必去想它。compositional layout 全在于描述或定义你想做什么。它是一种声明式的 API。

好了，组合——你会在这场大会中经常听到这个词。那我们如何用这个 compositional layout 理念来组合呢？嗯，全在于拿小块布局，这些小组件，把它们缝合在一起。所以你从更小的布局块组合出更大的布局。我们从 flow layout 的伟大经验中学习，把其中一些基于行的经验带进来，你可以在一行上布局。我们可能知道有多少 item，也可能不知道。但我们可以一行一行地把 item 布局到这些小组布局 group 里。

最后，如其名所示，你不子类化。你字面意义上创建一个东西，组合一些元素，然后——就搞定了。好了。那是很多 talk，但没有 code。在这样的大会上我们都谈 code，对吧？所以让我们去看看 code。好了。

这是 hello world 级别的 compositional layout。五行代码。现在，我要切到我这边的设备。

好了。这里我们看到示例 App。我要去 list 示例。哇，那是个无聊的布局。好吧，这看起来像表格，对吧？我们开始。

没多少东西。好了。那让我们严格看几秒钟 code。来看看这个。

好了。有几处观察会立刻跳出来。第一处，因为我知道开发者会说，「嘿，Steve，我用 flow 两行 code 就能写这个。这是什么 nonsense？」绝对没错，你大概可以那样做。但我想让你在脑中锚定并贯穿整个 presentation 思考的是，随着布局越来越复杂，code 量并不会线性增长，它会趋于平缓。因为我们只是以非常简单、易于推理的方式把新东西组合进布局，以得到非常复杂的布局。

我超级兴奋地向你展示这些。

第二处观察，我想让你看——这里这些类型有自然的递进，对吧？我们有，像，五个类型。有点——这是什么？我想先关注的类型是这四个，它们有这种自然的抽象，沿阶梯向上。我们从 item 开始，它被折叠进 group。group 进入 section。section 进入我们的 layout。

现在，让我们可视化地看。

好了。所以这里，这个大矩形是 layout。layout 就是你的整个布局。

现在我们有这些刺眼的白色家伙代表我们的 sections，对吧？这直接映射到数据源，那些 section 的内容。

然后我们要在本例中表示一种 grid 风格的传统布局，我们看到这些 groups 代表我们的行。

好了。所以里面我们有 items。

这基本上就是展示我们将在整个 talk 中看到的层次，这个 item、group、section、layout 的重复模式。

好了。现在我想先谈一点这些核心类型的概念。一旦我们过完所有这些，就可以跳到 demo 看它们如何组合。我想从谈尺寸开始。

所以 compositional layout 扩展了尺寸，让你很容易推理在 compositional layout 内部如何尺寸化东西。

并且所有东西都有显式尺寸，对它有多大有强意见。

现在，我们在欧几里得 2D 几何平面里，还有 flexion view。因此尺寸真的只是两个属性。宽度和高度维度。

这里我们可以看到我们有那个类型定义的精简版。它有 width 和 height 维度。但注意 width 和 height 维度——它们不是——不是标量值。它不只是 float 或什么，实际上是另一种类型，NSCollectionLayoutDimension。

好了。那是什么？真的很简单。这是描述特定轴有多大的一种与轴无关的方式。我们有四种不同的变体来定义这个东西。

让我们以可视化的方式 walkthrough。

所以假设你有一个 item，你想描述它的尺寸相对于它的容器。

所以最外层的容器将是你的 CollectionView。

这里我们只需说，嘿，这个 item 的 widthDimension 将是其容器宽度的 fractional width，或 50%。

类似地，我们可以说某物的高度是其容器高度的 fractional height，在这个例子中是 30%。

因为你可以以这种与轴无关的方式指定东西，我们可以定义某物具有特定的 aspect ratio，在这个例子中 aspect ratio 为 1，方法是把 width 和 height 都定义为 dimension，即其容器宽度的 fraction。

我们说它是其容器的 25%，height 镜像这个。

好了。这些是 fractional 变体，创建 dimension。

基于 point 的值呢？我们有两个。

第一个最简单，absolute。

你知道这个东西必须是 200 points，因为你的设计师坚持它得是 200 points。就是那样，对吧？我们有 estimated 这个有趣的 concept。所以如果你不知道一个 item 究竟有多大——我们稍后会大量谈这个——你可以估算它。说它是 200 points。然后随着时间推移，随着 item 渲染、我们对那个 item 中的内容了解更多，它会增长。

好了。那就是 layout dimension 和 size。

接下来让我们谈一点 item。这非常简单。这是一个 cell 或 supplementary。它是渲染在屏幕上的东西。

STK 里还有更多东西，但这只是那个类型定义的一点味道。

我们看到，当我们构造其中一个时，我们给它一个 size。所有东西都对 size 有意见。

好了。我们继续向上抽象层次。我们有 item，现在进入 group。group 是什么？group 是——它是 workhorse。这是你将组合在一起的基本布局单元。我们有三种形式：horizontal、vertical。

你可以把它们想象成，像，小的 mini flow layout，对吧？它们在 horizontal 轴和 vertical 轴上的一行上布局。

但记住我们之前说过它很灵活。如果你有东西不沿 line 布局，而且有很多布局是不那样的。我们有 custom group。

那是什么？它允许你以自定义方式指定 items 的 absolute size 和 position。所以如果你有东西，其中有一个预定义的 generator 来生成布局，你可以用 custom group。

或者如果你在做 radial layout 并想计算它，你可以用 custom group。

酷的是你可以把 custom groups 和 vertical、horizontal 一起组合。所以我们将简单构建复杂。

好了。那就是 group，workhorse。

接下来我们有 NSCollectionLayoutSection。

正如其名，这是 CollectionView 每个 section 的布局定义，直接映射到数据源中该 section 有多少 item 的概念。我们看到，如承诺，initializer 在这里接受 allow group。所以我们就从 item、group、section 走过来了。

好了，我们这次 traversal 的最后一站，这两个顶层布局类，对吧？所以 iOS 和 tvOS，我们有 UI CollectionView CompositionalLayout。

在 Mac 上我们有 NSViewCompositionalLayout。

现在有趣的是，所有这些东西的定义都是一样的，无论平台。

顶层类只有一些细微差异。

好了，最后一点值得注意，这实际上真的很有趣，我们稍后在 demo 中会看到更多，就是构造 compositional layout 的方式。有两种。最简单的方式就是指定一个 layout section 的定义。这与我们今天用 flow 的方式非常相似，对吧？因为 flow 以同样的方式布局每个 section。它是 homogeneous 的。

compositional layout 扩展了这个 idea。

因为现在我们对 section 是什么有了很好的定义，你可以指定一个 closure，它会被回调并询问每个 section 的定义。这开启了很多可能性，因为现在你的布局在 sections 之间可以完全不同。我们稍后在 demo 中有大量展示。而且嘿，稍后就是现在。所以谈类型谈够了，我们要去看看实际效果。为此，我要请上我的同事 Troy Stephens。Troy？Troy Stephens：谢谢，Steve。

如承诺，我们将看 code。我们将直接深入 practical mechanics，看如何用 Steve 刚描述的这些简单元素构建你所能想到的几乎任何布局。

所以如果你还没下载这个 talk 的 sample project，请下载。这样你可以跟着看、按自己节奏学习，最重要的是，自由地在你自己的项目中使用我们的 code。无论你可能在想实现什么布局，我们今天看的示例中很可能有相似的。

以我们的 code 为基础，你会离目标更近、更快。我们将看到，拿任何现有的 compositional layout 描述并逐步 refine 到你想要的，真的很容易。

当我们 walkthrough 示例时，我希望你注意到每个示例中都在运作的同一个基本模式。这是 Steve 介绍给我们的模式。

每个 compositional layout 描述都由相同的四个基本部分组成：Item、group 和 section 描述，包在整体包含的 layout 里。所以在我们看的每个 code 示例中，我们会看到同样的四层嵌套结构。在更高级的主题中，我们将看到你实际上如何在 group 内嵌套 group，以便从简单、易于理解的部分构造或组合更复杂、更精致的布局。

让我们开始看 code。

这里我们有——我们将从 list 示例开始，这是 Steve 向我们展示的那个。所以这里——这是我们能想象的最简单的有用布局。一个单列 list，items 跨越 CollectionView 的宽度。

如果我旋转手机，我们可以看到 items 确实扩展以填满可用宽度，同时保持相同的固定高度。那我们如何用 compositional layout 实现这个？我打开了 list view controller source file，就是它实现的地方。在我们今天的每个示例中，我们只是声明了一个 create layout 函数， neatly 封装我们的 compositional layout 描述，然后返回以像其他任何 CollectionView layout 一样挂接到 CollectionView。

所以第一件事要注意，我们开始，如我承诺的，描述一个 item 及其 size。

我们拿那个 item 描述并用它描述一组 items。接下来，我们把 group 包在 section 里。

最后，我们创建并返回 compositional layout。

所以有 item、group、section、layout 结构。我想让你在进入其他示例之前真正理解的另一件事是 items 如何获得它们的 size。

在这个例子中，最终决定 item size 的是 group size。我要解释这是怎么工作的。所以 groups 在这个简单 list 示例中可能看起来有点多余。compositional layout 中的 group 通常代表你将拥有的某种重复结构，一列 items 或一行 items。本例中是一行，但我们真的是 trivial case，每行只有一个 item。所以每个 item 都有自己的 group。但 groups 作为 compositional layout 描述的一致部分始终存在，我们将利用它们来帮助定义 item sizes。

Steve 解释了所有 container-relevant sizing。

先看我们的 group size 描述。

我们要求 group——本例中 row——跨越其容器 100% 的宽度。group 的容器是其 section，而 section 又跨越 layout 或 CollectionView。

同时，我们要求每个 group 的高度为 absolute value，44 points 高。

注意，这基本上已经定义了我们的 item box 应该是什么——这就是我们想要的 item 尺寸，CollectionView 的宽度和 44 points 高。

所以我们在指定 item size 的地方要做的就是说，我们希望每个 item 是其容器——item 的容器是 group——的 100% 宽度和 100% 高度。

所以这就是实现 list 所需的全部。但有趣的是，随着我们继续，我们将看到我们不必做很多 code 更改就能得到相当不同的布局。

让我们看另一个示例，grid。这是一个五列 edge to edge items 的 grid。

我们可以看到，如果我旋转手机，这个布局确实被描述成这样：我们总是得到五列。items 始终保持方形，并且总是被尺寸化，让我们恰好得到五列宽。

这是 groups 实际上更有用、更容易理解其功能的示例。

打开 grid view controller source file，看我们同样的 create layout 函数，我们又有 item、group、section、layout 结构。

基本上看起来像 list layout 描述。唯一不同的是我们指定的 item 和 group sizes。所以让我们看看它们如何不同。

我们仍然希望每个 group——因为 group 代表一行——跨越 CollectionView 的整个宽度。很好。

但现在我们不希望 items 和它们的 group 宽度相同；我们希望一行五 items。在本例中，我们通过这里指定 item 的宽度为其自身容器的 20% 来实现。item 的容器是它的 group 或 row，所以我们会——因为指定的这个宽度，我们能恰好容纳五 items 一行。

至于高度，我们没有使用 absolute point value，而是声明我们希望每个 group 或 row 的高度是 group 容器宽度的 20%。注意我们在这里使用这种跨轴指定 fractional widths 或 heights 的能力。这真的很方便，因为这就是我们让 items 变成方形的方式。item 宽度和 group 高度相同。

并且因为 group 的高度设置 item 的高度，我们要做的就是把 item height 设为 group 高度的 100%。

所以就是这样，创建 grid 相当简单。我们这样做并没有使用与实现 list 根本不同的 code。

现在通常如果你从设计师那里得到布局，通常你会希望 items 之间有空间。让我们看看如何添加。

打开 inset items grid 示例，我们仍然有一个五列 grid，只是 items 周围和之间有空间。

让我们打开 InsetItemsGridViewController 看看。这里如果你和前一个示例比较，会看到只有一行 code 不同。这是一个有用的观察，因为你可以真正把这种布局看作几乎完全像前一个 edge-to-edge 布局一样计算。

每个 item 被分配到它之前得到的相同 box，相同的 edge-to-edge 方块。但本例中我们决定，我们不把 items 尺寸化为它们所分配的完整方块，作为最后一步，我们要把 item 内容向每边 inset 5 points。所以 item content insets 以这种方式有用。有点像对已经计算好的布局做最后阶段的减法。所以真的很酷。我们已经看到如何做 lists 和 grids。我们通过相对 item sizing 实现 grids。但还有另一种真正强大的方式来实现 grid-like 布局，用行和列。

我想向你展示，以便熟悉。

所以我要打开 two-column grid 示例。表面看起来和五列 grid 差不多，只是列更少，对吧？确实，如果我旋转设备，它会适配：始终两列，items 扩展到适当宽度。

但这实现方式有点不同，值得看看。

所以 in our TwoColumnViewController here, we're going to look at our createLayout function.

有趣的是要注意，我们再次有 item、group、section、layout 结构。但第一件可能不立即明显的事是，我们以稍微不同的方式构造代表每行的 horizontal group。

我们使用了 initializer 的另一种形式，它接受 explicit count 参数。这里我们显式指定我们希望每 group 恰好两个 items，每行两个 items。

这将导致 compositional layout 自动计算 item width 必须是什么才能实现。

我们确实指定 item width，因为总是必须。我们说 100% 的容器。但顶部的值最终 effectively 被覆盖。当你请求 group 中有一定数量的 items 时，compositional layout——compositional layout 将把那当作一种 override，它会计算实际需要的任何宽度来满足我们的请求。我们还使用不同的方式在 items 周围和之间放空间。compositional layout 提供多种方式来做这个，使它成为一个真正灵活的 API。

本例中，我们不指定 itemInsets，而是指定 section 上的 contentInsets。

所以这里我们希望左边和右边有一点 margin。我们只有一个 section，所以这基本适用于整个布局。所以我们要 leading 和 trailing 各 10 points。

注意，当我们在这行 code 上时，compositional layout 被结构化为鼓励你以与布局方向无关的方式表达布局。所以不是显式 left 和 right，我们指定 leading 和 trailing。这很棒，因为当你的 App 在 right to left 语言中运行时，你将自动得到正确的布局适配。

这里我们还使用 group 上名为 interItemSpacing 的 property。所以我们可以要求 group 在其 items 之间放一定量的空间，本例中 fixed spacing 为 10 points。就是这样。其他一切都非常类似前面的示例。我们只是使用显式指定每 group item 数量的能力。

所以都很 neat。

但 Steve 提到另一个我想深入的功能。

他提到可能每个 section 有不同布局。到目前为止我们只看过一个 section layout，但如果想要多个 sections，每个都能有自己的 distinct layout 呢？让我们打开 distinct sections 示例。

这里我们有 kind of 是其他一些布局的 composite。所以这个布局有三个 sections。

第一个 section 是简单的单列 list，如前。

第二个是五列 square items 的 grid。第三个是三列 rectangular items 的 grid。

我们怎么实现？让我们打开 DistinctSectionsViewController 并看 createLayout 函数。

乍一看这看起来相当不同，但其实只是最外层的 component——我们实例化 layout 的地方——从末尾移到了开头。

我们之所以实例化 compositional layout 是使用接受 section provider closure 作为参数的 initializer，这就是 Steve 提到的。

section provider closure，我的意思是，这是任意 code block。所以你可以想象，你可以 respond to this being invoked by returning whatever kind of layout you want for that section.

你 past 两个 parameters，section index 告诉你是哪个 section——本例中是 0、1 或 2。

以及包含各种有用 properties 可供参考的 layout environment。我们稍后会看这个。

所以——但这个 closure 内的其他一切与我们之前写的 code 基本相同。我们指定 item 描述。

我们把它包在 group 描述里。最后我们指定 section 描述，那就是我们从 section provider closure 返回的东西。

compositional layout 知道在需要重新查询特定 section 的新描述时自动 invoke 这个 closure。

所以内容与之前非常相似。

不同的iating 我们各种布局的主要事情是主要我们有不同的列数，对吧？所以我们声明了这个 SectionLayoutKind 类型，它声明在 source file 顶部。让我们看看。当我们初始化它时，我们传入 section index，将是 0、1 或 2。

它所做的是把那个映射到 enum 类型，告诉我们 SectionLayoutKind 将是 list、grid5 或 grid3。我们还添加了这个 handy gettable property，columnCount，我们可以直接问那个 SectionLayoutKind value 在该布局中应该有多少列。回到 createLayout 函数，我们可以看到我们问 columnCount，并在两个地方使用。如 two-column grid 示例，我们在实例化 horizontal group 时显式传递列数。

所以我们把它留给 compositional layout 自动计算那意味着什么 item width。我们还在这里使用列数来确定 group height 或布局的 row height，因为我们想改变它。所以你可以以任何你想要的方式做这个。所以相当 neat。但如果想让这个布局 adapt 呢？如果我们旋转手机，也许这没有最好地利用空间？也许我们可以容纳更多 items。

让我们看 adaptive sections layout。

乍一看，这看起来和前一个示例完全一样。但当我们旋转这个时，可以看到第一个 section 适配为显示两列；第二个显示十列；第三个显示六列。

我们如何在 code 中实现？其实和前一个示例相当相似。

打开 AdaptiveSectionsViewController 并看 createLayout 函数，这与前一个示例非常相似。第一个 notice 不同的是我们改变了 SectionLayoutKind 类型。

我们仍然有 SectionLayoutKind。但 columnCount 不再只是 gettable property，而是一个接受参数的函数。我们传给它从 layoutEnvironment 得到的 width。所以那个 layoutEnvironment 类型包含诸如布局必须使用的整体 container width 等信息，在 iOS 上它还包含 trait collections 信息。所以你可以用所有这些信息来 figure out 当前环境 appropriate 什么布局。这里我们只是使用 width。如果我们看顶部 where we declared SectionLayoutKind，我们可以看到那个 columnCount 函数现在是函数，它接受 width 参数，我们传入的。那就是基本上本例中的 CollectionView 宽度。我们基本上实现了 layout break。我们决定，如果我们有超过 800 points 的 width 可用在设备上，我们将进入 what we call wideMode。在 wideMode 中，我们只是为每个 section 返回更大的列数。

就是这样。如果我们回到 create layout 函数，可以看到在我们得到列数之后，我们基本上以和之前非常相似的方式使用它。所以为了得到 adaptive rotating layout，code 改动非常少。所以这都相当 neat。但到目前为止我们只谈了 items。我们甚至还没 delve into 你可以用 supplementary views 和 decoration views 做什么。compositional layout 最酷的事情之一是，它比以往更容易超越 headers 和 footers，与你自己设计的 arbitrary supplementary views 一起工作。

为了告诉我们更多关于这个并带我们进入 compositional layout 其他酷东西的一些更高级主题，我想邀请我的同事 Steve 回到台上。谢谢你。

Steve Breen：现在我们已经看到基础如何工作，如何上手 compositional layout，我将 walkthrough 如何处理更高级主题。因为用 compositional layout 做 custom layouts 有很多种方式。

好了。所以首先我想谈一点 supplementary items。

CollectionView 管理三种基本 view class 类型：你的 cells，你用来表达 model objects 交互的东西；它还代表 supplementary items 和 decoration items。

这些 meant to adorn 布局的其他部分，给你关于内容信息的视觉 cues，比如 cell 上的 badge，说「嘿，你的 tweet 有评论」之类的。

我们今天看到这些常见 uses 的三个示例——badges、headers 和 footers。flow 今天也有 sticky headers 和 footers 的支持。它们浮在内容之上。但我们扩展了 compositional layout，使其更容易。我们用这个 notion 简化了它，能够把内容锚定到布局中的 item 或 group 上。它简化了那种视觉关系，它如何工作。好了，让我们可视化地看。这里我们看到这个新类型，NSCollectionLayoutAnchor。

这里我们指定这两种类型之间的关系。所以我们的 supplementary 将相对于 host space 的 geometry 锚定，item 或 group，以这些 kinds of ways。

并且超容易推理。

好了。这里我们看到我们创建了 NSCollectionLayoutAnchor。我们指定 edges。我们希望这个 item 被 pinned 到那个 cell 的 top trailing side。

我们希望它稍微 poke out 那个 geometry 一点。我们用 fractional height 看到这个。

好了。这里我们看到设备。所以这些 badges 在那里，对吧？用我 wonderful 的设计技巧。我们有一个四 item grid，带有那些 wonderful corn flower blue cells。

我们看到这里有些 items 有这些 little notifiers 在它们上面，对吧，让它们知道，「嘿，你有东西要注意。」有了这个，它们 kind of poke out 那个 cell 的 geometry 一点，对吧？它们并不真正 inside 那个 cell 的 geometry。

让我们快速回到 slides walkthrough。好了。所以那个 fractionalOffset 买到了我们 poke out 一点的能力。我们将在正 X 方向 fractionally 移动 30%，然后在负 Y 方向也 up 30%。然后我们看到我们用 badgeSize 和 elementKind 定义了 CollectionLayout SupplementaryItem。所以我们将回指 CollectionView 的 view class，使用那个 registered supplementary type。

然后我们指定 container's anchor，指定它如何 relate。现在我们有了 supplementary 的这个定义，我们需要把它与 something 关联。那就是 item，cell。

所以本例中我们用一个 extended variant 的 initializer，它接受 supplementaries 数组。就是这样。

好了。headers 和 footers 呢？所以 headers 和 footers 和这些 items 的 supplementaries 略有不同。当你想用 supplementary header 和 footer adorn 内容时，你真的不希望那个 supplementary heard 和 footer occlude 内容；你希望扩展内容区域，以便可以看到内容本身。

所以在这种实例中，我们有不同 variation 的 supplementary，叫 boundary supplementaries。我们将 bin 它到 supplementary 的 boundaries——host geometry。

现在，我们可以对 sections 或整个 layout 做这些 boundary supplementary items，并且我们可以把它们 pin 到 whole balance，这做了一些 pretty cool stuff。

好了。我要切回设备，希望。

那里。好了。让我们看看这是什么样子。

所以 pretty straightforward 示例。这里我们有 pinned section headers 和 footers。我们滚动，一切看起来都如我们预期。看 code。

好了。所以这里我们有什么。所以这与我们一分钟前看到的 BoundarySupplementaryItems 类似，除了现在不是那个 container anchor，我们看到有 alignment property。

这里我们为 header 指定 top，为 footer 指定 bottom。我们想去那个 section geometry 的 top 和 bottom。

为了确保 header kind of float 并保持 pinned 到它在 section 中的内容区域，我们只需指定 PinToVisibleBounds。然后我们需要把 header 和 footer 与它们将要在的 geometry 关联，那就是 section。我们只需用 BoundarySupplementaryItems 数组做。

Pretty straightforward。

好了。到目前为止你已经玩过全新的 iOS 13 card presentation，这种 card design language 遍布整个系统。

我们也在滚动 UI 中看到这个，各种内容 logical grouped together with cards。这是 CollectionView 的 natural fit，因为我们一直支持 decoration views 的 notion。嗯，过去你得自己做 math。嗯，现在我们用 compositional layout 让它更容易了。

我们用 CollectionLayoutDecorationItem 支持这个。你只需用 element kind 创建它，就 done。

这是 meant to be used to have a view behind section content itself，给你那种 nice visual grouping。

构造它只需一行 code。然后要把它添加到 section，你只需指定 items，off you go。

这里。好了。让我们 quick peek 看看这是什么样子。好了。Pretty straightforward。所以这是我们的 list with multiple sections，我们用单行 code 有 decoration views。所以 pretty simple。

好了。这里是一个 near and dear to my heart 的主题：Estimated cell-sizing。

所以 iOS 13 中我们花了大量时间让这个 fast and accurate。

compositional layout 以非常 specific ways 扩展 estimated cell-sizing 的 notion。它允许你做 per-axis cell-sizing。这 super important。

因为 oftentimes 你想在渲染内容时获取内容的 view hierarchy，你不一定想 fully constrained and wild on all axes 并在 X 和 Y 上增长。你可能知道这个东西有多宽，例如。

我们的 headers 和 footers 示例，我们可能知道我们希望它 exactly CollectionView 的宽度。但是，你知道，我们希望 height vary a little bit。

所以我要 real quick 展示一个示例。我们之前已经在 code 里了。

这里我们看到我们 very familiar sections, headers and footers。我要 pull down 并去我的 text size widget，ramp it up。

好了。这里 everything's just adapted。它 did the right thing，对吧？现在我们怎么做到这个？好了。这里我们看到 height dimension's estimated。我们这里只是 did differently，对吧？我们指定 we knew exactly how wide 这个东西会是，但 we don't know about height。我们只是 estimate 它为 44 points。

所以 as content's rendered，we have a better idea。我们可以 automatically invalidate layout。并且 this happens all automatically，makes it really easy to support dynamic type in your applications，even with supplementaries and headers and footers。所以 this is——this is pretty great。

好了。现在我们进入 really fun stuff。那 nesting 呢？我们谈过 early on composition 的 notion。嗯，让我们谈 how that works。

所以 compositional layout 内部的核心布局东西是 layout group。layout group 实际上是 NSCollectionLayoutItem 的 subtype。

因为 this is a relationship，当你指定 layout group 中的 items 时，你也可以有 other groups。所以你可以 nest these。并且 this particular nesting 没有限制，it's arbitrary。并且因为 we have this，it unlocks a ton of interesting new designs。

好了。在这个示例中我们看到一个 group 由三个 items 组成。

我们看到 leading side 上这个 big old monster，它 trailing side 上有一个 vertical group，对吧？我们如何在 code 中 reason about this？好了，这 pretty straightforward，对吧？我们底部有这个 horizontal group。它的 subitems 是 leadingItem itself，对吧，和一个 trailingGroup。所以非常容易 reason about these kinds of things。我们立刻看到 we're trying to do。我们只是 compose in additional stuff 并得到这些 great layouts。

好了。nested groups pretty cool。但 what about——what about nesting CollectionViews？好了。这里我们看到 App Store，iOS 13 的 refresh。

我不知道你怎么样，但当我作为 third-party developer 时，如果看到这个 particular design 交给我，我会 heart attack。这是 complicated stuff。这可能具有挑战。有很多 bookkeeping involved。并且——但它是一个 common pattern。我们 today's applications 中 all the time 看到。要让这个 perform well 且 look great 是 bit of a challenge。嗯，compositional layout 用一行 code 解决。

我想 right now 展示一个 demo。

好了。这里我们有 same group I had from prior one。但我们 notice group 有点 squishier，对吧？大约是 container width 的 80%。这是一个 vertically scrolling CollectionView。它有五个 sections。

但每个 section 用 single line of code orthogonally scroll。

好了。我们有 ton of different variations of this。bear with me。我要 switch around here。好了。所以我们有五种 different ways to do this，对吧，包括 none case，我不想要那个。

然后我们有三种 paging cases。好了。我要 walk through each one in kind here。

好了，去我们的 orthogonal scrolling section behaviors demo。

continuous 就如你预期。这是 very simple、straightforward scroll view-like behavior，你知道？你——you had me at bounce，对吧？它有 that great——gosh，我可以做这个 hours，对吧？好了。那就是 normal scroll view behavior。但我们还有一个额外的，针对 this continuous、你知道、fluid kind of scrolling，我们称之为 continuous group-leading boundary。那是 mouthful 但 pretty descriptive。所以当我们 scroll 并 impart volume，我们自然 come to rest at that group's semantic-leading boundary。所以你 people that clap 以前做过 targeted content offset 或 proposed offset，你知道 it's a pain。好了。随着 continuous behaviors 的 addition，我们有一些 paging behaviors。这变得 really cool。所以这就像 normal scroll view paging behavior，我们 named 这个 behavior paging。

Pretty creative。

这里我们可以看到 no matter how much velocity 用户 impart，我们只 get one page of content。这个 page 被定义为 default scroll view behavior，也就是 CollectionView 的 width。

我们还有两个 variants，好了？如你 probably intuit，我们有这个 notion of group paging。

所以现在我们有了 group 的 semantic notion，我们可以 make page size be the size of group。

这给你 really nice behavior。Yeah。

你可以 automatically get that no occlusion thing going on，对吧，你的 content's always front and centered。然后 final one 是 group paging centered。它就像 group paging，但现在我们为你 centered that group automatically。Yeah，pretty cool，对吧？这给你 that great peekaboo effect，对吧，你可以在 side 上 see content leading and trailing，你知道 exactly what's going on。

好了，那就是 compositional app 中一些 additional features 的 advanced tour。还有很多。Grab SDK and check it out。

所以 at Apple，dealing with collaboration 的 notion super duper important to us。我们不得不与公司里 all over 的其他 teams work to solve problems。

作为 framework engineer，super duper important for us to deal all the different teams in the company，以确保 we know what their needs are for new framework features。

这些 teams 之一，App Store team，有一个 iOS 13 upcoming redesign。他们 really wanted to simplify their code base quite a bit。所以作为 that conversation 的一部分，我们谈了 compositional layout。他们 real excited about it，went through a bunch of code。所以为此，我要请上 App Store 团队的一位 adopter，Dersu Abolfathi。Dersu？Dersu Abolfathi：谢谢，Steve。

App Store 是数百万顾客寻找 help 他们 get the most out of their devices 的 apps 的目的地。

你们中的许多人会每天访问 App Store，所以内容需要 rich、engaging 和 dynamic。

CollectionView 在交付 that experience 中起 key role。

所以这里是 App Store。

如果你想 today 使用 just flow layout 构建 such UI，你大概会从一个 vertically scrolling 的 CollectionView 开始。

然后对于每个 horizontally scrolling 的 section，你将需要一个 additional CollectionView，这意味着更多 support code 来 intermediate 每个 collection 的 presentation 和 behavior。

用 compositional layout，这可以用 just a single CollectionView 完成。事实上，我们 just did that。

iOS 13 中，App Store 已用 compositional layout rearchitected。

这个页面上你看到的每个 content type 都 capable of vending 自己的 layout description。所有这些 layout sections come together to comprise 我们的一个 overall CollectionViewLayout。

我们用 just a single layout item 描述这个 section，它有一个 known height 并占据其容器 100% 的宽度。

那个 layout item 坐在 layout group 里，而 layout group 本身占据其容器宽度的一半。这些 really 是我们让这个 UI 工作所需的 all basic building blocks。

我们拿那个 layout group，stick it in a layout section，并为了得到我们想要的 paging behavior，我们把 orthogonal scroll behavior 设置为 group paging。

我们 off to the races。

iOS 13 中 App Store 也得到 UI support for languages that read from right to left。compositional layout helps make that possible。

我们用今天你看到的所有 same primitives 构造 layouts，compositional layout just takes care of the rest。它确保 supplementaries 和 cells 的 placement appropriate for our right to left environment。

并且 furthermore，我们不必写 single line of code 来确保 paging behavior 也 translates for right to left layout direction。

所以这个新 API enabled us to take all those scrollable regions 我们 previously micromanaging 并把它们 flatten 成 top level 的单个 CollectionView。所有 these，我们的 code 变得更 concise、easy to reason about，以及 easier to maintain going forward。

compositional layout reimagined 我们在自己 application 中 think about CollectionViews 的方式，我们 cannot wait to see 它如何 enhances the experience for apps all of you bring to the App Store。Back to you，Troy。

Troy Stephens：非常感谢，Dersu。Boy，那是 beautiful redesign。我们 couldn't be more thrilled to see compositional layout already making a difference simplifying development process for one of our prominent user-facing apps。我 so happy to be making same API available to developers across our platforms。Speaking of which，我想 real quick 展示 compositional layout 与 NSCollectionView on Mac OS 工作的 demo。

所以当你在 Xcode 中打开下载的 sample project 时，注意 there's a build scheme and target for the Mac。我们这里 build and run 它。

让我们 just open up 我们在 this talk 中看过的 all layout examples，并 fan them out。

所以这里。我们 various compositional layout examples。这些 essentially 就是我们使用的 same code。我们 programming to same API's。你真正看到的 only adjustments 是 metrics，我们 wanted to apply more macOS-appropriate metrics for things。但我们有 orthogonal scrolling working here。

并且，of course，在 Mac 上我们 expect things to behave in Mac-like ways。Mac 上 CollectionViews 的一件事是它们 usually continually resizable，对吧？所以我们——我们 ensured resize nice and fast，super light-weight，这些 layouts reevaluate very quickly。我们的 adaptive sections layout 有 layout break just like before。现在你知道 how this works，你可以 easily add additional layout breaks for wider window widths and screen widths if you want。

of course，我们有 features like clicking items to select them。我可以 use arrow keys and navigate around。

我可以 hold down shift key while arrowing around 来 accumulate selection。

并且 of course 我可以 drag to rubber band select。我可以 bulk select items。这 works in any old compositional layout，包括 more advanced ones like this。所以 users would expect on the Mac 的 all the stuff。我们有 all these layouts running。并且 enough of the code down below，item section and group descriptions is in common in terms of the API that's used。你可以 even factor out code if you want and share code between your different platform projects if you want to。

所以我们可以看到 compositional layout 真的是 here to make our lives a lot easier across our various platforms。它 really has a lot to recommend it。

它 available for you to start using today on iOS、tvOS 和 macOS。它 makes it incredibly easy to create new custom layouts for CollectionView to use by simply describing it。我们 think this is a big game-changer。

这 in turn makes CollectionView an even more versatile tool than ever before for presenting your content in arbitrary ways however you want to。

并且 the ease with which 你可以 describe new layouts、adjust layouts、make different changes、try different things、iterate on them is going to enable much faster iteration with your designers。所以 we think this is a really big game-changer。

所以 go out，take the sample project，experiment with it，try changing various things，use our code as a basis for yours and start working on custom layouts for your next app versions。我们 cannot wait to see the delightful user experiences that this is going to empower you to create in a fraction of the time。

现在，如果你觉得 this talk exciting，我们有 another that I think you're really going to love，尤其如果你 work with collection views 或 even UI table views。In Advances in UI Data Sources 我们介绍 an entirely new radically simpler API for feeding model data to your CollectionViews 和 your UI table views while getting automatic computation of differences and automatic animations for free。It's going to create delightful users experiences。所以 make sure to check this session out。

非常感谢观看。

[ Applause ]
