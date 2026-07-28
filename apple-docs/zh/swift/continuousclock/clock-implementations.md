---
title: 时钟实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/continuousclock/clock-implementations
source_url: 'https://developer.apple.com/documentation/swift/continuousclock/clock-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/continuousclock/clock-implementations.json'
content_hash: 'sha256:e0967b5f5c8720e2'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [时间](../time-and-duration.md) · [ContinuousClock](../continuousclock.md)

# 时钟实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [minimumResolution](minimumresolution.md) — 任意两次调用 `now` 之间的最小非零分辨率。
- [now](now-swift.property.md) — 当前的连续时刻。

### 实例方法

- [measure(_:)](<measure(__)-73b0n.md>) — 测量执行一个闭包（closure）所经过的时间。
- [measure(_:)](<measure(__)-9npzl.md>) — 测量执行一个异步闭包所经过的时间。
- [measure(isolation:_:)](<measure(isolation___).md>) _(已废弃)_
- [sleep(for:tolerance:)](<sleep(for_tolerance_).md>) — 挂起指定的时长。
- [sleep(until:tolerance:)](<sleep(until_tolerance_).md>) — 在给定容差范围内将任务执行挂起至给定截止时间。如果未指定容差，系统可能会调整截止时间以合并 CPU 唤醒操作，从而以更节能的方式更高效地处理这些唤醒。

### 类型别名

- [Duration](duration.md)

### 类型属性

- [continuous](continuous.md) — 一种始终递增、并且在系统休眠期间也不会停止递增的时钟。
