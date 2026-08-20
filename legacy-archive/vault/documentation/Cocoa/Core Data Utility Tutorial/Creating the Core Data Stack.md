---
title: Core Data 实用工具教程
apple_id: TP40001800
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataUtilityTutorial/Articles/05_createStack.html
archived_at: '2026-07-15T07:14:28.937406Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 实用工具教程](Introduction%20to%20Core%20Data%20Utility%20Tutorial.md)


[下一页](The%20Custom%20Managed%20Object%20Class.md)[上一页](The%20Application%20Log%20Directory.md)

# 创建 Core Data 技术栈

本章将向你展示如何创建并配置 Core Data 技术栈，从托管对象上下文一直到底层的持久化存储。

托管对象上下文负责管理一个托管对象的[对象图](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectGraph.html#//apple_ref/doc/uid/TP40008195-CH54)。管理持久化存储的任务则落在持久化存储协调器身上。它的职责是在托管对象上下文（一个或多个）与持久化存储（一个或多个）之间进行协调。它向上下文呈现一个外观（façade），把一组存储表示为一个单一的虚拟存储。在这个例子中，协调器只管理一个存储。

要添加一个存储，你使用 `NSPersistentStoreCoordinator` 的 `addPersistentStoreWithType:configuration:URL:options:error:` 方法。该方法返回一个表示新存储的对象（如果无法创建，则返回 `nil`）。你必须同时指定该存储在文件系统中的位置及其类型（本示例不使用模型配置）。在这个例子中使用的是 XML 存储——因为它相对易读的形式便于测试。文件的扩展名不是 `.xml`。你应该避免使用过于通用的文件扩展名——想想如果所有应用程序都使用同一个扩展名会发生什么……

`managedObjectContext` 函数返回一个已完全配置好的托管对象上下文。如有必要，它还会创建并配置 Core Data 技术栈的其余部分。

`managedObjectContext` 函数在 main 函数中被使用，但其实现放在 main 函数之后；因此你需要先为 `managedObjectContext` 函数提供一个前向声明。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)声明 managedObjectContext 函数

- 在主源文件的顶部、`main` 之前，添加该函数的声明。

```objc
NSManagedObjectContext *managedObjectContext();
```

下一步是声明并创建 `managedObjectContext` 函数的一个初步实现。该函数应判断托管对象上下文实例是否已经存在。如果已存在，直接返回它；如果不存在，则创建它，然后配置技术栈的其余部分。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)开始实现 managedObjectContext 函数

- 在主源文件中，开始实现 `managedObjectContext` 函数。

  在实现中，为该上下文声明一个 static 变量。如果该变量不为 `nil`，立即返回它。如果为 `nil`，则创建一个新的上下文，然后将其作为函数结果返回。

```objc
NSManagedObjectContext *managedObjectContext()
{
    static NSManagedObjectContext *moc = nil;
    if (moc != nil) {
        return moc;
    }

    // 实现继续……

    return moc;
}
```

接下来几步的代码，都应放在 return 语句之前（即注释"实现继续……"所在的位置）。

下一步是创建持久化存储协调器，并配置持久化存储。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)设置持久化存储协调器和存储

1. 创建一个持久化存储协调器。

   你可以使用 [initWithManagedObjectModel:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468895-init) 来初始化一个持久化存储协调器。该模型指定了协调器可能要管理的存储的模式（schema）。你可以使用 [setPersistentStoreCoordinator:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506618-persistentstorecoordinator) 告诉托管对象上下文应该使用哪个持久化存储协调器。

```objc
NSPersistentStoreCoordinator *coordinator =
    [[NSPersistentStoreCoordinator alloc]
        initWithManagedObjectModel:managedObjectModel()];
```
2. 创建一个合适类型的新持久化存储。

   你使用 [addPersistentStoreWithType:configuration:URL:options:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore) 向持久化存储协调器添加一个存储。使用这个方法可以指定：

   - 存储的类型（例如 XML 或 SQLite）。
   - 要使用持久化存储协调器托管对象模型中的哪个配置。

     在这个简单的示例中，没有任何配置。
   - 该存储的 URL。
   - 存储选项，例如——如果该存储已经存在——是否应更新为使用新模型。

     将存储更新为使用模型的新版本，称为迁移——参见 _[Core Data Model Versioning and Data Migration Programming Guide](../Core%20Data%20Model%20Versioning%20and%20Data%20Migration%20Programming%20Guide/Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojz)_。

     在这个简单的示例中，不指定任何选项。
   - 一个指向错误对象的指针。

   该方法返回新的存储；如果无法创建，则返回 `nil`。如果由于某种原因无法创建存储，记录一条合适的警告。

```objc
NSString *STORE_TYPE = NSXMLStoreType;
NSString *STORE_FILENAME = @"CDCLI.cdcli";

NSError *error;
NSURL *url = [applicationLogDirectory() URLByAppendingPathComponent:STORE_FILENAME];

NSPersistentStore *newStore = [coordinator addPersistentStoreWithType:STORE_TYPE
                                           configuration:nil
                                           URL:url
                                           options:nil
                                           error:&error];

if (newStore == nil) {
    NSLog(@"Store Configuration Failure\n%@",
        ([error localizedDescription] != nil) ?
        [error localizedDescription] : @"Unknown Error");
}
```

最后，创建上下文，并将其与持久化存储协调器关联起来。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)创建托管对象上下文

1. 创建该上下文。

   在创建一个上下文时（使用 [initWithConcurrencyType:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506709-init)），你需要指定其并发类型；并发类型告诉该上下文它应该运行在哪个进程队列上。为确保该上下文只会在主队列上使用，指定 [NSMainQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsmainqueueconcurrencytype)

```objc
moc = [[NSManagedObjectContext alloc] initWithConcurrencyType:NSMainQueueConcurrencyType];
```
2. 将持久化存储协调器与该上下文关联起来。

```objc
[moc setPersistentStoreCoordinator:coordinator];
```


为了能够测试目前为止的实现，实例化该托管对象上下文。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)测试目前为止的实现

1. 实例化托管对象上下文。

   在 `main` 函数中，在记录托管对象模型描述的那一行之后，声明一个 `NSManagedObjectContext` 类型的变量，并将其值赋为调用 `managedObjectContext` 函数的结果。

```objc
NSManagedObjectContext *moc = managedObjectContext();
```
2. 构建并运行该项目。

   该项目应该能够无错误地编译通过，不过你会收到一条警告，提示 `main` 函数中的变量 `moc` 未被使用。运行该工具时，`managedObjectContext` 函数不应记录任何错误。

`managedObjectContext` 函数的完整清单如清单 4-1 所示。

__清单 4-1__  `managedObjectContext` 函数的完整清单

```objc
NSManagedObjectContext *managedObjectContext()
{
    static NSManagedObjectContext *moc = nil;

    if (moc != nil) {
        return moc;
    }

    NSPersistentStoreCoordinator *coordinator =
        [[NSPersistentStoreCoordinator alloc]
            initWithManagedObjectModel: managedObjectModel()];

    NSString *STORE_TYPE = NSXMLStoreType;
    NSString *STORE_FILENAME = @"CDCLI.cdcli";

    NSError *error;
    NSURL *url = [applicationLogDirectory() URLByAppendingPathComponent:STORE_FILENAME];

    NSPersistentStore *newStore = [coordinator addPersistentStoreWithType:STORE_TYPE
                                               configuration:nil URL:url options:nil
                                               error:&error];

    if (newStore == nil) {

        NSLog(@"Store Configuration Failure\n%@",
              ([error localizedDescription] != nil) ?
              [error localizedDescription] : @"Unknown Error");
    }


    moc = [[NSManagedObjectContext alloc] initWithConcurrencyType:NSMainQueueConcurrencyType];
    [moc setPersistentStoreCoordinator:coordinator];

    return moc;
}
```

[下一页](The%20Custom%20Managed%20Object%20Class.md)[上一页](The%20Application%20Log%20Directory.md)
