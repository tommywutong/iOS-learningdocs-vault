---
title: 集合编程主题
apple_id: 10000034i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/Dictionaries.html
archived_at: '2026-07-15T07:13:32.300972Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [集合编程主题](About%20Collections.md)


[下一页](Sets-%20Unordered%20Collections%20of%20Objects.md)[上一页](Arrays-%20Ordered%20Collections.md)

# 字典：键值集合

字典用于管理键值对。字典中的一个键值对被称为一个条目（entry）。每个条目由代表键的一个对象，和作为该键对应值的第二个对象组成。在一个字典内部，各个键是唯一的——也就是说，同一个字典中不会有两个相等的键（由 `isEqual:` 判定）。任何实现了 `NSCopying` 协议、并实现了 `hash` 和 `isEqual:` 方法的对象都可以作为键。图 1 展示了一个包含某个假想人物信息的字典。如图所示，字典中的值可以是任意对象，甚至可以是另一个集合。

__图 1__  字典示例

!

`NSDictionary` 对象管理的是一个不可变字典——也就是说，创建字典之后，你不能添加、移除或替换其中的键和值。不过，你可以修改各个值本身（如果它们支持修改的话），但键本身不能被修改。集合的可变性不会影响集合内部对象的可变性。如果字典很少发生变化，或者只是整体替换，就应该使用不可变字典。

`NSMutableDictionary` 对象管理的是一个[可变](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)字典，允许在任何时候添加和删除条目，并按需自动分配内存。如果字典是逐步变化的，或者字典非常大——因为大型集合的[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)需要更多时间——就应该使用可变字典。

你可以使用初始化方法 `initWithDictionary:` 或便捷构造方法 `dictionaryWithDictionary:`，轻松地[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一种类型字典对应的另一种类型实例。

一般来说，你可以通过向 `NSDictionary` 或 `NSMutableDictionary` 类发送某个 `dictionary...` [消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)来实例化一个字典。`dictionary...` 消息会返回一个包含你以参数形式传入的键和值的字典。作为值加入字典的对象不会被[复制](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCopying.html#//apple_ref/doc/uid/TP40008195-CH38)（除非你向 [initWithDictionary:copyItems:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithDictionary:copyItems:) 传入 `YES` 作为参数）。取而代之的是，字典会保存一个指向该对象的强引用。关于字典如何处理键对象的内容，请参阅[使用自定义键](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgeztilktk44a)。关于复制和内存管理的更多信息，请参阅[复制集合](Copying%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnrsfvjvomi)。

在内部，字典使用哈希表来组织其存储，并根据对应的键提供快速访问值的能力。不过，字典所定义的各个方法把你与哈希表、哈希函数或键的哈希值这些复杂细节隔离开来。这些方法直接接受键本身，而不是其哈希后的形式。

从可变字典中移除一个条目时，请记住字典对构成该条目的键和值对象所持有的强引用会被丢弃。如果这些对象没有其他强引用了，它们就会被释放。

向可变字典中添加对象相对简单直接。要添加单个键值对，或替换某个键对应的对象，可以使用 [setObject:forKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/setObject:forKey:) 实例方法，如清单 1 所示。

__清单 1__  向字典添加对象

```objc
NSString *last = @"lastName";
NSString *first = @"firstName";

NSMutableDictionary *dict = [NSMutableDictionary dictionaryWithObjectsAndKeys:
        @"Jo", first, @"Smith", last, nil];
NSString *middle = @"middleInitial";

[dict setObject:@"M" forKey:middle];
```

你还可以使用 [addEntriesFromDictionary:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/addEntriesFromDictionary:) 实例方法，从另一个字典添加条目。如果两个字典都包含相同的键，接收者原来对应该键的值对象会被释放，由新对象取而代之。例如，清单 2 中的代码执行之后，`dict` 中键 "lastName" 对应的值将变为 "Jones"。

__清单 2__  从另一个字典添加条目

```objc
NSString *last = @"lastName";
NSString *first = @"firstName";
NSString *suffix = @"suffix";
NSString *title = @"title";

NSMutableDictionary *dict = [NSMutableDictionary dictionaryWithObjectsAndKeys:
    @"Jo", first, @"Smith", last, nil];

NSDictionary *newDict = [NSDictionary dictionaryWithObjectsAndKeys:
    @"Jones", last, @"Hon.", title, @"J.D.", suffix, nil];

[dict addEntriesFromDictionary: newDict];
```


`NSDictionary` 提供了 [keysSortedByValueUsingSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/keysSortedByValueUsingSelector:) 方法，它会返回一个数组，其中包含按照该字典的值排序后各键应有的顺序，如清单 3 所示。

__清单 3__  按值对字典的键排序

```objc
NSDictionary *dict = [NSDictionary dictionaryWithObjectsAndKeys:
    [NSNumber numberWithInt:63], @"Mathematics",
    [NSNumber numberWithInt:72], @"English",
    [NSNumber numberWithInt:55], @"History",
    [NSNumber numberWithInt:49], @"Geography",
    nil];

NSArray *sortedKeysArray =
    [dict keysSortedByValueUsingSelector:@selector(compare:)];
// sortedKeysArray contains: Geography, History, Mathematics, English
```

你也可以使用[块（block）](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3)，根据字典中键所对应的值轻松地对键进行排序。`NSDictionary` 的 [keysSortedByValueUsingComparator:](https://developer.apple.com/documentation/foundation/nsdictionary/1411105-keyssortedbyvalueusingcomparator) 方法允许你使用块来比较各个键，并将排序结果放入一个新数组。清单 4 展示了使用块排序的示例。

__清单 4__  使用块简化字典的自定义排序

```objc
NSArray *blockSortedKeys = [dict keysSortedByValueUsingComparator: ^(id obj1, id obj2) {

     if ([obj1 integerValue] > [obj2 integerValue]) {
          return (NSComparisonResult)NSOrderedDescending;
     }

     if ([obj1 integerValue] < [obj2 integerValue]) {
          return (NSComparisonResult)NSOrderedAscending;
     }
     return (NSComparisonResult)NSOrderedSame;
}];
```


在大多数情况下，Cocoa 自带的对象（如 `NSString` 对象）作为键已经足够。不过，某些情况下可能需要使用自定义对象作为字典的键。使用自定义对象作为键时，有几个重要事项需要注意。

键必须遵循 [NSCopying](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCopying/Description.html#//apple_ref/occ/intf/NSCopying) 协议。向字典添加条目的方法——无论是在初始化时（对所有字典而言），还是在修改时（对[可变](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)字典而言）——都不会把键对象本身直接添加到字典中。相反，它们会复制每个键参数，并将该拷贝添加到字典中。键被复制进字典之后，字典所持有的这些拷贝不应该再被修改。

键必须实现 `hash` 和 `isEqual:` 方法，因为字典使用哈希表来组织其存储，并借此快速访问其中的对象。此外，字典的性能在很大程度上取决于所使用的哈希函数。如果哈希函数设计不佳，性能下降可能会非常严重。关于 `hash` 和 `isEqual:` 方法的更多信息，请参阅 [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intf/NSObject)。

`NSMapTable` 类默认配置为像 `NSMutableDictionary` 那样持有对象。它还允许你为特定场景定制额外的存储选项，例如需要高级[内存管理](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)选项，或需要持有特定类型的指针。例如，图 2 中的映射表（map table）被配置为对其值对象持有弱引用。你还可以指定是否希望在对象加入数组时被复制。

__图 2__  映射表的对象所有权

!

当你想要一个使用弱引用的键值对集合时，可以使用 `NSMapTable` 对象。例如，假设你有一个包含若干对象的全局映射表。由于全局对象永远不会被回收，除非其内容是弱持有的，否则其中的对象都无法被释放。配置为弱持有对象的映射表并不拥有其内容。如果这样的映射表中的对象没有其他强引用，这些对象就会被释放。例如，[图 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgeztilktk4za) 中的映射表对其内容持有弱引用，对象 D 和对象 E 将被释放，其余对象则保留。

要创建映射表，可以使用 [mapTableWithKeyOptions:valueOptions:](https://developer.apple.com/documentation/foundation/nsmaptable/1391414-init) 或 [initWithKeyOptions:valueOptions:capacity:](https://developer.apple.com/documentation/foundation/nsmaptable/1391382-init) 并配合合适的指针函数选项来创建或初始化它。也可以使用 [initWithKeyPointerFunctions:valuePointerFunctions:capacity:](https://developer.apple.com/documentation/foundation/nsmaptable/1391429-initwithkeypointerfunctions) 并配合合适的 [NSPointerFunctions](https://developer.apple.com/documentation/foundation/nspointerfunctions) 实例来初始化。关于指针函数选项的更多信息，请参阅[指针函数选项](Pointer%20Function%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcojzfvjvomi)。

`NSMapTable` 类还定义了若干便捷构造方法，用于创建对其内容持有强引用或弱引用的映射表。例如，[mapTableWithStrongToWeakObjects](https://developer.apple.com/documentation/foundation/nsmaptable/1391372-maptablewithstrongtoweakobjects) 创建一个对键持有强引用、对值持有弱引用的映射表。这些便捷构造方法仅应在存储对象时使用。

要将映射表配置为使用任意指针，可以同时使用 `NSPointerFunctionsOpaqueMemory` 和 `NSPointerFunctionsOpaquePersonality` 值选项对其进行初始化。键和值的选项不必相同。当使用映射表存储任意指针时，应使用针对 `void *` 指针的 C 函数 API。更多信息请参阅 Managing Map Tables。例如，你可以按照清单 5 所示的方式添加一个指向 `int` 值的指针。请注意，此映射表使用 `NSString` 对象作为键，且键会被复制进映射表中。

__清单 5__  为非对象指针配置的映射表

```objc
NSPointerFunctionsOptions keyOptions=NSPointerFunctionsStrongMemory |
     NSPointerFunctionsObjectPersonality | NSPointerFunctionsCopyIn;
NSPointerFunctionsOptions valueOptions=NSPointerFunctionsOpaqueMemory |
     NSPointerFunctionsOpaquePersonality;

NSMapTable *mapTable = [NSMapTable mapTableWithKeyOptions:keyOptions
        valueOptions:valueOptions];

NSString *key1 = @"Key1";
NSMapInsert(mapTable, key1, someIntPtr);
```

随后你可以使用 [NSMapGet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMapGet) 函数访问该整数。

```objc
NSLog(@" Key1 contains: %i", *(int *) NSMapGet(mapTable, @"Key1"));
```

当配置为使用任意指针时，映射表也会带有使用指针本身所固有的风险。例如，如果这些指针指向某个函数内基于栈创建的数据，那么即使映射表本身仍然有效，这些指针在函数之外也是无效的。尝试访问它们将导致未定义行为。

[下一页](Sets-%20Unordered%20Collections%20of%20Objects.md)[上一页](Arrays-%20Ordered%20Collections.md)
