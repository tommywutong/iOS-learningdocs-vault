---
title: dispatch_barrier_sync
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_barrier_sync
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_barrier_sync'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_barrier_sync.json'
content_hash: 'sha256:11f1e55b4ff30fdd'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_barrier_sync

<sub>函数</sub>

提交一个屏障（barrier）block 对象以供执行，并等待该 block 完成。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_barrier_sync(dispatch_queue_t queue, dispatch_block_t block);
```

## 参数

- `queue` — 在其上执行屏障 block 的 dispatch queue。此参数不能为 `NULL`。

- `block` — 要执行的屏障 block。此参数不能为 `NULL`。

## 讨论

此函数将一个屏障 block 提交到某个 dispatch queue 以进行同步执行。与 [dispatch_barrier_async](dispatch_barrier_async.md) 不同，此函数在屏障 block 完成之前不会返回。调用此函数并以当前队列为目标会导致死锁。

当屏障 block 到达私有并发队列的队首时，它不会立即执行。相反，该队列会等待当前正在执行的 block 全部完成。此时，队列会单独执行该屏障 block。在屏障 block 之后提交的任何 block，都要等到该屏障 block 完成后才会执行。

你指定的队列应当是你自己使用 [dispatch_queue_create](dispatch_queue_create.md) 函数创建的并发队列。如果传给此函数的队列是串行队列或某个全局并发队列，则此函数的行为与 [dispatch_sync](<dispatchqueue/sync(execute_)-3segw.md>) 函数相同。

与 [dispatch_barrier_async](dispatch_barrier_async.md) 不同，此函数不会对目标队列执行保留（retain）。由于对此函数的调用是同步的，它会“借用”调用方的引用。此外，也不会对该 block 执行 `Block_copy`。

作为一项优化，此函数在可能时会在当前线程上调用该屏障 block。

## 另请参阅

### 同步创建屏障

- [dispatch_barrier_sync_f](dispatch_barrier_sync_f.md) — 提交一个屏障函数以供执行，并等待该函数完成。
- [dispatch_barrier_async_and_wait](dispatch_barrier_async_and_wait.md) — 提交一个工作项以进行同步执行，并将其标记为后续并发任务的屏障。
- [dispatch_barrier_async_and_wait_f](dispatch_barrier_async_and_wait_f.md) — 提交一个基于函数的工作项以进行同步执行，并将其标记为后续并发任务的屏障。
