---
title: dispatch_queue_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_t.json'
content_hash: 'sha256:9688b38c78407fc2'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_queue_t

<sub>类型别名</sub>

你的 App 用来提交 block 以供后续执行的一个轻量对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias dispatch_queue_t = DispatchQueue
```

## 讨论

dispatch queue 会以先进先出（FIFO）顺序串行地调用提交给它的 block。串行队列一次只调用一个 block，但彼此独立的队列可以相对于彼此并发地调用各自的 block。

全局并发队列也会以 FIFO 顺序调用 block，但不会等待它们完成，从而允许多个 block 并发地被调用。

系统管理一个线程池，用于处理 dispatch queue 并调用提交给它们的 block。从概念上讲，一个 dispatch queue 可以拥有自己的执行线程，并且队列之间的交互高度异步。

dispatch queue 通过调用 [dispatch_retain](dispatch_retain.md) 和 [dispatch_release](dispatch_release.md) 进行引用计数。提交到队列且尚未完成的挂起 block 也会持有对该队列的引用。一旦对该队列的所有引用都被释放，系统就会释放该队列。

## 另请参阅

### 数据类型

- [dispatch_group_t](dispatch_group_t.md) — 一组提交到队列以供异步调用的 block 对象。
- [dispatch_io_t](dispatch_io_t.md) — 一个 dispatch I/O 通道。
- [dispatch_object_t](dispatch_object_t.md) — 一个 dispatch 对象。
- [dispatch_queue_attr_t](dispatch_queue_attr_t.md) — 描述某个 dispatch queue 行为的一组特性。
- [dispatch_queue_serial_executor_t](dispatch_queue_serial_executor_t.md)
- [dispatch_semaphore_t](dispatch_semaphore_t.md) — 一个 dispatch 信号量对象。
