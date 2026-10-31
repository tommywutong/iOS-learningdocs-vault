---
title: 持久化存储
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/persistent-storage
source_url: 'https://developer.apple.com/documentation/swiftui/persistent-storage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/persistent-storage.json'
content_hash: 'sha256:025ebd6a1f4e2064'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 持久化存储

<sub>API 集合</sub>

存储数据，以便在你的 App 的多次会话之间使用。

## 概述

操作系统提供了在你的 App 关闭时存储数据的方法，这样当人们稍后再次打开你的 App 时，就可以不间断地继续工作。你使用哪种机制取决于诸多因素，例如需要存储什么、存储多少、是否需要对数据进行序列化访问或随机访问等等。

![](../../../attachments/45f566a52f46e696909b2586bde96bd8/persistent-storage-hero@2x.png)

你在 SwiftUI App 中使用的存储类型与其他任何 App 中使用的相同。例如，你可以使用 [FileManager](../foundation/filemanager.md) 接口访问磁盘上的文件。不过，SwiftUI 还提供了一些便利功能，让你在声明式环境中更容易使用某些类型的持久化存储。例如，你可以使用 [FetchRequest](fetchrequest.md) 和 [FetchedResults](fetchedresults.md) 来与 Core Data 模型交互。

## 主题

### 跨 App 启动保存状态

- [使用 SwiftUI 恢复你的 App 的状态](restoring-your-app-s-state-with-swiftui.md) — 通过保留用户当前的活动来为用户提供 App 连续性。
- [defaultAppStorage(_:)](<view/defaultappstorage(__).md>) — 视图内包含的 `AppStorage` 所使用的默认存储。
- [AppStorage](appstorage.md) — 一种属性包装器类型，反映来自 `UserDefaults` 的值，并在该 user default 中的值发生变化时使视图失效。
- [SceneStorage](scenestorage.md) — 一种属性包装器类型，读取和写入持久化的按场景存储。

### 访问 Core Data

- [加载并显示大型数据源](loading-and-displaying-a-large-data-feed.md) — 在后台消费数据，并通过批量导入和防止重复记录来降低内存占用。
- [managedObjectContext](environmentvalues/managedobjectcontext.md)
- [FetchRequest](fetchrequest.md) — 一种属性包装器类型，从 Core Data 持久化存储中获取实体。
- [FetchedResults](fetchedresults.md) — 从 Core Data 存储中获取的结果集合。
- [SectionedFetchRequest](sectionedfetchrequest.md) — 一种属性包装器类型，从 Core Data 持久化存储中获取分组为分区的实体。
- [SectionedFetchResults](sectionedfetchresults.md) — 从 Core Data 持久化存储中获取的结果集合，分组为分区。

## 另请参阅

### 数据与存储

- [模型数据](model-data.md) — 管理你的 App 用来驱动其界面的数据。
- [环境值](environment-values.md) — 使用环境在整个视图层级结构中共享数据。
- [偏好设置](preferences.md) — 从视图向其容器视图指示配置偏好。
