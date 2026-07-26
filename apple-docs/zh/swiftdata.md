---
title: SwiftData
framework: SwiftData
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata
source_url: 'https://developer.apple.com/documentation/swiftdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata.json'
content_hash: 'sha256:25d7bd5be1f27035'
translated: true
---

> 导航：[Technologies](technologies.md)

# SwiftData

<sub>框架</sub>

以声明式方式编写模型代码，以添加托管持久化并高效获取模型。

## 概述

SwiftData 结合了 Core Data 久经验证的持久化技术与 Swift 现代的并发特性，让你只需极少的代码、且无需外部依赖，就能快速为 App 添加持久化。借助宏这样的现代语言特性，SwiftData 让你能够编写快速、高效且安全的代码，从而描述 App 的整个模型层（或称对象图）。该框架负责存储底层模型数据，并可选择将该数据同步到多台设备。

SwiftData 的用途不仅限于持久化本地创建的内容。例如，从远程 Web 服务获取数据的 App 可能会使用 SwiftData 实现一个轻量级缓存机制，并提供有限的离线功能。

![以蓝图风格背景为底、包含 1 和 0 的白色 Swift 标志。](../../attachments/aa99d190da3e4c58796b4201d5e7b4c7/swiftdata-hero@2x.png)

SwiftData 在设计上是非侵入式的，可以补充 App 现有的模型类。将 [Model()](<swiftdata/model().md>) 宏附加到任意模型类上即可使其可持久化。使用 [Attribute(_:originalName:hashModifier:)](<swiftdata/attribute(__originalname_hashmodifier_).md>) 和 [Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](<swiftdata/relationship(__deleterule_minimummodelcount_maximummodelcount_originalname_inverse_hashmodifier_).md>) 宏来自定义该模型属性的行为。使用 [ModelContext](swiftdata/modelcontext.md) 类来插入、更新和删除该模型的实例，并将未保存的更改写入磁盘。

要在 SwiftUI 视图中显示模型，可使用 [Query()](<swiftdata/query().md>) 宏并指定谓词或获取描述符。SwiftData 会在视图出现时执行获取操作，并将后续对已获取模型的任何更改告知 SwiftUI，以便视图相应地更新。你可以使用 [modelContext](swiftui/environmentvalues/modelcontext.md) 环境值在任意 SwiftUI 视图中访问模型上下文，并通过 [modelContainer(_:)](<swiftui/view/modelcontainer(__).md>) 和 [modelContext(_:)](<swiftui/view/modelcontext(__).md>) 视图修饰符为某个视图指定特定的模型容器或上下文。

## 主题

### 基础

- [Preserving your app’s model data across launches](swiftdata/preserving-your-apps-model-data-across-launches.md) — 使用框架的宏向 SwiftData 描述你的模型类，并存储这些模型的实例，使其在 App 运行期之外仍然存在。
- [Adding and editing persistent data in your app](swiftdata/adding-and-editing-persistent-data-in-your-app.md) — 创建一个用于收集和更改由 SwiftData 管理数据的数据输入表单。
- [Adopting SwiftData for a Core Data app](coredata/adopting-swiftdata-for-a-core-data-app.md) — 使用 Swift 原生的持久化框架，直观地为 App 持久化数据。 _(beta)_
- [SwiftData updates](updates/swiftdata.md) — 了解 SwiftData 的重要变更。
- [Adopting inheritance in SwiftData](swiftdata/adopting-inheritance-in-swiftdata.md) — 使用类继承为你的模型增加灵活性。

### 模型定义

- [Model()](<swiftdata/model().md>) — 将一个 Swift 类转换为由 SwiftData 管理的存储模型。
- [Attribute(_:originalName:hashModifier:)](<swiftdata/attribute(__originalname_hashmodifier_).md>) — 指定 SwiftData 在管理所属类时应用于被注解属性的自定义行为。
- [Unique(_:)](<swiftdata/unique(__).md>) — 指定 SwiftData 用于强制模型实例唯一性的键路径。
- [Index(_:)](<swiftdata/index(__)-74ia2.md>) — 指定 SwiftData 用于为关联模型创建一个或多个二进制索引的键路径。
- [Index(_:)](<swiftdata/index(__)-7d4z0.md>) — 指定 SwiftData 用于为关联模型创建一个或多个索引的键路径，其中每个索引可以是二进制索引或 R 树索引。
- [Defining data relationships with enumerations and model classes](swiftdata/defining-data-relationships-with-enumerations-and-model-classes.md) — 为 App 中存储的静态和动态数据创建关系。
- [Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](<swiftdata/relationship(__deleterule_minimummodelcount_maximummodelcount_originalname_inverse_hashmodifier_).md>) — 指定 SwiftData 需要用来将被注解属性管理为两个模型之间关系的选项。
- [Transient()](<swiftdata/transient().md>) — 告知 SwiftData 在管理所属类时不要持久化被注解的属性。

### 模型生命周期

- [ModelContainer](swiftdata/modelcontainer.md) — 一个用于管理 App 的模式和模型存储配置的对象。
- [ModelContext](swiftdata/modelcontext.md) — 一个用于获取、插入和删除模型、并将任何更改保存到磁盘的对象。
- [Fetching and filtering time-based model changes](swiftdata/fetching-and-filtering-time-based-model-changes.md) — 跟踪数据存储中发生的所有插入、更新和删除操作，并将其作为一系列按时间顺序排列的事务进行处理。
- [HistoryDescriptor](swiftdata/historydescriptor.md) — 一种类型，用于描述获取历史数据时使用的条件，以及（可选的）排序方式
- [Deleting persistent data from your app](swiftdata/deleting-persistent-data-from-your-app.md) — 探索使用 SwiftData 删除持久化数据的不同方式。
- [Reverting data changes using the undo manager](swiftdata/reverting-data-changes-using-the-undo-manager.md) — 自动记录用户在你的 SwiftUI App 中执行的数据更改操作，让他们能够撤销和重做这些更改。
- [Syncing model data across a person’s devices](swiftdata/syncing-model-data-across-a-persons-devices.md) — 添加所需的能力并定义一个兼容的模式，使 SwiftData 能够使用 iCloud 自动同步 App 的模型数据。
- [Concurrency support](swiftdata/concurrencysupport.md) — 用于以安全且隔离的方式访问模型属性并执行存储相关任务的类型。

### 模型获取

- [Filtering and sorting persistent data](swiftdata/filtering-and-sorting-persistent-data.md) — 使用谓词和动态查询管理数据存储的呈现方式。
- [Query()](<swiftdata/query().md>) — 获取所附加模型类型的所有实例。
- [Additional query macros](swiftdata/additionalquerymacros.md) — 附加的宏，让你能够缩小查询结果范围，并告知 SwiftData 如何对结果进行排序和分组。
- [Query](swiftdata/query.md) — 一种使用指定条件获取模型、并管理这些模型使其与底层数据保持同步的类型。
- [FetchDescriptor](swiftdata/fetchdescriptor.md) — 一种类型，用于描述执行获取操作时使用的条件、排序方式以及任何附加配置。

### 模型存储

- [Maintaining a local copy of server data](swiftdata/maintaining-a-local-copy-of-server-data.md) — 创建并更新一个持久化存储，用于缓存只读网络数据。
- [DefaultStore](swiftdata/defaultstore.md) — 一种使用 Core Data 作为其底层存储机制的数据存储。
- [DataStore](swiftdata/datastore.md) — 一个接口，使 SwiftData 能够在不了解底层存储机制的情况下读写模型数据。
- [DataStoreBatching](swiftdata/datastorebatching.md) — 一个接口，使自定义数据存储能够支持批量请求。
- [HistoryProviding](swiftdata/historyproviding.md) — 一个接口，使自定义数据存储能够为其持久化的模型提供更改历史。
- [Building a document-based app using SwiftData](swiftui/building-a-document-based-app-using-swiftdata.md) — 跟随 WWDC 演讲者一起编写代码，改造一个使用 SwiftData 的 App。
- [ModelDocument](swiftdata/modeldocument.md) — 一种使用 SwiftData 管理其存储的文稿类型。

### 历史生命周期

- [HistoryChange](swiftdata/historychange.md) — 描述数据历史事务的值。
- [HistoryDelete](swiftdata/historydelete.md) — 一个接口，使自定义数据存储能够从其持久化模型的更改历史中删除条目。
- [HistoryInsert](swiftdata/historyinsert.md)
- [HistoryToken](swiftdata/historytoken.md)
- [HistoryTransaction](swiftdata/historytransaction.md)
- [HistoryUpdate](swiftdata/historyupdate.md)
- [HistoryTombstone](swiftdata/historytombstone.md)
- [DefaultHistoryInsert](swiftdata/defaulthistoryinsert.md)
- [DefaultHistoryUpdate](swiftdata/defaulthistoryupdate.md)
- [DefaultHistoryDelete](swiftdata/defaulthistorydelete.md)
- [DefaultHistoryToken](swiftdata/defaulthistorytoken.md)
- [DefaultHistoryTransaction](swiftdata/defaulthistorytransaction.md)

### 数据存储观察

- [ResultsObserver](swiftdata/resultsobserver.md) — 观察并跟踪某个模型上下文中一组持久化模型的更改。 _(beta)_
- [HistoryObserver](swiftdata/historyobserver.md) — 监视模型容器的数据存储中的远程更改，并在有新的历史事务可用时发出通知。 _(beta)_

### 可编码支持

- [DataStoreSnapshotCodingKey](swiftdata/datastoresnapshotcodingkey.md) — 为数据存储快照实现自定义编码器和解码器时使用的键空间，

### 错误

- [SwiftDataError](swiftdata/swiftdataerror.md) — 一种描述 SwiftData 错误的类型。
- [DataStoreError](swiftdata/datastoreerror.md) — 一种描述数据存储错误的类型。
