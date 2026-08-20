---
title: 在 SwiftData 中创建自定义数据存储
session_id: 10138
collection: wwdc2024
year: 2024
duration: '13:52'
topics: [App Services, Swift]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2024/10138/'
content_hash: 'sha256:fbe35bba5505e8bf'
translated: true
---

# 在 SwiftData 中创建自定义数据存储

<sub>WWDC2024 · 13:52 · App Services、Swift</sub>

将 SwiftData 富有表现力的声明式（declarative）建模 API 与你自己的持久化后端相结合。了解如何构建自定义数据存储……

> [!note] 归档理由
> 自定义数据存储后端，看清 SwiftData 抽象层

## 章节

- [简介](/videos/play/wwdc2024/10138/?time=0)
- [概述](/videos/play/wwdc2024/10138/?time=81)
- [认识 DataStore](/videos/play/wwdc2024/10138/?time=290)
- [示例存储](/videos/play/wwdc2024/10138/?time=462)

## 相关资源

- [简介](https://developer.apple.com/videos/play/wwdc2024/10138/?time=0)
- [概述](https://developer.apple.com/videos/play/wwdc2024/10138/?time=81)
- [认识 DataStore](https://developer.apple.com/videos/play/wwdc2024/10138/?time=290)
- [示例存储](https://developer.apple.com/videos/play/wwdc2024/10138/?time=462)
- [论坛：编程语言](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010)
- [SwiftData](https://developer.apple.com/documentation/SwiftData)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10138/4/A149C0AB-2AB1-48C1-B259-4D5621873D5F/downloads/wwdc2024-10138_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10138/4/A149C0AB-2AB1-48C1-B259-4D5621873D5F/downloads/wwdc2024-10138_sd.mp4?dl=1)
- [使用 SwiftData 历史记录跟踪模型更改](https://developer.apple.com/videos/play/wwdc2024/10075)
- [实现一个 JSON 存储](https://developer.apple.com/videos/play/wwdc2024/10138/?time=495)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好！我是 Luvena，很高兴能和你们聊聊 SwiftData 中的自定义 DataStore，这是一种将 SwiftData 与你自己的持久化后端结合使用的方式。自定义数据存储是 SwiftData 中的新功能，允许你使用任何你选择的文稿（document）、文件格式或持久化后端。而且它们能与你现有的所有 SwiftData 代码完美配合。

在这段 SampleTrips App 的实现代码中，只需将 `ModelConfiguration` 替换为 `JSONStoreConfiguration`（我将在稍后的视频中实现的一个示例），我就可以更改存储的类型。仅需这一处替换，`ModelContainer` 就知道要使用不同的存储类型，而无需我更改 SampleTrips App 中的任何模型或视图（view）代码。

在本视频中，我将首先介绍存储（store）在 SwiftData 中所扮演的角色，以及它与 `ModelContext` 和 `ModelContainer` 的交互方式。

然后，我将探讨如何使用新的 `DataStore` 协议来构建它们。最后，我将通过一个使用 JSON 文件进行持久化的示例，介绍实现自定义 DataStore 的要点。从高层视角来看，存储负责获取和保存所有支持持久化模型所需的数据。为了探讨自定义数据存储在 SwiftData 中的工作方式，我将研究它们如何为我的 App SampleTrips 提供持久化支持。SampleTrips 建立在 SwiftUI 和 SwiftData 的强大协同作用之上。一个典型的 App 由三个重要部分组成。SwiftUI 提供用户界面，通常是一个视图，例如列表或标签（label），用于显示 `ModelContext` 中模型的数据。`ModelContext` 使用 `ModelContainer` 中的存储来读写数据。在本视频中，我将重点介绍存储（store）在 SwiftData 中扮演的角色。

SampleTrips 使用 `ModelContext` 来驱动视图并显示旅行记录。`ModelContext` 为视图中的每条旅行记录实例化持久化模型。每条旅行记录也有一个对应的持久化标识符（Persistent Identifier），用于唯一标识该模型。`ModelContext` 会跟踪我做出的更改，以便在需要时保存到存储中。

例如，如果我决定取消前往洛杉矶的旅行，并新增一趟前往东京的旅行，这些更改会被 `ModelContext` 跟踪。当新的东京模型被插入到模型上下文中时，它由一个临时的 `PersistentIdentifier` 标识。当 `ModelContext` 执行保存时，它会告诉存储删除洛杉矶的旅行并插入新的东京旅行。

然后，存储会为东京模型分配一个永久的持久化标识符 `Trip-5`，并将其之前的临时标识符 `Trip-t1` 映射到它，这个过程称为“重新映射”（remapping）。

接着，存储将东京旅行更新后的持久化标识符返回给 `ModelContext`。

在模型上下文完成其状态更新后，UI 可以更新视图以渲染这些旅行记录。

持久化更改只是 `ModelContext` 和存储协同工作以支持 SwiftData 中 `PersistentModel` 的一个例子。它们使用一组定义操作（如 fetch 或 save）的请求和响应进行通信。存储的角色是提供模型值如何被持久化的实现。这种通信利用了模型的一种可发送（Sendable）、可编码（codable）的表示，称为 `DataStoreSnapshot`。

在 SampleTrips App 中，视图使用持久化模型与 `ModelContext` 进行通信。

然而，当 `ModelContext` 需要与存储（store）通信时，它会创建一个快照（snapshot）来保存模型的当前状态。

快照是一个可发送（Sendable）、可编码（codable）的容器，其中包含了模型在那一刻的值。与持久化模型一样，每个快照都由一个持久化标识符（Persistent Identifier）标识。

然后，存储使用这些快照并将这些值应用到它的存储中。反之亦然。

当 `ModelContext` 从存储中读取数据时，存储会创建一组与上下文请求的 `PersistentModel` 相对应的快照。

然后，`ModelContext` 为每个快照创建 `PersistentModel`，供视图、查询或上下文正在执行的其他工作使用。

存储（store）在 SwiftData 中扮演着关键角色，它允许 `ModelContext` 将模型数据读写到任何存储格式。接下来，让我带你了解新的 `DataStore` 协议，以及它如何实现这一点。

一个存储有三个关键部分：一个描述存储的配置（configuration）、用于与模型上下文通信模型值的快照（snapshots），以及一个 `ModelContainer` 可以管理的存储实现。这些部分中的每一个都符合三个不同的协议：`DataStoreConfiguration`、`DataStoreSnapshot` 和 `DataStore`。

SwiftData 中的默认存储（Default Store）提供了这些类型的自身实现：`ModelConfiguration`、`DefaultSnapshot` 和 `DefaultStore`。`DefaultStore` 支持 SwiftData 的所有丰富特性，如迁移（migration）、历史记录跟踪（history tracking）和 CloudKit 同步（sync）。它封装了平台在性能和可伸缩性方面的最佳实践，使其成为持久化模型的最佳默认选择。

`DataStore` 协议定义了 SwiftData 需要存储（store）以便能被 `ModelContext` 使用的所有功能，包括保存（save）、获取（fetch）和缓存（caching）。其他协议定义了可选的数据存储功能，例如新的用于描述对存储（store）所有更改的 History 协议。

模型上下文（model context）使用来自 `DataStore` 协议的请求和响应与存储（store）通信。

例如，当从存储中获取数据时，`ModelContext` 会向存储发送一个 `DataStoreFetchRequest`，其中包含描述存储应检索哪些数据的 `FetchDescriptor`。

存储检索到模型值后，会为每个模型创建一个快照（snapshot），并将它们放在 `DataStoreFetchResult` 中返回。

然后，`ModelContext` 为每个快照创建一个 `PersistentModel`。

当模型在模型上下文中被更改并调用保存（save）时，也会发生类似的过程。模型上下文会创建一个 `DataStoreSaveChangesRequest`，其中包含所有被修改的模型的快照，并将请求发送给存储。

接着，存储将这些快照应用到其存储中，并创建一个 `DataStoreSaveChangesResult` 发送回 `ModelContext`。在结果中，存储为任何新插入的模型（例如 `Trip-t1`）提供了重新映射（remapped）标识符的映射关系。这告诉模型上下文将插入的旅行记录的持久化标识符更新为 `Trip-5`。

最后，模型上下文处理来自存储的保存结果并更新其状态，将新的永久持久化标识符分配给插入的旅行记录。

现在我已经介绍了 DataStore 的机制，我想探索一下实际实现一个存储是怎样的体验。我将实现一个使用 JSON 文件来持久化 SampleTrips 应用程序中模型的存储。在开始之前，我想澄清两点。这个存储是一个“归档存储”（archival store），意味着在读写时会加载整个文件。

此外，我将使用 Foundation 提供的 JSON 编码器（JSON coders），并将数据作为快照数组存储在文件中。

创建存储的第一步是声明符合 `DataStoreConfiguration` 和 `DataStore` 协议的配置和存储类型。

这些类型使用关联类型（associated type）相互引用。在配置（configuration）上，我将 `Store` 类型设置为 `JSONStore`，在存储（store）上，我将 `Configuration` 设置为 `JSONStoreConfiguration`。

此外，`JSONStore` 声明了它用于与 `ModelContext` 通信的快照（snapshot）类型。这里，我使用 `DefaultSnapshot`，因为我不需要自定义模型数据的编码或解码。

现在我可以开始实现一个 DataStore 能被 `ModelContext` 使用所需的两个方法：`fetch` 和 `save`。

当 `ModelContext` 发送 `DataStoreFetchRequest` 时，我需要加载存储中的数据，并实例化一个 `DataStoreFetchResult`。

由于 `DefaultSnapshot` 是可编码（codable）的，我可以使用 `JSONDecoder` 从配置提供的文件 URL 加载存储的数据。

然后，我将实例化一个 `DataStoreFetchResult` 并用文件中的快照返回它。目前，这个实现没有处理 `FetchDescriptor` 上的谓词（predicate）或排序比较器。谓词（Predicate）或排序比较器的翻译可能是一个复杂的过程，我可以改用 `ModelContext` 来为我执行这项工作。

为此，当请求包含谓词或排序描述符时，我将抛出 `preferInMemoryFilter` 和 `preferInMemorySort` 错误。这很适合我的情况，因为这是一个可以加载到内存中的小数据集。现在我有了一个完全可用的 fetch 实现，可以支持查询和排序。实现了 fetch 之后，我可以实现 save 来将快照写入 JSON 文件。

在实现 save 时，我需要考虑并处理 3 种类型的更改：插入（insertions）、更新（updates）和删除（deletions）。

在开始处理保存请求中的传入快照之前，我首先必须读取文件的当前内容，我在一个名为 `read` 的单独方法中处理它。我将所有快照组织成一个以它们的持久化标识符为键的字典，这将是我最终要写入磁盘的新 JSON 文件的工作副本。

然后我处理保存请求中插入模型的快照。这涉及为每个插入的快照分配和重新映射标识符。让我更详细地研究一下。

回想一下，当模型被插入到存储中时，每个模型都包含一个不与任何存储关联的临时标识符。对于这里的每个插入的快照，我创建一个新的、永久的持久化标识符。然后我创建一个使用新持久化标识符的快照副本。

这个新的持久化标识符会被映射到 `remappedIdentifiers` 字典中的临时标识符，以便稍后在保存结果中返回给 `ModelContext`。最后，我将插入的快照添加到最初从文件加载的快照中。

处理完插入的快照后，我通过用保存请求中的快照替换文件中的快照来处理更新。

最后，我从从文件加载的快照中移除已删除的快照。现在我在 `snapshotsByIdentifier` 字典中拥有了一组完整且更新的数据，我想将其写回文件。

我将使用 `JSONEncoder` 将这个快照的工作副本作为一个 JSON 文件写回磁盘。

最后，我返回一个包含保存结果的 `DataStoreSaveChangesResult`。`DataStoreSaveChangesResult` 包含重新映射后的 `persistentIdentifiers`，供上下文更新。

现在我已经有了一个完整的自定义数据存储，我可以在 SampleTrips 中采用它。在 App 定义中，只需将 `ModelConfiguration` 替换为 `JSONStoreConfiguration`，我就可以更改存储的类型。仅需这一处替换，`ModelContainer` 就知道要使用不同的存储类型，而无需我更改 SampleTrips App 中的任何模型或视图代码。

有了 `DataStore`，SwiftData 可以读写数据到任何存储格式或持久化后端。

这让你可以将 SwiftUI 和 `PersistentModel` 的强大功能与你需要的任何文稿（document）、数据库或云存储结合使用，而 `ModelContext` 通过为你提供过滤和排序功能，有助于降低简单存储实现的复杂性。

在 SwiftData 中采用自定义存储就像更改 `DataStoreConfiguration` 一样简单，而通过新的 `DataStore` 协议，你可以实现对任何持久化后端的支持。这为 SwiftData 开辟了巨大的新可能性。

请务必观看“SwiftData 新变化”，了解其他新功能，如索引（Indexing）和唯一约束（Unique constraints）。也请不要错过“使用 SwiftData 历史记录跟踪模型更改”，全面了解如何检查存储（store）的历史记录。

感谢你的参与！我迫不及待想看到你构建的作品。
