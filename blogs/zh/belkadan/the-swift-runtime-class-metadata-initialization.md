---
title: "Swift 运行时：类元数据初始化"
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/'
original_language: en
published: 2020-10-06
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f2b0a87cd23b336a'
translated: true
---

> 原文：[The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift 运行时：类元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/)

[Swift 运行时：枚举](https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/) »

« [Swift 运行时：类元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/?tag=swift)

[Swift 运行时：枚举](https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/?tag=swift) »

« [Swift 运行时：类元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/?tag=swift-runtime)

[Swift 运行时：枚举](https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/?tag=swift-runtime) »

## [Swift 运行时：类元数据初始化](#)

欢迎来到 Swift 运行时系列文章的第六篇。本系列的目标是结合我在 [Swift on Mac OS 9 项目](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/)中学到的知识，梳理 Swift 运行时的各项功能。上一次我们介绍了类元数据的字段；今天我们将完成它们的初始化。

如前所述，我尽可能地用 Swift 实现了我自己的精简版运行时，尽管过程中不得不使用一些未文档化的 Swift 特性。我将在本系列文章中展示我运行时代码的片段，你可以在 [ppc-swift 仓库](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime)中查看完整代码。

## `swift_initClassMetadata2`

就像结构体元数据同时有 `swift_allocateGenericValueMetadata` 和 `swift_initStructMetadata` 一样，类元数据也有 `swift_allocateGenericClassMetadata` 和 `swift_initClassMetadata2`。等等，为什么要叫“2”？因为最初的 `swift_initClassMetadata` 无法处理元数据初始化中的循环引用，这是 [Swift 项目中最古老的公开问题之一](https://bugs.swift.org/browse/SR-263)。但是[如前所述](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/)，我的运行时同样不处理元数据初始化中的循环引用，所以我打算完全忽略这个问题。

高级算法只需几行代码就能概括：

```
@_silgen_name("swift_initClassMetadata2")
func swift_initClassMetadata2(
  _ metadata: UnsafeMutablePointer<ClassMetadata>,
  _ flags: ClassLayoutFlags,
  _ numFields: UInt,
  _ fieldTypes: UnsafePointer<UnsafePointer<TypeLayout>>,
  _ fieldOffsets: UnsafeMutablePointer<UInt>
) -> MetadataDependency {
  metadata[]._.superclass = getSuperclassMetadata(forSubclass: metadata)
  copySuperclassMetadataToSubclass(metadata, flags)
  if !flags.hasStaticVTable {
    fatalError("This should never happen without library evolution.")
  }
  initClassFieldOffsetVector(metadata, numFields, fieldTypes, fieldOffsets)

  return MetadataDependency() // 用于处理循环引用，未实现
}
```

首先我们获取超类。然后将超类元数据的相关部分复制下来。接着处理“字段偏移向量”（field offset vector），不管它是什么。然后……就这些了，不过在支持 Objective-C 互操作性的运行时中，这显然要复杂得多。（此外，由于我的项目不支持[库演化（library evolution）](https://swift.org/blog/swift-5-1-released/#module-stability)，所有虚函数表（vtable）布局——即方法等——的偏移量都应在编译时静态确定。）所以这篇文章的剩余部分将逐一介绍每个辅助函数。

## `getSuperclassMetadata(forSubclass:)`

这个辅助函数看起来也很短小，但它把复杂性隐藏在了别处：

```
private func getSuperclassMetadata(
  forSubclass metadata: UnsafePointer<ClassMetadata>
) -> UnsafePointer<ClassMetadata>? {
  return metadata[]._.description.superclassMangledName.map {
    let genericArgs = metadata.upcast(to: \._.base).genericArgs
    let metadata = metadataFromMangledName($0, genericArgs)
    return metadata.downcast(from: \ClassMetadata._.base)
  }
}
```

超类的混淆名称（mangled name）存储在类的类型描述（type description）中。它是一个可选值（Optional）（因为可能没有超类），所以我们使用 [`map`](https://developer.apple.com/documentation/swift/optional/1539476-map) 来仅在非 `nil` 的情况下解码该元数据。_当前_类的泛型参数可能对于正确设置超类是必需的——考虑 `class Child<Foo> : Parent<[String: Foo]>`。然后我们看到了 `upcast(to:)` 和 `downcast(from:)` 这两个辅助函数，以及 `metadataFromMangledName(_:_:)` 中的内容。让我们依次处理它们。

还记得在第三篇文章中我谈到的[将结构体嵌入其他结构体作为一种继承（subclassing）形式](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata#filling-in-the-fields)吗？因为这些结构体（几乎）总是将“基类”类型作为第一个元素嵌入，所以“基类”和“子类”拥有相同的地址。这使得通过 UnsafeRawPointer 在它们之间进行转换成为可能。但这并不能阻止我在这种情况下写入_错误_的类型，这就是这些辅助函数的作用所在：

```
extension UnsafePointer {
  func upcast<Base>(
    to keyPath: KeyPath<Pointee, Base>
  ) -> UnsafePointer<Base> {
    // 理想情况下我们会确保 Base 相对于 Pointee 的偏移量为 0，
    // 但这尚未实现。
    return UnsafeRawPointer(self).assumingMemoryBound(to: Base.self)
  }

  func downcast<Subtype>(
    from keyPath: KeyPath<Subtype, Pointee>
  ) -> UnsafePointer<Subtype> {
    return UnsafeRawPointer(self).assumingMemoryBound(to: Subtype.self)
  }
}
```

使用键路径（key path）强制要求“转型”（cast）实际上是针对嵌入层级结构中的“基类”或“子类”，这比我添加这些辅助函数之前显式地转为 UnsafeRawPointer 再转回来要安全得多。我实际上并未实现运行时对键路径的任何支持，但它们仍然可以以静态方式使用，在这种场景下纯粹是为了强制类型检查。（你会注意到 `keyPath` 参数在函数体中完全没有被使用。）

多亏了这些辅助函数，我对自己的运行时实现感觉好多了，你会在后续的示例中看到它们的频繁出现。

另一方面，`metadataFromMangledName(_:_:)` 包含的内容足够丰富，值得用单独的一节来介绍。

## 混淆名称的类型编码

当 `swift_initClassMetadata2` 完成时，`superclass` 字段必须是一个有效的 ClassMetadata 指针，但如果超类是泛型的，那么该指针（不一定）可以在编译时就确定！解决这个问题最简单的方法是使用一个“访问器函数”（accessor function），该函数接受泛型参数并返回相应的超类（可能在其实现中调用了 [`swift_getGenericMetadata`](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/)），然后让子类引用它。这确实是一种有效的方法，但它有一个主要缺点：代码体积。这个函数不会太大，因为大部分工作由 `swift_getGenericMetadata` 处理，但这仍然足够重要，以至于 Apple 的 Swift 团队希望做得更好。他们^[1](#fn:they)需要的是一个紧凑的、结构化的格式，能够唯一地引用一个类型，而事实证明他们已经有了这样一种格式：混淆名称（mangled names）。（我不打算在这里解释什么是混淆名称；[Gwynne Raskind 在 Mike Ash 的博客上有一个很好的解释](https://mikeash.com/pyblog/friday-qa-2014-08-15-swift-name-mangling.html)。请注意，[Swift 名称混淆的细节](https://github.com/apple/swift/blob/release/5.3/docs/ABI/Mangling.rst)自 2014 年以来已经发生了相当大的变化，但其原理仍然适用。）

现在，混淆名称通常只用作符号名称，或在索引代码库时用于引用声明（用于重构、跳转到定义、查找 API 文档等）。但是要在运行时使用它们来描述类型元数据，它们必须能够处理无法通过符号名称查找的内容，比如在函数内部声明的类型。因此，Swift 团队增加了在“混淆名称”内嵌相对和绝对指针的能力，像 `metadataFromMangledName` 这样的代码知道如何解析它们。这意味着，在运行时意义上的“混淆名称”可能不再是一个有效的、可打印的“名称”。

在真实的 Swift 代码库中，_反混淆器（demangler）_——即获取混淆名称并重构其结构的代码^[2](#fn:structure)——是用 C++ 编写的，这使得它可以在运行时、编译器、`swift-demangle` 命令行工具以及调试器使用的进程外检查库中使用。用 Swift 实现它将会是一项漫长且相当枯燥的工作，但我也不希望尝试让那段 C++ 代码在 Mac OS 9 上运行。（我没有检查过，但它很可能依赖于一个比 2001 年可用的 C++ 标准库更新的版本。）

幸运的是，编译器使用的名称混淆方案有一个逃逸出口：一种嵌入指向我在本节开头提到的简单“访问器函数”的指针的方法。因此，这是我少量修改 Swift 编译器以支持此项目的地方之一：在发出混淆名称风格的类型引用时，它_始终_使用访问器函数。（理论上，我可以移除这层额外的间接引用，直接指向访问器函数，因为它不再有实际用途，但在实践中，这可能意味着需要在编译器中做更多的修改，这并不值得付出努力。）

所有这些都说明，我的 `metadataFromMangledName(_:_:)` 比真实的实现要简单得多：

```
func metadataFromMangledName(
  _ mangledRef: UnsafePointer<UInt8>,
  _ genericArgs: UnsafePointer<UnsafeRawPointer?>?
) -> UnsafePointer<TypeMetadata> {
  guard mangledRef[0] == 255 && mangledRef[1] == 9 else {
    fatalError()
  }

  typealias MetadataAccessFn = @convention(c) (
    UnsafePointer<UnsafeRawPointer?>?
  ) -> TypeErasedPointer<TypeMetadata>

  let offset = RelativePointerOffset<MetadataAccessFn>(
    fromUnalignedBytes: mangledRef + 2)
  let accessFn = mangledRef.applying(offset, additionalOffset: 2)!
  return accessFn[](genericArgs).assumingMemoryBound(to: TypeMetadata.self)
}
```

我们检查混淆名称的前两个字节是否具有访问器函数的签名。然后加载存储在“混淆名称”中的相对指针，将其解析为指向函数的绝对指针，然后调用该函数并假设结果正是我们想要的。（`init(fromUnalignedBytes:)` 是一个辅助函数，用于从 `UnsafePointer<UInt8>` 重建一个 32 位有符号偏移量。）这就是你能从我这里得到的全部“混淆名称处理”。抱歉！

## `copySuperclassMetadataToSubclass(_:_:)`

一个类需要从其超类中获取哪些信息？最明显的是方法，但如果不支持库演化（library evolution），这实际上可以在编译时解析。相反，有两件事取决于_特定的_具体超类：泛型参数和字段偏移向量（field offset vector）。

- 为什么_超类的_泛型参数需要出现在_子类_中？因为我们将要调用从超类继承的方法，而这些方法期望超类的泛型参数位于类元数据中的特定偏移处。
- 什么是“字段偏移向量”？实际上，在[结构体元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#what-about-structs)的初始化中已经提到过它。它将存储结构体/类中每个字段的偏移量，这样当你访问像下面这样的类中的 `second` 字段时：

  ```
  class Pair<First, Second> {
    var first: First
    var second: Second
  }
  ```

  ……偏移量就不必每次都重新计算。同样，超类字段的偏移量需要复制到子类元数据中，以便超类的_方法_可以直接访问存储属性（stored properties）。
- 我们能从超类中获得所有这些信息吗？事实证明，不能！我们_只_需要泛型参数和字段偏移量；如果我们复制超类中_所有_内容，就会覆盖此类已重写方法的任何条目。当然，我们可以在之后用某种方式将这些方法_复制回去_，但那样的话，我们要么增加用于专用函数的代码体积，要么采用比简单地进行一系列范围复制更复杂的方法。因此 Swift 运行时选择遍历整个超类链，以决定需要复制哪些位。（不过，它仍然只从直接超类（immediate superclass）获取这些位，以避免访问比所需更多的内存和缓存行（cache lines）。）

```
private func copySuperclassMetadataToSubclass(
  _ metadata: UnsafeMutablePointer<ClassMetadata>,
  _ flags: ClassLayoutFlags
) {
  guard let superclass = metadata[]._.superclass else { return }

  let rawMetadata = UnsafeMutableRawPointer(metadata)
  let rawSuperclass = UnsafeRawPointer(superclass)

  for ancestor in sequence(first: superclass, next: { $0[]._.superclass }) {
    let description = ancestor[]._.description

    if let generics = description.upcast(to: \._.base).fullGenericContextHeader {
      let offset = description[].metadataBounds.immediateMembersOffset
      let superclassGenericArgs =
        (rawSuperclass + offset).assumingMemoryBound(to: UnsafeRawPointer.self)
      (rawMetadata + offset).initializeMemory(
        as: UnsafeRawPointer.self,
        from: superclassGenericArgs,
        count: generics[]._.base.totalArgumentCount)
    }

    if !flags.hasStaticVTable {
      fatalError("This should never happen without library evolution.")
    }

    if description[]._.fieldOffsetVectorOffset != 0 {
      let offset = Int(description[]._.fieldOffsetVectorOffset) &*
        MemoryLayout<UInt>.size
      let superclassFieldOffsets =
        (rawSuperclass + offset).assumingMemoryBound(to: UInt.self)
      (rawMetadata + offset).initializeMemory(
        as: UInt.self,
        from: superclassFieldOffsets,
        count: Int(description[]._.numFields))
    }
  }
}
```

实际上，编译器和运行时可以做一个优化但没有做，那就是当泛型参数与超类完全相同时，不进行复制。

```
class ChildWrapper<Value> : ParentWrapper<Value>
```

但这仅在它们与超类的泛型参数_完全_相同时才有效，包括所有约束。^[3](#fn:key)否则，我们必须将额外信息存储在其他地方，那么请求“某个类型的泛型参数”的逻辑将会丢失关于如何使用该类型的重要信息！（运行时中还有其他逻辑假设泛型参数在内存中是连续的。）这也意味着需要在类上为泛型参数所在位置存储一个额外的字段，而不是简单地假设它们位于“直接成员”（immediate members）区域的起始位置。所以也许这不值得。

## `initClassFieldOffsetVector(_:_:_:_:)`

在完成了上述关于超类的一切之后，最后这部分应该看起来令人欣慰地熟悉——它基本上与 [`swift_initStructMetadata`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#what-about-structs) 所做的相同。

```
private func initClassFieldOffsetVector(
  _ metadata: UnsafeMutablePointer<ClassMetadata>,
  _ numFields: UInt,
  _ fieldTypes: UnsafePointer<UnsafePointer<TypeLayout>>,
  _ fieldOffsets: UnsafeMutablePointer<UInt>
) {
  let size: UInt
  let alignMask: UInt32

  if let superclass = metadata[]._.superclass {
    size = UInt(superclass[]._.instanceSize)
    alignMask = UInt32(superclass[]._.instanceAlignMask)
  } else {
    size = 2 &* UInt(MemoryLayout<UInt>.size)
    alignMask = UInt32(MemoryLayout<UInt>.alignment) &- 1
  }

  var layout = TypeLayout((
    size: size,
    stride: size,
    flags: ValueWitnessFlags(rawValue: alignMask),
    extraInhabitantCount: 0))

  let fields = UnsafeBufferPointer(start: fieldTypes, count: Int(numFields))
  performBasicLayout(&layout, fields.lazy.map { $0[] }) {
    fieldOffsets[$0] = UInt($1)
  }
  metadata[]._.instanceSize = UInt32(layout._.size)
  metadata[]._.instanceAlignMask = UInt16(layout._.flags.alignMask)
}
```

我们从超类的大小和对齐开始，或者如果没有超类，则从[堆对象头部（heap object header）](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/)开始。对于类，我们不需要关心步长（stride）或额外居民（extra inhabitants），所以我们不费心将这些字段设置为其精确值，只需设置为不会破坏 [`performBasicLayout(_:_:setOffset:)`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#all-together-now) 的某个值即可。（太好了，我们可以一直复用 `performBasicLayout(_:_:setOffset:)`！）

## 总结

至此，我们已经看到了创建和初始化类元数据的完整过程，就像我们对结构体所做的那样。当然，在很多情况下，编译器能够在编译时完成大部分工作，但如果不能，Swift 运行时也足够强大，可以自行完成所有工作。

我们已经讨论了结构体和类；[下一次我们终于要讨论枚举了](https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/)。

1. 我当时在 Apple 从事 Swift 的工作，但与此功能关系不大，因此我不把自己包括在内。[↩︎](#fnref:they)
2. 术语“反混淆器”（demangler）通常指一个工具，用于获取混淆名称并打印出其扁平的、人类可读的形式，这些工具甚至可能不需要构建名称的结构化表示。但由于 Swift 对“反混淆树”（demangle trees）的处理远不止是展示给人类，因此人类可读的打印只是另一个消费者。你可以通过将 `-expand` 选项传递给 `swift-demangle` 来查看这些树的结构。[↩︎](#fnref:structure)
3. 严格来说，唯一重要的约束是[那些被视为“键”（key）或“额外”（extra）参数的约束](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/#choosing-our-cache-key)；同类型约束（same-type constraints）实际上不会为泛型类型添加任何运行时信息。[↩︎](#fnref:key)

这篇文章发布于 [2020](https://belkadan.com/blog/2020)年[10月](https://belkadan.com/blog/2020/10) 06 日，归类在 [技术](https://belkadan.com/blog/technical) 下。标签：[Swift](https://belkadan.com/blog/tags/swift), [Swift 运行时](https://belkadan.com/blog/tags/swift-runtime)
