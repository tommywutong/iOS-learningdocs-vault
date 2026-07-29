---
title: 深入了解 SwiftData
session_id: 10196
collection: wwdc2023
year: 2023
duration: '15:35'
topics: [Swift]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10196/'
content_hash: 'sha256:7d3e4757b3f283c0'
translated: true
---

# 深入了解 SwiftData

<sub>WWDC2023 · 15:35 · Swift</sub>

了解如何在你的 App 中充分发挥 SwiftData 的强大能力。了解 ModelContext 和 ModelContainer 如何协作以持久化你的...

> [!note] 归档理由
> SwiftData 的底层：ModelContext、持久化后端

## 章节

- [简介](/videos/play/wwdc2023/10196/?time=0)
- [配置持久化](/videos/play/wwdc2023/10196/?time=222)
- [追踪和持久化更改](/videos/play/wwdc2023/10196/?time=441)
- [规模化建模](/videos/play/wwdc2023/10196/?time=680)
- [总结](/videos/play/wwdc2023/10196/?time=894)

## 相关资源

- [简介](https://developer.apple.com/videos/play/wwdc2023/10196/?time=0)
- [配置持久化](https://developer.apple.com/videos/play/wwdc2023/10196/?time=222)
- [追踪和持久化更改](https://developer.apple.com/videos/play/wwdc2023/10196/?time=441)
- [规模化建模](https://developer.apple.com/videos/play/wwdc2023/10196/?time=680)
- [总结](https://developer.apple.com/videos/play/wwdc2023/10196/?time=894)
- [SwiftData](https://developer.apple.com/documentation/SwiftData)
- [为 Core Data App 采用 SwiftData](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10196/5/44001952-2ED6-45B5-9BF4-CFCE817D1CA7/downloads/wwdc2023-10196_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10196/5/44001952-2ED6-45B5-9BF4-CFCE817D1CA7/downloads/wwdc2023-10196_sd.mp4?dl=1)
- [使用 SwiftData 构建 App](https://developer.apple.com/videos/play/wwdc2023/10154)
- [探索 SwiftUI 中的观察](https://developer.apple.com/videos/play/wwdc2023/10149)
- [认识 SwiftData](https://developer.apple.com/videos/play/wwdc2023/10187)
- [迁移到 SwiftData](https://developer.apple.com/videos/play/wwdc2023/10189)
- [使用 SwiftData 建模你的 Schema](https://developer.apple.com/videos/play/wwdc2023/10195)
- [问答：SwiftData](https://developer.apple.com/videos/play/wwdc2023/10331)
- [问答：SwiftData](https://developer.apple.com/videos/play/wwdc2023/111543)
- [带级联关系的 Trip 模型](https://developer.apple.com/videos/play/wwdc2023/10196/?time=105)
- [初始化 ModelContainer](https://developer.apple.com/videos/play/wwdc2023/10196/?time=261)
- [使用 ModelConfiguration 自定义 ModelContainer](https://developer.apple.com/videos/play/wwdc2023/10196/?time=341)
- [在 SwiftUI 中创建 ModelContainer](https://developer.apple.com/videos/play/wwdc2023/10196/?time=409)
- [使用 modelContainer 修饰器](https://developer.apple.com/videos/play/wwdc2023/10196/?time=460)
- [在 SwiftUI 视图中引用 ModelContext](https://developer.apple.com/videos/play/wwdc2023/10196/?time=470)
- [在 ModelContainer 上启用撤销](https://developer.apple.com/videos/play/wwdc2023/10196/?time=597)
- [在 ModelContainer 上启用自动保存](https://developer.apple.com/videos/play/wwdc2023/10196/?time=665)
- [使用 FetchDescriptor 获取对象](https://developer.apple.com/videos/play/wwdc2023/10196/?time=714)
- [使用 #Predicate 和 FetchDescriptor 获取对象](https://developer.apple.com/videos/play/wwdc2023/10196/?time=734)
- [使用 #Predicate 和 FetchDescriptor 获取对象](https://developer.apple.com/videos/play/wwdc2023/10196/?time=747)
- [使用 FetchDescriptor 枚举对象](https://developer.apple.com/videos/play/wwdc2023/10196/?time=798)
- [使用 FetchDescriptor 和 SortDescriptor 枚举对象](https://developer.apple.com/videos/play/wwdc2023/10196/?time=816)
- [使用 batchSize 细化 enumerate](https://developer.apple.com/videos/play/wwdc2023/10196/?time=841)
- [使用 batchSize 和 allowEscapingMutations 细化 enumerate](https://developer.apple.com/videos/play/wwdc2023/10196/?time=868)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Nick Gillett：大家好，我是 Nick Gillett，Apple 公司 SwiftData 团队的一名工程师。在这次演讲中，我将详细探讨使用 SwiftData 构建的应用程序如何演变，以充分利用这个丰富而强大的新框架。首先，我将探讨如何在应用程序中配置持久化。接下来，我将讨论如何使用 ModelContext 来追踪和持久化更改。最后，我将探讨在处理代码中的对象时如何充分利用 SwiftData。我想指出的是，本次演讲建立在“认识 SwiftData”和“使用 SwiftData 建模你的 Schema”中介绍的概念和 API 之上。我强烈建议在继续本次演讲之前先回顾那些演讲。在这次演讲中，我将引用一个我们今年构建的新示例应用程序 SampleTrips，以演示使用 SwiftData 构建应用程序是多么容易。SampleTrips 让我能够轻松地组织关于我想去哪里以及何时旅行的想法。SwiftData 也使得实现标准的平台实践变得容易，例如撤销以及在用户切换应用程序时自动保存。SwiftData 是一种在 Swift 应用程序中持久化数据的新方法。它被设计为与你代码中已有的类型（如类（Class）和结构体（Struct））一起工作。此概念的核心是模型（Model），由一个名为 `@Model` 的新宏（macro）描述，它告诉 SwiftData 你想要持久化的类型。这是来自 SampleTrips 应用程序的 Trip 类。它有一些属性来捕获关于旅行的信息，以及一些对 SampleTrips 中使用的其他对象的引用。我们设计 SwiftData 的目的是提供尽可能小的距离——即你通常在没有持久化的情况下编写的代码（就像我这里展示的），与你需要为持久化编写的代码之间的距离。只需进行一些更改，我就告诉了 SwiftData 这个 Trip 是我想要持久化的模型，并描述了它与 BucketListItem 和 LivingAccommodations 的关系应如何表现。在可能的情况下，SwiftData 会根据你编写的代码自动推断你想要使用的结构。但 SwiftData 也提供了一组强大的自定义选项，以帮助你精确描述你希望如何存储数据。你可以在“使用 SwiftData 建模你的 Schema”中了解关于 Model 强大功能的一切。这些对 Trip 类的注解使其能够在 SwiftData 中扮演两个重要角色。第一个是描述应用程序的对象图，称为 Schema；第二个是 Trip 类将成为一个我可以编写代码的接口。这种双重性——能够扮演两个角色——使得被 `@Model` 宏注解的类成为使用 SwiftData 的应用程序中的核心接触点，并且有一个对齐的 API 概念来支持这些角色中的每一个。

Schema 被应用到一个名为 ModelContainer 的类，以描述应如何持久化数据。

ModelContainer 使用 Schema 生成一个能够保存 Model 类实例的数据库。

当在代码中处理 Model 类的实例时，这些实例被链接到一个 ModelContext，该 ModelContext 在内存中追踪并管理它们的状态。这种双重性是 SwiftData 的核心，在本节中，我将详细探讨模型的第一个角色：描述持久化的结构，以及它如何与 ModelContainer 配合工作。ModelContainer 是你描述数据如何在设备上存储或持久化的地方。我们可以把 ModelContainer 看作是 Schema 与其持久化之间的桥梁。它既是描述对象如何存储（例如在内存中还是在磁盘上）的地方，也是实现该存储的操作和演进语义（如版本控制、迁移和图分离）的地方。使用 Schema 实例化一个容器很容易。我只需提供我想要处理的类型，SwiftData 就会为我找出 Schema 的其余部分。例如，因为 Trip 类与其他模型类型相关，所以 ModelContainer 实际上会推断出这个 Schema，即使我只向它传递了一个类型。ModelContainer 还有许多其他强大的初始化方法，这些方法旨在与你的代码一起成长，使你能够使用一个名为 ModelConfiguration 的类实现日益复杂的配置。

ModelConfiguration 描述了一个 Schema 的持久化方式。它控制数据存储的位置，例如在内存中用于临时数据，或在磁盘上用于持久数据。ModelConfiguration 可以使用由你选择的特定文件 URL，或者使用你的应用程序的 entitlement（例如 group container entitlement）自动生成一个 URL。该配置还可以描述一个持久化文件应以只读模式加载，以防止写入敏感或模板数据。最后，使用多个 CloudKit 容器的应用程序可以将其指定为 Schema 的 ModelConfiguration 的一部分。

假设我想使用新的 Person 和 Address 类为 SampleTrips 添加一些联系人信息。首先，声明包含我想要使用的所有类型的完整 Schema。接下来，为包含 Trip、BucketListItem 和 LivingAccommodations 模型的 SampleTrips 数据声明一个 Configuration。它声明了一个用于存储这个特定对象图数据的文件 URL，以及一个在将 SampleTrips 数据同步到 CloudKit 时要使用的 CloudKit 容器标识符。然后，包含 Person 和 Address 的新 Schema 的模型在自己的 Configuration 中声明，带有唯一的文件 URL 和 CloudKit 容器标识符，以保持此数据与 Trips 图分离。最后，Schema 和配置组合起来形成 ModelContainer。

凭借 ModelConfiguration 的强大功能，描述应用程序的持久化需求变得很容易，无论这些需求可能多么复杂。除了手动实例化容器之外，SwiftUI 应用程序还可以使用新的 modelContainer 修饰器来创建它们想要使用的容器。

modelContainer 修饰器可以添加到应用程序中的任何视图（View）或场景（Scene），并支持从简单到强大及介于其间的各种 ModelContainer。在本节中，我探讨了如何使用 ModelContainer 将 Schema 与持久化结合起来。随着你构建更强大的功能和对象图，它与你的应用程序一起成长。我还演示了如何使用 ModelConfiguration 来解锁强大的持久化能力。正如我们在“认识 SwiftData”中学到的，Model 和 ModelContext 是编写用户界面或操作模型对象时最常用的两个概念。在本节中，我将深入探讨 ModelContext 如何追踪更改并通过 ModelContainer 持久化编辑。

当我们在视图或场景代码中使用 modelContainer 修饰器时，它会以特定方式准备应用程序的环境。该修饰器将环境中新的 modelContext 键绑定到容器的主上下文（mainContext）。主上下文是一个特殊的、对齐 @MainActor 的模型上下文，旨在用于在场景和视图中处理 ModelObjects。通过使用环境中的模型上下文，视图代码可以轻松访问此处的 Query 所使用的上下文，从而执行诸如删除等操作。

因此，模型上下文易于使用和访问，但它们实际上做什么呢？我们可以把 ModelContext 看作是应用程序所管理数据的一个视图。

我们想要处理的数据在被使用时被获取到模型上下文中。在 SampleTrips 中，当“即将到来的旅行”视图加载列表数据时，每个旅行对象都被获取到主上下文中。如果某次旅行被编辑，该更改会被模型上下文记录为快照（snapshot）。随着其他更改的进行（例如插入新的 Trip 或删除现有的 Trip），上下文会追踪并维护这些更改的状态，直到你调用 `context.save()`。这意味着，尽管被删除的旅行不再在列表中可见，但它仍然存在于 ModelContext 中，直到通过调用 save 将该删除持久化。

一旦 save 被调用，上下文就会将更改持久化到 ModelContainer 并清除其状态。

如果你仍在引用上下文中的对象（例如在列表中显示它们），它们将存在于上下文中，直到你处理完毕。届时它们将被释放，上下文也被清空。ModelContext 与其绑定的 ModelContainer 协同工作。它追踪你在视图中获取的对象，然后在 save 执行时传播任何更改。ModelContext 还支持诸如回滚（rollback）或重置（reset）之类的功能，以便在需要时清除其缓存状态。这使得它成为支持撤销和自动保存等平台功能的理想场所。

在 SwiftUI 应用程序中，modelContainer 修饰器具有这个 isUndoEnabled 参数，它将窗口的撤销管理器绑定到容器的主上下文。这意味着，随着在主上下文中进行更改，诸如三指滑动和摇动等系统手势可用来撤销或重做更改，而无需额外的代码。当对模型对象进行更改时，ModelContext 会自动注册撤销和重做操作。modelContainer 修饰器使用环境中的 undoManager，该 undoManager 通常由系统作为窗口或窗口组的一部分提供。因此，像三指滑动和摇动这样的系统手势将在你的应用程序中自动生效。ModelContext 支持的另一个标准系统功能是自动保存。当启用自动保存时，模型上下文将响应于系统事件（例如应用程序进入前台或后台）进行保存。主上下文还会在应用程序被使用时定期保存。自动保存在应用程序中默认启用，如果愿意，可以使用 modelContainer 修饰器的 isAutosaveEnabled 参数禁用它。对于手动创建的模型上下文，自动保存是禁用的。在“认识 SwiftData”中，我们学到了很多关于如何在应用程序中使用 ModelContext 以及它与 SwiftUI 配合得多么好的知识。但用户界面并不是应用程序处理模型对象的唯一场所。在本节中，我将探讨 SwiftData 如何使编写强大、可扩展的代码比以往任何时候都更简单、更安全。

在后台队列上处理数据、与远程服务器或其他持久化机制同步以及批量处理等任务，都会处理模型对象，通常是集合或图的形式。

许多这些任务将从通过 ModelContext 上的 fetch 方法获取一组要处理的对象开始。在此示例中，Trip 模型的 FetchDescriptor 告诉 Swift，trips 数组将是一个 Trip 对象的集合。无需担心类型转换或复杂的结果元组。

FetchDescriptor 使得使用新的 Predicate 宏（macro）构建复杂查询变得容易。例如，哪些旅行涉及住在某个特定的酒店？或者哪些旅行还有一些我需要预订的活动？在 SwiftData 中，支持子查询和联接的复杂查询都可以用纯 Swift 编写。Predicate 使用你创建的模型，而 SwiftData 使用从这些模型生成的 Schema 将这些谓词转换为数据库查询。FetchDescriptor 将新的 Foundation Predicate 宏的强大功能与 Schema 相结合，首次为 Apple 平台上的持久化带来了编译器验证的查询。FetchDescriptor 和相关类（如 SortDescriptor）使用泛型来形成结果类型，并告诉编译器你可以使用的模型的属性。有许多你熟悉并喜欢的调优选项，例如 offset 和 limit，以及用于惰值（faulting）和预取（prefetching）的参数。

所有这些强大功能都结合在 ModelContext 新的 enumerate 函数中。它的设计目的是通过在单个调用点封装平台最佳实践，使容易出错的批量遍历模式变得隐式高效。无论 FetchDescriptor 的复杂度如何，从简单到强大及介于其间的所有情况，Enumerate 都能很好地与它们配合使用。Enumerate 自动实现了遍历的最佳实践，如批处理和突变保护（mutation guards）。这些是可定制的，以满足你特定用例的需求。例如，enumerate 使用的批次大小默认为 5,000 个对象。但我可以将其更改为 10,000，以减少遍历期间的 I/O 操作，代价是内存增长。更重的对象图（例如那些包含图像、视频或其他大型数据 blob 的对象图）可能会选择使用更小的批次大小。减小批次大小可以减少内存增长，但会增加枚举期间的 I/O。Enumerate 也默认包含突变保护。大型遍历中性能问题的最常见原因之一，是在枚举期间上下文中滞留了突变。allowEscapingMutations 告诉 enumerate 这是有意为之，当未设置时，如果 enumerate 发现正在执行枚举的 ModelContext 是脏的（dirty），它将抛出错误，从而防止释放已遍历的对象。

在本次讲座中，我们学习了如何使用 Schema 和 ModelConfiguration 创建强大的持久化配置。我们还了解了使用 ModelContainer 和 ModelContext 采用诸如撤销和重做之类的标准系统实践是多么容易。你现在就可以开始使用 SwiftData，通过 FetchDescriptor、Predicate 和 enumerate，在你的项目中编写前所未有的安全、高性能代码。我迫不及待地想看看在未来的几个月和几年里，你将如何利用这个新框架来突破可能的极限。感谢观看，祝编码愉快。
