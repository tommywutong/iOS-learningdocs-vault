---
title: Swift 运行时：类型元数据
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/'
original_language: en
published: 2020-09-14
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ce8250a287e54d79'
translated: true
---

> 原文：[The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/)

[The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/) »

« [The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/?tag=swift)

[The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/?tag=swift) »

« [The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/?tag=swift-runtime)

[The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/?tag=swift-runtime) »

## [Swift 运行时：类型元数据](#)

欢迎来到 [Swift 运行时](https://belkadan.com/blog/tags/swift-runtime)系列文章的第三篇。本系列的目标是参照我在 [Swift on Mac OS 9 项目](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/)中的经验，逐一剖析 Swift 运行时（Swift Runtime）的各项功能。这次我们要讨论的是**类型元数据（Type Metadata）**，即类型在运行时的表示。

如前所述，我在实现自己的精简版运行时时，尽可能使用了 Swift 本身来编写，尽管为此不得不借助一些未文档化的 Swift 特性。在整个系列文章中，我将展示部分运行时代码片段，你可以在 [ppc-swift 仓库](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime)中查看完整实现。

### 背景

在某些语言中，类型纯粹是编译期概念。它们在开发者和编译器之间提供了一条沟通渠道，用于捕捉错误（“那是浮点数，不是指针”）、抽象操作（“读取第三个字段”而非“读取偏移 8 处的两字节值”）以及优化（“这个无符号整数永远不会小于 0”）。但许多其他语言——如今可能是**大多数**语言——同样至少具有一些类型的运行时用途，例如验证类型（“将此转换为表格视图”）、根据类型执行不同操作（“重写此方法”）以及检查类型及其实例的信息（“转储此结构体的内容”）。而某些语言**仅**以运行时方式使用类型，完全放弃编译期用途。

Swift 是一种介于两者之间的语言，既在编译期也在运行时使用类型。类型最明显的运行时用途是当你显式编写 `Array<Int>.self` 时，但当你使用泛型类型或泛型函数、将具体值转换为协议类型或在类上调用可重写方法时，它们也会出现。因此，运行时必须提供信息来表示类型。

### 在运行时表示类型

在 Swift 中，类型由指向结构化数据的唯一指针表示，这些数据可以是静态或动态分配的。根据我们讨论的**是哪种**类型，这些数据采用不同的表示形式，因此如果我们不确定拥有的类型种类，只能安全访问两个字段：偏移 0 处的**种类（kind）** 字段，以及位于类型元数据**起始地址之前**的值见证表（Value Witness Table）指针^[1](#fn:vwt)。要获取其他任何信息，我们必须先检查种类，然后转换为适当的类型。

在这篇文章中，我们将重点关注结构体元数据（Struct Metadata），实际上它与枚举元数据（Enum Metadata）共享其布局。结构体元数据添加了一个必需字段：指向**类型上下文描述符（Type Context Descriptor）** 的指针。那是什么？如果类型元数据表示一个完全具体的类型，如 `Array<Int>`，那么类型描述符表示一个类型声明，如 `Array`。事实证明，**这里**才是类型大部分有趣反射信息的存放位置，例如其名称、字段或 case 的描述以及泛型参数上的约束（如果有）。没有理由为泛型类型的每个具体实例化都保留一份单独的副本，因此 Swift 将其分开存储。（类型描述符也是用于查找某个类型是否符合某个协议的键，因为这必须独立于当前使用的任何泛型参数。）

而 `Array<Int>` **确实**需要存储的是 `Int`——即任何泛型参数，以及满足这些泛型参数约束的符合性。这些数据紧跟在结构体元数据主体之后存储，这意味着泛型结构体元数据的总分配大小将是“2 个指针 + 1 个指针大小的种类字段 + 一些额外的数据”。运行时实际上不需要频繁操作这些数据；它只需将其复制进来，并让类型的各个方法根据需要访问。

那么让我们开始构建泛型结构体元数据分配函数：

```
@_cdecl("swift_allocateGenericValueMetadata")
func swift_allocateGenericValueMetadata(
  _ rawDescription: TypeErasedPointer<TypeContextDescriptor>,
  _ arguments: UnsafePointer<UnsafeRawPointer>,
  _ pattern: TypeErasedPointer<GenericValueMetadataPattern>,
  _ extraDataSize: UInt
) -> TypeErasedPointer<ValueMetadata> {
  let description = rawDescription.assumingMemoryBound(to: TypeContextDescriptor.self)

  let headerSize = MemoryLayout<UnsafePointer<ValueWitnessTable>>.size
  let totalSize = headerSize + MemoryLayout<ValueMetadata>.size + Int(extraDataSize)
  let bytes = UnsafeMutableRawPointer(NewPtr(totalSize)!)

  let rawMetadata = (bytes + headerSize)
  // 为本文进行了简化；
  // 实际上我们需要检查是结构体还是枚举。
  _ = rawMetadata.bindMemory(to: StructMetadata.self, capacity: 1)

  // 示意部分 1（将在下面解释）
  initializeValueMetadata(
    rawMetadata.assumingMemoryBound(to: ValueMetadata.self),
    description: description,
    from: pattern.assumingMemoryBound(to: GenericValueMetadataPattern.self))

  // 示意部分 2（将在下面解释，也适用于类）
  installGenericArguments(
    in: rawMetadata.assumingMemoryBound(to: TypeMetadata.self),
    at: MemoryLayout<ValueMetadata>.size,
    description: description,
    from: arguments)

  return UnsafeRawPointer(rawMetadata)
}
```

`swift_allocateGenericValueMetadata` 被传入了一个类型描述符和一些泛型参数，但它还接收了一个**模式（pattern）** 和一个“额外数据大小”值。这些是干什么用的？嗯，“额外数据大小”表示泛型参数所需的空间……以及与该类型相关的任何其他内容。（还记得上篇文章中的那些“字段偏移”吗？）模式将在 `initializeValueMetadata` 中用于设置元数据，然后 `installGenericArguments` 将泛型参数复制到固定大小元数据之后的位置。相当直接，对吧？

### 填充字段

让我们“放大”这些辅助函数，从 `initializeValueMetadata` 开始。这将需要设置种类和值见证表指针，我想还要复制描述符指针。

```
private func initializeValueMetadata(
  _ metadata: UnsafeMutablePointer<ValueMetadata>,
  description: UnsafePointer<TypeContextDescriptor>,
  from pattern: UnsafePointer<GenericValueMetadataPattern>
) {
  UnsafeMutableRawPointer(metadata).storeBytes(
    of: pattern.valueWitnesses,
    toByteOffset: -MemoryLayout<UnsafeRawPointer>.stride,
    as: UnsafePointer<ValueWitnessTable>.self)
  metadata[]._.base.rawKind = pattern[]._.base._.flags.value_metadataKind
  metadata[]._.description = description

  if pattern[]._.base._.flags.hasExtraDataPattern {
    let extraData = UnsafeMutableRawPointer(metadata + 1)
    extraData.initialize(from: pattern.extraDataPattern)
  }
}
```

这次我不打算展示这些结构体的完整布局，但你可以看到 `ValueMetadata` 有一个表示 `TypeMetadata` 部分的 `base` 字段，而 `GenericValueMetadataPattern` 有一个表示通用 `GenericMetadataPattern` 的 `base` 字段，这使得这成为一种类似子类化的做法。值见证指针来自模式而非类型描述符，这允许类型描述符数据存储在真正的常量内存中（通过不引用来自其他库的任何东西）。奇怪的是，种类也来自模式；我原本以为它会从类型描述符的种类派生出来。（不过，它不会完全相同，因为可选类型非常重要，以至于它们拥有自己的元数据种类，尽管它们本就是枚举的一种。）

这个函数做的另一件事是复制一个“额外数据模式”，就在内存中 `ValueMetadata` 必需字段之后的位置。（这就是 `UnsafeMutableRawPointer(metadata + 1)` 的含义。）这还不是泛型参数，因为它们被单独传递，但它可以包含字面值，或者只是将大量额外数据清零以备后用。

```
extension UnsafeMutableRawPointer {
  func initialize(from pattern: UnsafePointer<GenericMetadataPartialPattern>) {
    let offsetInBytes = Int(pattern[]._.offsetInWords) &* MemoryLayout<UInt>.size
    memset(self, 0, offsetInBytes)
    (self + offsetInBytes).copyMemory(
      from: pattern.data,
      byteCount: Int(pattern[]._.sizeInWords) &* MemoryLayout<UInt>.size)
  }
}
```

这种 C 和 Swift 底层内存操作混合使用是为了遵守 Swift 的[指针类型规则](https://twitter.com/AirspeedSwift/status/1276565629609230336)。Swift 的指针没有提供一种很好的方式来**在未赋予类型的情况下**将内存清零，或者复制已知仅包含未知但平凡类型的值**并**保留这些类型的内存。（`copyMemory` 保留当前类型而不是覆盖它。）

至此，剩下要做的就是复制泛型参数。这基本上很简单：

```
private func installGenericArguments(
  in metadata: UnsafeMutablePointer<TypeMetadata>,
  at offset: Int,
  description: UnsafePointer<TypeContextDescriptor>,
  from arguments: UnsafePointer<UnsafeRawPointer>
{
  let generics = description.fullGenericContextHeader!
  let argumentStart = UnsafeMutableRawPointer(metadata) + byteOffset
  argumentStart.initializeMemory(
    as: UnsafeRawPointer.self,
    from: arguments,
    count: generics[]._.base.totalArgumentCount)
}
```

你是不是开始习惯于阅读那些使用元组布局的指向结构体的指针表达式了？那么你可能会注意到这里有一个不太合适的地方：`description` 是一个指针，但我们在它上面直接访问 `fullGenericContextHeader`。这意味着什么？其实没什么大不了：它只是试图访问存储在类型描述符末尾的数据，为此需要计算一个新指针。

```
extension UnsafePointer where Pointee == TypeContextDescriptor {
  var fullGenericContextHeader: UnsafePointer<TypeGenericContextDescriptorHeader> {
    let trailingObjectPtr: UnsafeRawPointer
    switch self[]._.base._.flags.kind {
    case .struct:
      trailingObjectPtr = UnsafeRawPointer(self) + MemoryLayout<StructDescriptor>.stride
    case .class:
      trailingObjectPtr = UnsafeRawPointer(self) + MemoryLayout<ClassDescriptor>.stride
    case .enum:
      trailingObjectPtr = UnsafeRawPointer(self) + MemoryLayout<EnumDescriptor>.stride
    default:
      fatalError()
    }
    return trailingObjectPtr.assumingMemoryBound(to: TypeGenericContextDescriptorHeader.self)
  }
}
```

就是这样，我们已经构建了一个有效的泛型类型！

### 总结

我们现在知道了泛型类型的类型元数据是如何在运行时构建的：给定一个类型描述符、一个模式和某些泛型参数，就会分配并填充一个新的类型。但上次的 [`swift_initStructMetadata`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#what-about-structs) 调用在哪里？又是谁调用了 `swift_allocateGenericValueMetadata` 呢？它不可能每次有人需要 `Array<Int>` 的类型时都被调用，因为那样最终可能会分配同一个类型的数千个副本。[我们需要某种形式的缓存，这将在下次讨论。](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/)

1. 正如上篇文章中简要提到的，值见证表定义了类型的基本操作，这对于完全泛型的函数是必需的。（当你写 `var x: T = y` 时，为 `x` 分配了多少内存，以及它如何从 `y` 初始化每个字段？）它位于负偏移处，以便在现代化的 Apple 平台上，Swift 类类型能与 Objective-C 类类型保持兼容的布局。[↩︎](#fnref:vwt)

这条目发布于 [2020 年](https://belkadan.com/blog/2020)[9 月](https://belkadan.com/blog/2020/09) 14 日，归入 [技术](https://belkadan.com/blog/technical) 分类。标签：[Swift](https://belkadan.com/blog/tags/swift)、[Swift 运行时](https://belkadan.com/blog/tags/swift-runtime)
