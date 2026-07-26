---
title: SIMD 向量类型
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/simd-vector-types
source_url: 'https://developer.apple.com/documentation/swift/simd-vector-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd-vector-types.json'
content_hash: 'sha256:4990b5141030ac32'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md) · [数字和基本值](numbers-and-basic-values.md)

# SIMD 向量类型

<sub>API 集合</sub>

处理由不同大小的定宽数值类型组成的定宽向量。

## 主题

### SIMD 向量

- [SIMD2](simd2.md) — 由两个标量值组成的向量。
- [SIMD3](simd3.md) — 由三个标量值组成的向量。
- [SIMD4](simd4.md) — 由四个标量值组成的向量。
- [SIMD8](simd8.md) — 由八个标量值组成的向量。
- [SIMD16](simd16.md) — 由 16 个标量值组成的向量。
- [SIMD32](simd32.md) — 由 32 个标量值组成的向量。
- [SIMD64](simd64.md) — 由 64 个标量值组成的向量。

### 支持类型

- [SIMD](simd.md) — 一种元素数量固定的 SIMD 向量。
- [SIMDScalar](simdscalar.md) — 一种可以用作 SIMD 向量元素的类型。
- [SIMDStorage](simdstorage.md) — 一种可以充当 SIMD 向量类型存储的类型。
- [SIMDMask](simdmask.md)

### 支持函数

- [all(_:)](<all(__).md>) — 如果掩码的每一个通道都为真，则返回真。
- [any(_:)](<any(__).md>) — 如果掩码的任意一个通道为真，则返回真。
- [pointwiseMax(_:_:)](<pointwisemax(____)-29hn2.md>) — 两个向量按通道取得的最大值。
- [pointwiseMax(_:_:)](<pointwisemax(____)-2k6er.md>) — 两个向量按通道取得的最大值。
- [pointwiseMin(_:_:)](<pointwisemin(____)-39txi.md>) — 两个向量按通道取得的最小值。
- [pointwiseMin(_:_:)](<pointwisemin(____)-8v95p.md>) — 两个向量按通道取得的最小值。

## 另请参阅

### 数值进阶

- [数值协议](numeric-protocols.md) — 编写适用于任何数值类型的泛型代码。
- [特殊用途数值类型](special-use-numeric-types.md) — 处理不同大小的定宽数值类型。
- [全局数值函数](global-numeric-functions.md) — 将这些函数用于数值和其他可比较类型。
