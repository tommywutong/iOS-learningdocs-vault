---
title: 集合编程主题
apple_id: 10000034i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/Enumerators.html
archived_at: '2026-07-15T07:13:33.808568Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [集合编程主题](About%20Collections.md)


[下一页](Pointer%20Function%20Options.md)[上一页](Copying%20Collections.md)

# 枚举：遍历集合的元素

Cocoa 定义了三种主要的[枚举](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Enumeration.html#//apple_ref/doc/uid/TP40008195-CH17)集合内容的方式，包括快速枚举和基于 block 的枚举。此外还有 `NSEnumerator` 类，不过它总体上已被快速枚举取代。

快速枚举是遍历集合内容的首选方式，因为它具有以下优点：

- 相比直接使用 `NSEnumerator`，枚举效率更高。
- 语法简洁。
- 如果在枚举过程中修改集合，枚举器会抛出异常。
- 你可以并发执行多个枚举。

快速枚举的行为会因集合类型的不同而略有差异。数组和集（set）枚举其内容，字典枚举其键。`NSIndexSet` 和 `NSIndexPath` 不支持快速枚举。你可以像清单 1 那样对集合对象使用快速枚举。

__清单 1__  对字典使用快速枚举

```objc
for (NSString *element in someArray) {
     NSLog(@"element: %@", element);
}

NSString *key;
for (key in someDictionary){
     NSLog(@"Key: %@, Value %@", key, [someDictionary objectForKey: key]);
}
```

关于快速枚举的更多信息，请参阅 _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ 中的 [Fast Enumeration](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocFastEnumeration.html#//apple_ref/doc/uid/TP30001163-CH18)。

`NSArray`、`NSDictionary` 和 `NSSet` 都允许使用 [block](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) 来枚举其内容。要使用 block 进行枚举，调用相应的方法并指定要使用的 block 即可。清单 2 演示了针对 `NSArray` 对象的基于 block 的枚举。

__清单 2__  对数组进行基于 block 的枚举

```objc
NSArray *anArray = [NSArray arrayWithObjects:@"A", @"B", @"D", @"M", nil];
NSString *string = @"c";

[anArray enumerateObjectsUsingBlock:^(id obj, NSUInteger index, BOOL *stop){
     if ([obj localizedStandardCompare:string] == NSOrderedSame) {
          NSLog(@"Object Found: %@ at index: %i",obj, index);
          *stop = YES;
     }
} ];
```

对于 `NSSet` 对象，你可以使用类似的代码，如清单 3 所示。

__清单 3__  对集（set）进行基于 block 的枚举

```objc
NSSet *aSet = [NSSet setWithObjects: @"X", @"Y", @"Z", @"Pi", nil];
NSString *aString = @"z";

[aSet enumerateObjectsUsingBlock:^(id obj, BOOL *stop){
     if ([obj localizedStandardCompare:aString]==NSOrderedSame) {
          NSLog(@"Object Found: %@", obj);
          *stop = YES;
     }
} ];
```

对于 `NSArray` 的枚举，_index_ 参数在并发枚举时很有用。如果没有这个参数，获取索引的唯一方式就是使用 [indexOfObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/indexOfObject:) 方法，而这种方式效率较低。_stop_ 参数对性能很重要，因为它允许枚举根据 block 内部判断的某个条件提前结束。其他集合的基于 block 的枚举方法在方法名和 block 签名上略有不同，具体的方法定义请参阅各自的类参考文档。

[NSEnumerator](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSEnumerator/Description.html#//apple_ref/occ/cl/NSEnumerator) 是一个简单的抽象类，它的子类用于枚举其他对象的集合。数组、集、字典等集合对象会提供专门的 `NSEnumerator` 对象，用于枚举其内容。你可以对一个新创建的 `NSEnumerator` 对象反复发送 `nextObject` 消息，使其返回原集合中的下一个对象。当集合中的元素被取尽时，它会返回 `nil`。一个枚举器一旦耗尽其集合，就无法被"重置"。要再次枚举一个集合，你必须创建一个新的枚举器。

`NSArray`、`NSSet`、`NSDictionary` 等集合类都包含用于返回适合其集合类型的枚举器的方法。例如，`NSArray` 有两个返回 `NSEnumerator` 对象的方法：`objectEnumerator` 和 `reverseObjectEnumerator`。`NSDictionary` 类也有两个返回 `NSEnumerator` 对象的方法：`keyEnumerator` 和 `objectEnumerator`。这些方法让你可以分别按键或按值枚举 `NSDictionary` 对象的内容。

在 Objective-C 中，`NSEnumerator` 对象会保留（retain）它正在枚举的集合（除非某个自定义子类以不同方式实现）。

在枚举一个可变集合的过程中，移除、替换或添加其元素都是不安全的。如果你需要在枚举期间修改集合，可以先拷贝该集合再对拷贝进行枚举，或者在枚举期间收集所需的信息，之后再应用这些变更。清单 4 演示了第二种模式。

__清单 4__  枚举字典并移除对象

```objc
NSMutableDictionary *myMutableDictionary = <#Get a mutable dictionary#> ;
NSMutableArray *keysToDeleteArray =
    [NSMutableArray arrayWithCapacity:[myMutableDictionary count]];
NSString *aKey;
NSEnumerator *keyEnumerator = [myMutableDictionary keyEnumerator];
while (aKey = [keyEnumerator nextObject])
{
    if ( /* 针对键或值的判断条件 */ ) {
        [keysToDeleteArray addObject:aKey];
    }
}
[myMutableDictionary removeObjectsForKeys:keysToDeleteArray];
```

[下一页](Pointer%20Function%20Options.md)[上一页](Copying%20Collections.md)
