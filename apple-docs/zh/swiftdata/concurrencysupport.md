---
title: 并发支持
framework: SwiftData
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/concurrencysupport
source_url: 'https://developer.apple.com/documentation/swiftdata/concurrencysupport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/concurrencysupport.json'
content_hash: 'sha256:58be5b7c107eae5c'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftData](../swiftdata.md)

# 并发支持

<sub>API 集合</sub>

用于以安全且隔离的方式访问模型属性并执行存储相关任务的类型。

## 主题

### Model Actor

- [ModelActor()](<modelactor().md>) — 通过生成满足关联协议所需的样板代码，将 Swift Actor 转换为 Model Actor。
- [ModelActor](modelactor.md) — 一个接口，为符合协议的模型提供互斥的属性访问。

### Model Executor

- [DefaultSerialModelExecutor](defaultserialmodelexecutor.md) — 使用隔离的模型上下文安全地执行存储相关任务的对象。
- [SerialModelExecutor](serialmodelexecutor.md) — 一个接口，用于使用隔离的模型上下文执行串行的存储相关任务。
- [ModelExecutor](modelexecutor.md) — 一个接口，用于使用隔离的模型上下文执行存储相关任务。

## 另请参阅

### 模型生命周期

- [ModelContainer](modelcontainer.md) — 管理 App 的 schema 和模型存储配置的对象。
- [ModelContext](modelcontext.md) — 一个对象，让你能获取、插入和删除模型，并将任何更改保存到磁盘。
- [获取和筛选基于时间的模型更改](fetching-and-filtering-time-based-model-changes.md) — 跟踪数据存储中发生的所有插入、更新和删除操作，并将它们作为一系列按时间顺序的事务进行处理。
- [HistoryDescriptor](historydescriptor.md) — 一种类型，描述在获取历史数据时使用的条件以及可选的排序顺序。
- [从 App 中删除持久化数据](deleting-persistent-data-from-your-app.md) — 探索使用 SwiftData 删除持久化数据的不同方式。
- [使用撤消管理器还原数据更改](reverting-data-changes-using-the-undo-manager.md) — 自动记录用户在 SwiftUI App 中执行的数据更改操作，并让他们可以撤消和重做这些更改。
- [在用户的设备间同步模型数据](syncing-model-data-across-a-persons-devices.md) — 添加所需功能并定义兼容的 schema，使 SwiftData 能够使用 iCloud 自动同步 App 的模型数据。
