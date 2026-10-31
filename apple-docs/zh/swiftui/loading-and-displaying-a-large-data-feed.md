---
title: 加载并显示大型数据馈送
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, Xcode 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/loading-and-displaying-a-large-data-feed
source_url: 'https://developer.apple.com/documentation/swiftui/loading-and-displaying-a-large-data-feed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/loading-and-displaying-a-large-data-feed.json'
content_hash: 'sha256:df195a8413e25af1'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [持久化存储](persistent-storage.md)

# 加载并显示大型数据馈送

<sub>示例代码</sub>

在后台消耗数据，并通过分批导入和防止重复记录来降低内存占用。

## 概述

本示例创建一个 App，通过消耗美国地质调查局（USGS）的实时数据馈送，显示过去 30 天在美国记录的地震列表。

要加载 USGS JSON 馈送，请执行以下任一操作：

- 在 iOS 上，下拉刷新 [List](list.md)。
- 在 iOS 和 macOS 上，按下刷新按钮（⌘R）。

App 将在 [URLSession](../foundation/urlsession.md) 的默认委托队列（一个在后台运行的操作队列）上加载请求的数据。在馈送下载完成且会话数据任务结束后，App 会继续在此队列上工作，将大量馈送元素导入存储，而不会阻塞主队列。

> [!note] 注意
> 本示例代码项目关联 WWDC21 场次 [10017: Bring Core Data Concurrency to Swift and SwiftUI](https://developer.apple.com/wwdc21/10017/)。

### 在后台导入数据

要在后台导入数据，App 可以使用一个或两个托管对象上下文。本示例使用两个 [NSManagedObjectContext](../coredata/nsmanagedobjectcontext.md) 实例：

- 一个主队列上下文，用于向用户界面提供数据。
- 一个私有队列上下文，用于在后台队列上执行导入。

两个上下文都连接到同一个 [persistentStoreCoordinator](../coredata/nspersistentcontainer/persistentstorecoordinator.md)。这种配置比使用嵌套上下文更高效。

本示例通过使用 [NSPersistentContainer](../coredata/nspersistentcontainer.md) 搭建 Core Data 栈来创建主队列上下文，该容器会在其 [viewContext](../coredata/nspersistentcontainer/viewcontext.md) 属性中初始化一个主队列上下文。

```swift
let container = NSPersistentContainer(name: "Earthquakes")
```

通过调用持久化容器的 [newBackgroundContext()](<../coredata/nspersistentcontainer/newbackgroundcontext().md>) 方法创建私有队列上下文。

```swift
let taskContext = container.newBackgroundContext()
```

馈送下载完成后，示例会使用任务上下文在后台消耗馈送。在 Core Data 中，每个基于队列的上下文都有自己的串行队列，App 必须通过使用 [perform(_:)](<../coredata/nsmanagedobjectcontext/perform(__).md>)（带或不带 `await` 关键字）或 [performAndWait(_:)](<../coredata/nsmanagedobjectcontext/performandwait(__)-ypye.md>) 闭包包裹代码，来对操控上下文与队列的任务进行串行化。

```swift
try await taskContext.perform {
```

有关使用并发的更多信息，请参阅 [NSManagedObjectContext](../coredata/nsmanagedobjectcontext.md#Concurrency)。

为了高效处理大型数据集，示例使用了 [NSBatchInsertRequest](../coredata/nsbatchinsertrequest.md)，它直接访问存储——不与上下文交互、不触发任何键值观察、也不分配托管对象。[NSBatchInsertRequest](../coredata/nsbatchinsertrequest.md) 的闭包式初始化方法允许 App 在 Core Data 调用 `dictionaryHandler` 闭包时一次提供一条记录，这有助于 App 保持较低的内存占用空间，因为它们无需为所有记录准备缓冲区。

```swift
let batchInsertRequest = self.newBatchInsertRequest(with: propertiesList)
if let fetchResult = try? taskContext.execute(batchInsertRequest),
   let batchInsertResult = fetchResult as? NSBatchInsertResult,
   let success = batchInsertResult.result as? Bool, success {
    return
}
```

### 合并更改并更新用户界面

由于 [NSBatchInsertRequest](../coredata/nsbatchinsertrequest.md) 绕过了上下文，不会触发 [NSManagedObjectContextDidSaveNotification](../coredata/nsmanagedobjectcontextdidsavenotification.md) 通知，需要用这些更改更新 UI 的 App 有两种选择：

- 通过解析存储的[持久化历史](../coredata/persistent-history.md)提取相关更改，然后将它们合并到视图上下文。有关持久化历史跟踪的更多信息，请参阅[消耗相关的存储更改](../coredata/consuming-relevant-store-changes.md)。
- 从存储重新获取数据。但是，如果视图上下文被固定到某个查询生成（query generation），则需要在获取数据前重置上下文。有关查询生成的更多信息，请参阅[存储变化时访问数据](../coredata/accessing-data-when-the-store-changes.md)。

本示例使用持久化存储远程更改通知和持久化历史跟踪来更新 UI，原因如下：

- 数据模型只包含一个实体，因此所有更改都与 `List` 相关，无需解析历史中的特定更改。
- [FetchRequest](fetchrequest.md) 直接从存储获取和检索结果，`List` 会自动刷新其内容。
- SwiftUI 只关心视图上下文，因此 `QuakesProvider` 观察 [NSPersistentStoreRemoteChange](../foundation/nsnotification/name-swift.struct/nspersistentstoreremotechange.md) 通知，将来自后台上下文（执行批量操作）的更改合并到视图上下文。

通过将存储描述上的 [NSPersistentStoreRemoteChangeNotificationPostOptionKey](../coredata/nspersistentstoreremotechangenotificationpostoptionkey.md) 选项设置为 `true`，为持久化存储启用远程更改通知。

```swift
description.setOption(true as NSNumber,
                      forKey: NSPersistentStoreRemoteChangeNotificationPostOptionKey)
```

同样，通过将 [NSPersistentHistoryTrackingKey](../coredata/nspersistenthistorytrackingkey.md) 选项设置为 `true`，为持久化存储启用持久化历史跟踪。

```swift
description.setOption(true as NSNumber,
                      forKey: NSPersistentHistoryTrackingKey)
```

只要持久化存储内发生更改（包括其他进程的写入），存储就会发布远程更改通知。示例收到通知后，会获取在给定令牌之后发生的持久化历史事务和更改。在持久化历史更改请求检索到历史后，示例通过 [mergeChanges(fromContextDidSave:)](<../coredata/nsmanagedobjectcontext/mergechanges(fromcontextdidsave_).md>) 将每个事务的 [objectIDNotification()](<../coredata/nspersistenthistorytransaction/objectidnotification().md>) 合并到视图上下文。

```swift
let changeRequest = NSPersistentHistoryChangeRequest.fetchHistory(after: lastToken)
let historyResult = try taskContext.execute(changeRequest) as? NSPersistentHistoryResult
if let history = historyResult?.result as? [NSPersistentHistoryTransaction] {
    return history
}
```

在执行每个 [NSBatchInsertRequest](../coredata/nsbatchinsertrequest.md) 或 [NSBatchDeleteRequest](../coredata/nsbatchdeleterequest.md) 后，示例会将所有 UI 更新派发回主队列，以便在 SwiftUI 中渲染。

```swift
let viewContext = container.viewContext
let tokens = await viewContext.perform {
    history.map { (transaction: NSPersistentHistoryTransaction) -> NSPersistentHistoryToken in
        viewContext.mergeChanges(fromContextDidSave: transaction.objectIDNotification())
        return transaction.token
    }
}
```

在合并最后一个事务的更改后，示例需要将该令牌存储在内存中或磁盘上，以便在后续的持久化历史更改请求中使用它。

### 分批工作以降低内存占用空间

当 App 在上下文中获取或创建对象时，Core Data 会缓存该对象，以避免 App 再次使用这些对象时对存储文件产生一来一回的开销。但是，随着 App 处理越来越多的对象，这种方式会增大 App 的内存占用空间，并最终可能在 iOS 上导致内存不足警告或 App 被终止。[NSBatchInsertRequest](../coredata/nsbatchinsertrequest.md) 不会明显增加 App 的内存占用空间，因为它不会将数据载入内存。

> [!note] 注意
> 以在早于 iOS 13 或 macOS 10.15 的系统上运行为目标的 App，需要通过分批处理对象并在每批处理后调用 [reset()](<../coredata/nsmanagedobjectcontext/reset().md>) 重置上下文，来避免内存占用空间增长。

示例将 `viewContext` 的 [automaticallyMergesChangesFromParent](../coredata/nsmanagedobjectcontext/automaticallymergeschangesfromparent.md) 属性设置为 `false`，以防止 Core Data 在每次保存后台上下文时自动合并更改。

```swift
container.viewContext.automaticallyMergesChangesFromParent = false
```

### 防止存储中出现重复数据

示例 App 每次重新加载 JSON 馈送时，解析出的数据都包含过去一个月的所有地震记录，因此可能包含许多已导入数据的重复项。为避免创建重复记录，App 将某个属性或属性组合约束为在所有实例中唯一。

`code` 属性唯一标识一条地震记录，因此将 `Quake` 实体约束在 `code` 上可确保存储的任意两条记录都不会具有相同的 `code` 值。

在数据模型编辑器中选择 `Quake` 实体。在数据模型检查器中，点击 Constraints 列表下方的 + 按钮添加新约束。此时会出现一个约束占位符。

```swift
comma, separated, properties
```

双击占位符进行编辑。输入作为实体唯一约束的属性名称，或以逗号分隔的属性列表。

```swift
code
```

保存新记录时，存储现在会检查是否已存在约束属性值相同的记录。一旦发生冲突，就会启用 [NSMergeByPropertyObjectTrumpMergePolicy](../coredata/nsmergebypropertyobjecttrumpmergepolicy.md) 策略，新记录会覆盖现有记录中的所有字段。

```swift
container.viewContext.automaticallyMergesChangesFromParent = false
```

## 另请参阅

### 访问 Core Data

- [managedObjectContext](environmentvalues/managedobjectcontext.md)
- [FetchRequest](fetchrequest.md) — 一种属性包装器类型，从 Core Data 持久化存储中检索实体。
- [FetchedResults](fetchedresults.md) — 从 Core Data 存储检索到的结果集合。
- [SectionedFetchRequest](sectionedfetchrequest.md) — 一种属性包装器类型，从 Core Data 持久化存储中检索按分区分组的实体。
- [SectionedFetchResults](sectionedfetchresults.md) — 从 Core Data 持久化存储检索到的结果集合，按分区分组。

## 下载

- [LoadingAndDisplayingALargeDataFeed.zip](https://docs-assets.developer.apple.com/published/c1a1a08fa8d2/LoadingAndDisplayingALargeDataFeed.zip)
