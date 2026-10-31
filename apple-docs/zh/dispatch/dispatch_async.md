---
title: dispatch_async
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_async
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_async'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_async.json'
content_hash: 'sha256:b42b8a14b37ee01e'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_async

<sub>函数</sub>

将一个 block 提交到某个 dispatch queue 上异步执行，并立即返回。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_async(dispatch_queue_t queue, dispatch_block_t block);
```

## 参数

- `queue` — 用于提交该 block 的队列。系统会保留该队列，直到该 block 运行完成。此参数不能为 `NULL`。

- `block` — 要提交到目标 dispatch queue 的 block。此函数会代表调用方执行 `Block_copy` 和 `Block_release`。此参数不能为 `NULL`。

## 讨论

此函数是向 dispatch queue 提交 block 的基本机制。调用此函数时，总会在提交 block 后立即返回，并且决不会等待该 block 被调用。目标队列决定该 block 相对于提交到同一队列的其他 block 是串行还是并发地被调用。彼此独立的串行队列相对于彼此是并发处理的。

## 另请参阅

### 异步执行任务

- [dispatch_async_f](dispatch_async_f.md) — 将一个 App 定义的函数提交到某个 dispatch queue 上异步执行，并立即返回。
- [dispatch_after](dispatch_after.md) — 将一个 block 排队，以便在指定时间执行。
- [dispatch_after_f](dispatch_after_f.md) — 将一个 App 定义的函数排队，以便在指定时间执行。
- [dispatch_function_t](dispatch_function_t.md) — 提交到 dispatch queue 的函数的原型。
- [dispatch_block_t](dispatch_block_t.md) — 提交到 dispatch queue 的 block 的原型；这些 block 不接受参数且无返回值。
