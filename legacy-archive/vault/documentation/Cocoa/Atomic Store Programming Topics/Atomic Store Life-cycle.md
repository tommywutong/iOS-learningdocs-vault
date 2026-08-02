---
title: 原子存储编程主题
apple_id: TP40004521
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AtomicStore_Concepts/Articles/asLifecycle.html
archived_at: '2026-07-15T05:25:48.179437Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [原子存储编程主题](Introduction%20to%20Atomic%20Store%20Programming%20Topics.md)


[下一页](Registering%20a%20Custom%20Store%20Type.md)[上一页](Atomic%20Store%20Fundamentals.md)

# 原子存储生命周期

本文介绍了原子存储的生命周期。阅读本文可以了解在什么时机会调用存储的哪些方法，以及存储应该如何响应这些调用。这有助于你理解如何实现一个自定义存储。

要在应用程序中使用自定义存储类型，你必须使用 [registerStoreClass:forStoreType:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468786-registerstoreclass) 方法向 `NSPersistentStoreCoordinator` 类注册该存储类型。更多细节请参阅[注册自定义存储类型](Registering%20a%20Custom%20Store%20Type.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgmbrfvjvomi)。

你可以使用 `NSPersistentStoreCoordinator` 的 [addPersistentStoreWithType:configuration:URL:options:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore) 方法创建给定类型的存储实例。你必须实现相应的方法，正确地初始化存储并加载其内容。

协调器会分配一个新的存储对象，并使用 [initWithPersistentStoreCoordinator:configurationName:URL:options:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388054-initwithpersistentstorecoordinat) 对其进行初始化。无论是新建的存储还是已存在的存储，都会调用这个方法；因此你在实现 `initWithPersistentStoreCoordinator:configurationName:URL:options:` 时，应检查给定 URL 处是否存在文件——如果不存在，就必须创建它。

你还必须初始化该存储的元数据。在调用 `initWithPersistentStoreCoordinator:configurationName:URL:options:` 之后，协调器会在新存储上调用 [metadata](https://developer.apple.com/documentation/coredata/nsatomicstore/1808737-metadata)；此时元数据必须是正确的。

存储初始化完成后，协调器会通过发送一条 [load:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388060-load) 消息，指示存储加载其数据。

`load:` 方法应从 `initWithPersistentStoreCoordinator:configurationName:URL:options:` 中为存储指定的 URL 处取回数据。`load:` 方法应解析存储的内容以提取持久化数据，并为每个元素创建一个引用数据对象——例如一个字典。

对于每一个要表示的对象，你的存储必须执行以下操作：

1. 使用 [objectIDForEntity:referenceObject:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388058-objectidforentity)，根据该节点的引用数据和实体类型创建一个托管对象 ID。

   缓存节点的对象 ID 同时也是表示该缓存节点的托管对象的对象 ID。
2. 使用 [initWithObjectID:](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/1506754-init) 创建一个缓存节点（`NSAtomicStoreCacheNode` 的实例）。

   存储必须为每个节点提供一个可变的属性缓存对象。
3. （可选）将对应的持久化数据推入该节点。

   如果你实现了延迟加载或其他行为，这一步可以省略。

   `NSAtomicStoreCacheNode` 的默认实现为属性存储提供了符合键值编码（KVC）规范的访问方式，因此在常见情况下你不需要创建 `NSAtomicStoreCacheNode` 的自定义子类。

在创建完所有节点之后，你需要使用 [addCacheNodes:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388062-addcachenodes) 将它们注册到存储中。

至此，缓存中已经注册了各个节点，框架也已准备就绪。Core Data 会处理所有的抓取请求，并根据底层缓存节点信息创建托管对象。

关于这一过程的更详细说明及示例，请参阅[初始化与加载数据](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmrxfvjvomy)。

`NSAtomicStore` 的任何子类都必须能够处理使用指向零长度文件的 URL 进行初始化的情况。这种情况表示需要在指定位置构建一个新的存储，从而使你能够在已知位置安全地创建预留文件（reservation file），随后再将其传递给 Core Data 用于构建存储。

你可以选择在 `initWithPersistentStoreCoordinator:configurationName:URL:options:` 或 `load:` 方法中创建零长度的预留文件。如果这样做，那么在存储被保存之前如果它从协调器中被移除，你必须删除该预留文件。

当托管对象上下文收到一条 `save:` 消息时，与之关联的存储必须（按此顺序）处理所有分配给它（该存储）的已插入、已更新和已删除对象，然后再将变更提交到外部数据仓库。

1. _新对象_

   对于上下文中每一个新插入的对象，存储会收到一条 [newReferenceObjectForManagedObject:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388050-newreferenceobjectformanagedobje) 消息。你的存储必须为该存储中的这个实例及其实体类型提供一个唯一且不变的值（参见[新引用对象](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmrxfvjvona)）。

   返回引用数据之后，存储会请求为这些对象各自使用 [newCacheNodeForManagedObject:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388052-newcachenodeformanagedobject) 创建一个新的缓存节点。

   `NSAtomicStore` 提供了一个在大多数情况下都够用的默认实现。但是，如果你想自定义缓存节点的创建方式或使用自定义的缓存节点，可以重写 [newCacheNodeForManagedObject:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388052-newcachenodeformanagedobject)。在你的实现中，应使用所传入托管对象的托管对象 ID 创建缓存节点，并将要持久化的值从托管对象推送到缓存节点中。然后使用 [addCacheNodes:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388062-addcachenodes) 将新节点注册到存储中。
2. _更新的对象_

   对于上下文中所有发生变更的对象，存储会收到一条 [updateCacheNode:fromManagedObject:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388044-updatecachenode) 消息。该方法的参数是一对缓存节点和托管对象（二者共享相同的对象 ID）。存储必须将持久化的值从托管对象推送到缓存节点中。
3. _删除的对象_

   你的存储会收到一个 [willRemoveCacheNodes:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388064-willremovecachenodes) 回调；如有必要，你可以重写该方法以断开任何强引用循环，确保已删除的对象能够被正确回收。
4. _保存变更_

   最后，存储会收到一条 [save:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388056-save) 消息，将变更提交到外部数据仓库。

   你的存储必须以其所使用的格式，将数据（各个缓存节点）以及元数据写入为该存储指定的 URL 处。

你实现的 [newReferenceObjectForManagedObject:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388050-newreferenceobjectformanagedobje) 必须为任意给定对象返回一个稳定（不变）的值。如果不这样做，"另存为"（Save As）和迁移操作将无法正确工作。

这意味着，只有当你将该值与该对象的其余数据一起保存时，才能使用任意数字、UUID 或其他随机值。如果你无法保存最初分配的引用对象，那么 `newReferenceObjectForManagedObject:` 就必须根据托管对象的值来推导出引用对象。由于这一约束是"另存为"和存储迁移操作所要求的，你也可以使用一个辅助表或内存中的数据结构，以确保新迁移的存储在加载其原子存储缓存节点时，使用的是当前托管对象上下文为已迁移托管对象所使用的相同 objectID。

如果某个存储要从协调器中移除，它会收到消息 [willRemoveFromPersistentStoreCoordinator:](https://developer.apple.com/documentation/coredata/nspersistentstore/1506731-willremovefrompersistentstorecoo)。在自定义的原子存储类中，你可以重写该方法以实现清理或其他行为。如果这样做，你在 `willRemoveFromPersistentStoreCoordinator:` 中的实现应调用父类的实现。

请注意，coordinator 参数在以下情况下可能为 `nil`：

- 在 load: 方法执行期间发生了错误，导致该存储无法被添加到协调器中
- 协调器正处于被释放（dealloc）的过程中

在这些情况下，会调用 `willRemoveFromPersistentStoreCoordinator:`，以便你执行任何必要的资源清理工作（例如移除预留文件——参见[零长度文件](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmrxfvjvomq)）。

[下一页](Registering%20a%20Custom%20Store%20Type.md)[上一页](Atomic%20Store%20Fundamentals.md)

