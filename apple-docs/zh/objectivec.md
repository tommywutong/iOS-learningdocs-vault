---
title: Objective-C Runtime
framework: Objective-C Runtime
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec
source_url: 'https://developer.apple.com/documentation/objectivec'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec.json'
content_hash: 'sha256:3ed1a38a61fe5b10'
translated: true
---

> 导航： [技术](technologies.md)

# Objective-C Runtime

<sub>框架</sub>

获得对 Objective-C runtime 及 Objective-C 根类型的底层访问能力。

## 概述

[Objective-C Runtime](objectivec.md) 模块 API 定义了 Objective-C 语言的基础。这些 API 包括：

- 类型，例如提供大多数 Objective-C 类根功能的 [NSObject](objectivec/nsobject-swift.class.md) 类和 [NSObjectProtocol](objectivec/nsobjectprotocol.md) 协议
- 构成 Objective-C runtime 的函数与数据结构，为 Objective-C 语言的动态特性提供支持

通常你不需要直接使用这个模块。

## 主题

### 类

- [NSObject](objectivec/nsobject-swift.class.md) — 大多数 Objective-C 类层级结构的根类，子类由此继承与 runtime 系统交互的基本接口，以及作为 Objective-C 对象运作的能力。
- [Protocol](objectivec/protocol.md)

### 协议

- [NSObjectProtocol](objectivec/nsobjectprotocol.md) — 所有 Objective-C 对象所共有的基础方法。

### 参考

- [Objective-C Runtime](objectivec/objective-c-runtime.md) — 描述 macOS 上 Objective-C runtime 库支持的函数和数据结构。
- [Objective-C Structures](objectivec/objective-c-structures.md)
- [Objective-C Constants](objectivec/objective-c-constants.md)
- [Objective-C Functions](objectivec/objective-c-functions.md)
- [Objective-C Data Types](objectivec/objective-c-data-types.md)
- [Objective-C Macros](objectivec/objective-c-macros.md)
- [Objective-C Enumerations](objectivec/objective-c-enums.md)

### 函数

- [objc_copyImageHeaders](<objectivec/objc_copyimageheaders(__).md>) — 返回当前进程中已加载的、包含 Objective-C 或 Swift 代码的所有映像的 Mach 头。 _(beta)_
