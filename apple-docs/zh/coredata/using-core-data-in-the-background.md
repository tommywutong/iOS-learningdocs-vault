---
title: 在后台使用 Core Data
framework: Core Data
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/using-core-data-in-the-background
source_url: 'https://developer.apple.com/documentation/coredata/using-core-data-in-the-background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/using-core-data-in-the-background.json'
content_hash: 'sha256:99b143ebc7aa2584'
translated: true
---

> 导航：[技术](../technologies.md) · [Core Data](../coredata.md)

# 在后台使用 Core Data

<sub>文章</sub>

在单线程和多线程 App 中使用 Core Data。

## 概述

Core Data 可在多线程环境中工作。但是，并非 Core Data 框架下的所有对象都是线程安全的。要在多线程环境中使用 Core Data，请确保：

- 将托管对象上下文（managed object context）绑定到它们初始化所在的线程（队列）。
- 将从上下文中检索到的托管对象（managed object）绑定到与该上下文相同的队列。

### 比较主队列和私有队列上下文

托管对象上下文有两种类型：主队列和私有队列。你在初始化上下文时定义其类型。

主队列上下文（由 [NSMainQueueConcurrencyType](nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype.md) 定义）专门用于你的 App 界面。仅在你的 App 的主队列上使用它。

私有队列上下文（由 [NSPrivateQueueConcurrencyType](nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.md) 定义）在初始化时创建自己的队列。仅在该队列上使用它。由于该队列是私有的，且属于 [NSManagedObjectContext](nsmanagedobjectcontext.md) 实例的内部，你只能通过 [- performBlock:](<nsmanagedobjectcontext/perform(__).md>) 和 [- performBlockAndWait:](<nsmanagedobjectcontext/performandwait(__)-ypye.md>) 方法来访问它。

### 初始化并配置上下文

使用 [- initWithConcurrencyType:](<nsmanagedobjectcontext/init(concurrencytype_).md>) 创建新上下文。例如，要创建一个私有队列上下文：

```swift
// 创建一个私有队列上下文。
let context = NSManagedObjectContext(.privateQueue)
```

初始化时传入的参数决定了你将收到哪种类型的 [NSManagedObjectContext](nsmanagedobjectcontext.md)。

当你使用 [NSPersistentContainer](nspersistentcontainer.md) 时，你将 [viewContext](nspersistentcontainer/viewcontext.md) 属性配置为主队列（[NSMainQueueConcurrencyType](nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype.md)）上下文，并将与 [- performBackgroundTask:](<nspersistentcontainer/performbackgroundtask(__)-39sch.md>) 和 [- newBackgroundContext](<nspersistentcontainer/newbackgroundcontext().md>) 关联的上下文配置为私有队列（[NSPrivateQueueConcurrencyType](nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.md)）。

### 避免问题

**一般而言，避免在主队列上执行与用户无关的数据处理。** 数据处理可能非常消耗 CPU，如果在主队列上执行，可能导致用户界面无响应。如果你的 App 要处理数据，例如将 JSON 数据导入 Core Data，请创建一个私有队列上下文，并在该私有上下文上执行导入操作。

**不要在队列之间传递托管对象实例。** 这样做可能导致数据损坏和 App 终止。当需要将一个托管对象引用从一个队列传递到另一个队列时，请使用 [NSManagedObjectID](nsmanagedobjectid.md) 实例。

你可以通过调用 [NSManagedObject](nsmanagedobject.md) 实例上的 `objectID` 访问器来获取托管对象的托管对象 ID（managed object ID）。

## 另请参阅

### 后台任务

- [加载和显示大量数据馈送](../swiftui/loading-and-displaying-a-large-data-feed.md) — 在后台使用数据，并通过批处理导入和防止重复记录来降低内存使用。
- [冲突解决](conflict-resolution.md) — 检测并解决多线程上数据更改时发生的冲突。
- [批处理](batch-processing.md) — 使用批处理来管理大量数据更改。
