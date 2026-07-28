---
title: 'NSMapTable：不仅仅是弱指针版的 NSDictionary | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/07/nsmaptable-more-than-nsdictionary-for.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:80abcfdd0e6d2b95'
translated: true
---

> 原文：[NSMapTable: more than an NSDictionary for weak pointers | Cocoa with Love](https://www.cocoawithlove.com/2008/07/nsmaptable-more-than-nsdictionary-for.html)　·　Cocoa with Love (Matt Gallagher)

NSMapTable 是 Mac OS X 10.5（Leopard）中引入的一个集合类。乍看之下，它最有用的地方似乎是作为 NSDictionary 的替代品，可以在“强”指针和“弱”指针之间选择。在这篇文章中，我将向你展示为什么它在垃圾回收之外也很有用，以及它如何做到 NSDictionary 无法（或不应）做到的事情。

## 为你的 Leopard 带来更多 Cocoa

Cocoa 在 Mac OS X 10.5（Leopard）中新增了几个集合类。包括：

- [NSPointerArray](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSPointerArray_Class/index.html)
- [NSHashTable](http://developer.apple.com/documentation/Cocoa/Reference/NSHashTable_class/index.html)
- [NSMapTable](http://developer.apple.com/documentation/Cocoa/Reference/NSMapTable_class/index.html)

NSPointerArray 是全新的，但 NSHashTable 和 NSMapTable 的大部分功能之前已经通过[同名的 Foundation 不透明 C 结构体](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/Reference/reference.html)提供。

在某些方面，这些新类的工作方式分别类似于 NSMutableArray、NSMutableSet 和 NSMutableDictionary，但提供了使用“弱”垃圾回收指针的选项。如果你在使用带垃圾回收的 Objective-C 2.0，你应该[了解“弱”指针的含义](http://developer.apple.com/documentation/Cocoa/Conceptual/GarbageCollection/Articles/gcDesignPatterns.html)，因此使用此选项的优势应该很明确。

NSPointerArray 还可以用于纯指针（不一定是 Objective-C 类的指针），但 NSHashTable 和 NSMutableArray 类都要求其内容为 Objective-C 对象。

不过，从一般意义上说，NSPointerArray 和 NSHashTable 分别填补了与 NSMutableArray 和 NSMutableSet（一个是有序数组，另一个是无序集合）相同的设计角色。

NSMapTable 则不同，因为它可以填补 NSMutableDictionary 无法（或不应）完成的设计角色。

## NSDictionary 的局限性

NSDictionary 提供了键到对象的映射。本质上，NSDictionary 将“对象”存储在由“键”索引的位置。

由于对象存储在特定位置，NSDictionary 要求键的值不改变（否则对象会突然出现在键对应的错误位置）。为了确保维持这一要求，NSDictionary 总是将键复制到自己的私有位置。

这种键复制行为是 NSDictionary 工作方式的基础，但也是一个限制：只有支持 NSCopying 协议的 Objective-C 对象才能用作 NSDictionary 的键。此外，键应该足够小且高效，以便复制不会给 CPU 或内存带来负担。

这意味着 NSDictionary 实际上只适合使用“值”类型的对象作为键（例如小字符串和数字）。对于将完整功能的对象映射到其他对象来说，它并不理想。

## 对象到对象的映射

NSMapTable（顾名思义）更适合一般意义上的映射。根据其构造方式，NSMapTable 可以处理 NSDictionary 那种“键到对象”的映射风格，也可以处理“对象到对象”的映射——也称为“[关联数组](http://en.wikipedia.org/wiki/Associative_array)”或简称为“[映射](http://www.sgi.com/tech/stl/Map.html)”。

例如，按如下方式构造的 NSMapTable：

```objc
NSMapTable *keyToObjectMapping =
    [NSMapTable
        mapTableWithKeyOptions:NSMapTableCopyIn
        valueOptions:NSMapTableStrongMemory];
```

其工作方式与 NSMutableDictionary 非常相似，会复制其“键”值并保留其“对象”值。

一个纯粹的对象到对象映射可以按如下方式构造：

```objc
NSMapTable *objectToObjectMapping =
    [NSMapTable mapTableWithStrongToStrongObjects];
```

以前，如果所有键都是包含映射中源对象内存地址的 NSNumber，那么可以使用 NSDictionary 来模拟对象到对象的行为（别笑，我见过有人这么做），但除了这种绕弯子的方式，NSMapTable 首次在 Cocoa 集合类中提供了真正的对象到对象映射。

## NSMapTable 的选项

提供给 NSMapTable 的选项由三部分组成：“内存选项（memory option）”、“个性选项（personality option）”和“复制入（copy in）”标志。你可以为每个部分使用一个选项（如果某个部分没有提供选项，将使用默认行为）。这些部分都是位标志（将它们按位“或”组合起来即可）。

官方允许 NSMapTable 使用以下选项：

- NSMapTableStrongMemory（一个“内存选项”）
- NSMapTableWeakMemory（一个“内存选项”）
- NSMapTableObjectPointerPersonality（一个“个性选项”）
- NSMapTableCopyIn（一个“复制选项”）

NSMapTableStrongMemory 是默认的“内存选项”。然而，默认的“个性选项”和默认的“复制入”行为没有名称，因此这两个值可以视为隐式包含在列表中。

### 内存选项

由于“强”和“弱”是与 Objective-C 垃圾回收相关的术语，因此可能不清楚这些选项是否可以在垃圾回收代码之外（Apple 所称的手动管理内存）使用。

在垃圾回收之外，适用以下定义：

- **_强_**：使用 retain 和 release
- **_弱_**：不使用 retain 和 release

NSMapTable 只允许与 Objective-C 对象对应的 NSPointerFunctionsOptions“个性选项”。还有其他 NSPointerFunctionsOptions“个性选项”，其中“强”指针的行为不包括 retain 和 release，但这些选项不被 NSMapTable 允许。

> _关于在垃圾回收之外使用“弱”的警告：_
> 指针不会像在垃圾回收环境中那样被清零，因此如果指针被释放，你必须小心不要解引用它。

### 个性选项

使用 NSMapTableObjectPointerPersonality 选项来控制将对象添加到集合时是否使用该对象的 isEqualTo: 和 hash 方法。

- _指定了 NSMapTableObjectPointerPersonality_
   使用对象的指针值进行直接比较和位移哈希生成（_不_使用 isEqualTo: 和 hash 方法）。
- _**未**指定 NSMapTableObjectPointerPersonality_（默认行为）
   将对键调用 hash 和 isEqualTo: 方法以确定 NSMapTable 中的存储位置。在键用于 NSMapTable 的持续时间内，这些方法的返回值不应改变（应保持不可变）。

两种行为都意味着内容实现了 NSObject 协议，因此也可能会对键和对象调用此协议中的方法。特别是，无论使用何种个性选项，都可能对 NSMapTable 中包含的键和对象调用 description 方法。NSMapTable 仅在所有键和对象也都实现 NSCoding 协议时才支持 NSCoding。

### 复制选项

如果指定了 NSMapTableCopyIn，则 NSMapTable 在添加数据时会使用 NSCopying 协议制作自己的数据副本。如果你不指定此选项（默认行为），则不会进行复制。
