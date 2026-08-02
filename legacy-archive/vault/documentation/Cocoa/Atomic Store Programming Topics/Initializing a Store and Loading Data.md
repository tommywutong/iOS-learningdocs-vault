---
title: 原子存储编程主题
apple_id: TP40004521
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AtomicStore_Concepts/Articles/asLoading.html
archived_at: '2026-07-15T05:25:48.189382Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [原子存储编程主题](Introduction%20to%20Atomic%20Store%20Programming%20Topics.md)


[下一页](Document%20Revision%20History.md)[上一页](Registering%20a%20Custom%20Store%20Type.md)

# 初始化存储并加载数据

本文详细介绍了如何初始化持久化存储，以及如何从 URL 加载数据。

当你将一个存储添加到持久化存储协调器时，该存储会通过 [initWithPersistentStoreCoordinator:configurationName:URL:options:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388054-initwithpersistentstorecoordinat) 方法进行初始化。存储初始化完成后，会收到持久化存储协调器通过 [load:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388060-load) 方法发出的加载数据请求。

你不一定需要实现 `initWithPersistentStoreCoordinator:configurationName:URL:options:`——在某些情况下，默认实现已经足够。但如果你确实需要提供额外的初始化逻辑，需要注意 `initWithPersistentStoreCoordinator:configurationName:URL:options:` 既会在已有存储时被调用，也会在新建存储时被调用。

你对 `initWithPersistentStoreCoordinator:configurationName:URL:options:` 的实现必须能够处理传入 `nil` URL，以及指向一个零长度文件的 URL 这两种情况。后者用于表示需要在指定位置构建一个新的存储，这也让你可以安全地在已知位置预先创建占位文件，然后再将其传给 Core Data 用于构建存储。

`load:` 方法负责从存储所指定的 URL 中获取数据，并创建所需的对象。对于存储中的每个元素，你都必须创建：

- 一个包含该元素数据的引用数据对象
- 一个托管对象 ID
- 一个原子存储缓存节点

创建好所有节点后，使用 [addCacheNodes:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388062-addcachenodes) 将它们注册到存储中。

举个例子，假设有一个包含以下内容的存储：

```
Person,Robert,Tibbot,86349382003
Person,Jeff,Hancock,5987749473
Person,Derek,Benson,7987082467
Person,George,Andronov,7987082467
```


引用数据对象只是存储中数据的一种对象化表示。例如，你可以为每个 Person 创建一个 `NSMutableDictionary` 对象：

```
{ firstName = @"Robert", lastName = @"Tibbot", id = 86349382003 }
{ firstName = @"Jeff", lastName = @"Hancock" id = 5987749473 }
{ firstName = @"Derek", lastName = @"Benson" id = 7987082467 }
{ firstName = @"George", lastName = @"Andronov" id = 3492475026 }
```


你可以使用 [objectIDForEntity:referenceObject:](https://developer.apple.com/documentation/coredata/nsatomicstore/1388058-objectidforentity) 方法创建托管对象 ID，传入节点的实体和键数据。你可以从该存储所属持久化存储协调器关联的托管对象模型中获取实体，例如：

```
NSEntityDescription *personEntity =
    [[[[self persistentStoreCoordinator] managedObjectModel]
        entitiesByName] objectForKey:@"Person"];
NSManagedObjectID *moID =
    [self objectIDForEntity:personEntity referenceObject:[personDictionary objectForKey: @"id"]];
```

缓存节点的对象 ID，同时也是表示该缓存节点的托管对象的对象 ID。键信息不必编码在引用值中，但它必须在该存储中持久化的实体实例集合中保持唯一，并且是可重复推导得出的。

你可以使用 `NSAtomicStoreCacheNode` 的 [initWithObjectID:](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/1506754-init) 方法创建缓存节点。

```
NSAtomicStoreCacheNode *personNode =
                [[NSAtomicStoreCacheNode alloc] initWithObjectID:moID];
```

创建每个节点后，你通常会把对应的持久化数据推送到该节点中（不过你也可以实现惰性加载或其他行为）。

缓存节点使用一个可变字典作为其底层存储。如果你在解析数据时为每个元素创建了 `NSMutableDictionary` 实例，且字典中的键就是对应实体的属性名，那么你可以直接设置缓存节点：

```
[personNode setPropertyCache:personDictionary];
```

缓存节点中的值必须满足：

- 对于属性值，必须是 Core Data 支持的某种属性类型的实例（参见 [NSAttributeDescription](https://developer.apple.com/documentation/coredata/nsattributedescription)）；
- 对于一对一关系，必须是另一个缓存节点实例；
- 对于一对多关系，必须是相关缓存节点组成的集合。

假设有一个包含以下内容的存储：

```
Person::first:Robert:last:Tibbot:id:86349382003
Person::first:Jeff:last:Hancock:id:5987749473
Person::first:Derek:last:Benson:id:7987082467
Person::first:George:last:Andronov:id:7987082467
```

`load:` 方法可能会先解析文件，为每个 Person 创建一个 `NSMutableDictionary` 对象：

```
{ firstName = @"Robert", lastName = @"Tibbot", id = 86349382003 }
{ firstName = @"Jeff", lastName = @"Hancock", id = 5987749473 }
{ firstName = @"Derek", lastName = @"Benson", id = 7987082467 }
{ firstName = @"George", lastName = @"Andronov", id = 3492475026 }
```

并将它们收集到一个数组 `personDictionaries` 中。在这个例子中，字典所使用的键与 Person 实体的属性名相同。

接下来你可以按如下方式创建 Core Data 对象：

```objc
NSEntityDescription *personEntity =
    [[[[self persistentStoreCoordinator] managedObjectModel]
        entitiesByName] objectForKey:@"Person"];

NSMutableSet *cacheNodes = [NSMutableSet set];

NSDictionary *objectData;
id referenceObject;
NSManagedObjectID *moID;
NSAtomicStoreCacheNode *personNode;

for (NSMutableDictionary *personDictionary in personDictionaries) {

    objectData = [personDictionary mutableCopy];
    // 托管对象本身不应把标识符的值存储为一个属性。
    referenceObject = [personDictionary valueForKey:@"id"];
    [objectData removeObjectForKey: @"id"];
    moID = [self objectIDForEntity:personEntity
                                referenceObject:referenceObject];

    personNode = [[NSAtomicStoreCacheNode alloc] initWithObjectID:moID];
    [personNode setPropertyCache:objectData];
    [cacheNodes addObject:personNode];
}

[self addCacheNodes:cacheNodes];
```

[下一页](Document%20Revision%20History.md)[上一页](Registering%20a%20Custom%20Store%20Type.md)
