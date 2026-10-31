---
title: 时间
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/time-and-duration
source_url: 'https://developer.apple.com/documentation/swift/time-and-duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/time-and-duration.json'
content_hash: 'sha256:05a026c4b93b38df'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md)

# 时间

<sub>API 集合</sub>

测量一次操作耗费的时长，并确定未来的时间安排。

## 主题

### 时钟

- [Clock](clock.md) — 一种测量时间的机制，可将工作延迟到给定的时间点。
- [ContinuousClock](continuousclock.md) — 一种测量时间的时钟，其时间值始终递增，并且在系统休眠期间也不会停止递增。
- [SuspendingClock](suspendingclock.md) — 一种始终递增、但在系统休眠期间停止递增的时钟。

### 时长

- [Duration](duration.md) — 高精度时间的一种表示。
- [DurationProtocol](durationprotocol.md) — 为给定的 `InstantProtocol` 类型定义时长的类型。

### 支持类型

- [InstantProtocol](instantprotocol.md)

## 另请参阅

### 值与集合

- [Numbers and Basic Values](numbers-and-basic-values.md) — 使用数字、布尔值和其他基础类型为数据建模。
- [Strings and Text](strings-and-text.md) — 使用 Unicode 安全的字符串处理文本。
- [Collections](collections.md) — 使用数组、字典、集合和其他数据结构来存储和组织数据。
