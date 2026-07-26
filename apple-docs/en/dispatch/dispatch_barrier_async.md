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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_barrier_async

<sub>Function</sub>

Submits a barrier block for asynchronous execution and returns immediately.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_barrier_async(dispatch_queue_t queue, dispatch_block_t block);
```

## Parameters

- `queue` — The dispatch queue on which to execute the barrier block. The system retains the queue until the block runs to completion. This parameter cannot be `NULL`.

- `block` — The barrier block to submit to the target dispatch queue. This block is copied and retained until it finishes executing, at which point it is released. This parameter cannot be `NULL`.

## Discussion

Calls to this function always return immediately after the block is submitted and never wait for the block to be invoked. When the barrier block reaches the front of a private concurrent queue, it is not executed immediately. Instead, the queue waits until its currently executing blocks finish executing. At that point, the barrier block executes by itself. Any blocks submitted after the barrier block are not executed until the barrier block completes.

The queue you specify should be a concurrent queue that you create yourself using the [dispatch_queue_create](dispatch_queue_create.md) function. If the queue you pass to this function is a serial queue or one of the global concurrent queues, this function behaves like the [dispatch_async](dispatch_async.md) function.

## See Also

### Creating a Barrier Asynchronously

- [dispatch_barrier_async_f](dispatch_barrier_async_f.md) — Submits a barrier function for asynchronous execution and returns immediately.
