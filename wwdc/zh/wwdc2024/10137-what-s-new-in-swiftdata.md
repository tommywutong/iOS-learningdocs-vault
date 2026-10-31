---
title: SwiftData 新变化
session_id: 10137
collection: wwdc2024
year: 2024
duration: '14:01'
topics: [App Services, Swift]
group: H · 持久化与文件系统
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2024/10137/'
content_hash: 'sha256:6a6459e459b349f2'
translated: true
---

# SwiftData 新变化

<sub>WWDC2024 · 14:01 · App Services、Swift</sub>

SwiftData 通过其富有表现力的声明式 API 让你轻松为 App 添加持久化。了解 SwiftData 的改进……

> [!note] 归档理由
> SwiftData 年度更新

## 章节

- [Introduction](/videos/play/wwdc2024/10137/?time=0)
- [Adopt SwiftData](/videos/play/wwdc2024/10137/?time=57)
- [Customize the schema](/videos/play/wwdc2024/10137/?time=131)
- [#Unique macro](/videos/play/wwdc2024/10137/?time=163)
- [History API](/videos/play/wwdc2024/10137/?time=217)
- [Tailor a model container](/videos/play/wwdc2024/10137/?time=269)
- [Custom data stores](/videos/play/wwdc2024/10137/?time=339)
- [Xcode previews](/videos/play/wwdc2024/10137/?time=401)
- [Customize queries](/videos/play/wwdc2024/10137/?time=560)
- [#Expression macro](/videos/play/wwdc2024/10137/?time=618)
- [#Index macro](/videos/play/wwdc2024/10137/?time=716)

## 相关资源

- [Introduction](https://developer.apple.com/videos/play/wwdc2024/10137/?time=0)
- [Adopt SwiftData](https://developer.apple.com/videos/play/wwdc2024/10137/?time=57)
- [Customize the schema](https://developer.apple.com/videos/play/wwdc2024/10137/?time=131)
- [#Unique macro](https://developer.apple.com/videos/play/wwdc2024/10137/?time=163)
- [History API](https://developer.apple.com/videos/play/wwdc2024/10137/?time=217)
- [Tailor a model container](https://developer.apple.com/videos/play/wwdc2024/10137/?time=269)
- [Custom data stores](https://developer.apple.com/videos/play/wwdc2024/10137/?time=339)
- [Xcode previews](https://developer.apple.com/videos/play/wwdc2024/10137/?time=401)
- [Customize queries](https://developer.apple.com/videos/play/wwdc2024/10137/?time=560)
- [#Expression macro](https://developer.apple.com/videos/play/wwdc2024/10137/?time=618)
- [#Index macro](https://developer.apple.com/videos/play/wwdc2024/10137/?time=716)
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010)
- [SwiftData](https://developer.apple.com/documentation/SwiftData)
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10137/4/44213251-C991-4280-BBF1-5CA6AFCA5222/downloads/wwdc2024-10137_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10137/4/44213251-C991-4280-BBF1-5CA6AFCA5222/downloads/wwdc2024-10137_sd.mp4?dl=1)
- [Create a custom data store with SwiftData](https://developer.apple.com/videos/play/wwdc2024/10138)
- [Track model changes with SwiftData history](https://developer.apple.com/videos/play/wwdc2024/10075)
- [Meet SwiftData](https://developer.apple.com/videos/play/wwdc2023/10187)
- [SampleTrips models decorated with @Model](https://developer.apple.com/videos/play/wwdc2024/10137/?time=92)
- [SampleTrips using modelContainer scene modifier](https://developer.apple.com/videos/play/wwdc2024/10137/?time=103)
- [SampleTrips using @Query](https://developer.apple.com/videos/play/wwdc2024/10137/?time=113)
- [SampleTrips models decorated with @Model](https://developer.apple.com/videos/play/wwdc2024/10137/?time=136)
- [Add unique constraints to avoid duplication](https://developer.apple.com/videos/play/wwdc2024/10137/?time=188)
- [Add .preserveValueOnDeletion to capture unique columns](https://developer.apple.com/videos/play/wwdc2024/10137/?time=216)
- [SampleTrips using modelContainer scene modifier](https://developer.apple.com/videos/play/wwdc2024/10137/?time=275)
- [Customize a model container in the app](https://developer.apple.com/videos/play/wwdc2024/10137/?time=292)
- [Add a model container to the app](https://developer.apple.com/videos/play/wwdc2024/10137/?time=313)
- [Use your own custom data store](https://developer.apple.com/videos/play/wwdc2024/10137/?time=359)
- [Make preview data using traits](https://developer.apple.com/videos/play/wwdc2024/10137/?time=418)
- [Use sample data in a preview](https://developer.apple.com/videos/play/wwdc2024/10137/?time=495)
- [Create a preview query using @Previewable](https://developer.apple.com/videos/play/wwdc2024/10137/?time=530)
- [Create a predicate to find a Trip based on search text](https://developer.apple.com/videos/play/wwdc2024/10137/?time=595)
- [Create a Compound Predicate to find a Trip based on Search Text](https://developer.apple.com/videos/play/wwdc2024/10137/?time=606)
- [Build a predicate to find Trips with BucketListItems that are not in the plan](https://developer.apple.com/videos/play/wwdc2024/10137/?time=646)
- [Add Index for commonly used KeyPaths or combination of KeyPaths](https://developer.apple.com/videos/play/wwdc2024/10137/?time=761)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我是 Rishi Verma，SwiftData 团队的工程师。今天我很兴奋与你分享 SwiftData 的所有新内容。

iOS 17 引入了 SwiftData——一个让你用 Swift 在所有 Apple 平台上建模并持久化 App 数据的框架。它通过利用现代 Swift 语言特性（如宏）让你编写快速、高效、安全的代码。在这段视频中，我们将从对 SwiftData 框架的快速重新介绍开始，深入新内容，首先是用新的 Schema 宏避免重复模型！然后我们将介绍设置和配置模型容器的新方式。

最后深入探讨如何用复杂过滤器优化查询，并利用新宏提升性能！首先快速浏览 SwiftData。SwiftData 是一个让 App 轻松构建模型层并跨 App 启动持久化的框架。

框架不仅提供持久化，还提供 schema 的建模与迁移、图管理、与 CloudKit 同步等等！为了向你展示在 App 中采用 SwiftData 有多简单，让我展示我和团队一直在做的一个 App——Trips！Trips 是用 SwiftUI 编写的 App，跟踪我正在考虑的各种度假想法。

要在 App 中使用 SwiftData，我只需导入框架，并用 @Model 宏装饰每个模型——这是 SwiftData 的 powerhouse！在 App 定义中，WindowGroup 上的 modelContainer 修饰符把整个视图层级告知 Trip 模型。

有了这个，我的视图可以移除静态数据，转而用 @Query 填充视图。这会从模型容器获取 Trip 模型并返回 Trip 数组。就是这样！App 现在持久化我创建的所有行程，并完美融入我的 SwiftUI 视图。

第一步是添加 @Model 宏，而这只是自定义 Schema 的开始。

@Model 宏强大，能快速启动持久化体验。只需用宏装饰所有可持久化类，Trip 类和相关模型就会持久化其存储属性。

你还可以用 @Attributes 和 @Relationships 宏更进一步自定义 schema，并能用 @Transient 标记存储属性以避免持久化该数据。

今年，有一个新 schema 宏允许你在持久化模型上构建复合约束！你可以用新的 #Unique 宏告诉 SwiftData，模型属性的哪些组合必须在模型数据中始终保持唯一。当两个模型实例共享相同的唯一值时，SwiftData 会在与现有模型碰撞时执行 upsert！例如在 Trips App 中，我可以使用 #Unique 宏确保行程在名称、开始日期和结束日期上唯一。这让我 App 可以有多个同名行程，但只有在开始或结束日期不同时。这使得避免数据重复变得非常简单，因为 SwiftData 有更多信息来推理哪些模型真正代表重复，并执行数据更新。

而且因为这些 #Unique 属性帮助确保这些 @Model 不被重复，它们也代表这个模型的身份。你还可以用 @Attribute 宏装饰这些属性，加上 preserveValueOnDeletion。这将确保这些身份值在使用 SwiftData 的 history API 时可用。

SwiftData history 提供一种方式让你的 App 知道随时间插入、更新或删除了哪些模型。当模型被删除时，标记为保留的值作为墓碑值保存在 history 信息中，给你的 App 处理这些变化可能需要的信息。它还能与支持它的自定义数据存储无缝协作。要了解更多，请观看视频"Track model changes with SwiftData history"。

定制模型容器允许 App 微调其数据位置以及在整个 App 中的使用方式。

modelContainer 修饰符是开始使用 SwiftData 最简单的方式。只需提供要持久化的模型类型，SwiftData 就为你设置一个容器。modelContainer 修饰符还允许你自定义容器的一些属性。

例如，它可以将数据保存在内存而非磁盘，可以启用或禁用自动保存，可以打开或关闭撤销重做支持。

要更进一步自定义 modelContainer，比如改变它在磁盘上的保存位置，你可以单独构建自己的 modelContainer 实例。让我为 Trips App 做这个。

我不再用 modelContainer 修饰符构造容器，而是创建自己的，通过一个名为 container 的属性。

在该属性的闭包中，我为模型创建配置并传入 schema。这里我也会自定义磁盘上的数据 URL。

然后把这个配置传给 ModelContainer 初始化器并返回它。

在 iOS 18 中，SwiftData 让你可以用完全自定义的数据存储进一步自定义 modelContainer。默认数据存储提供支持所有 SwiftData 特性的稳健持久化后端。但现在你可以创建自己的数据存储，使用自己的实现跨容器持久化数据。

例如在 Trips App 中，我实现了一个由 JSON 文件组成的自定义文档格式。要在 App 中使用它，我只需把模型配置替换为自定义数据存储提供的配置——本例中是 JSONStoreConfiguration。

自定义数据存储让你无论数据需要以什么格式持久化，都能使用熟悉的 SwiftData API，如 @Model 和 @Query 宏。它还为数据存储提供逐步采用特性的能力，让你快速开始。要了解更多，请观看视频"Create a custom data store with SwiftData"。

你还可以创建自定义容器用于 Xcode 预览。预览是用 SwiftUI 开发 App 的完美伴侣，与 SwiftData 配合得很好。

我想为 Trips App 中的每个视图创建出色的预览。我将从使用预览 trait 开始。

为此，我创建一个名为 SampleData 的新结构体，遵循 PreviewModifier，它有两个需要填充的函数。一个为预览设置共享上下文，另一个把共享上下文应用到视图。对于 Trips 预览，我将提供一个 ModelContainer 作为 sampleData 的共享上下文。

因为预览不需要把任何东西存储到磁盘，我将创建只在内存中存储数据的 ModelConfiguration，并设置 ModelContainer。

然后我调用之前创建的方法，创建一组示例行程并保存到模型容器。因为行程现在按名称和日期唯一，这段代码不需要去重数据——SwiftData 为我做！最后返回容器。接下来我需要实现一个方法，把这个 modelContainer 添加到使用这个 sampleData 的任何视图。为此，我只需用 modelContainer 修饰符应用容器。

最后，我给 PreviewTrait 添加扩展，以便轻松访问这个 sampleData。这创建一个新的静态属性 sampleData()，把 SampleData() 结构体作为修饰符应用。

现在，当我为任何 SwiftUI 视图声明预览时，我可以在 traits 参数中使用 .sampleData。这会创建内存中的模型容器，加载 sampleData，并修改我的预览以在 SwiftUI 视图中使用它。

拥有出色的示例数据，让用 SwiftData 查询处理 App 的任何视图都变得容易。

但有些 App 视图可能不包含查询，因为它们依赖传入的模型。现在你可以用 @Previewable 宏为这些视图创建出色预览。

例如在 Trips 中，BucketListItemView 接受单个 trip 作为参数。有了 sampleData，bucketListItemView 现在有一个带 sampleData 的模型容器，但它还没有查询数据！现在你可以用 @Previewable 宏直接在预览声明中创建查询。这提供一个 trip 数组，可传给 BucketListItemView 以用 sampleData 创建预览。

最后，让我们谈谈为 SwiftData 创建丰富且优化的查询。Query 用可按排序和过滤的模型数组驱动你的 SwiftUI 视图，并自动响应对 ModelContainer 所做的更改！#Predicate 促进过滤，可在数据查询期间而非大型内存数据集上求值！让我们看看几种过滤 Trips 的方式！如果我给 Trips App 添加搜索栏，searchText 可用于构建过滤查询或甚至获取的谓词！构建谓词很容易，我取用户提供的 searchText 并查看 Trip 的名称是否包含该文本！但文本可能适用于不止 Trip 的名称。

因此我构建复合谓词，也检查 Trip 上的 destination 属性！构建复合谓词只用了这么多，但我还可以让谓词做更多！iOS 18 新增使用 Foundation 的 #Expression 宏轻松构建复杂谓词的能力！表达式允许引用值，这些值不产生 true 或 false，而是允许任意类型。

表达式可用于表示使用模型属性的复杂求值，并组合在谓词内以进一步定制查询结果！在 Trips App 中，我想创建一个查询，获取仍有 sights 要看的进行中行程！这些由 trip 上 isInPlan 属性仍为 false 的 BucketListItems 建模。我从构建谓词开始。

在谓词中，我指定行程应该进行中，因此当前日期落在开始和结束之间。

但我还需要指定 trip 上至少有一个 BucketListItem 的 isInPlan 属性设为 false。仅谓词无法表达这一点，因为没有属性计数未计划的 BucketListItems 数量。为此，我可以构造一个表达式，把此逻辑构建到谓词中。

这个表达式将计数我尚未计划的 bucket list items 数量。它取 bucket list items 数组，返回满足过滤条件的项目数。

现在，我可以把此表达式作为谓词的一部分，用提供的 trip 的 bucketList items 求值。然后我的谓词可以检查表达式结果是否大于零。表达式让谓词宏成为更强大、更有表现力的查询编写工具，高效获取 App 所需数据。但还有一种方式让这些查询高性能，那就是全新的 schema 宏 #Index！新的 #Index 宏添加了在模型上创建单个或复合索引的能力。就像书的目录，索引代表 SwiftData 生成并保存在容器中的额外元数据。这个元数据让指定 key path 的查询更快、更高效。

要获得这些好处，你声明 SwiftData 应为哪些属性创建索引。考虑那些最常出现在查询的排序和过滤中的属性。

在 Trips App 中，行程经常用涉及名称、开始和结束日期属性的过滤和排序查询。为了使这些查询更快，我可以添加 #Index 宏并为名称、开始和结束日期指定 key path，以及三者的复合索引。对于大型数据集，如我广泛的度假想法，这使过滤和排序大幅加快。查询在 SwiftUI 中用谓词宏易于使用，配合表达式变得更强大。现在有了 #Index 宏，你可以在 App 中让它们更 performant。

利用 SwiftData 的力量构建 App 的模型层。考虑向 schema 添加 #Unique 约束，使避免重复模型更容易。并通过添加新的 #Index 宏加速你的查询。

使用新的 history API 跟踪 App 模型的变化。借助自定义数据存储，你现在可以用自己的文档格式或持久化后端利用 SwiftData 的力量。

谢谢！这是一份荣誉，我们期待你创造出的精彩事物！
