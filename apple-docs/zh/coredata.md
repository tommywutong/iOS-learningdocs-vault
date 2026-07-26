---
title: Core Data
framework: Core Data
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata
source_url: 'https://developer.apple.com/documentation/coredata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata.json'
content_hash: 'sha256:068b4377557abc08'
translated: true
---

> 导航：[Technologies](technologies.md)

# Core Data

<sub>框架</sub>

在单台设备上持久化或缓存数据，或使用 CloudKit 将数据同步到多台设备。

## 概述

使用 Core Data 在单台设备上保存 App 的永久数据以供离线使用、缓存临时数据，并为 App 添加撤销功能。要在同一个 iCloud 账户下跨多台设备同步数据，Core Data 会自动将你的模式镜像到一个 CloudKit 容器。

通过 Core Data 的数据模型编辑器，你可以定义数据的类型和关系，并生成相应的类定义。之后 Core Data 就能在运行时管理对象实例，提供以下功能。

### 持久化

Core Data 会抽象出将对象映射到存储的细节，让你无需直接管理数据库，就能轻松地从 Swift 和 Objective-C 中保存数据。

![流程图，展示 App 将数据保存到持久化存储并从中加载数据。](../../attachments/75428f775be2ff5c6fe139221ff330d4/media-3119932@2x.png)

### 单个及批量更改的撤销与重做

Core Data 的撤销管理器会跟踪更改，并可以逐个、成组或一次性回滚这些更改，让你轻松为 App 添加撤销与重做支持。

![图示展示了摇动撤销手势导致某个元素从列表中移除。](../../attachments/640964de6db0e195490edb69b0d5aae8/media-3118362@2x.png)

### 后台数据任务

在后台执行可能阻塞 UI 的数据任务，比如将 JSON 解析为对象。之后你可以缓存或存储结果，以减少服务器往返次数。

![流程图，展示来自某个端点的数据在后台填充对象，然后再更新 UI。](../../attachments/d71b242e7299eb1f75bd78763df7278c/media-3118359@2x.png)

### 视图同步

Core Data 还通过为表格视图和集合视图提供数据源，帮助保持视图与数据同步。

### 版本控制与迁移

Core Data 包含了对数据模型进行版本控制、以及随着 App 演进迁移用户数据的机制。

## 主题

### 基础

- [Creating a Core Data model](coredata/creating-a-core-data-model.md) — 使用数据模型文件定义 App 的对象结构。
- [Setting up a Core Data stack](coredata/setting-up-a-core-data-stack.md) — 设置用于管理和持久化 App 对象的类。
- [Core Data stack](coredata/core-data-stack.md) — 管理并持久化 App 的模型层。
- [Handling Different Data Types in Core Data](coredata/handling-different-data-types-in-core-data.md) — 为各种数据类型创建、存储和呈现记录。
- [Linking Data Between Two Core Data Stores](coredata/linking-data-between-two-core-data-stores.md) — 将数据组织在两个不同的存储中，并实现它们之间的链接。

### 数据建模

- [Modeling data](coredata/modeling-data.md) — 配置数据模型文件，使其包含 App 的对象图。
- [Core Data model](coredata/core-data-model.md) — 描述 App 的对象结构。

### 获取请求

- [NSFetchRequest](coredata/nsfetchrequest.md) — 用于从持久化存储中检索数据的搜索条件描述。
- [NSAsynchronousFetchRequest](coredata/nsasynchronousfetchrequest.md) — 一种异步检索结果并支持进度通知的获取请求。
- [NSAsynchronousFetchResult](coredata/nsasynchronousfetchresult.md) — 一个获取结果对象，封装了已执行的异步获取请求的响应。
- [NSFetchedResultsController](coredata/nsfetchedresultscontroller.md) — 一个用于管理 Core Data 获取请求结果、并向用户展示数据的控制器。

### SwiftData 迁移与共存

- [Adopting SwiftData for a Core Data app](coredata/adopting-swiftdata-for-a-core-data-app.md) — 使用 Swift 原生的持久化框架，直观地为 App 持久化数据。

### CloudKit 镜像

- [Mirroring a Core Data store with CloudKit](coredata/mirroring-a-core-data-store-with-cloudkit.md) — 用 CloudKit 私有数据库的本地副本支撑用户界面。
- [Synchronizing a local store to the cloud](coredata/synchronizing-a-local-store-to-the-cloud.md) — 在用户的多台设备之间以及不同的 iCloud 用户之间共享数据。
- [NSPersistentCloudKitContainer](coredata/nspersistentcloudkitcontainer.md) — 一个封装了 App 中 Core Data 堆栈、并将选定的持久化存储镜像到 CloudKit 私有数据库的容器。
- [NSPersistentCloudKitContainerOptions](coredata/nspersistentcloudkitcontaineroptions.md) — 一个对象，用于自定义存储描述与 CloudKit 数据库对齐的方式。
- [Sharing Core Data objects between iCloud users](coredata/sharing-core-data-objects-between-icloud-users.md) — 使用 Core Data 和 CloudKit，在同一 iCloud 用户的多台设备间同步数据，并在不同 iCloud 用户之间共享数据。

### 变更处理

- [Accessing data when the store changes](coredata/accessing-data-when-the-store-changes.md) — 确保在你告知上下文之前，它不会察觉到存储的更改。
- [Consuming relevant store changes](coredata/consuming-relevant-store-changes.md) — 筛选存储事务中与当前视图相关的更改。
- [Persistent history](coredata/persistent-history.md) — 使用持久化历史跟踪，确定自启用持久化历史跟踪以来存储中发生了哪些更改。

### 后台任务

- [Using Core Data in the background](coredata/using-core-data-in-the-background.md) — 在单线程和多线程 App 中使用 Core Data。
- [Loading and displaying a large data feed](swiftui/loading-and-displaying-a-large-data-feed.md) — 在后台消费数据，并通过批量导入和防止重复记录来降低内存占用。
- [Conflict resolution](coredata/conflict-resolution.md) — 检测并解决在多个线程上更改数据时出现的冲突。
- [Batch processing](coredata/batch-processing.md) — 使用批处理来管理大规模数据更改。

### 数据模型迁移

- [Migrating your data model automatically](coredata/migrating-your-data-model-automatically.md) — 启用轻量级迁移，让数据模型与底层数据保持一致状态。
- [Staged migrations](coredata/staged-migrations.md) — 迁移包含与轻量级迁移不兼容的更改的复杂数据模型。
- [Manual migrations](coredata/manual-migrations.md) — 迁移超出轻量级迁移和分阶段迁移能力范围的复杂数据模型。

### 相关类型

- [Core Data Constants](coredata/core-data-constants.md) — 用于持久化存储和 Core Data 通知的键。
