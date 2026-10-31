---
title: 类型转换与既存类型
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/type-casting-and-existential-types
source_url: 'https://developer.apple.com/documentation/swift/type-casting-and-existential-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/type-casting-and-existential-types.json'
content_hash: 'sha256:f8810c278f3beb37'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# 类型转换与既存类型

<sub>API 集合</sub>

在类型之间执行转换，或表示任意类型的值。

## 主题

### 整数值转换

- [numericCast(_:)](<numericcast(__).md>) — 以另一种整数类型中的等价值返回给定的整数。

### 闭包转换

- [withoutActuallyEscaping(_:do:)](<withoutactuallyescaping(__do_).md>) — 允许非逃逸闭包暂时像可逃逸闭包一样使用。

### 实例转换

- [unsafeDowncast(_:to:)](<unsafedowncast(__to_).md>) — 将给定的实例无条件转换为指定类型并返回。
- [unsafeBitCast(_:to:)](<unsafebitcast(__to_).md>) — 返回给定实例的位，并将其解释为具有指定的类型。

### 既存类型

- [AnyObject](anyobject.md) — 所有类都隐式符合的协议。
- [AnyClass](anyclass.md) — 所有类类型都隐式符合的协议。

### 比较身份

- [===(_:_:)](<===(____).md>)
- [!==(_:_:)](<!==(____).md>) — 返回一个布尔值，指示两个引用是否指向不同的对象实例。

### Void 类型

- [Void](void.md) — 未显式指定返回类型的函数的返回类型，即空元组 `()`。

## 另请参阅

### 编程任务

- [Input and Output](input-and-output.md) — 向控制台输出值，从文本流读取和写入，并使用命令行参数。
- [Debugging and Reflection](debugging-and-reflection.md) — 使用运行时检查加固你的代码，并检查你的值的运行时表示。
- [Macros](macros.md) — 生成样板代码并执行其他编译期操作。
- [Concurrency](concurrency.md) — 执行异步和并行操作。
- [Key-Path Expressions](key-path-expressions.md) — 使用键路径表达式动态访问属性。
- [Manual Memory Management](manual-memory-management.md) — 手动分配和管理内存。
- [C Interoperability](c-interoperability.md) — 使用导入的 C 类型或调用 C 变参函数。
- [Operator Declarations](operator-declarations.md) — 使用前缀、后缀和中缀运算符。
