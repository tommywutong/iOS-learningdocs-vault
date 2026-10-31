---
title: 输入与输出
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/input-and-output
source_url: 'https://developer.apple.com/documentation/swift/input-and-output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/input-and-output.json'
content_hash: 'sha256:73b1e0e2977ee7d2'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md)

# 输入与输出

<sub>API 集合</sub>

将值打印到控制台，从文本流中读取和写入，并使用命令行参数。

## 主题

### 文本输出

- [print(_:separator:terminator:)](<print(__separator_terminator_).md>) — 将给定条目的文本表示写入标准输出。
- [print(_:separator:terminator:to:)](<print(__separator_terminator_to_).md>) — 将给定条目的文本表示写入给定的输出流。

### 命令行输入

- [CommandLine](commandline.md) — 当前进程的命令行实参。
- [readLine(strippingNewline:)](<readline(strippingnewline_).md>) — 返回一个从标准输入读取的字符串，读取到当前行末尾或到达 EOF 为止。

### 流

- [TextOutputStream](textoutputstream.md) — 可以作为文本流操作目标的一种类型。
- [TextOutputStreamable](textoutputstreamable.md) — 文本流操作的一种来源。

## 另请参阅

### 编程任务

- [调试与反射](debugging-and-reflection.md) — 使用运行时检查强化你的代码，并检查你的值的运行时表示。
- [宏](macros.md) — 生成样板代码，并执行其他编译期操作。
- [并发](concurrency.md) — 执行异步和并行操作。
- [键路径表达式](key-path-expressions.md) — 使用键路径表达式动态访问属性。
- [手动内存管理](manual-memory-management.md) — 手动分配和管理内存。
- [类型转换与既存类型](type-casting-and-existential-types.md) — 在类型之间执行转换，或表示任意类型的值。
- [C 互操作性](c-interoperability.md) — 使用导入的 C 类型，或调用 C 可变参数函数。
- [运算符声明](operator-declarations.md) — 使用前缀、后缀和中缀运算符。
