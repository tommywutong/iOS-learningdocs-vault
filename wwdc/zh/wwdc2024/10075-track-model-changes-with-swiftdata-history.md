---
title: 使用 SwiftData 历史记录追踪模型变更
session_id: 10075
collection: wwdc2024
year: 2024
duration: '16:52'
topics: [App Services, Swift]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2024/10075/'
content_hash: 'sha256:bffbe518c3b49c3f'
translated: true
---

# 使用 SwiftData 历史记录追踪模型变更

<sub>WWDC2024 · 16:52 · App Services、Swift</sub>

探索 SwiftData 中模型变更的历史记录！使用历史记录 API 了解数据存储何时发生了变更，并学习...

> [!note] 归档理由
> 历史追踪（change history）机制

## 章节

- [简介](/videos/play/wwdc2024/10075/?time=0)
- [基础](/videos/play/wwdc2024/10075/?time=45)
- [事务与变更](/videos/play/wwdc2024/10075/?time=318)
- [自定义存储](/videos/play/wwdc2024/10075/?time=757)

## 相关资源

- [简介](https://developer.apple.com/videos/play/wwdc2024/10075/?time=0)
- [基础](https://developer.apple.com/videos/play/wwdc2024/10075/?time=45)
- [事务与变更](https://developer.apple.com/videos/play/wwdc2024/10075/?time=318)
- [自定义存储](https://developer.apple.com/videos/play/wwdc2024/10075/?time=757)
- [获取和筛选基于时间的模型变更](https://developer.apple.com/documentation/SwiftData/Fetching-and-filtering-time-based-model-changes)
- [论坛：编程语言](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010)
- [SwiftData](https://developer.apple.com/documentation/SwiftData)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10075/4/0F3D64B6-B594-42E8-8B59-2088D1B251F8/downloads/wwdc2024-10075_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10075/4/0F3D64B6-B594-42E8-8B59-2088D1B251F8/downloads/wwdc2024-10075_sd.mp4?dl=1)
- [使用 SwiftData 创建自定义数据存储](https://developer.apple.com/videos/play/wwdc2024/10138)
- [在删除时保留历史值](https://developer.apple.com/videos/play/wwdc2024/10075/?time=297)
- [从历史记录中获取事务](https://developer.apple.com/videos/play/wwdc2024/10075/?time=386)
- [处理历史变更](https://developer.apple.com/videos/play/wwdc2024/10075/?time=454)
- [保存并使用历史记录 token](https://developer.apple.com/videos/play/wwdc2024/10075/?time=619)
- [更新用户界面](https://developer.apple.com/videos/play/wwdc2024/10075/?time=690)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好！我叫 David，是 SwiftData 团队的一名工程师。SwiftData 历史记录（SwiftData History）是一项新技术，可以让你的 App 追踪其数据的修改。你可以利用历史记录来构建需要处理这些变更的功能，例如与你的服务器同步，或者响应来自 App Extension 的变更。在这个视频中，我将介绍 SwiftData 历史记录的基础知识，并使用历史记录事务和变更在我的示例 App 中构建一个新功能。

最后，我将介绍在自定义数据存储中支持历史记录时需要考虑的一些事项。

让我们来谈谈 SwiftData 历史记录是什么，以及你为什么要使用它。

当人们使用 App 时，SwiftData 存储的内容会随时间变化。例如，当 App 启动时，它可能会创建一些模型，或者插入从远程服务器获取的模型。

当模型上下文被保存时，所有待处理的变更都会被保存到数据存储中。

随着时间的推移，随着用户与你的 App 及其不同功能进行交互，其中一些模型可能会发生变化，或被删除。

在任何时候，你的 App 都可以查询数据存储中的数据。然而，查询的结果代表的是数据存储中的当前内容。如果没有历史记录或手动比对，就无法通过查询得知自上次查询以来哪些模型可能已被添加、删除或更新。SwiftData 历史记录提供了一种简单有效的方式来追踪数据存储随时间的变化。

你可以利用它来构建多种不同的功能。例如，你可能希望有一个按时间顺序排列的变更日志，记录在 App 离线时发生的变更。之后，这些变更可以高效地与远程服务器同步。

你可能希望发现另一个进程（例如小组件扩展）中发生的数据变更，以便在你的 App 中正确体现这些变更。

或者，你可能只是想要一种有效的方式来了解自上次查询以来哪些模型被插入或删除，以便在运行时更新某些状态。让我们来探索它是如何工作的。

SwiftData 历史记录允许你的 App 按照变更发生的顺序进行查询和处理。

每次你的模型被保存时，它都会记录一个事务，该事务包含关于所有变更的元数据。

SwiftData 历史记录由事务（Transaction）和变更（Change）组成。事务将在某个边界（例如 ModelContext 保存）时数据存储中发生的所有变更分组在一起。事务按其发生的时间排序。

在一个事务中，其所包含的变更集也保留了每个变更发生的顺序。每个变更代表一个已被插入、更新或删除的模型，并通过一个 PersistentModel 进行参数化。这使得你可以使用 KeyPaths 来引用 PersistentModel 的属性。

SwiftData 历史记录使用了 token 的概念，它充当历史记录中事务的书签。token 可以帮助你的 App 追踪它在历史记录流中处理的最后一个事务。

Token 仅对与其关联的数据存储有效。在 SwiftData 中，可以通过模型上下文删除历史信息。

当发生这种情况时，已删除历史记录部分的 token 会过期，并且不能用于获取操作。

涉及过期 token 的 SwiftData 历史记录操作会抛出 `historyTokenExpired` 错误。如果发生这种情况，请丢弃该 token，因为它不再有效，然后获取一个新的 token。

当模型被删除时，模型中的数据会被丢弃。这意味着像标识符这样的关键数据可能会丢失，并且无法在你的 App 处理历史信息时提供足够的信息。为了解决这个问题，SwiftData 历史记录允许你在模型上保留特定的属性。当模型被删除时，这些属性会作为墓碑值（tombstone values）被保留，并让你能够处理已删除模型的历史信息。

一个 PersistentModel 中已使用 `.preserveValueOnDeletion` 修饰符标记的属性会保留在墓碑中。墓碑也通过 PersistentModel 进行参数化，这样它们的 KeyPaths 就可以用来检索墓碑值，或者按需进行迭代。

SwiftData 中的历史记录易于使用，并且建立在 Swift 丰富的类型系统之上。让我们探索如何在一个 App 中使用它。为了展示它的实际应用，我将为 SampleTrips App 开发一个新功能。这个 App 让我可以记录所有我最喜爱的旅行，以帮助我计划下一次假期。

我想添加一个新功能，让有未读变更的旅行（Trip）显示标记以供我查看。这可能发生在 App 外部，无论是来自远程服务器的同步，还是在 App 的小组件中。

在小组件中，我将添加直接从主屏幕确认特定住宿地点的功能。使用 SwiftData 历史记录，我可以通过找出此数据何时变更、由谁变更，并更新 UI 来构建此功能。

为此，我将把这个任务分解为三个步骤：获取 SwiftData 历史记录，通过检查变更上的属性来处理变更，最后更新我的用户界面。首先，我将构建一个函数，该函数基于一个 token 参数和作者从数据存储中获取事务。在这种情况下，token 的类型是 `DefaultHistoryToken`，因为 App 使用的是 SwiftData 中的默认存储（DefaultStore）。

接下来，我将创建一个 `HistoryDescriptor`，它允许我为我的请求配置约束条件。

我将构建一个谓词（predicate），用于约束事务必须发生在提供的 token 之后。

因为我希望此函数只显示来自我小组件的变更，所以我还会添加一个约束条件，用于获取由指定作者创作的变更。如果我在没有 token 的情况下调用此函数，我将只获取所有可用的历史记录。

接下来，我将创建一个数组，用于包含所有需要处理的事务。然后，我将使用该描述符在 ModelContext 上调用 `fetchHistory`。这将提供一组 `DefaultHistoryTransaction`，然后我可以遍历它们。现在我已经能够检索到我关心的事务，我将定义另一个函数来处理它们。此函数将接受一个事务数组，并返回一个包含需要因未读变更而进行标记的旅行和一个 token 的集合。每次函数运行时，它都会返回一个新的 token，我可以在下次想要查找变更时使用它。

我将首先定义一个 ModelContext 和一个用于存储有未读变更的旅行的集合。

对于每个事务以及事务中的每个变更，History API 都提供了持久化模型标识符（persistent model id）。为了获取该旅行的模型实例，我将使用那个持久化模型标识符为 `LivingAccommodation` 构建一个 fetch descriptor。然后，我将从模型上下文中获取该模型，并存储与 `LivingAccommodation` 关联的旅行。

为了确定事务中的变更代表插入、更新还是删除，我将使用一个 switch 语句来检查其类型。

在这个 App 中，如果我的小组件插入了、更改了或删除了一个 `LivingAccommodation` 模型，我想在 UI 中应用一个标记。为此，我将首先检查 `LivingAccommodation` 的 `DefaultHistoryInsert` 类型的变更。如果匹配到这个 case，它表示一个 `LivingAccommodation` 的插入，所以将这个旅行添加到集合中。再次注意，这里的类型叫做 `DefaultHistoryInsert`，因为在这种情况下，我为此模型使用了默认存储。我还将通过添加一个 `LivingAccommodation` 的 `DefaultHistoryUpdate` 类型的 case 来检查更新。如果这个变更是更新，我将更新集合中的旅行。

如果旅行被删除，我在 App 界面中不需要做任何事。为了处理这种情况，我将添加一个 `LivingAccommodation` 的 `DefaultHistoryDelete` 类型的 case，并将其从我的集合中移除。

最后，我将返回最后一个 token 以及我的旅行集合，以便将来对该函数的调用只返回发生在该事务之后的变更。

使用 SwiftData 历史记录，App 现在可以发现自上次检查变更以来，哪些旅行被小组件更改了。现在，我需要存储这个 token，以便它只考虑自上次发现变更以来的变更。为此，我将定义第三个函数，并使用 `UserDefaults` 来存储最近的 token。在我的函数 `findUnreadTrips` 中，我将获取 token（如果有的话），并将其从 JSON 解码，然后再使用该 token 调用我的 `findTransactions` 函数。我想指定的作者是小组件，所以在小组件中，我设置了 `ModelContext` 上的 `.author` 属性等于 `TransactionAuthor.widget`。

在调用 `findTrips` 之后，我将返回的 token 存储回 `UserDefaults`。现在，每次我调用 `findUnreadTrips` 时，它只会返回自上次调用以来需要添加标记的旅行。

我的功能几乎准备好了。只需要再添加两个部分：第一，当 App 打开时，检查未读旅行；第二，当点击一个旅行时，将它从未读旅行集合中移除，这样标记就会消失。在我的 SwiftUI 视图中，我将在场景阶段变为活跃时调用 `findUnreadTripIdentifiers`。这将用需要添加标记的新旅行更新界面。

然后，当选择一个旅行时，我会将其标识符从 `unreadTripIdentifiers` 集合中移除，这样标记就会消失。

最后，我将为 `unreadTripIdentifiers` 集合中包含的任何旅行添加标记。

现在所有必要的代码都已实现，我将构建并运行 App。App 中已经录入了一个旅行，我想在小组件中直接从主屏幕确认住宿地点。

我会轻点 “Accommodation”，UI 将随之改变，指示它已被确认。下次我启动旅行 App 时，前往  “formation flyover” 的旅行将会有一个蓝色的未读标记，表示该旅行有变更。在查看完旅行后，该标记会被移除。

对于那些使用 SwiftData 构建自定义数据存储的开发者，你的自定义存储也可以支持历史记录。如果你的底层模型支持，你也可以在你的存储实现中支持这些相同的工作流程。要为你的自定义数据存储添加历史记录，你需要为你自己的数据存储实现一些类型来表示 SwiftData 历史记录 API 的基本元素。这包括事务、每种变更类型以及一个用于在事务之间充当书签的 token。此外，你的自定义数据存储需要遵循 `HistoryProviding` 协议。

事务的边界需要明确定义，因为数据存储中的写操作需要被合并和排序。在默认存储中，保存时对 ModelContext 上模型实例的所有变更都会被分组为一个单独的事务。

当你创建自己的事务类型时，你需要定义一种方法来在你的持久化后端中唯一标识一个事务。与事务类似，变更的边界也必须明确定义。在默认存储中，变更的边界限定在单个模型实例范围内。

选择一个能够追踪这些变更粒度特性的标识符。

你的 App 可能不需要所有现有的变更类型，或者可能需要不同的变更类型。例如，如果你的 App 仅以时间序列日志的形式插入模型，你可能就不需要更新和删除的变更类型。另一个需要考虑的问题是，你的 App 是否需要支持在删除时保留值，以及删除的值将如何存储。

自定义存储需要实现 `HistoryProviding` 协议来提供历史记录。这将需要能够从存储中组合出定义事务和变更的数据行。

在识别出哪些行属于一个事务之后，你需要构建特定的模型集。

默认数据存储管理历史记录的有效期。作为自定义提供者，你需要决定何时删除历史记录。虽然 SwiftData 历史记录很健壮，可以处理大量的历史数据，但在某些特定情况下，你可能想要删除历史记录。例如，如果你从 App 中移除了某些模型，那么关于这些模型的历史数据你将来可能永远不会再使用。在这种情况下，你可能希望从数据存储中删除这些历史记录。

最后，在向你的自定义存储添加历史记录支持时，你需要创建一个自定义的 token 类型。`HistoryToken` 是 token 的基础协议。需要一些状态来在你的事务流中唯一标识你的位置。

考虑你的 App 是否使用了多个相关的存储。你的自定义 token 应该包含事务中所有使用的存储的状态。

历史记录是一项强大的功能，允许你查询变更，例如发现来自旅行 App 中小组件的更新。SwiftData 使用 Swift 富有表现力的类型系统，使你很容易理解每个模型变更如何在你的 App 中被使用。你可以使用 SwiftData 历史记录在你的 App 中构建令人愉悦的体验。对于正在使用与 Core Data 共存以利用持久化历史记录的开发者，你现在可以转而迁移到 SwiftData 历史记录。如果你正在构建自定义存储，你可以通过创建自己的历史记录类型来支持历史追踪的所有功能。感谢观看。
