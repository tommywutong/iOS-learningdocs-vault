---
title: dispatch_after
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_after
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_after'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_after.json'
content_hash: 'sha256:7b554929154bea0d'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_after

<sub>函数</sub>

将一个 block 排队，以便在指定时间执行。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_after(dispatch_time_t when, dispatch_queue_t queue, dispatch_block_t block);
```

## 参数

- `when` — [dispatch_time](dispatch_time.md) 或 [dispatch_walltime](dispatch_walltime.md) 返回的时间里程碑。

- `queue` — 用于提交该 block 的队列。系统会保留该队列，直到该 block 运行完成。此参数不能为 `NULL`。

- `block` — 要提交的 block。此函数会代表调用方执行 `Block_copy` 和 `Block_release`。此参数不能为 `NULL`。

## 讨论

此函数会等到指定时间，然后异步地将 `block` 添加到指定的 `queue`。

将 [DISPATCH_TIME_NOW](dispatch_time_now.md) 作为 `when` 参数传入是受支持的，但不如改为调用 [dispatch_async](dispatch_async.md) 那样优化。传入 [DISPATCH_TIME_FOREVER](dispatch_time_forever.md) 的行为未定义。

## 另请参阅

### 异步执行任务

- [dispatch_async](dispatch_async.md) — 将一个 block 提交到某个 dispatch queue 上异步执行，并立即返回。
- [dispatch_async_f](dispatch_async_f.md) — 将一个 App 定义的函数提交到某个 dispatch queue 上异步执行，并立即返回。
- [dispatch_after_f](dispatch_after_f.md) — 将一个 App 定义的函数排队，以便在指定时间执行。
- [dispatch_function_t](dispatch_function_t.md) — 提交到 dispatch queue 的函数的原型。
- [dispatch_block_t](dispatch_block_t.md) — 提交到 dispatch queue 的 block 的原型；这些 block 不接受参数且无返回值。
