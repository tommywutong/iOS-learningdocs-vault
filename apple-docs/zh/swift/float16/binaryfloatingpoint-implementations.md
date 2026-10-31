---
title: BinaryFloatingPoint 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/binaryfloatingpoint-implementations
source_url: 'https://developer.apple.com/documentation/swift/float16/binaryfloatingpoint-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/binaryfloatingpoint-implementations.json'
content_hash: 'sha256:8933361ea8181be1'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [特殊用途数值类型](../special-use-numeric-types.md) · [Float16](../float16.md)

# BinaryFloatingPoint 实现

<sub>API 集合</sub>

## 主题

### 初始化方法

- [init(_:)](<init(__)-469bw.md>) — 创建一个近似于给定值的新实例。
- [init(_:)](<init(__)-6u8fq.md>) — 用给定值创建一个新实例，并舍入到最接近的可能表示。
- [init(_:)](<init(__)-7teyd.md>) — 创建一个新值，并舍入到最接近的可能表示。
- [init(_:)](<init(__)-7x3fq.md>) — 创建一个近似于给定值的新实例。
- [init(exactly:)](<init(exactly_)-6c0t5.md>) — 如果给定的整数可以被精确表示，则创建一个新值。
- [init(exactly:)](<init(exactly_)-d42j.md>) — 如果给定值可以被精确表示，则用该值创建一个新实例。
- [init(sign:exponentBitPattern:significandBitPattern:)](<init(sign_exponentbitpattern_significandbitpattern_).md>) — 用指定的符号和位模式创建一个新实例。

### 实例属性

- [binade](binade.md) — 一个浮点值，其符号和指数与此值相同，但有效数字为 1.0。
- [exponentBitPattern](exponentbitpattern.md) — 值的指数字段的原始编码。
- [significandBitPattern](significandbitpattern.md) — 值的有效数字字段的原始编码。
- [significandWidth](significandwidth.md) — 表示值的有效数字所需的位数。

### 类型别名

- [RawExponent](rawexponent.md) — 表示值的编码指数的类型。
- [RawSignificand](rawsignificand.md) — 表示值的编码有效数字的类型。

### 类型属性

- [exponentBitCount](exponentbitcount.md) — 用于表示该类型指数的位数。
- [significandBitCount](significandbitcount.md) — 可用的有效数字小数位数。

### 类型方法

- [random(in:)](<random(in_)-4blql.md>) — 返回指定范围内的一个随机值。
- [random(in:)](<random(in_)-6nryy.md>) — 返回指定范围内的一个随机值。
- [random(in:using:)](<random(in_using_)-1prt0.md>) — 返回指定范围内的一个随机值，使用给定的生成器作为随机源。
- [random(in:using:)](<random(in_using_)-9qt91.md>) — 返回指定范围内的一个随机值，使用给定的生成器作为随机源。
