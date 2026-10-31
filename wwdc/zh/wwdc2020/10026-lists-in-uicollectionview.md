---
title: UICollectionView 中的列表
session_id: 10026
collection: wwdc2020
year: 2020
duration: '16:54'
topics: ['SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10026/'
content_hash: 'sha256:fbdddd14de08eac1'
translated: true
---

# UICollectionView 中的列表

<sub>WWDC2020 · 16:54 · SwiftUI & UI Frameworks</sub>

了解如何用 UICollectionView 在 App 中构建列表和边栏。替换表格视图外观，同时利用全……

> [!note] 归档理由
> UICollectionView 列表化

## 相关资源

- [Implementing modern collection views](https://developer.apple.com/documentation/UIKit/implementing-modern-collection-views)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10026/6/9DBF6E96-B0C9-4104-B03E-F016434855BD/wwdc2020_10026_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10026/6/9DBF6E96-B0C9-4104-B03E-F016434855BD/wwdc2020_10026_sd.mp4?dl=1)
- [Advances in diffable data sources](https://developer.apple.com/videos/play/wwdc2020/10045)
- [Advances in UICollectionView](https://developer.apple.com/videos/play/wwdc2020/10097)
- [Build for iPad](https://developer.apple.com/videos/play/wwdc2020/10105)
- [Modern cell configuration](https://developer.apple.com/videos/play/wwdc2020/10027)
- [Advances in Collection View Layout](https://developer.apple.com/videos/play/wwdc2019/215)
- [Simple Setup](https://developer.apple.com/videos/play/wwdc2020/10026/?time=227)
- [Per-Section Setup](https://developer.apple.com/videos/play/wwdc2020/10026/?time=265)
- [Per-Section Setup full](https://developer.apple.com/videos/play/wwdc2020/10026/?time=280)
- [Header Mode Supplementary](https://developer.apple.com/videos/play/wwdc2020/10026/?time=349)
- [Header Mode Supplementary Optional Header](https://developer.apple.com/videos/play/wwdc2020/10026/?time=411)
- [Header Mode First Item In Section](https://developer.apple.com/videos/play/wwdc2020/10026/?time=427)
- [Swipe Actions](https://developer.apple.com/videos/play/wwdc2020/10026/?time=700)
- [Accessories](https://developer.apple.com/videos/play/wwdc2020/10026/?time=895)
- [Accessories w/ Parameters](https://developer.apple.com/videos/play/wwdc2020/10026/?time=951)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。

大家好，欢迎。我是 Michael Ochs，我是 UIKit 团队的 frameworks 工程师，在这段视频中我们将讨论 UICollectionView 中的列表。

你在这里看到的是我们认为现代集合视图设置的一部分架构，这个图在"Advances in Collection View"中详细涵盖。图的不同部分有单独视频，在这段视频中我们涵盖列表配置和列表单元格。

但先让我们谈谈集合视图中的列表到底是什么。iOS 14 中的列表在集合视图中给你 UITableView 风格的外观。我们建立在 iOS 13 引入的 Compositional Layout 之上。这使它非常灵活且高度可定制。

我们还特别为列表大幅改进了自调整大小支持，并把自调整大小作为在 UICollectionView 中使用列表时的新默认行为。这意味着你不再需要手动计算单元格高度，而是可以简单地用 Auto Layout 构建单元格，集合视图会为你处理其余部分。如果你确实需要手动调整大小，仍然可以通过重写 preferredLayoutAttributesFittingAttributes 在单元格子类上做到。

但让我们回到自定义方面，看看我说"高度可定制"时的意思。这里你可以看到一个展示我最近使用的所有 emoji 的 App 示例，顶行正交滚动。在那下面，你看到一个按分组排序所有 emoji 的大纲，并把层级构建进去。底部我们有看起来更像 UITableView 的东西，此外你还可以滑动每个单元格来标记你最喜欢的 emoji。你在这里看到的是单个集合视图使用列表和 Compositional Layout 的组合。在深入这是如何工作之前，让我们看看列表的组件。

在 iOS 14 中，我们提供名为 UICollectionLayoutListConfiguration 的新类型。这是布局侧构建集合视图列表所需的唯一新类型。UICollectionLayoutListConfiguration 建立在 NSCollectionLayoutSection 以及 UICollectionViewCompositionalLayout 之上，这两者都是 iOS 13 引入的现有 Compositional Layout 系统的一部分。

我们不会在这场中详细涵盖 Compositional Layout，所以如果你不熟悉它，我强烈建议你查看 WWDC 2019 的"Advances in Collection View Layout"。

但现在让我们看看列表配置。

列表配置给你 Table View 已知的相同外观作为样式：plain、grouped 和 inset-grouped。但我们还引入两种仅限 UICollectionView 列表的新样式，我们称之为"sidebar"和"sidebar plain"。你可以用这些新样式在 iPadOS 14 上构建惊人的多列 App。除了通用外观，列表配置还给你显示或隐藏分隔符的选项，以及配置列表的页眉和页脚。

列表配置上的所有术语如果你用过 UITableView 应该听起来熟悉。但我们确实添加了几个新特性，我们稍后讨论。但首先让我们看看如何创建列表。

创建列表最简单的方式是创建 UICollectionLayoutListConfiguration，给它外观，然后用这个配置创建 UICollectionViewCompositionalLayout。

在这个例子中，我们使用 inset-grouped 样式，这将使它看起来完全像 inset-grouped UITableView，这个布局中的每个 section 看起来相同。

所以它与 UITableView 非常相似，我建议在可能时使用这种方法。然而，有更强大的方式创建列表，我们称之为 per-section setup。

在 per-section setup 中，你使用完全相同的配置，但不是用它创建组合式布局，而是用这个配置创建 NSCollectionLayoutSection。

这段代码随后可在组合式布局上现有的 section-provider 初始化器中使用，它会对集合视图中的每个 section 调用，允许你返回特定 section 的单独布局定义。

你在这里看到的结果与我早先展示的简单设置完全相同的设计。然而，现在我们有了这个设置，我们可以在每个 section 基础上开始自定义布局。

例如，这里，对于第一个 section，我返回用现有 Compositional Layout API 构建的自定义网格布局。这非常强大，可用于像视频早些时候展示的那种布局，我展示了最近使用 emoji 的正交滚动 section。既然你已看到如何在 UICollectionView 中创建列表，让我们谈谈如何在列表 section 中配置页眉和页脚。

集合视图列表中的页眉和页脚工作方式与你从 UITableView 习惯的有点不同。UICollectionView 列表中的页眉和页脚必须显式启用，有两种方式。

第一种方式是把页眉和页脚注册为 supplementary views。在这个例子中，我们将配置页眉，但相同代码也适用于页脚。只需在配置上把 header 或 footer 模式设为"supplementary"。接下来，以这种方式配置时，集合视图将在需要在屏幕上渲染页眉或页脚时请求你提供 supplementary view。

提供这个视图的最简单方式是通过 diffable data source 上的 supplementary-view provider，但你也可以在 UICollectionView 委托上实现等效方法。

在这个回调内，你可以检查 element kind 是否为 elementKindSectionHeader 或 elementKindSectionFooter 并配置并返回适当的视图。

重要的是记住，使用这种方法时，你必须在集合视图请求时提供 supplementary view。如果在 supplementary-view 回调中返回 nil，集合视图会断言。所以如果你的布局中有些 section 需要页眉而其他不需要，只需使用我早先展示的 per-section 配置，并根据这个特定 section 是否应显示页眉，把模式设为"supplementary"或"none"。我提到有两种选项。第二种选项仅适用于页眉，通过把 header 模式设为 firstItemInSection 启用。这告诉集合视图把这个特定 section 中的第一个单元格配置成看起来像页眉。

这是我们推荐使用层级数据结构和新 section-snapshot API 时的模式。你可以在"Advances in Diffable Data Source"中了解这一切如何工作。然而记住使用这个模式时，你的数据源需要意识到这一点，因为数据源中的第一个项目不再代表 section 的实际内容，而是 section 的页眉（可能只是标题）。既然我们已涵盖集合视图列表的布局，让我们谈谈呈现侧。在 iOS 14 中，我们引入新的 UICollectionView cell 子类 UICollectionViewListCell。

值得一提的是，忠于集合视图的组合性质，你可以在任何期望常规集合视图单元格的地方使用列表单元格，也可以用任何 UICollectionView 单元格配合列表 section。所以你可以只挑 API 中你需要的位和块来实现你 aiming 的设计。让我们看看列表单元格能帮助你的部分。

列表单元格有更细粒度的支持来配置分隔符的缩进以及单元格内容的缩进。与 UITableView 相比，滑动操作现在也是单元格的特性。

此外，我们有大幅改进的 accessories API，当然你可以访问默认系统内容和背景配置，你可以在"Modern Cell Configuration"视频中了解全部。让我们谈谈分隔符。

这里你可以看到渲染图像和标签并在其下有分隔符的单元格示例。这是相当常见的布局。然而，如你可能已注意，这里看到的布局实际上不正确。分隔符应该与单元格的主内容对齐，本例中主内容不是图像视图而是单元格的标签。所以 leading 侧，分隔符应缩进以匹配这个标签的边缘。

像这样。

在 UITableView 中，这是通过提供名为分隔符缩进的基于点的值来完成的。当此 API 引入时相当容易，因为你可能已经有了手动计算标签 x 偏移的方法，所以你可以用相同方法用相同值配置分隔符缩进。然而在现代 Auto Layout 世界中，有安全区域缩进、布局边距、动态字体大小和 SF Symbols，就不那么容易了。今天我们有一个高度动态的环境，所有这些值可能随时改变。用动态字体和 SF Symbols，即使你的图像大小也可能根据用户首选字体大小改变，然后改变标签位置。所以很难提前知道标签最终在哪里。在列表单元格中，我们引入名为分隔符布局指南的新概念。这个布局指南工作方式与 UIKit 中现有布局指南有点不同。不是把内容约束到这个布局指南，而是把这个布局指南约束到你的内容，所以与使用布局指南时习惯的相反。设置分隔符布局指南的最简单方式是先配置单元格布局，一旦单元格看起来如你所愿，只需添加单个额外约束。把 separatorLayoutGuide 的 leading anchor 约束到你的标签的 leading anchor 或单元格中的任何主内容。列表单元格与列表 section 随后会确保自动保持分隔符与单元格主内容对齐。

注意如果你使用系统提供的内容配置，它会自动为你做这件事，你不必担心。但如果你有自定义单元格布局，这是确保分隔符正确定位的简单方式。

现在谈谈滑动操作。

与 UITableView 相比，滑动操作现在是列表单元格的特性。你与单元格内容一起配置它们。所以无论你在哪里配置图像视图或单元格标签，现在也可以设置 leading 或 trailing 滑动操作配置。

这需要单元格与布局之间的通信，所以滑动操作仅在单元格渲染在用列表配置配置的 section 内时支持。

如果你需要 UITableView 上滑动操作 API 的动态特性，只有当滑动即将开始时才创建滑动配置，你可以重写 leading 或 trailing swipe-actions configuration getter，然后在那里创建配置。我们确保只在用户实际尝试滑动这个单元格时才调用 getter。

一个警告。在滑动操作的 action handler 中，确保永远不要捕获你正在配置的单元格的 index path。Index path 不是稳定标识符。只要你在其上方插入或删除内容（不一定会重新加载这个特定单元格），这个单元格的 index path 就会改变。

所以如果你使用存储的 index path 在用户触发滑动操作时获取单元格的数据模型，你可能实际操作另一个单元格的数据。这对删除操作特别危险，因为你可能删除错误的数据。

改为捕获数据模型直接或可用于识别此单元格内容的稳定标识符。Diffable data source 及其稳定 item identifiers，以及 iOS 14 中新的 cell-registration 类型，非常适合这个。

接下来，谈谈 accessories。在 UITableView 上，accessories API 相当有限。你可以访问 accessory type 和 accessory view，它们互斥且仅与单元格 trailing 侧相关。

列表单元格提供许多新 accessory 类型，还允许你为单元格的 trailing 和 leading 两侧配置 accessories，你甚至可以在同一侧配置多个 accessories。

此外，UITableView 单元格 accessories 更像装饰视图，而在列表单元格中它们可以启用功能。

例如，如果你用 reorder accessory 配置单元格，当用户点按这个 accessory 时，我们会自动把集合视图置于重新排序模式，假设你也实现了必要的重新排序回调。

另一个例子是 delete accessory，以前称为 delete edit control。如果用户点按这个 accessory，列表单元格会自动揭示单元格的任何已配置 trailing 滑动操作。

我们还有全新的 accessory：outline-disclosure accessory。当用户点按这个 accessory 时，单元格会自动与数据源通信并展开或折叠此单元格的子项。这需要使用新的 section-snapshot API，你可以在"Advances in Diffable Data Source"中了解全部。现在让我们看看 API 如何工作。为了配置单元格的 accessories，你只需把列表单元格上的单个 accessories 属性设为 UI cell accessories 数组。在这个例子中，我将用 disclosure indicator 和 delete accessory 配置单元格。系统知道 disclosure indicator 应始终在单元格的 trailing 侧，而 delete accessory 始终显示在单元格的 leading 侧。所以 UIKit 会自动把 accessories 排序为正确顺序并显示在适当侧。

此外，系统还知道，虽然 disclosure indicator 应该始终可见，delete accessory 只应在集合视图处于编辑模式时可见。所以 UIKit 会在进入或退出编辑模式时自动动画 delete accessory 进出。

我们提供很多这些系统默认，但允许你自定义几乎所有。例如，如果你希望 disclosure indicator 只在非编辑模式时可见，只需把 displayed 参数设为 whenNotEditing。这是超级声明式 API，UIKit 为你处理所有状态。如你所见，列表是高度可定制的布局，非常模块化且灵活。采用超简单，所以去看看示例代码并玩玩。那里还有更多要发现。一旦你熟悉新 API，想想在哪里可以增强 App 中的布局。想想在哪里可以替换现有表格视图并利用灵活性把列表与任何自定义组合式布局混合。当然，也查看我们关于 UICollectionView 的所有其他视频。iOS 14 中集合视图还有更多惊人功能。

非常感谢观看。
