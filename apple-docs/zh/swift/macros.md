---
title: 宏
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/macros
source_url: 'https://developer.apple.com/documentation/swift/macros'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/macros.json'
content_hash: 'sha256:53388320837587b0'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md)

# 宏

<sub>API 集合</sub>

生成样板代码并执行其他编译期操作。

## 主题

### 基础

- [应用宏](applying-macros.md) — 使用宏在编译期生成重复性的代码。

### 获取源码位置信息

- [file()](<file().md>) — 产生它所在文件的路径。
- [fileID()](<fileid().md>) — 产生宏所在源文件的唯一标识符。
- [filePath()](<filepath().md>) — 产生宏所在文件的完整路径。
- [function()](<function().md>) — 产生它所在声明的名称。
- [line()](<line().md>) — 产生它所在的行号。
- [column()](<column().md>) — 产生宏开始处的列号。

### 生成编译期诊断

- [warning(_:)](<warning(__).md>) — 在编译期间产生给定的警告消息。
- [error(_:)](<error(__).md>) — 将给定消息作为致命错误发出，并终止编译过程。

### 编写自定义宏

- [externalMacro(module:type:)](<externalmacro(module_type_).md>) — 为宏的实现指定模块和类型名称。

### 访问动态共享对象句柄

- [dsohandle()](<dsohandle().md>) — 产生宏所在位置正在使用的动态共享对象（DSO）句柄。

## 另请参阅

### 编程任务

- [输入与输出](input-and-output.md) — 把值打印到控制台，从文本流读取和写入，并使用命令行实参。
- [调试与反射](debugging-and-reflection.md) — 用运行时检查加固你的代码，并查看你的值的运行时表示。
- [并发](concurrency.md) — 执行异步和并行操作。
- [键路径表达式](key-path-expressions.md) — 使用键路径表达式动态访问属性。
- [手动内存管理](manual-memory-management.md) — 手动分配和管理内存。
- [类型转换与既存类型](type-casting-and-existential-types.md) — 在类型之间执行转换，或表示任何类型的值。
- [C 互操作性](c-interoperability.md) — 使用导入的 C 类型或调用 C 可变参数函数。
- [运算符声明](operator-declarations.md) — 使用前缀、后缀和中缀运算符。
