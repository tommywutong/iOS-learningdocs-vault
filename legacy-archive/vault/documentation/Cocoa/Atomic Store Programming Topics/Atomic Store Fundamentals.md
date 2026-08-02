---
title: 原子存储编程主题
apple_id: TP40004521
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AtomicStore_Concepts/Articles/asFundamentals.html
archived_at: '2026-07-15T05:25:48.171699Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [原子存储编程主题](Introduction%20to%20Atomic%20Store%20Programming%20Topics.md)


[下一页](Atomic%20Store%20Life-cycle.md)[上一页](Introduction%20to%20Atomic%20Store%20Programming%20Topics.md)

# 原子存储基础

本文介绍了原子存储所依托的基本概念。

Core Data 提供了四种原生的持久化存储类型：

- SQLite
- Binary
- XML
- In-Memory

这些存储类型各有不同的优缺点，具体描述见《Persistent Store Features》。Binary 存储和 XML 存储是"原子"（atomic）存储——它们必须被整体读取和写入，这一点与 SQLite 存储不同，后者可以按记录进行零散的局部修改。

Core Data 管理着与这些存储的所有交互，负责在托管对象上下文与存储之间转换托管对象的插入、删除和更新操作。Core Data 同时也管理着文件格式。

原子存储 API 允许你为数据创建自定义的存储格式，并使用标准的 Core Data API 与数据进行交互。这使你既能够在应用程序中利用 Core Data，又能够沿用某种既有的（也许是历史遗留的）文件格式，或者定义一种可供不使用 Core Data 的外部应用程序使用的新文件格式。例如，你可以创建一种"通用"存储类型，比如用于 HTML 或逗号分隔值（CSV）的格式，或者用于与第三方集成的其他中间格式。不过需要注意的是，原子存储 API 并不支持与客户端-服务器关系型数据库或类似的基于 SQL 的存储进行集成。

如果你实现了自定义存储类型，它通常会与描述该存储所编码的模式（schema）的特定托管对象模型相关联。

实现自定义存储时会用到三个类：

- [NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstore)

  这是所有 Core Data 存储的抽象基类。
- [NSAtomicStore](https://developer.apple.com/documentation/coredata/nsatomicstore)

  这是 `NSPersistentStore` 的子类。
- [NSAtomicStoreCacheNode](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode)

  这是一个具体类，为存储中的"节点"提供了基本的表示形式。

在这三个类中，你唯一需要子类化的是 `NSAtomicStore`。它是一个抽象超类，供你通过子类化来创建原子存储，并提供了一些实用方法的默认实现。你不能直接子类化 `NSPersistentStore`。如有必要，你可以子类化 `NSAtomicStoreCacheNode` 以提供特殊行为。

[NSAtomicStore](https://developer.apple.com/documentation/coredata/nsatomicstore) 是 [NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstore) 的子类。这两个类都要求你实现若干方法。

在 `NSPersistentStore` 的子类中，你必须重写以下方法：

|  |  |
| --- | --- |
| [type](https://developer.apple.com/documentation/coredata/nspersistentstore/1506250-type) |  |
| [identifier](https://developer.apple.com/documentation/coredata/nspersistentstore/1506215-identifier) |  |
| [metadata](https://developer.apple.com/documentation/coredata/nspersistentstore/1506564-metadata) |  |
| [metadataForPersistentStoreWithURL:error:](https://developer.apple.com/documentation/coredata/nspersistentstore/1506741-metadataforpersistentstore) |  |

在 `NSAtomicStore` 的子类中，你必须重写以下方法：

|  |  |
| --- | --- |
| [load:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388060-load) |  |
| [newCacheNodeForManagedObject:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388052-newcachenodeformanagedobject) |  |
| [newReferenceObjectForManagedObject:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388050-newreferenceobjectformanagedobje) |  |
| [save:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388056-save) |  |
| [updateCacheNode:fromManagedObject:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388044-updatecachenode) |  |

[下一页](Atomic%20Store%20Life-cycle.md)[上一页](Introduction%20to%20Atomic%20Store%20Programming%20Topics.md)

