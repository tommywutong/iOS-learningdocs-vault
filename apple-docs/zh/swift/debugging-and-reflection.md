---
title: 调试与反射
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/debugging-and-reflection
source_url: 'https://developer.apple.com/documentation/swift/debugging-and-reflection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/debugging-and-reflection.json'
content_hash: 'sha256:48d6b35beaba138a'
translated: true
---

> 导航： [技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md)

# 调试与反射

<sub>API 集合</sub>

使用运行时检查强化你的代码，并检查你的值的运行时表示。

## 主题

### 打印与转储

- [print(_:separator:terminator:)](<print(__separator_terminator_).md>) — 将给定条目的文本表示写入标准输出。
- [print(_:separator:terminator:to:)](<print(__separator_terminator_to_).md>) — 将给定条目的文本表示写入给定的输出流。
- [debugPrint(_:separator:terminator:)](<debugprint(__separator_terminator_).md>) — 将给定条目最适合调试的文本表示写入标准输出。
- [debugPrint(_:separator:terminator:to:)](<debugprint(__separator_terminator_to_).md>) — 将给定条目最适合调试的文本表示写入给定的输出流。
- [dump(_:name:indent:maxDepth:maxItems:)](<dump(__name_indent_maxdepth_maxitems_).md>) — 使用给定对象的镜像（mirror），将其内容转储到标准输出。
- [dump(_:to:name:indent:maxDepth:maxItems:)](<dump(__to_name_indent_maxdepth_maxitems_).md>) — 使用给定对象的镜像，将其内容转储到指定的输出流。

### 测试

- [assert(_:_:file:line:)](<assert(____file_line_).md>) — 执行一个传统 C 风格的断言，可附带一条可选消息。
- [assertionFailure(_:file:line:)](<assertionfailure(__file_line_).md>) — 表示内部一致性检查失败。
- [precondition(_:_:file:line:)](<precondition(____file_line_).md>) — 检查继续执行所必需的一项前置条件。
- [preconditionFailure(_:file:line:)](<preconditionfailure(__file_line_).md>) — 表示某个前置条件被违反。

### 退出程序

- [fatalError(_:file:line:)](<fatalerror(__file_line_).md>) — 无条件打印给定消息并停止执行。
- [Never](never.md) — 一种没有值、且无法被构造的类型。

### 查询运行时值

- [Mirror](mirror.md) — 对任意类型实例的子结构和显示样式的一种表示。
- [ObjectIdentifier](objectidentifier.md) — 类实例、actor 实例或元类型的唯一标识符。
- [type(of:)](<type(of_).md>) — 返回一个值的动态类型。

### 定制你的类型的反射

- [CustomReflectable](customreflectable.md) — 一种显式提供自身镜像的类型。
- [CustomLeafReflectable](customleafreflectable.md) — 一种显式提供自身镜像的类型，但其子类除非也重写了 `customMirror`，否则不会在镜像中表示出来。
- [CustomPlaygroundDisplayConvertible](customplaygrounddisplayconvertible.md) — 一种为 playground 日志记录提供自定义描述的类型。
- [PlaygroundQuickLook](playgroundquicklook.md) — 可用作 Quick Look 表示形式的各类型的联合。
- [DebugDescription()](<debugdescription().md>) — 将描述定义转换为调试器的类型摘要（Type Summary）。

## 另请参阅

### 编程任务

- [Input and Output](input-and-output.md) — 将值打印到控制台，从文本流中读取和写入，并使用命令行参数。
- [Macros](macros.md) — 生成样板代码，并执行其他编译期操作。
- [Concurrency](concurrency.md) — 执行异步和并行操作。
- [Key-Path Expressions](key-path-expressions.md) — 使用键路径表达式动态访问属性。
- [Manual Memory Management](manual-memory-management.md) — 手动分配和管理内存。
- [Type Casting and Existential Types](type-casting-and-existential-types.md) — 在类型之间执行转换，或表示任意类型的值。
- [C Interoperability](c-interoperability.md) — 使用导入的 C 类型，或调用 C 可变参数函数。
- [Operator Declarations](operator-declarations.md) — 使用前缀、后缀和中缀运算符。
