---
title: Core Data 模型版本管理与数据迁移编程指南
apple_id: TP40004399
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/vmInitiating.html
archived_at: '2026-07-15T07:14:29.014546Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 模型版本管理与数据迁移编程指南](Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md)


[下一页](Customizing%20the%20Migration%20Process.md)[上一页](The%20Migration%20Process.md)

# 启动迁移过程

本章介绍如何启动迁移过程，以及默认迁移过程的工作原理。它不涉及如何定制迁移过程——这部分内容在 [Customizing the Migration Process](Customizing%20the%20Migration%20Process.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqobnknltc) 中说明。

当你初始化一个持久化存储协调器时，会为它指定一个托管对象模型（参见 [initWithManagedObjectModel:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468895-init)）；该协调器会使用该模型来打开持久化存储。你使用 [addPersistentStoreWithType:configuration:URL:options:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore) 打开一个持久化存储。不过，你具体如何使用该方法，取决于你的应用程序是否使用模型版本管理，以及你选择以何种方式支持迁移——是使用默认迁移过程，还是自定义版本偏差检测与迁移启动逻辑。以下列出了不同场景，以及每种场景下你应该怎么做：

- 你的应用程序不支持版本管理

  你可以直接使用 [addPersistentStoreWithType:configuration:URL:options:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore)。

  如果由于某种原因，协调器的模型与存储的模式不兼容（也就是说，当前模型各实体的版本哈希与存储元数据中的版本哈希不相等），协调器会检测到这一点，产生一个错误，并且 `addPersistentStoreWithType:configuration:URL:options:error:` 会返回 `NO`。你必须对这个错误进行妥善处理。
- 你的应用程序支持版本管理，并且你选择使用轻量级迁移或默认迁移过程

  你可以按照 [Lightweight Migration](Lightweight%20Migration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnbnknltc) 和 [The Default Migration Process](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnznknltg) 中所描述的方式使用 `addPersistentStoreWithType:configuration:URL:options:error:`。

  与不支持版本管理的方式相比，根本区别在于：你需要在选项字典中添加一个条目，其键为 [NSMigratePersistentStoresAutomaticallyOption](https://developer.apple.com/documentation/coredata/nsmigratepersistentstoresautomaticallyoption)、值为表示 `YES` 的 `NSNumber` 对象，以此指示协调器自动将存储迁移到当前模型版本。
- 你的应用程序支持版本管理，并且你选择使用自定义的版本偏差检测与迁移启动逻辑

  在打开存储之前，你可以使用 [isConfiguration:compatibleWithStoreMetadata:](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506940-isconfiguration) 来检查其模式是否与协调器的模型兼容：

  - 如果兼容，你可以直接使用 `addPersistentStoreWithType:configuration:URL:options:error:` 打开该存储；
  - 如果不兼容，你必须先迁移该存储，然后再打开它（同样使用 `addPersistentStoreWithType:configuration:URL:options:error:`）。

  你也可以简单地使用 [addPersistentStoreWithType:configuration:URL:options:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore) 来检查是否需要迁移，不过这是一个重量级操作，用于这个目的并不高效。

需要认识到有两个_正交_的概念：

1. 你可以在迁移过程中执行自定义代码。
2. 你可以为版本偏差检测和迁移启动编写自定义代码。

迁移策略类允许你以多种方式定制实体和属性的迁移，通常这些方式就足够满足你的需求。不过，你也可以使用自定义的偏差检测和迁移启动逻辑，从而掌控整个迁移过程。例如，如果你的存储非常大，你可以使用这两个数据模型建立一个迁移管理器，然后使用一系列映射模型将数据迁移到目标存储中（如果每次调用都使用相同的目标 URL，Core Data 会把新对象添加到已有的存储中）。这样一来，框架（以及你自己）就可以在转换过程中限制内存中数据的数量。

要打开一个存储并（在必要时）执行迁移，可以使用 [addPersistentStoreWithType:configuration:URL:options:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore)，并在选项字典中添加一个条目，其键为 [NSMigratePersistentStoresAutomaticallyOption](https://developer.apple.com/documentation/coredata/nsmigratepersistentstoresautomaticallyoption)、值为表示 `YES` 的 `NSNumber` 对象。你的代码看起来类似下面这样：

__清单 6-1__  使用自动迁移打开一个存储

```objc
NSError *error;
NSPersistentStoreCoordinator *psc = <#The coordinator#>;
NSURL *storeURL = <#The URL of a persistent store#>;
NSDictionary *optionsDictionary =
    [NSDictionary dictionaryWithObject:[NSNumber numberWithBool:YES]
                    forKey:NSMigratePersistentStoresAutomaticallyOption];

NSPersistentStore *store = [psc addPersistentStoreWithType:<#Store type#>
                                configuration:<#Configuration or nil#>
                                URL:storeURL
                                options:optionsDictionary
                                error:&error];
```

如果迁移顺利完成，`storeURL` 处原有的存储会在扩展名之前加上"~"后缀重命名，迁移后的存储则保存到 `storeURL`。

在 [addPersistentStoreWithType:configuration:URL:options:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore) 的实现中，Core Data 会执行以下操作：

1. 尝试寻找一个可用于打开该存储的托管对象模型。

   Core Data 会在你应用程序的资源中搜索模型，并逐一进行测试。如果找不到合适的模型，Core Data 会返回 `nil` 并给出相应的错误。
2. 尝试寻找一个映射模型，将现有存储的托管对象模型映射到持久化存储协调器所使用的模型。

   Core Data 会在你应用程序的资源中搜索可用的映射模型，并逐一进行测试。如果找不到合适的映射，Core Data 会返回 `NO` 并给出相应的错误。

   请注意，你必须已经创建好合适的映射模型，这一阶段才能成功。
3. 创建映射模型所需的迁移策略对象实例。

请注意，即使你使用默认迁移过程，仍然可以通过自定义迁移策略类来定制迁移本身。

[下一页](Customizing%20the%20Migration%20Process.md)[上一页](The%20Migration%20Process.md)
