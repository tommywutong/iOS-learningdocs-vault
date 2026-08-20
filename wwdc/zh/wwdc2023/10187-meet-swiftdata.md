---
title: 认识 SwiftData
session_id: 10187
collection: wwdc2023
year: 2023
duration: '8:52'
topics: [Essentials, Swift]
group: H · 持久化与文件系统
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10187/'
content_hash: 'sha256:5b5d389f7de47d68'
translated: true
---

# 认识 SwiftData

<sub>WWDC2023 · 8:52 · Essentials、Swift</sub>

SwiftData 是一个为 Swift 构建的强大而富有表现力的持久化框架。我们将向你展示如何直接从...

> [!note] 归档理由
> SwiftData 入门

## 章节

- [介绍](/videos/play/wwdc2023/10187/?time=0)
- [使用模型宏](/videos/play/wwdc2023/10187/?time=67)
- [处理你的数据](/videos/play/wwdc2023/10187/?time=197)
- [在 SwiftUI 中使用 SwiftData](/videos/play/wwdc2023/10187/?time=422)
- [总结](/videos/play/wwdc2023/10187/?time=490)

## 相关资源

- [介绍](https://developer.apple.com/videos/play/wwdc2023/10187/?time=0)
- [使用模型宏](https://developer.apple.com/videos/play/wwdc2023/10187/?time=67)
- [处理你的数据](https://developer.apple.com/videos/play/wwdc2023/10187/?time=197)
- [在 SwiftUI 中使用 SwiftData](https://developer.apple.com/videos/play/wwdc2023/10187/?time=422)
- [总结](https://developer.apple.com/videos/play/wwdc2023/10187/?time=490)
- [SwiftData](https://developer.apple.com/documentation/SwiftData)
- [为 Core Data App 采用 SwiftData](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10187/5/1D820D6D-4F01-48EB-8F22-901F4A4B69FE/downloads/wwdc2023-10187_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10187/5/1D820D6D-4F01-48EB-8F22-901F4A4B69FE/downloads/wwdc2023-10187_sd.mp4?dl=1)
- [用 SwiftData 构建 App](https://developer.apple.com/videos/play/wwdc2023/10154)
- [探索 SwiftUI 中的观察](https://developer.apple.com/videos/play/wwdc2023/10149)
- [深入探索 SwiftData](https://developer.apple.com/videos/play/wwdc2023/10196)
- [迁移到 SwiftData](https://developer.apple.com/videos/play/wwdc2023/10189)
- [使用 SwiftData 建模你的模式](https://developer.apple.com/videos/play/wwdc2023/10195)
- [问答：SwiftData](https://developer.apple.com/videos/play/wwdc2023/10331)
- [问答：SwiftData](https://developer.apple.com/videos/play/wwdc2023/111543)
- [Swift 新特性](https://developer.apple.com/videos/play/wwdc2023/10164)
- [SwiftUI 新特性](https://developer.apple.com/videos/play/wwdc2023/10148)
- [将 @Model 添加到 Trip](https://developer.apple.com/videos/play/wwdc2023/10187/?time=87)
- [为 @Attribute 和 @Relationship 提供选项](https://developer.apple.com/videos/play/wwdc2023/10187/?time=166)
- [初始化 ModelContainer](https://developer.apple.com/videos/play/wwdc2023/10187/?time=223)
- [在 SwiftUI 中创建模型容器](https://developer.apple.com/videos/play/wwdc2023/10187/?time=238)
- [访问环境中的 ModelContext](https://developer.apple.com/videos/play/wwdc2023/10187/?time=260)
- [构建谓词](https://developer.apple.com/videos/play/wwdc2023/10187/?time=313)
- [使用 FetchDescriptor 获取](https://developer.apple.com/videos/play/wwdc2023/10187/?time=332)
- [使用获取与排序描述符获取](https://developer.apple.com/videos/play/wwdc2023/10187/?time=346)
- [使用 ModelContext](https://developer.apple.com/videos/play/wwdc2023/10187/?time=375)
- [在 SwiftUI 中使用 @Query](https://developer.apple.com/videos/play/wwdc2023/10187/?time=458)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Ben: 嗨，我是 Ben Trumbull，我很高兴向大家介绍 SwiftData。

SwiftData 是一个用于数据建模和管理的强大框架，能增强你的现代 Swift App。与 SwiftUI 类似，它完全专注于代码，没有外部文件格式，并利用 Swift 新的宏（macro）系统来创建无缝的 API 体验。

SwiftData 依靠新的 Swift 语言宏（macro）所提供的表达能力来创建无缝的 API 体验。它自然地与 SwiftUI 集成，并与其他平台特性（如 CloudKit 和 Widgets）协同工作。在这次讲座中，我们将了解新的 @Model 宏（macro）以及它如何直接从 Swift 代码对数据进行建模，我将向你介绍如何使用 SwiftData 获取和修改数据，然后我将简要介绍一些其他与 SwiftData 无缝协作的平台框架。

现在我们将进一步了解 @Model。

@Model 是一个新的 Swift 宏（macro），它有助于从你的 Swift 代码定义模型的模式（schema）。SwiftData 的模式（schema）就是普通的 Swift 代码，但需要时，你可以用额外的元数据（metadata）来注解你的属性（property）。利用这个模式（schema），SwiftData 为你的模型对象增加了强大的功能。只需用 @Model 装饰你的类，模式（schema）就生成了。SwiftData 中的模型是你 App 模式（schema）的数据源，并驱动着持久化体验。这个过程会将类的存储属性（stored property）转换并变成持久化属性（persisted property）。给你的模型添加 @Model 会打开一个充满可能性的世界。SwiftData 原生地将你的值类型属性（value type property）适配为可直接使用的特性（attribute）。这些属性（property）包括基本的 Swift 值类型，如 string、int 和 float。它们还可以包含更复杂的值类型，例如 struct、enum 和 codable 类型，包括集合（collection）。SwiftData 模型将引用类型视为关系（relationship）。你可以在模型类型之间用关系（relationship）和模型类型的集合（collection）创建链接。@Model 会修改你的类型上所有的存储属性（stored property）。你可以通过对属性（property）使用元数据（metadata）来影响 SwiftData 构建模式（schema）的方式。使用 @Attribute，你可以添加唯一性约束。你可以使用 @Relationship 来控制反向关系（inverse）的选择并指定删除传播规则。这些会改变模型之间链接的行为。你可以使用 Transient 宏（macro）告诉 SwiftData 不包含特定的属性（property）。这是我们之前的 Trip 示例。我将通过给存储属性（stored property）添加元数据（metadata）来调整 SwiftData 的模式（schema）生成。

我可以给 name 添加 @Attribute 并指定它应该是唯一的。我还可以用 @Relationship 装饰我们的 bucket list 关系（relationship），并指示 SwiftData 在删除此旅行时删除所有相关的 bucket list 项。要了解更多关于 SwiftData 建模的信息，请查看「使用 SwiftData 建模你的模式」讲座。现在我将介绍如何使用你的模型类型，以及你将用于驱动操作的两个关键对象：SwiftData 的 ModelContainer 和 ModelContext。模型容器为你的模型类型提供持久化后端。你可以只指定你的模式（schema）来使用默认设置，或者你可以用配置和迁移选项来自定义它。你可以只通过指定你想要存储的模型类型列表来创建一个模型容器。如果你想进一步自定义你的容器，你可以使用配置来更改你的 URL、CloudKit 和 group container 标识符以及迁移选项。设置好容器后，你就准备好使用模型上下文（model context）来获取和保存数据了。你也可以使用 SwiftUI 的视图（view）和场景（scene）修饰符（modifier）来设置容器，并让它自动在视图（view）的环境中建立。模型上下文（model context）会观察你的模型的所有更改，并提供许多对它们进行操作的动作。它们是你用于跟踪更新、获取数据、保存更改，甚至撤销这些更改的接口。

在 SwiftUI 中，你通常在创建模型容器后从视图（view）的环境中获取 modelContext。

在视图层级结构（view hierarchy）之外，你可以要求模型容器给你一个共享的主要 Actor（main actor）绑定的上下文（context），或者你可以简单地为给定的模型容器实例化新的上下文（context）。一旦你有了上下文（context），你就可以获取数据了。SwiftData 受益于新的 Swift 原生类型，如谓词（predicate）和 FetchDescriptor，以及 Swift 原生排序描述符（sort descriptor）的重大改进。

在 iOS 17 中新增，谓词（predicate）与原生的 Swift 类型一起工作，并使用 Swift 宏（macro）进行强类型构造。它是对 NSPredicate 的完全类型检查的现代替代品。借助 Xcode 支持（如自动补全），实现你的谓词（predicate）也很容易。这里有几个为我们的示例 Trip App 构建谓词（predicate）的例子。首先，我可以指定所有目的地是纽约的旅行。我可以将查询缩小到仅关于生日的旅行，并且我可以指定我们只对计划在未来的旅行感兴趣，而不是我们过去的任何冒险。一旦我们决定了要获取哪些旅行，我们就可以使用新的 FetchDescriptor 类型并指示我们的 ModelContext 获取这些旅行。与 FetchDescriptor 一起，Swift SortDescriptor 正在获得一些更新以支持原生 Swift 类型和 keypath，我们可以使用 SortDescriptor 来指定我们希望获取的 Trip 的排序顺序。FetchDescriptor 提供了许多其他定制 SwiftData 查询的方法。除了谓词（predicate）和排序，你还可以指定要预取的相关对象、限制结果数量、从结果中排除未保存的更改等等。SwiftData 还通过使用 ModelContext 来驱动这些操作，使得创建、删除和更改你的数据变得容易。在像创建其他 Swift 类一样创建模型对象后，你可以将它们插入到上下文（context）中，并开始使用 SwiftData 的特性，如更改跟踪和持久化。删除持久化对象就像告诉 ModelContext 将它们标记为删除一样简单，你可以通过要求 ModelContext 保存并将这些及其他待处理的更改提交到持久化容器来保存它们。更改模型对象上的属性（property）值就像平常使用属性（property）设置器一样简单。Model 宏（macro）会修改你的存储属性（stored property），以帮助 ModelContext 自动跟踪你的更改，并将它们包含在你的下一次保存操作中。

要了解更多关于 SwiftData 容器和上下文（context）以及如何驱动其操作的信息，请查看「深入探索 SwiftData」讲座。SwiftData 在设计时就考虑到了 SwiftUI，将它们一起使用再简单不过了。SwiftUI 是开始使用 SwiftData 的最简单方式。无论是设置你的 SwiftData 容器、获取数据还是驱动你的视图（view）更新，我们都构建了直接集成这些框架的 API。新的 SwiftUI 场景（scene）和视图（view）修饰符（modifier）是开始构建 SwiftData 应用程序的最简单方式。使用 SwiftUI，你可以配置你的数据存储、更改你的选项、启用撤销以及切换（toggle）自动保存。SwiftUI 会在其环境中传播你的模型上下文（model context）。一旦设置完成，开始使用数据的最简单方式就是新的 @Query 属性包装器（property wrapper）。你可以用一行代码轻松加载和过滤数据库中存储的任何内容。SwiftData 为你的模型属性（property）支持全新的可观察（observable）功能。SwiftUI 会自动刷新任何被观察属性（property）上的更改。SwiftUI 和 SwiftData 携手合作，帮助你构建引人入胜且功能强大的 App。在我们的「用 SwiftData 构建 App」讲座中了解更多关于如何一起使用这些框架的信息。

SwiftData 是一个强大的全新数据管理解决方案，它对 Swift 的特性提供了一流支持。它使用 Swift 新的宏（macro）系统完全专注于你的代码。使用 @Model 设置你的模式（schema），并用模型容器配置你的持久化体验。你可以轻松启用持久化、撤销和重做、iCloud 同步、小组件（widget）开发等等。通过利用 SwiftUI 的无缝集成，立即开始将 SwiftData 集成到你的 App 中。我们很期待看到你用 SwiftData 构建了什么，感谢收看。♪ ♪
