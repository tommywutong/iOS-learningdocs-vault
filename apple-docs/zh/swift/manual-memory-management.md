---
title: 手动内存管理
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/manual-memory-management
source_url: 'https://developer.apple.com/documentation/swift/manual-memory-management'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/manual-memory-management.json'
content_hash: 'sha256:44ed74dcb790ce43'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# 手动内存管理

<sub>API 集合</sub>

手动分配和管理内存。

## 主题

### 起步

- [Calling Functions With Pointer Parameters](calling-functions-with-pointer-parameters.md) — 在调用接受指针参数的函数时，使用隐式指针转换或桥接。

### 安全的内存访问

- [Span](span.md) — `Span<Element>` 表示一段连续的内存区域，其中包含已初始化的 `Element` 实例。
- [RawSpan](rawspan.md) — `RawSpan` 表示一段包含已初始化字节的连续内存区域。
- [OutputSpan](outputspan.md) — `OutputSpan` 是对一段连续内存区域的引用，该区域以若干已初始化的 `Element` 实例开头，后面跟着未初始化的内存。它提供了访问其存储项、添加新元素以及移除现有元素的操作。
- [OutputRawSpan](outputrawspan.md) — `OutputRawSpan` 是对一段连续内存区域的引用，该区域以若干已初始化的字节开头，后面跟着未初始化的内存。它提供了访问其存储字节、追加字节以及移除字节的操作。
- [UTF8Span](utf8span.md) — 对包含合法编码的 UTF-8 码元的连续内存的一个借用视图。
- [MutableSpan](mutablespan.md) — `MutableSpan<Element>` 表示一段连续的内存区域，其中包含已初始化的 `Element` 实例。
- [MutableRawSpan](mutablerawspan.md) — `MutableRawSpan` 表示一段包含已初始化字节的连续内存区域。
- [SpanIterator](spaniterator.md) _(beta)_

### 对原始字节的安全访问

- [FullyInhabited](fullyinhabited.md) — 适用于那些内存可以安全地写为原始字节或从原始字节读取的类型的协议。
- [ConvertibleFromBytes](convertiblefrombytes.md) — 适用于那些内存可以安全地由原始字节填充、从而得到一个有效实例的类型的协议。
- [ConvertibleToBytes](convertibletobytes.md) — 适用于那些内存可以安全地按单个原始字节读取的类型的协议。
- [ByteOrder](byteorder.md) — 内存中的一种字节序。 _(beta)_
- [bitCast(_:to:)](<bitcast(__to_).md>) — 返回给定实例的位模式，并将其解释为指定的类型。

### 有类型指针

- [UnsafePointer](unsafepointer.md) — 用于访问特定类型数据的指针。
- [UnsafeMutablePointer](unsafemutablepointer.md) — 用于访问和操作特定类型数据的指针。
- [UnsafeBufferPointer](unsafebufferpointer.md) — 对连续存储在内存中的一组元素的非持有集合接口。
- [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md) — 对连续存储在内存中的一组可变元素的非持有集合接口。

### 原始指针

- [UnsafeRawPointer](unsaferawpointer.md) — 用于访问无类型数据的原始指针。
- [UnsafeMutableRawPointer](unsafemutablerawpointer.md) — 用于访问和操作无类型数据的原始指针。
- [UnsafeRawBufferPointer](unsaferawbufferpointer.md) — 对一段内存区域中字节的非持有集合接口。
- [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md) — 对一段内存区域中字节的可变非持有集合接口。

### 内存访问

- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-9fjn6.md>) — 使用指向给定实参的指针调用给定闭包。
- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-35wrn.md>) — 使用指向给定实参的指针调用给定闭包。
- [withUnsafeMutablePointer(to:_:)](<withunsafemutablepointer(to___).md>) — 使用指向给定实参的可变指针调用给定闭包。
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-3ywhh.md>) — 使用覆盖给定实参原始字节的缓冲区指针调用给定闭包。
- [withUnsafeMutableBytes(of:_:)](<withunsafemutablebytes(of___).md>) — 使用覆盖给定实参原始字节的可变缓冲区指针调用给定闭包。
- [withTemporaryAllocation(byteCount:alignment:_:)](<withtemporaryallocation(bytecount_alignment___).md>) — 提供对具有指定字节数和对齐方式的输出原始 span 的作用域访问。
- [withTemporaryAllocation(of:capacity:_:)](<withtemporaryallocation(of_capacity___).md>) — 提供对具有指定类型和容量的输出 span 的作用域访问。
- [withUnsafeTemporaryAllocation(of:capacity:_:)](<withunsafetemporaryallocation(of_capacity___).md>) — 提供对具有指定类型和容量的内存的缓冲区指针的作用域访问。
- [withUnsafeTemporaryAllocation(byteCount:alignment:_:)](<withunsafetemporaryallocation(bytecount_alignment___).md>) — 提供对具有指定字节数和对齐方式的原始缓冲区指针的作用域访问。
- [swap(_:_:)](<swap(____).md>) — 交换两个实参的值。
- [exchange(_:with:)](<exchange(__with_).md>) — 用提供的新值替换某个可变值的值，并返回原值。

### 内存布局

- [MemoryLayout](memorylayout.md) — 一个类型的内存布局，描述其大小、步幅和对齐方式。

### 堆存储

- [UniqueArray](uniquearray.md) — 一个动态自调整大小、堆分配、其元素可能不可复制的不可复制数组。 _(beta)_
- [UniqueBox](uniquebox.md) — 一种智能指针类型，在堆上唯一拥有一个 `Value` 实例。 _(beta)_

### 引用计数

- [Unmanaged](unmanaged.md) — 用于传播非托管对象引用的一种类型。
- [withExtendedLifetime(_:_:)](<withextendedlifetime(____)-4mmpv.md>) — 对闭包求值，同时确保给定实例在闭包返回之前不会被销毁。
- [withExtendedLifetime(_:_:)](<withextendedlifetime(____)-59dz3.md>) — 对闭包求值，同时确保给定实例在闭包返回之前不会被销毁。
- [extendLifetime(_:)](<extendlifetime(__).md>) — 延长给定实例的生命周期。

## 另请参阅

### Programming Tasks

- [Input and Output](input-and-output.md) — 将值打印到控制台，从文本流读取或写入文本流，并使用命令行参数。
- [Debugging and Reflection](debugging-and-reflection.md) — 用运行时检查强化你的代码，并检查你的值的运行时表示。
- [Macros](macros.md) — 生成样板代码并执行其他编译期操作。
- [Concurrency](concurrency.md) — 执行异步和并行操作。
- [Key-Path Expressions](key-path-expressions.md) — 使用键路径表达式动态访问属性。
- [Type Casting and Existential Types](type-casting-and-existential-types.md) — 在类型之间执行转换，或表示任意类型的值。
- [C Interoperability](c-interoperability.md) — 使用导入的 C 类型或调用 C 可变参数函数。
- [Operator Declarations](operator-declarations.md) — 使用前缀、后缀和中缀运算符。
</content>
