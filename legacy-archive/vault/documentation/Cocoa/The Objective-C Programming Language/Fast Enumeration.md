---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocFastEnumeration.html
archived_at: '2026-07-15T07:17:30.392078Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Enabling%20Static%20Behavior.md)[上一页](Associative%20References.md)

# 快速枚举

快速枚举（fast enumeration）是一项语言特性，让你能够使用简洁的语法高效、安全地枚举一个集合的内容。

快速枚举的语法定义如下：

```objc
for ( Type newVariable in expression ) { statements }
```

或者

```objc
Type existingItem;
for ( existingItem in expression ) { statements }
```

在这两种情况下，_expression_ 都会得到一个遵循 [NSFastEnumeration](https://developer.apple.com/documentation/foundation/nsfastenumeration) 协议的对象（参见[采用快速枚举](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjyfvjvomq)）。迭代变量依次被设为返回对象中的每一项，并执行由 `statements` 定义的代码。当循环因源对象池耗尽而结束时，迭代变量会被设为 `nil`。如果循环提前终止，迭代变量则保留指向最后一次迭代的项。

使用快速枚举有若干优点：

- 相比直接使用 `NSEnumerator`，枚举的效率要高得多。
- 语法简洁。
- 枚举是"安全的"——枚举器带有变更（mutation）保护机制，如果你试图在枚举期间修改集合，就会引发异常。

由于枚举期间禁止修改对象，你可以并发地执行多个枚举。

在其他方面，这项特性的行为与标准的 `for` 循环相同。你可以用 `break` 中断迭代，用 `continue` 前进到下一个元素。

任何一个类，只要其实例能够提供对其他对象集合的访问，就可以采用 [NSFastEnumeration](https://developer.apple.com/documentation/foundation/nsfastenumeration) 协议。Foundation 框架中的集合类——[NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray)、[NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) 和 [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet)——都采用了这个协议，`NSEnumerator` 也是如此。显然，对于 `NSArray` 和 `NSSet` 来说，枚举的是它们的内容。对于其他类，相应的文档会说明具体枚举的是哪个属性——例如，[NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) 和 Core Data 的 [NSManagedObjectModel](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel) 类都支持快速枚举；`NSDictionary` 枚举其键，`NSManagedObjectModel` 枚举其实体。

下面的代码示例展示了如何对 `NSArray` 和 `NSDictionary` 对象使用快速枚举。

```objc
NSArray *array = [NSArray arrayWithObjects:
        @"one", @"two", @"three", @"four", nil];

for (NSString *element in array) {
    NSLog(@"element: %@", element);
}

NSDictionary *dictionary = [NSDictionary dictionaryWithObjectsAndKeys:
    @"quattuor", @"four", @"quinque", @"five", @"sex", @"six", nil];

NSString *key;
for (key in dictionary) {
    NSLog(@"English: %@, Latin: %@", key, [dictionary objectForKey:key]);
}
```

你也可以对快速枚举使用 `NSEnumerator` 对象，如下例所示：

```objc
NSArray *array = [NSArray arrayWithObjects:
        @"one", @"two", @"three", @"four", nil];

NSEnumerator *enumerator = [array reverseObjectEnumerator];
for (NSString *element in enumerator) {
    if ([element isEqualToString:@"three"]) {
        break;
    }
}

NSString *next = [enumerator nextObject];
// next = "two"
```

对于具有明确顺序的集合或枚举器——比如 `NSArray`，或者从数组派生出的 `NSEnumerator` 实例——枚举会按照该顺序进行，因此如果你需要的话，只需简单地计数迭代次数，就能得到集合中恰当的索引。

```objc
NSArray *array = <#Get an array#>;
NSUInteger index = 0;

for (id element in array) {
    NSLog(@"Element at index %u is: %@", index, element);
    index++;
}
```

[下一页](Enabling%20Static%20Behavior.md)[上一页](Associative%20References.md)

