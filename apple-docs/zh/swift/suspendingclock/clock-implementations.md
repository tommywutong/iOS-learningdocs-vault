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
doc_path: /documentation/swift/suspendingclock/clock-implementations
source_url: 'https://developer.apple.com/documentation/swift/suspendingclock/clock-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/suspendingclock/clock-implementations.json'
content_hash: 'sha256:20d543ea68c683ba'
translated: true
---

> 导航：[Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Time](../time-and-duration.md) · [SuspendingClock](../suspendingclock.md)

# 时钟实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [minimumResolution](minimumresolution.md) — 任意两次调用 `now` 之间的最小非零分辨率。
- [now](now-swift.property.md) — 计入机器挂起时间的当前时刻。

### 实例方法

- [measure(_:)](<measure(__)-1zuvn.md>) — 测量执行一个异步闭包所耗费的时间。
- [measure(_:)](<measure(__)-6nlcy.md>) — 测量执行一个闭包所耗费的时间。
- [measure(isolation:_:)](<measure(isolation___).md>) _(已废弃)_
- [sleep(for:tolerance:)](<sleep(for_tolerance_).md>) — 挂起指定的时长。
- [sleep(until:tolerance:)](<sleep(until_tolerance_).md>) — 在给定的容差范围内，将任务执行挂起至给定的截止时间。如果未指定容差，系统可能会调整截止时间，以合并 CPU 唤醒操作，从而以更省电的方式更高效地处理这些唤醒。

### 类型别名

- [Duration](duration.md)

### 类型属性

- [suspending](suspending.md) — 一种始终递增、但在系统休眠期间停止递增的时钟。
