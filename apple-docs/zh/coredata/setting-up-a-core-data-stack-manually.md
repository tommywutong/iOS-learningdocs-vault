---
title: 手动设置 Core Data 堆栈
framework: Core Data
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/setting-up-a-core-data-stack-manually
source_url: 'https://developer.apple.com/documentation/coredata/setting-up-a-core-data-stack-manually'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/setting-up-a-core-data-stack-manually.json'
content_hash: 'sha256:b1fafbcbc67e743d'
translated: true
---

> 导航：[技术](../technologies.md) · [Core Data](../coredata.md) · [设置 Core Data 堆栈](setting-up-a-core-data-stack.md)

# 手动设置 Core Data 堆栈

<sub>文章</sub>

手动创建 Core Data 所需的各个组件，以支持较早版本的 Apple 操作系统。

## 概述

如果你的 App 目标平台为 iOS 10+、macOS 10.12+、tvOS 10+、watchOS 3+ 或 visionOS 1+，你可以使用 [NSPersistentContainer](nspersistentcontainer.md) 来简化 Core Data 堆栈的创建和管理。否则，你需要手动创建 [NSManagedObjectModel](nsmanagedobjectmodel.md)、[NSPersistentStoreCoordinator](nspersistentstorecoordinator.md) 以及至少一个 [NSManagedObjectContext](nsmanagedobjectcontext.md)。

### 创建托管对象模型

要实例化 [NSManagedObjectModel](nsmanagedobjectmodel.md)，请传入一个指向 `.xcdatamodeld` 文件编译版本的 URL。这个 `.momd` 文件通常位于你的 App bundle 中。

```swift
// 获取 App bundle 中编译后模型的 URL。
guard let modelURL = Bundle.main.url(forResource: "DataModel",
                                     withExtension: "momd") else {
    fatalError("Failed to find data model")
}

// 使用该 URL 创建一个托管对象模型（managed object model）。
guard let model = NSManagedObjectModel(contentsOf: modelURL) else {
    fatalError("Failed to create model from file: \(modelURL)")
}
```

### 创建持久化存储协调器

接下来，将托管对象模型传递给 [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md) 的初始化方法，以创建一个带有该模型的存储协调器。

```swift
// 使用托管对象模型创建一个持久化存储协调器。
let coordinator = NSPersistentStoreCoordinator(managedObjectModel: managedObjectModel)
```

#### 向协调器添加持久化存储

如果你希望 Core Data 将数据模型持久化到磁盘，请告诉存储协调器文件所在的位置以及要使用的格式。

```swift
// 获取文稿目录的 URL。
let documentDirectoryURL = FileManager.default.urls(for: .documentDirectory,
                                                    in: .userDomainMask).last
// 创建指向数据存储的 URL。
guard let storeURL = URL(string: "DataModel.sqlite",
                         relativeTo: documentDirectoryURL) else {
    fatalError("Failed to create store URL")
}

do {
    // 设置选项以启用轻量级数据迁移。
    let options = [NSMigratePersistentStoresAutomaticallyOption: true,
                         NSInferMappingModelAutomaticallyOption: true]
    // 将存储添加到协调器。
    _ = try coordinator.addPersistentStore(type: .sqlite, at: storeURL,
                                       options: options)
} catch {
    fatalError("Failed to add persistent store: \(error.localizedDescription)")
}
```

> [!important] 重要
> 如果你不使用 [NSPersistentContainer](nspersistentcontainer.md) 来设置 Core Data 堆栈，你还需要手动设置选项以启用轻量级数据迁移。有关更多信息，请参阅[自动迁移数据模型](migrating-your-data-model-automatically.md)。

每种存储类型都有各自的优缺点。有关每种存储类型的详细信息，请参阅 [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md) 文档。

### 创建托管对象上下文

创建一个 [NSManagedObjectContext](nsmanagedobjectcontext.md)，并设置其 store coordinator 属性。

```swift
// 创建一个上下文以与托管对象交互。
let context = NSManagedObjectContext(concurrencyType: .mainQueueConcurrencyType)
// 将协调器分配给上下文。
context.persistentStoreCoordinator = persistentStoreCoordinator
```

你的 App 使用这个上下文与 Core Data 交互。将这个上下文的引用传递给你的用户界面。有关更多信息，请参阅[注入托管对象上下文](setting-up-a-core-data-stack.md#Inject-the-managed-object-context)。
