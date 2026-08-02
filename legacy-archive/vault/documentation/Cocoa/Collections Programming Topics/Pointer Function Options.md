---
title: 集合编程主题
apple_id: 10000034i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/pointer.html
archived_at: '2026-07-15T07:13:37.849362Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [集合编程主题](About%20Collections.md)


[下一页](Document%20Revision%20History.md)[上一页](Enumeration-%20Traversing%20a%20Collection%E2%80%99s%20Elements.md)

# 指针函数选项

指针集合类（`NSPointerArray`、`NSMapTable` 和 `NSHashTable`）允许你进一步定制集合，以满足自己的[内存](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)和存储需求。[NSPointerFunctionsOptions](https://developer.apple.com/documentation/foundation/nspointerfunctions/options) 指定的选项提供了一个便捷的接口，用于定制集合管理其所包含指针的方式。

指针集合通过三类不同的选项进行配置：内存选项、性质（personality）选项和拷贝行为。并非所有内存、性质和拷贝选项的组合都是有效的。

内存选项指定了当条目被添加到集合、从集合中移除、或被拷贝时的预期行为。一些较常用的选项包括：

- `NSPointerFunctionsStrongMemory`，用于对其内容持有强引用的集合。
- `NSPointerFunctionsZeroingWeakMemory`，用于对其内容持有弱引用的集合。
- `NSPointerFunctionsOpaqueMemory`，用于内容的所有权完全由集合外部管理的情况。它通常用于持有整数或 C 字符串等基本类型指针的集合。

性质选项指定了集合中存储的指针类型，例如指向对象的指针，或指向其他数据类型的指针。它们还指定了哈希和相等性测试时的行为。一些较常用的选项包括：

- `NSPointerFunctionsObjectPersonality`，用于持有对象、并使用 `isEqual:` 来判断[相等性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectComparison.html#//apple_ref/doc/uid/TP40008195-CH37)的集合。
- `NSPointerFunctionsObjectPointerPersonality`，通常用于持有对象、并使用直接比较来判断相等性的集合。
- `NSPointerFunctionsOpaquePersonality`，通常用于持有整数或 C 字符串等基本类型指针的集合。

拷贝选项指定集合是否应该[拷贝](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCopying.html#//apple_ref/doc/uid/TP40008195-CH38)加入集合中的元素。如果指定了 `NSPointerFunctionsCopyIn` 选项，集合会拷贝加入的元素；否则不会。

如果 `NSPointerFunctionsOptions` 提供的定制能力不能满足你的需求，你可以使用 [NSPointerFunctions](https://developer.apple.com/documentation/foundation/nspointerfunctions) 类为内存分配、哈希、相等性测试等操作定义自定义函数。例如，如果你有一个 `struct` 集合，你需要指定该 `struct` 的大小。

如果你想配置一个用于持有对象的指针集合，有几个选项可用。对于对象来说，只有两种性质选项是有意义的：

- `NSPointerFunctionsObjectPersonality`，默认的对象选项，使用 `isEqual:` 方法来判断相等性。
- `NSPointerFunctionsObjectPointerPersonality`，也是一个可行的选项，使用指针相等来判断相等性。

你还可以选择使用强引用或置零弱引用（zeroing weak reference）。如果选择使用强引用，你还可以选择在对象被加入集合时是否要对其进行拷贝。

例如，如果你希望某个集合对对象持有弱引用，并使用 `isEqual:` 来判断相等性，可以按如下方式指定选项：

```objc
NSPointerFunctionsOptions collectionOptions = NSPointerFunctionsObjectPersonality
          | NSPointerFunctionsZeroingWeakMemory;
```

指定好选项后，`collectionOptions` 就可以在初始化时传递给集合。

如果你想配置一个用于持有任意（非对象）指针的指针集合，可以根据该集合将要持有的指针类型进行一定程度的灵活配置。为了获得最大的灵活性，你可以选择 `NSPointerFunctionsOpaquePersonality`，它允许你持有指向大多数基本类型的指针。你也可以选择以下某个特定类型的选项：

- `NSPointerFunctionsIntegerPersonality` 持有整数指针。
- `NSPointerFunctionsStructPersonality` 持有指向结构体的指针。如果你指定此选项，必须为所使用的 [NSPointerFunctions](https://developer.apple.com/documentation/foundation/nspointerfunctions) 对象设置 [sizeFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1408045-sizefunction) 属性。
- `NSPointerFunctionsCStringPersonality` 持有指向 C 字符串的指针。

在处理任意指针时，通常应使用 `NSPointerFunctionsOpaqueMemory`，因为它与所有性质选项都兼容。如果需要，你也可以将 `NSPointerFunctionsMallocMemory` 或 `NSPointerFunctionsMachVirtualMemory` 与 opaque、C 字符串以及 struct 性质选项配合使用，不过通常不建议这样做。

唯一支持拷入（copy-in）行为的任意指针配置，是在使用 malloc 或 Mach 虚拟内存时的 C 字符串和 struct 性质选项。

如果你想让一个集合使用 opaque 内存来持有任意指针，可以按如下方式指定选项：

```objc
NSPointerFunctionsOptions collectionOptions = NSPointerFunctionsOpaquePersonality
          | NSPointerFunctionsOpaqueMemory;
```

指定好选项后，`collectionOptions` 就可以在初始化时传递给集合。

[下一页](Document%20Revision%20History.md)[上一页](Enumeration-%20Traversing%20a%20Collection%E2%80%99s%20Elements.md)
