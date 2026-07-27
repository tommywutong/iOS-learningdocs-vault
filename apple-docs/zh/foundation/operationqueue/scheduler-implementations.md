---
title: 调度器实现
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/scheduler-implementations
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/scheduler-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/scheduler-implementations.json'
content_hash: 'sha256:83796bd8d3b88c34'
translated: true
---

> 导航：[Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Processes and Threads](../processes-and-threads.md) · [OperationQueue](../operationqueue.md)

# 调度器实现

<sub>API 集合</sub>

## 主题

### 结构体

- [SchedulerOptions](scheduleroptions.md) — 定义操作队列所接受选项的类型。
- [SchedulerTimeType](schedulertimetype.md) — 操作队列所使用的调度器时间类型。

### 实例属性

- [minimumTolerance](minimumtolerance.md) — 调度队列的调度器所允许的最小容差。
- [now](now.md) — 操作队列对当前时刻的定义。

### 实例方法

- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — 在指定日期之后的某个时间，以指定的频率执行操作，并在可能的情况下选择性地考虑容差。
- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — 在指定日期之后的某个时间执行操作，并在可能的情况下选择性地考虑容差。
- [schedule(options:_:)](<schedule(options___).md>) — 在下一个可能的时机执行操作。
