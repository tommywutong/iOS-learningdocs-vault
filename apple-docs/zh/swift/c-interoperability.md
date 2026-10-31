---
title: C 互操作性
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/c-interoperability
source_url: 'https://developer.apple.com/documentation/swift/c-interoperability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/c-interoperability.json'
content_hash: 'sha256:45370d01b902970d'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md)

# C 互操作性

<sub>API 集合</sub>

使用导入的 C 类型，或调用 C 可变参数函数。

## 主题

### C 与 Objective-C 指针

- [OpaquePointer](opaquepointer.md) — 不透明 C 指针的包装器。
- [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md) — 一个可变指针，指向一个不拥有其目标的 Objective-C 引用。

### C 可变参数函数

- [withVaList(_:_:)](<withvalist(____).md>) — 使用由给定实参数组导出的 C `va_list` 实参来调用给定的闭包。
- [CVaListPointer](cvalistpointer.md)
- [CVarArg](cvararg.md) — 一种类型，其实例可以作为 C `va_list` 的元素进行编码并恰当地传递。
- [getVaList(_:)](<getvalist(__).md>) — 返回一个 `CVaListPointer`，它由给定实参数组构建，并以自动释放存储作为后端。

### 指向值的指针

- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-9fjn6.md>) — 使用指向给定实参的指针调用给定闭包。
- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-35wrn.md>) — 使用指向给定实参的指针调用给定闭包。
- [withUnsafeMutablePointer(to:_:)](<withunsafemutablepointer(to___).md>) — 使用指向给定实参的可变指针调用给定闭包。
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-3ywhh.md>) — 使用覆盖给定实参原始字节的缓冲区指针调用给定闭包。
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-5gesg.md>) — 使用覆盖给定实参原始字节的缓冲区指针调用给定闭包。
- [withUnsafeMutableBytes(of:_:)](<withunsafemutablebytes(of___).md>) — 使用覆盖给定实参原始字节的可变缓冲区指针调用给定闭包。

### 导入的 C 类型的别名

- [CBool](cbool.md) — C 的 ‘_Bool’ 类型与 C++ 的 ‘bool’ 类型。
- [CChar](cchar.md) — C 的 ‘char’ 类型。
- [CChar8](cchar8.md) — C++20 的 ‘char8_t’ 类型，采用 UTF-8 编码。
- [CChar16](cchar16.md) — C++11 的 ‘char16_t’ 类型，采用 UTF-16 编码。
- [CChar32](cchar32.md) — C++11 的 ‘char32_t’ 类型，采用 UTF-32 编码。
- [CDouble](cdouble.md) — C 的 ‘double’ 类型。
- [CLongDouble](clongdouble.md)
- [CFloat](cfloat.md) — C 的 ‘float’ 类型。
- [CFloat16](cfloat16.md) — C 的 ‘_Float16’ 类型。
- [CInt](cint.md)
- [CLong](clong.md)
- [CLongLong](clonglong.md) — C 的 ‘long long’ 类型。
- [CShort](cshort.md) — C 的 ‘short’ 类型。
- [CSignedChar](csignedchar.md) — C 的 ‘signed char’ 类型。
- [CUnsignedChar](cunsignedchar.md) — C 的 ‘unsigned char’ 类型。
- [CUnsignedInt](cunsignedint.md)
- [CUnsignedLong](cunsignedlong.md)
- [CUnsignedLongLong](cunsignedlonglong.md) — C 的 ‘unsigned long long’ 类型。
- [CUnsignedShort](cunsignedshort.md) — C 的 ‘unsigned short’ 类型。
- [CWideChar](cwidechar.md)

## 另请参阅

### 编程任务

- [输入与输出](input-and-output.md) — 将值打印到控制台，从文本流中读取和写入，并使用命令行参数。
- [调试与反射](debugging-and-reflection.md) — 使用运行时检查强化你的代码，并检查你的值的运行时表示。
- [宏](macros.md) — 生成样板代码，并执行其他编译期操作。
- [并发](concurrency.md) — 执行异步和并行操作。
- [键路径表达式](key-path-expressions.md) — 使用键路径表达式动态访问属性。
- [手动内存管理](manual-memory-management.md) — 手动分配和管理内存。
- [类型转换与既存类型](type-casting-and-existential-types.md) — 在类型之间执行转换，或表示任意类型的值。
- [运算符声明](operator-declarations.md) — 使用前缀、后缀和中缀运算符。
