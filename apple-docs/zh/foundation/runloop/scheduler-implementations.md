---
title: 调度器实现
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/scheduler-implementations
source_url: 'https://developer.apple.com/documentation/foundation/runloop/scheduler-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/scheduler-implementations.json'
content_hash: 'sha256:edb24d77eb35ceaf'
translated: true
---

> 导航：[技术](../../technologies.md) · [Foundation](../../foundation.md) · [进程与线程](../processes-and-threads.md) · [RunLoop](../runloop.md)

# 调度器实现

<sub>API 集合</sub>

## 主题

### 结构体

- [SchedulerOptions](scheduleroptions.md) — 影响运行循环（run loop）调度器运行方式的一组选项。
- [SchedulerTimeType](schedulertimetype.md) — 运行循环使用的调度器时间类型。

### 实例属性

- [minimumTolerance](minimumtolerance.md) — 运行循环调度器允许的最小容差。
- [now](now.md) — 运行循环调度器对当前时刻的定义。

### 实例方法

- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — 在指定日期之后的某个时间，以指定频率并使用指定的容差和选项执行操作。
- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — 在指定日期之后的某个时间，使用指定的容差和选项执行操作。
- [schedule(options:_:)](<schedule(options___).md>) — 在指定日期之后的某个时间，使用调度器的最小容差执行操作。
