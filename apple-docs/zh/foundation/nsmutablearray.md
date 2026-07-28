---
title: NSMutableArray
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutablearray
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray.json'
content_hash: 'sha256:fee5e1171c6781d9'
translated: true
---

> 导航： [技术](../technologies.md) · [Foundation](../foundation.md)

# NSMutableArray

<sub>类</sub>

一种可动态调整的对象有序集合。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableArray
```

## 概述

在需要引用语义的情况下，你可以在 Swift 中使用此类型来代替 [Array](../swift/array.md) 变量。

`NSMutableArray` 类声明了管理可修改对象数组的对象的编程接口。此类在继承自 [NSArray](nsarray.md) 的基本数组处理行为上增加了插入和删除操作。

NSMutableArray 与其 Core Foundation 中的对应类型 [CFMutableArray](../corefoundation/cfmutablearray.md) 是“免费桥接（toll-free bridged）”的。更多信息请参见 [免费桥接（Toll-Free Bridging）](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2)。

### 使用下标访问值

除了提供的实例方法（如 `[- replaceObjectAtIndex:withObject:](<nsmutablearray/replaceobject(at_with_).md>)`）之外，你还可以使用 _下标（subscripting）_ 通过索引访问 `NSArray` 的值。

**Swift**

```swift
mutableArray[3] = "someValue"
```

**Objective-C**

```objc
mutableArray[3] = @"someValue";
```

### 派生子类说明

通常很少有理由需要派生子类（subclass）`NSMutableArray`。该类在其设计目的上表现良好——维护一个可修改的、有序的对象集合。但在某些情况下，自定义的 `NSArray` 对象可能会派上用场。以下是几种可能的场景：

- 改变 `NSMutableArray` 存储其集合元素的方式。你可能是出于性能原因，或为了与遗留代码更好地兼容。
- 获取有关集合所发生事件的更多信息（例如，统计信息收集）。

#### 需要重写的方法

`NSMutableArray` 定义了五个基本方法：

- `[- insertObject:atIndex:](<nsmutablearray/insert(__at_)-5dbx5.md>)`
- `[- removeObjectAtIndex:](<nsmutablearray/removeobject(at_).md>)`
- `[- addObject:](<nsmutablearray/add(__).md>)`
- `[- removeLastObject](<nsmutablearray/removelastobject().md>)`
- `[- replaceObjectAtIndex:withObject:](<nsmutablearray/replaceobject(at_with_).md>)`

在子类中，你必须重写所有这些方法。你还必须重写 [NSArray](nsarray.md) 类的基本方法。

## 关系

- **继承自**: [NSArray](nsarray.md)

- **遵循**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## 主题

### 创建和初始化可变数组

- `[init(contentsOfURL:)](<nsmutablearray/init(contentsofurl_).md>)` — 创建并返回一个包含由给定 URL 所指定内容的可变数组。
- `[- init](<nsmutablearray/init().md>)` — 初始化一个新分配的数组。
- `[- initWithCapacity:](<nsmutablearray/init(capacity_).md>)` — 返回一个数组，该数组已初始化，拥有足以最初容纳给定数量对象的内存。

### 添加对象

- `[- addObject:](<nsmutablearray/add(__).md>)` — 将给定对象插入到数组的末尾。
- `[- addObjectsFromArray:](<nsmutablearray/addobjects(from_).md>)` — 将另一个给定数组中的对象添加到接收数组内容的末尾。
- `[- insertObject:atIndex:](<nsmutablearray/insert(__at_)-5dbx5.md>)` — 将给定对象插入到数组内容中的指定索引处。
- `[- insertObjects:atIndexes:](<nsmutablearray/insert(__at_)-73pln.md>)` — 将提供的数组中的对象插入到接收数组中指定的索引处。

### 移除对象

- `[- removeAllObjects](<nsmutablearray/removeallobjects().md>)` — 清空数组的所有元素。
- `[- removeLastObject](<nsmutablearray/removelastobject().md>)` — 移除数组中索引值最高的对象。
- `[- removeObject:](<nsmutablearray/remove(__).md>)` — 移除数组中给定对象的所有出现。
- `[- removeObject:inRange:](<nsmutablearray/remove(__in_).md>)` — 移除数组中指定范围内给定对象的所有出现。
- `[- removeObjectAtIndex:](<nsmutablearray/removeobject(at_).md>)` — 移除 `index` 处的对象。
- `[- removeObjectsAtIndexes:](<nsmutablearray/removeobjects(at_).md>)` — 从数组中移除指定索引处的对象。
- `[- removeObjectIdenticalTo:](<nsmutablearray/removeobject(identicalto_).md>)` — 移除数组中给定对象的所有出现。
- `[- removeObjectIdenticalTo:inRange:](<nsmutablearray/removeobject(identicalto_in_).md>)` — 移除数组中指定范围内 `anObject` 的所有出现。
- `[- removeObjectsFromIndices:numIndices:](<nsmutablearray/removeobjects(fromindices_numindices_).md>)` — 从数组中移除指定数量的对象，从指定索引开始。 _(已废弃)_
- `[- removeObjectsInArray:](<nsmutablearray/removeobjects(in_)-4yb26.md>)` — 从接收数组中移除另一个给定数组中的对象。
- `[- removeObjectsInRange:](<nsmutablearray/removeobjects(in_)-1udmn.md>)` — 从数组中移除给定范围内的每个对象。

### 替换对象

- `[- replaceObjectAtIndex:withObject:](<nsmutablearray/replaceobject(at_with_).md>)` — 使用 `anObject` 替换 `index` 处的对象。
- `[- replaceObjectsAtIndexes:withObjects:](<nsmutablearray/replaceobjects(at_with_).md>)` — 将接收数组中指定位置的对象替换为给定数组中的对象。
- `[- replaceObjectsInRange:withObjectsFromArray:range:](<nsmutablearray/replaceobjects(in_withobjectsfrom_range_).md>)` — 将接收数组中由一个给定范围指定的对象替换为另一个数组中由另一个范围指定的对象。
- `[- replaceObjectsInRange:withObjectsFromArray:](<nsmutablearray/replaceobjects(in_withobjectsfrom_).md>)` — 将接收数组中由给定范围指定的对象替换为给定数组中的所有对象。
- `[- setArray:](<nsmutablearray/setarray(__).md>)` — 将接收数组的元素设置为另一个给定数组中的元素。

### 过滤内容

- `[- filterUsingPredicate:](<nsmutablearray/filter(using_).md>)` — 针对数组内容评估给定的谓词（predicate），并只保留匹配的对象。

### 重排内容

- `[- exchangeObjectAtIndex:withObjectAtIndex:](<nsmutablearray/exchangeobject(at_withobjectat_).md>)` — 交换数组中给定索引处的对象。
- `[- sortUsingDescriptors:](<nsmutablearray/sort(using_)-4eh07.md>)` — 使用给定的排序描述符（sort descriptors）数组对接收者进行排序。
- `[- sortUsingComparator:](<nsmutablearray/sort(comparator_).md>)` — 使用给定的 [Comparator](comparator.md) block 指定的比较方法，对接收者进行升序排序。
- `[- sortWithOptions:usingComparator:](<nsmutablearray/sort(options_usingcomparator_).md>)` — 使用指定的选项和给定的 [Comparator](comparator.md) block 指定的比较方法，对接收者进行升序排序。
- `[- sortUsingFunction:context:](<nsmutablearray/sort(__context_).md>)` — 按比较函数 `compare` 定义的方式对接收者进行升序排序。
- `[- sortUsingSelector:](<nsmutablearray/sort(using_)-537vs.md>)` — 按给定的选择器（selector）指定的比较方法所确定的方式，对接收者进行升序排序。

### 初始化方法

- `[- initWithCoder:](<nsmutablearray/init(coder_).md>)`
- `[init(objects:count:)](<nsmutablearray/init(objects_count_).md>)`

### 默认实现

- `[NSMutableArray 实现](nsmutablearray/nsmutablearray-implementations.md)`
