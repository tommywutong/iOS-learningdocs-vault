---
title: 原子存储编程主题
apple_id: TP40004521
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AtomicStore_Concepts/Articles/asRegistration.html
archived_at: '2026-07-15T05:25:48.203643Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [原子存储编程主题](Introduction%20to%20Atomic%20Store%20Programming%20Topics.md)


[下一页](Initializing%20a%20Store%20and%20Loading%20Data.md)[上一页](Atomic%20Store%20Life-cycle.md)

# 注册自定义存储类型

要在应用程序中使用自定义存储类型，你必须使用 [registerStoreClass:forStoreType:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468786-registerstoreclass) 方法向 `NSPersistentStoreCoordinator` 类注册该存储类型。类型名必须是一个唯一的字符串。

通常你会将存储类型定义为一个字符串常量：

```objc
// in MyAtomicStore.h
extern NSString *MY_ATOMIC_STORE_TYPE;

// in MyAtomicStore.m
NSString *MY_ATOMIC_STORE_TYPE = @"MyAtomicStore";
```

你应该确保在尝试向持久化存储协调器添加某个类型的存储之前，该类型已经完成注册。例如，在 OS X 的应用程序委托中，你可以在 [applicationWillFinishLaunching:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428623-applicationwillfinishlaunching) 中进行注册。

```objc
- (void)applicationWillFinishLaunching:(NSNotification *)aNotification
{
    [NSPersistentStoreCoordinator registerStoreClass:[MyAtomicStore class]
                                     forStoreType:MY_ATOMIC_STORE_TYPE];
}
```

在基于文档的应用程序中，该类型就是 `NSPersistentDocument` 用来将持久化存储类型与文档类型相关联的标识符（参见 [persistentStoreTypeForFileType:](https://developer.apple.com/documentation/appkit/nspersistentdocument/1396168-persistentstoretypeforfiletype)）。

[下一页](Initializing%20a%20Store%20and%20Loading%20Data.md)[上一页](Atomic%20Store%20Life-cycle.md)

