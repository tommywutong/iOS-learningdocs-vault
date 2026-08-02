---
title: Core Data 模型版本管理与数据迁移编程指南
apple_id: TP40004399
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/vmCustomizing.html
archived_at: '2026-07-15T07:14:29.004069Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 模型版本管理与数据迁移编程指南](Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md)


[下一页](Migration%20and%20iCloud.md)[上一页](Initiating%20the%20Migration%20Process.md)

# 定制迁移过程

只有当你想自行发起迁移时，才需要定制迁移过程。例如，你可能想在应用程序主 bundle 之外的位置查找模型，或者想通过使用不同的映射模型分多轮执行迁移，来处理大型数据集（参见 [Multiple Passes—Dealing With Large Datasets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqobnknlts)）。

在发起迁移过程之前，应该先判断是否确实有必要迁移。你可以使用 `NSManagedObjectModel` 的 [isConfiguration:compatibleWithStoreMetadata:](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506940-isconfiguration) 方法进行检查，如[清单 7-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqobnknltg) 所示。

__清单 7-1__  检查是否需要迁移

```objc
NSPersistentStoreCoordinator *psc = /* get a coordinator */ ;
NSString *sourceStoreType = /* type for the source store, or nil if not known */ ;
NSURL *sourceStoreURL = /* URL for the source store */ ;
NSError *error = nil;

NSDictionary *sourceMetadata =
    [NSPersistentStoreCoordinator metadataForPersistentStoreOfType:sourceStoreType
                                  URL:sourceStoreURL
                                  error:&error];

if (sourceMetadata == nil) {
    // 处理错误
}

NSString *configuration = /* name of configuration, or nil */ ;
NSManagedObjectModel *destinationModel = [psc managedObjectModel];
BOOL pscCompatibile = [destinationModel
            isConfiguration:configuration
            compatibleWithStoreMetadata:sourceMetadata];

if (pscCompatibile) {
    // 无需迁移
}
```


你可以使用 [initWithSourceModel:destinationModel:](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417583-initwithsourcemodel) 来初始化一个迁移管理器；因此你首先需要找到该存储对应的合适模型。你可以使用 `NSManagedObjectModel` 的 [mergedModelFromBundles:forStoreMetadata:](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506788-mergedmodelfrombundles) 方法来获取该存储的模型。如果该方法返回了一个合适的模型，你就可以按照[清单 7-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqobnknltk) 所示的方式创建迁移管理器（这段代码是[清单 7-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqobnknltg) 的延续）。

__清单 7-2__  初始化一个迁移管理器

```objc
NSArray *bundlesForSourceModel = /* an array of bundles, or nil for the main bundle */ ;
NSManagedObjectModel *sourceModel =
    [NSManagedObjectModel mergedModelFromBundles:bundlesForSourceModel
                            forStoreMetadata:sourceMetadata];

if (sourceModel == nil) {
    // 处理错误
}

MyMigrationManager *migrationManager =
    [[MyMigrationManager alloc]
            initWithSourceModel:sourceModel
            destinationModel:destinationModel];
```


你可以使用 `NSMigrationManager` 的 [migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417584-migratestorefromurl) 方法来迁移一个存储。使用该方法需要准备好若干参数；其中大多数都很直接，唯一需要花点功夫的是找到合适的映射模型（可以使用 `NSMappingModel` 的 [mappingModelFromBundles:forSourceModel:destinationModel:](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506930-mappingmodelfrombundles) 方法来获取）。如[清单 7-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqobnknltm) 所示（这是[清单 7-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqobnknltk) 中示例的延续）。

__清单 7-3__  执行一次迁移

```objc
NSArray *bundlesForMappingModel = /* an array of bundles, or nil for the main bundle */ ;
NSError *error = nil;

NSMappingModel *mappingModel =
    [NSMappingModel
            mappingModelFromBundles:bundlesForMappingModel
            forSourceModel:sourceModel
            destinationModel:destinationModel];

if (mappingModel == nil) {
        // 处理错误
}

NSDictionary *sourceStoreOptions = /* options for the source store */ ;
NSURL *destinationStoreURL = /* URL for the destination store */ ;
NSString *destinationStoreType = /* type for the destination store */ ;
NSDictionary *destinationStoreOptions = /* options for the destination store */ ;

BOOL ok = [migrationManager migrateStoreFromURL:sourceStoreURL
                  type:sourceStoreType
                  options:sourceStoreOptions
                  withMappingModel:mappingModel
                  toDestinationURL:destinationStoreURL
                  destinationType:destinationStoreType
                  destinationOptions:destinationStoreOptions
                  error:&error];
```


上面展示的基本方式是让迁移管理器接收两个模型，然后遍历映射模型中提供的各个步骤（映射），将数据从一侧移动到另一侧。由于 Core Data 执行的是“三阶段”迁移——先创建全部数据，然后在第二阶段建立数据之间的关系——它必须维护“关联表”（用于记录目标存储中的哪个对象是源存储中哪个对象迁移而来的版本，反之亦然）。此外，由于它没有办法刷新（flush）正在使用的上下文，这意味着随着迁移的推进，迁移管理器中会累积大量对象。

为了解决这个问题，映射模型是作为 `migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:` 调用本身的参数传入的。这意味着，如果你能够（就映射而言）把对象图的各个部分分隔开，并分别创建到不同的映射模型中，你就可以执行以下操作：

1. 获取源数据模型和目标数据模型
2. 使用它们创建一个迁移管理器
3. 找到你所有的映射模型，并将它们放入一个数组（如有需要，可按特定顺序排列）
4. 遍历该数组，针对每个映射依次调用 `migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:`

这样你就可以每次只迁移一“块”数据，而不必一次性拉取全部数据。

从“跟踪/显示进度”的角度来看，这基本上只是多出了一层可供你利用的信息，因此你可以根据需要遍历的映射模型数量来确定完成百分比（进而再根据某个已处理模型中的实体映射数量做进一步细化）。

[下一页](Migration%20and%20iCloud.md)[上一页](Initiating%20the%20Migration%20Process.md)

