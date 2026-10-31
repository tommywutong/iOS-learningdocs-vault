---
title: dispatch_barrier_async
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_barrier_async
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_barrier_async'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_barrier_async.json'
content_hash: 'sha256:20bed1f0f5dab906'
translated: true
---

> 导航：[技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_barrier_async

<sub>函数</sub>

提交一个屏障 block 以供异步执行，并立即返回。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_barrier_async(dispatch_queue_t queue, dispatch_block_t block);
```

## 参数

- `queue` — 用于执行屏障 block 的 dispatch queue。系统会保留该队列，直到该 block 执行完毕。此参数不能为 `NULL`。

- `block` — 要提交到目标 dispatch queue 的屏障 block。该 block 会被复制并保留，直到执行完毕，随后被释放。此参数不能为 `NULL`。

## 讨论

调用此函数总会在提交 block 后立即返回，而从不等待该 block 被调用。当屏障 block 到达私有并发队列的队首时，并不会立即执行。相反，队列会等待当前正在执行的 block 全部执行完毕。此时，屏障 block 会单独执行。在屏障 block 之后提交的任何 block，都要等到屏障 block 完成后才会执行。

你指定的队列应当是你使用 [dispatch_queue_create](dispatch_queue_create.md) 函数自行创建的并发队列。如果你传给此函数的是串行队列或某个全局并发队列，则此函数的行为与 [dispatch_async](dispatch_async.md) 函数相同。

## 另请参阅

### 异步创建屏障

- [dispatch_barrier_async_f](dispatch_barrier_async_f.md) — 提交一个屏障函数以供异步执行，并立即返回。
