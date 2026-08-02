---
title: 集合编程主题
apple_id: 10000034i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/Sets.html
archived_at: '2026-07-15T07:13:35.317724Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [集合编程主题](About%20Collections.md)


[下一页](Index%20Sets-%20Storing%20Indexes%20into%20an%20Array.md)[上一页](Dictionaries-%20Collections%20of%20Keys%20and%20Values.md)

# 集（Set）：对象的无序集合

如图 1 所示，集（set）是对象的无序集合。当元素的顺序不重要、而测试某个对象是否在集中的性能很重要时，你可以使用集来替代数组。尽管数组是有序的，但测试其中是否包含某个成员的速度比测试集要慢。

__图 1__  集示例

!

`NSSet` 对象管理一个由互不相同的对象组成的不可变集——也就是说，一旦[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)了该集，就不能添加、移除或替换其中的对象。不过，你仍然可以修改这些对象本身（如果它们支持修改）。集合本身的可变性并不影响其中对象的可变性。如果一个集很少变化，或者是整体性地变化，你应该使用不可变集。

`NSMutableSet` 是 `NSSet` 的子类，是一个由互不相同的对象组成的[可变](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)集，允许随时添加和删除条目，并按需自动分配内存。如果一个集是逐步变化的，或者非常大——因为大型集合的[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)需要更多时间——你应该使用可变集。

`NSCountedSet` 是 `NSMutableSet` 的子类，是一个可变集，你可以向其中多次添加同一个特定对象；换句话说，该集中的元素不一定互不相同。计数集（counted set）也被称为 _bag_。该集会为插入的每个不同对象维护一个关联计数器。`NSCountedSet` 对象会记录对象被插入的次数，并要求对象被移除相同的次数才能将其从集中完全移除。因此，即使某个对象被添加了多次，计数集中也只会有该对象的一个实例。[countForObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/countForObject:) 方法会返回指定对象被添加到该集中的次数。

集中的对象必须响应 `NSObject` 协议的 `hash` 和 `isEqual:` 方法（更多信息请参阅 [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject)）。如果集中存储了可变对象，那么要么这些对象的 `hash` 方法不应依赖于该可变对象的内部状态，要么这些可变对象在集中时不应被修改。例如，一个可变字典可以被放入集中，但在其位于集中期间不能对其进行修改。（请注意，有时很难判断某个对象是否在某个集合中。）

`NSSet` 提供了若干[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)方法，例如 [setWithObjects:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObjects:) 和 [initWithArray:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithArray:)，它们会返回一个包含你作为参数传入的元素（如果有的话）的 `NSSet` 对象。添加到集中的对象不会被[拷贝](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCopying.html#//apple_ref/doc/uid/TP40008195-CH38)（除非你向 [initWithSet:copyItems:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithSet:copyItems:) 传入 `YES` 作为参数）。相反，加入集中的是对该对象的一个强引用。关于拷贝和内存管理的更多信息，请参阅 [Copying Collections](Copying%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnrsfvjvomi)。

如果你希望确保没有对象被表示多次，并且多次添加同一个对象不会产生额外效果，那么除 `NSCountedSet` 外的集是首选的集合类型。

你可以使用 `NSSet` 提供的任意初始化方法来创建 `NSMutableSet` 对象。你也可以使用 [setWithSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithSet:) 或 [initWithSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithSet:) 从一个 `NSSet` 实例创建 `NSMutableSet` 对象（反之亦然）。

`NSMutableSet` 类提供了用于向集中添加对象的方法：

- `addObject:` 向集中添加单个对象。
- `addObjectsFromArray:` 将指定数组中的所有对象添加到集中。
- `unionSet:` 将另一个集中尚不存在于当前集中的所有对象添加进来。

`NSMutableSet` 类还提供了以下用于从集中移除对象的方法：

- `intersectSet:` 移除所有不在另一个集中的对象。
- `removeAllObjects` 移除集中的所有对象。
- `removeObject:` 从集中移除某个特定对象。
- `minusSet:` 移除所有存在于另一个集中的对象。

由于 `NSCountedSet` 是 `NSMutableSet` 的子类，它继承了上述所有方法。不过，其中一些方法在 `NSCountedSet` 上的行为略有不同。例如：

- `unionSet:` 会添加另一个集中的所有对象，即使这些对象已经存在。
- `intersectSet:` 会移除所有不在另一个集中的对象。如果同一个对象在两个集中都存在多个实例，结果集中该对象出现的次数，等于实例数较少的那个集中该对象出现的次数。
- `minusSet:` 会移除所有存在于另一个集中的对象。如果某个对象在计数集中存在多个实例，该方法只会移除其中一个实例。

`NSSet` 类提供了用于查询集中元素的方法：

- `allObjects` 返回一个包含该集中所有对象的数组。
- `anyObject` 返回该集中的某个对象。（该对象是按方便原则选取的，_并非_随机选取。）
- `count` 返回当前集中对象的数量。
- `member:` 返回集中与指定对象相等的那个对象。
- `intersectsSet:` 测试两个集是否至少共享一个对象。
- `isEqualToSet:` 测试两个集是否相等。
- `isSubsetOfSet:` 测试该集所包含的全部对象是否也都存在于另一个集中。

`NSSet` 的 `objectEnumerator` 方法让你可以逐个遍历集中的元素。而 `makeObjectsPerformSelector:` 和 `makeObjectsPerformSelector:withObject:` 方法则用于向集中的各个对象发送[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)。在大多数情况下，应优先使用快速枚举，因为它比使用 `NSEnumerator` 或 `makeObjectsPerformSelector:` 方法更快、也更灵活。关于枚举的更多内容，请参阅 [Enumeration: Traversing a Collection's Elements](Enumeration-%20Traversing%20a%20Collection%E2%80%99s%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgeztklkcijbumqkcinba)。

`NSHashTable` 类在默认配置下持有对象的方式与 `NSMutableSet` 大致相同。它还提供了额外的存储选项，可以针对特定情况进行定制，例如当你需要更高级的[内存管理](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)选项，或者想持有特定类型的指针时。例如，图 2 中的映射表被配置为对其元素持有弱引用。你还可以指定是否要拷贝加入该集的对象。

__图 2__  哈希表对象所有权

!

当你想要一个使用弱引用的无序元素集合时，可以使用 `NSHashTable` 对象。例如，假设你有一个包含若干对象的全局哈希表。由于全局对象永远不会被回收，除非它们被弱持有，否则其内容都无法被释放。被配置为弱持有对象的哈希表并不拥有其内容。如果这样的哈希表中的对象没有任何强引用，这些对象就会被释放。例如，[图 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgeztmlktk43q) 中的哈希表对其内容持有弱引用。对象 A、C 和 Z 将被释放，而其余对象则会保留下来。

要创建一个哈希表，可以使用 [initWithOptions:capacity:](https://developer.apple.com/documentation/foundation/nshashtable/1411066-init) 方法及相应的指针函数选项对其进行初始化。也可以改用 [initWithPointerFunctions:capacity:](https://developer.apple.com/documentation/foundation/nshashtable/1416331-initwithpointerfunctions) 方法，配合相应的 [NSPointerFunctions](https://developer.apple.com/documentation/foundation/nspointerfunctions) 实例进行初始化。关于各种指针函数选项的更多信息，请参阅 [Pointer Function Options](Pointer%20Function%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcojzfvjvomi)。

`NSHashTable` 类还定义了便捷构造方法 [hashTableWithWeakObjects](https://developer.apple.com/documentation/foundation/nshashtable/1591430-hashtablewithweakobjects)，用于创建一个对其内容持有弱引用的哈希表。它只应在你存储对象时使用。

要将哈希表配置为使用任意指针，需要同时使用 `NSPointerFunctionsOpaqueMemory` 和 `NSPointerFunctionsOpaquePersonality` 选项对其进行初始化。当使用哈希表来容纳任意指针时，应使用针对 `void *` 指针的 C 函数 API。更多信息请参阅 Hash Tables。例如，你可以按照清单 1 所示的方式，添加一个指向 `int` 值的指针。

__清单 1__  配置为容纳非对象指针的哈希表

```objc
NSHashTable *hashTable=[[NSHashTable alloc] initWithOptions:
    NSPointerFunctionsOpaqueMemory |NSPointerFunctionsOpaquePersonality
    capacity: 1];

NSHashInsert(hashTable, someIntPtr);
```

当配置为使用任意指针时，哈希表会带有与使用指针相关的风险。例如，如果这些指针指向某个函数内基于栈创建的数据，那么即使该哈希表本身有效，这些指针在该函数之外也是无效的。尝试访问它们会导致未定义行为。

[下一页](Index%20Sets-%20Storing%20Indexes%20into%20an%20Array.md)[上一页](Dictionaries-%20Collections%20of%20Keys%20and%20Values.md)
