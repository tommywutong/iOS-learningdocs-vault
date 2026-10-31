---
title: UICollectionView 的新进展
session_id: 10097
collection: wwdc2020
year: 2020
duration: '9:55'
topics: ['SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10097/'
content_hash: 'sha256:cb83f936c7006b6d'
translated: true
---

# UICollectionView 的新进展

<sub>WWDC2020 · 9:55 · SwiftUI & UI 框架</sub>

了解 UICollectionView 让它更易于使用并解锁强大新功能的新特性。我们将向你展示如何使用……

> [!note] 归档理由
> UICollectionView 增强

## 相关资源

- [实现现代集合视图](https://developer.apple.com/documentation/UIKit/implementing-modern-collection-views)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10097/3/CE693EFF-2BF8-4B42-B483-04F69015A601/wwdc2020_10097_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10097/3/CE693EFF-2BF8-4B42-B483-04F69015A601/wwdc2020_10097_sd.mp4?dl=1)
- [打造极速的列表与集合视图](https://developer.apple.com/videos/play/wwdc2021/10252)
- [为 iPad 而构建](https://developer.apple.com/videos/play/wwdc2020/10105)
- [UICollectionView 中的列表](https://developer.apple.com/videos/play/wwdc2020/10026)
- [现代单元格配置](https://developer.apple.com/videos/play/wwdc2020/10027)
- [集合视图布局的新进展](https://developer.apple.com/videos/play/wwdc2019/215)
- [UI 数据源的新进展](https://developer.apple.com/videos/play/wwdc2019/220)
- [UICollectionViewCompositionalLayout 列表](https://developer.apple.com/videos/play/wwdc2020/10097/?time=375)
- [单元格注册](https://developer.apple.com/videos/play/wwdc2020/10097/?time=453)
- [.cell 内容配置](https://developer.apple.com/videos/play/wwdc2020/10097/?time=512)
- [.valueCell 内容配置](https://developer.apple.com/videos/play/wwdc2020/10097/?time=518)
- [.subtitleCell 内容配置](https://developer.apple.com/videos/play/wwdc2020/10097/?time=524)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。

欢迎。我叫 Steve Breen，是 UIKit 团队的一名工程师。在本视频中，我们将聊一聊 iOS 14 中 UICollectionView 的新进展。

在深入内容之前，我想先介绍一下与本视频配套的示例项目中的一个部分，它名为 Emoji Explorer。

这个示例的设计中包含许多有趣的组件。在第一部分中，有一个可水平滚动的表情符号网格。这是当今应用中相当常见的设计元素。而 Emoji Explorer 的中间部分则特别新颖：它是一个可展开可收起的大纲视图，是 iOS 14 中的新特性。

最后，在最后一部分中，有一个设计看起来非常像一个 UITableView——它就驻扎在我们 UICollectionView 的正中间。

好，这就是 Emoji Explorer。我们会在整个视频中反复提到它。

构成 UICollectionView 的 API 可以归入三个不同的类别——数据（Data）、布局（Layout）和呈现（Presentation）。UICollectionView 构建之初的一个新颖概念，就是把数据（即「内容是什么」）与布局（即内容渲染在「哪里」）的关注点分离开来。这一区分正是 UICollectionView 如此灵活的核心所在。

当 UICollectionView 早在 iOS 6 中首次发布时，数据是通过一个基于 indexPath 的协议 UICollectionViewDataSource 来管理的。

在布局方面，我们有一个抽象类 UICollectionViewLayout，并且随附了一个具体子类 UICollectionViewFlowLayout。

在呈现方面，我们发布了两种视图类型——UICollectionViewCell 和 UICollectionReusableView。

在 iOS 13 中，我们分别为数据和布局引入了两个新组件：可差分数据源（Diffable Data Source）和组合式布局（Compositional Layout）。这些是如今使用 UICollectionView 构建 App 时应当使用的 API。

在 iOS 14 中，我们在这些现代 API 的基础上，对全部三个 API 类别都引入了新特性：对可差分数据源、组合式布局和单元格的增强。

首先，让我们聊聊可差分数据源的增强。

iOS 13 中引入的可差分数据源，通过新增的快照（snapshot）数据类型，极大地简化了 UI 状态的管理。

快照通过使用唯一的分区和条目标识符来封装整个 UI 状态。

在更新 UICollectionView 时，我们首先创建一个新快照，用当前的 UI 状态填充它，然后将其应用到数据源。

可差分数据源会自动计算差异并生成动画，无需你进行任何额外的工作。

我们在 WWDC 2019 的视频「UI 数据源的新进展」中详细介绍过这个 API。我鼓励你去看那个视频以了解更多。

在 iOS 14 中，我们新增了一种快照类型，我们称之为分区快照（section snapshot）。顾名思义，分区快照封装的是 UICollectionView 中单个分区的数据。这一增强有两个原因：第一，让数据源能够以分区大小的数据块为单位更好地组合……

第二，支持对层级数据的建模，这是渲染大纲样式 UI 所必需的——这是 iOS 14 中随处可见的常见视觉设计。让我们回到 Emoji Explorer，看看这个示例 App 是如何使用分区快照构建的。首先，在可水平滚动的分区中，我们看到我们使用单个分区快照完整地建模了这里的内容。

接着，在第二个分区中，也就是我们看到这种可展开可收起的大纲样式的地方，第二个分区快照被用来建模这些层级数据。最后，在我们的列表分区中，我们再次用第三个分区快照来建模该分区的内容。所以在 Emoji Explorer 中，我们把可差分数据源组合成了三个不同的分区快照，每个代表一个分区的内容。这就是我们为 iOS 14 的 UICollectionView 可差分数据源新增的分区快照的简要概览。但还有更多内容。我们还新增了重排 API。要深入了解这些新 API，请观看视频「可差分数据源的新进展」。接下来，让我们谈谈 iOS 14 中组合式布局的一些进展。

组合式布局早在 iOS 13 中就已引入，它让我们可以通过把更小的、易于推理的布局片段组合起来，构建丰富而复杂的布局。组合式布局之所以快速，是因为你描述的是你希望布局长什么样，而不是布局应当如何运作。组合式布局还支持针对特定分区的布局，帮助你构建更复杂的 UI。它甚至支持正交滚动分区。要了解更多关于组合式布局的内容，请观看 WWDC 2019 的视频「集合视图布局的新进展」。好，在 iOS 14 中，我们在组合式布局的基础上引入了一个名为列表（Lists）的新特性。

列表让你可以在任何 UICollectionView 中直接加入类似 UITableView 的分区。

这些列表具备你在 UITableView 中习以为常的丰富特性，例如轻扫操作和许多常见的单元格布局。创建列表样式的布局非常简单。

由于列表构建在组合式布局之上，我们可以轻松地按分区将列表与其他类型的布局混搭。让我们看一段代码，看看用组合式布局创建列表样式的布局有多简单。

如你所见，非常简单——只要两行代码。

在这个例子中，我们创建了一个 UICollectionView 布局，其中 CollectionView 的每个分区都是一个具有 insetGrouped 外观的列表。

下面就是这个布局看起来的样子。

以上就是对组合式布局列表的简要介绍。但列表的功能远不止于此。还有新的具体类型 UICollectionViewListCell、对页眉和页脚的支持，以及我们在许多 iPadOS 系统 App 中都能看到的新边栏外观。

要深入了解，请观看视频「UICollectionView 中的列表」。最后，让我们聊聊 UICollectionView 与现代单元格。

在 iOS 14 中，我们提供了一种全新的单元格配置方式，这个新 API 称为单元格注册（cell registration）。

单元格注册是一种从视图模型设置单元格的简单、可复用的方式。

单元格注册免除了注册单元格类或 nib 并将其与重用标识符关联的额外步骤。

我们改为使用一个泛型的注册类型，它包含一个配置闭包，用于从视图模型设置新单元格。让我们看看这个 API 的实际运用。首先，我们创建单元格注册，它对单元格类（本例中为 MyCell）和我们的视图模型类进行泛型化。

注意，注册接受一个闭包，每当构造新单元格时都会调用它。这里就是我们从视图模型配置单元格内容的地方。有了单元格注册，我们不再需要调用 register 的额外步骤。我们只需在可差分数据源的单元格提供者中使用单元格注册，配合新 API dequeueConfiguredReusableCell(using registration)。以上就是单元格注册。

接下来是单元格内容配置。单元格内容配置为单元格提供标准化的布局，类似于 UITableView 的标准单元格类型。

这些配置可用于任何单元格，甚至一个普通的 UIView。它们非常灵活。让我们看几个直观的例子来体会它们的工作方式。这里我们可以看到一个简单的例子：在一个非常标准的单元格布局中包含一张图像和一些文本。这里是 valueCell 变体，第二段文本位于单元格的尾侧。

最后是 subtitleCell，辅助文本位于主文本下方。

注意——这些内容配置类型非常轻量，只是描述内容应当是什么样子。框架会处理所有布局考量，并自动针对性能进行优化。

最后是背景配置。它们与内容配置十分相似，但适用于任何单元格的背景，可以调整颜色、边框样式等属性。

以上只是对现代单元格配置的粗浅介绍。要深入了解，请观看视频「现代单元格配置」。以上就是对 iOS 14 中 Collection View 新进展的概览。去下载示例 App，看看这些 API 的实际运用吧。并以我们的代码为基础，将这些特性加入你的 App。

要了解更多，请去看相关视频。

感谢观看。
