---
title: Core Data 模型版本管理与数据迁移编程指南
apple_id: TP40004399
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/vmLightweightMigration.html
archived_at: '2026-07-15T07:14:29.021831Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 模型版本管理与数据迁移编程指南](Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md)


[下一页](Mapping%20Overview.md)[上一页](Model%20File%20Format%20and%20Versions.md)

# 轻量级迁移

如果你只是对模型做了一些简单的改动（例如为某个实体新增一个属性），Core Data 可以自动执行数据迁移，这称为_轻量级迁移_。轻量级迁移在本质上与普通迁移相同，区别只在于：你不需要提供映射模型（如 [Mapping Overview](Mapping%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnjnknltc) 中所述），而是由 Core Data 根据源、目标托管对象模型之间的差异自行推断出一个映射模型。

轻量级迁移在应用程序开发的早期阶段尤其方便，因为这个阶段你可能会频繁修改托管对象模型，但又不想每次都重新生成测试数据。你可以迁移现有数据，而不必为每个曾用于创建某个需要迁移的存储的模型版本，都创建一个自定义映射模型。

使用轻量级迁移的另一个优势——除了你不需要自己创建映射模型之外——是：如果你使用推断出的模型，并且使用的是 SQLite 存储，那么 Core Data 可以就地执行迁移（仅通过发出 SQL 语句）。由于 Core Data 不需要加载你的任何数据，这可以带来显著的性能提升。因此，即使你自己创建的映射模型会非常简单，也建议尽可能使用推断式迁移。

要执行自动轻量级迁移，Core Data 需要能够在运行时自行找到源和目标托管对象模型。Core Data 会在 [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) 的 `allBundles` 和 `allFrameworks` 方法所返回的 bundle 中查找模型。如果你把模型存放在其他位置，就必须遵循 [Use a Migration Manager if Models Cannot Be Found Automatically](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnbnknltg) 中描述的步骤。之后 Core Data 必须分析持久化实体和属性的模式变化，并生成一个推断出的映射模型。

要让 Core Data 能够生成推断出的映射模型，模型的变化必须符合一种明显的迁移模式，例如：

- 简单地新增一个属性
- 移除一个属性
- 将一个非可选属性改为可选
- 将一个可选属性改为非可选，_并同时定义一个默认值_
- 重命名一个实体或属性

如果你重命名了一个实体或属性，可以将目标模型中该实体或属性的重命名标识符（renaming identifier），设置为源模型中对应属性或实体的名称。你可以使用 Xcode 数据建模工具的属性检查器（针对实体或属性均可），在托管对象模型中设置重命名标识符。例如，你可以：

- 将 Car 实体重命名为 Automobile
- 将 Car 的 `color` 属性重命名为 `paintColor`

重命名标识符创建的是一个"规范名称"，因此你应该将重命名标识符设置为源模型中该属性的名称（除非该属性已经有了一个重命名标识符）。这意味着，你可以在模型的第 2 版中重命名一个属性，然后在第 3 版中再次重命名它，无论是从第 2 版迁移到第 3 版，还是从第 1 版迁移到第 3 版，重命名都能正确生效。

此外，Core Data 还支持：

- 添加关系以及更改关系的类型

  - 你可以添加一个新关系，或删除一个已有关系。
  - 重命名一个关系（使用重命名标识符，与属性的方式相同）
  - 将一个一对一关系改为一对多，或将无序的一对多改为有序（反之亦然）
- 更改实体层级结构

  - 你可以添加、移除、重命名实体
  - 你可以创建新的父实体或子实体，并在实体层级结构中上下移动属性
  - 你可以将实体移出某个层级结构

    但是你_不能_合并实体层级结构；如果两个已有实体在源模型中没有共同的父实体，那么它们在目标模型中也不能拥有共同的父实体

你可以通过传给 [addPersistentStoreWithType:configuration:URL:options:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore) 的选项字典，将 [NSMigratePersistentStoresAutomaticallyOption](https://developer.apple.com/documentation/coredata/nsmigratepersistentstoresautomaticallyoption) 和 [NSInferMappingModelAutomaticallyOption](https://developer.apple.com/documentation/coredata/nsinfermappingmodelautomaticallyoption) 这两个键对应的值都设为 `YES`，来请求自动轻量级迁移：

```objc
NSError *error = nil;
NSURL *storeURL = <#The URL of a persistent store#>;
NSPersistentStoreCoordinator *psc = <#The coordinator#>;
NSDictionary *options = [NSDictionary dictionaryWithObjectsAndKeys:
    [NSNumber numberWithBool:YES], NSMigratePersistentStoresAutomaticallyOption,
    [NSNumber numberWithBool:YES], NSInferMappingModelAutomaticallyOption, nil];

BOOL success = [psc addPersistentStoreWithType:<#Store type#>
                    configuration:<#Configuration or nil#> URL:storeURL
                    options:options error:&error];
if (!success) {
    // 处理错误。
}
```

如果你想提前判断 Core Data 能否推断出源模型和目标模型之间的映射，而不实际执行迁移操作，可以使用 [NSMappingModel](https://developer.apple.com/documentation/coredata/nsmappingmodel) 的 [inferredMappingModelForSourceModel:destinationModel:error:](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506468-inferredmappingmodel) 方法。如果 Core Data 能够创建该推断模型，该方法会返回该模型，否则返回 `nil`。

要执行自动迁移，Core Data 必须能够在运行时自行找到源和目标托管对象模型（参见 [Core Data Must Be Able to Infer the Mapping](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnbnknlte)）。如果你需要把模型放在自动发现机制无法检查到的位置，就需要自己生成推断模型，并使用迁移管理器（`NSMigrationManager` 的实例）来启动迁移。

以下代码示例演示了如何生成推断模型，并使用迁移管理器启动迁移。该代码假设你已经实现了两个方法——`sourceModel` 和 `destinationModel`——分别返回源和目标托管对象模型。

```objc
- (BOOL)migrateStore:(NSURL *)storeURL toVersionTwoStore:(NSURL *)dstStoreURL error:(NSError **)outError {

    // 尝试获取一个推断出的映射模型。
    NSMappingModel *mappingModel =
        [NSMappingModel inferredMappingModelForSourceModel:[self sourceModel]
                        destinationModel:[self destinationModel] error:outError];

    // 如果 Core Data 无法创建推断映射模型，返回 NO。
    if (!mappingModel) {
        return NO;
    }

    // 创建一个迁移管理器来执行迁移。
    NSMigrationManager *manager = [[NSMigrationManager alloc]
        initWithSourceModel:[self sourceModel] destinationModel:[self destinationModel]];

    BOOL success = [manager migrateStoreFromURL:storeURL type:NSSQLiteStoreType
        options:nil withMappingModel:mappingModel toDestinationURL:dstStoreURL
        destinationType:NSSQLiteStoreType destinationOptions:nil error:outError];

    return success;
}
```

[下一页](Mapping%20Overview.md)[上一页](Model%20File%20Format%20and%20Versions.md)
