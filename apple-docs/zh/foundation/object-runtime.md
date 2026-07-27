---
title: 对象运行时
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/object-runtime
source_url: 'https://developer.apple.com/documentation/foundation/object-runtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/object-runtime.json'
content_hash: 'sha256:dd6e4c4c8642fb4e'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 对象运行时

<sub>API 集合</sub>

获取对 Objective-C 基本功能、Cocoa 设计模式和 Swift 集成的底层支持。

## 主题

### 对象基础

- [NSObject](../objectivec/nsobject-swift.class.md) — 大多数 Objective-C 类层级结构的根类，子类从中继承运行时系统的基本接口以及作为 Objective-C 对象运行的能力。
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md) — 对所有 Objective-C 对象都至关重要的一组方法。
- [NSKeyValueCoding](../objectivec/nskeyvaluecoding.md) — 一种通过名称或键间接访问对象属性的机制。

### 复制

- [NSCopying](nscopying.md) — 对象为提供自身功能性副本而采纳的协议。
- [NSMutableCopying](nsmutablecopying.md) — 可变对象为提供自身功能性副本而采纳的协议。

### 值包装器与转换

- [NSNumber](nsnumber.md) — 原始标量数值的对象包装器。
- [NSValue](nsvalue.md) — 单个 C 或 Objective-C 数据项的简单容器。
- [ValueTransformer](valuetransformer.md) — 用于将值从一种表示转换为另一种表示的抽象类。

### Swift 支持

- [ReferenceConvertible](referenceconvertible.md) — 应用于由 Foundation 引用类型支持的类型的一种修饰。
- [桥接到 Swift 标准库值类型的类](classes-bridged-to-swift-standard-library-value-types.md) — 需要引用语义或 Foundation 专属行为时使用桥接的引用类型。

### 远程对象

- [NSProxy](nsproxy.md) — 一个抽象超类，定义供对象作为其他对象或尚不存在的对象之替身使用的 API。

### 内存管理

- [内存管理函数](memory-management-functions.md) — 执行底层内存管理任务。

### Objective-C 运行时

- [Objective-C 运行时实用工具](objective-c-runtime-utilities.md) — 与 Objective-C 运行时交互。

### 版本与 API 可用性

- [Foundation 框架版本号](foundation-framework-version-numbers.md) — 识别用于将当前运行的 Foundation 版本与已知操作系统版本号进行比较的常量。

### 旧式

- [分布式对象支持](distributed-objects-support.md) — 支持不同进程中的对象相互通信，包括本地系统和远程系统上的对象。
- [Objective-C 垃圾回收](objective-c-garbage-collection.md) — 与旧式垃圾回收系统交互。

## 另请参阅

### 底层实用工具

- [XPC](xpc.md) — 管理安全的进程间通信。
- [进程与线程](processes-and-threads.md) — 管理 App 与宿主操作系统及其他进程的交互，并实现底层并发功能。
- [流、套接字与端口](streams-sockets-and-ports.md) — 使用底层 Unix 功能管理文件、进程和网络之间的输入与输出。
