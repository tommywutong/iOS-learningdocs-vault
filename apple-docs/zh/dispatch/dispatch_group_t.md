---
title: dispatch_group_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_group_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_group_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_group_t.json'
content_hash: 'sha256:b5968c9f360f483b'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_group_t

<sub>类型别名</sub>

提交到队列以进行异步调用的一组 block 对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias dispatch_group_t = DispatchGroup
```

## 讨论

dispatch group 是一种用于监控一组 block 的机制。你的应用程序可以根据需要，同步或异步地监控该 group 中的 block。进一步而言，当某段代码依赖于其他任务完成时，group 也可用于同步。

请注意，group 中的 block 可能在不同队列上运行，并且每个单独的 block 都可以向该 group 再添加更多 block。

dispatch group 会跟踪尚未完成的 block 数量，并且在所有关联 block 执行完毕之前，GCD 会一直保留该 group。

## 另请参阅

### 数据类型

- [dispatch_io_t](dispatch_io_t.md) — 一个 dispatch I/O 通道。
- [dispatch_object_t](dispatch_object_t.md) — 一个 dispatch 对象。
- [dispatch_queue_attr_t](dispatch_queue_attr_t.md) — 描述 dispatch queue 行为的属性。
- [dispatch_queue_serial_executor_t](dispatch_queue_serial_executor_t.md)
- [dispatch_queue_t](dispatch_queue_t.md) — 一个轻量级对象，你的应用程序可向其提交 block 以供后续执行。
- [dispatch_semaphore_t](dispatch_semaphore_t.md) — 一个 dispatch 信号量对象。
