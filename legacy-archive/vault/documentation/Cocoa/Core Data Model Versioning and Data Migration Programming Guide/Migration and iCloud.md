---
title: Core Data 模型版本管理与数据迁移编程指南
apple_id: TP40004399
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/vmCloud/vmCloud.html
archived_at: '2026-07-15T07:14:31.773716Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 模型版本管理与数据迁移编程指南](Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md)


[下一页](Document%20Revision%20History.md)[上一页](Customizing%20the%20Migration%20Process.md)

# 迁移与 iCloud

如果你正在使用 iCloud，只能通过自动轻量级迁移来迁移存储的内容。要迁移一个位于 iCloud 中的持久化存储，需要使用 [addPersistentStoreWithType:configuration:URL:options:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore) 将该存储添加到持久化存储协调器，并在选项字典中至少传入以下选项：

```objc
NSDictionary *optionsDictionary = [[NSDictionary alloc] initWithObjectsAndKeys:
    [NSNumber numberWithBool:YES], NSInferMappingModelAutomaticallyOption,
    [NSNumber numberWithBool:YES], NSMigratePersistentStoresAutomaticallyOption,
    <#Ubiquitous content name#>, NSPersistentStoreUbiquitousContentNameKey, nil];
```

对存储的更改，会针对与给定 [NSPersistentStoreUbiquitousContentNameKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontentnamekey) 关联的每个模型版本，独立记录并保留下来。使用某个给定 `NSPersistentStoreUbiquitousContentNameKey` 配置的持久化存储，只有在模型版本匹配的情况下，才会与另一台设备上的存储同步数据。

如果你将一个使用 `NSPersistentStoreUbiquitousContentNameKey` 选项配置的持久化存储迁移到新的模型版本，该存储中源自当前设备的变更历史也会一并被迁移，然后与其他配置了该新模型版本的设备合并。使用新版本的存储所产生的变更也会一并被合并进来。但是，如果迁移是使用自定义映射模型执行的，现有的变更_不能_被迁移到新的模型版本。

[下一页](Document%20Revision%20History.md)[上一页](Customizing%20the%20Migration%20Process.md)
