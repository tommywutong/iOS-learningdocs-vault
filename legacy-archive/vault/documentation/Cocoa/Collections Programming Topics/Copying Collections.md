---
title: 集合编程主题
apple_id: 10000034i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/Copying.html
archived_at: '2026-07-15T07:13:31.299203Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [集合编程主题](About%20Collections.md)


[下一页](Enumeration-%20Traversing%20a%20Collection%E2%80%99s%20Elements.md)[上一页](Index%20Paths-%20Storing%20a%20Path%20Through%20Nested%20Arrays.md)

# 复制集合

[对象复制](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCopying.html#//apple_ref/doc/uid/TP40008195-CH38)分为两种：浅拷贝和深拷贝。普通的复制是浅拷贝，它会生成一个与原集合共享对象所有权的新集合。深拷贝则会根据原始对象创建新对象，并将这些新对象加入新集合。图 1 展示了这一区别。

__图 1__  浅拷贝与深拷贝

!

有多种方式可以对集合进行浅拷贝。创建浅拷贝时，原集合中的对象会收到一条 `retain` 消息，指针被复制到新集合中。清单 1 展示了使用浅拷贝创建新集合的一些方式。

__清单 1__  创建浅拷贝

```objc
NSArray *shallowCopyArray = [someArray copyWithZone:nil];

NSDictionary *shallowCopyDict = [[NSDictionary alloc] initWithDictionary:someDictionary copyItems:NO];
```

这些方法并不局限于示例中所展示的集合类型。例如，你也可以使用 [copyWithZone:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCopying/Description.html#//apple_ref/occ/intfm/NSCopying/copyWithZone:) 方法复制一个集，或使用 [mutableCopyWithZone:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSMutableCopying/Description.html#//apple_ref/occ/intfm/NSMutableCopying/mutableCopyWithZone:) 方法，或者使用 [initWithArray:copyItems:](https://developer.apple.com/documentation/foundation/nsarray/1408557-initwitharray) 方法复制一个数组。

有两种方式可以对集合进行深拷贝。你可以使用该集合类对应的 `initWithArray:copyItems:` 方法，并将第二个参数设为 `YES`。以这种方式创建集合的深拷贝时，集合中的每个对象都会收到一条 `copyWithZone:` 消息。如果集合中的对象实现了 [NSCopying](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCopying/Description.html#//apple_ref/occ/intf/NSCopying) 协议，这些对象就会被深拷贝到新集合中，新集合随后将成为这些拷贝对象的唯一所有者。如果对象没有实现 `NSCopying` 协议，尝试以这种方式复制它们会导致运行时错误。不过，`copyWithZone:` 产生的是浅拷贝，这种复制方式只能实现一层深度的复制。如果你只需要一层深度的复制，可以像清单 2 那样显式地调用它。

__清单 2__  创建深拷贝

```objc
NSArray *deepCopyArray=[[NSArray alloc] initWithArray:someArray copyItems:YES];
```

这一方法同样适用于其他集合类型。使用相应集合类对应的 `initWithArray:copyItems:`，并将第二个参数设为 `YES`。

如果你需要一个真正的深拷贝——例如当你有一个由数组组成的数组时——只要其中的内容都遵循 [NSCoding](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCoding/Description.html#//apple_ref/occ/intf/NSCoding) 协议，就可以通过归档（archive）再解档（unarchive）该集合来实现。清单 3 展示了这种方式的示例。

__清单 3__  真正的深拷贝

```objc
NSArray* trueDeepCopyArray = [NSKeyedUnarchiver unarchiveObjectWithData:
          [NSKeyedArchiver archivedDataWithRootObject:oldArray]];
```


当你复制一个集合时，该集合本身或其中所包含对象的[可变性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)可能会受到影响。对于任意深度的集合，每种复制方式对其中对象可变性的影响略有不同：

- `copyWithZone:` 使表层变为不可变，所有更深层次仍保留原有的可变性。
- 将第二个参数设为 `NO` 的 `initWithArray:copyItems:` 会使表层具有其所分配的类所对应的可变性，所有更深层次仍保留原有的可变性。
- 将第二个参数设为 `YES` 的 `initWithArray:copyItems:` 会使表层具有其所分配的类所对应的可变性，下一层将变为不可变，再往下的层次则仍保留原有的可变性。
- 对集合进行归档和解档不会改变任何层级原有的可变性。

[下一页](Enumeration-%20Traversing%20a%20Collection%E2%80%99s%20Elements.md)[上一页](Index%20Paths-%20Storing%20a%20Path%20Through%20Nested%20Arrays.md)
