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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_barrier_sync

<sub>Function</sub>

Submits a barrier block object for execution and waits until that block completes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_barrier_sync(dispatch_queue_t queue, dispatch_block_t block);
```

## Parameters

- `queue` — The dispatch queue on which to execute the barrier block. This parameter cannot be `NULL`.

- `block` — The barrier block to execute. This parameter cannot be `NULL`.

## Discussion

This function submits a barrier block to a dispatch queue for synchronous execution. Unlike [dispatch_barrier_async](dispatch_barrier_async.md), this function does not return until the barrier block has finished. Calling this function and targeting the current queue results in deadlock.

When the barrier block reaches the front of a private concurrent queue, it is not executed immediately. Instead, the queue waits until its currently executing blocks finish executing. At that point, the queue executes the barrier block by itself. Any blocks submitted after the barrier block are not executed until the barrier block completes.

The queue you specify should be a concurrent queue that you create yourself using the [dispatch_queue_create](dispatch_queue_create.md) function. If the queue you pass to this function is a serial queue or one of the global concurrent queues, this function behaves like the [dispatch_sync](<dispatchqueue/sync(execute_)-3segw.md>) function.

Unlike with [dispatch_barrier_async](dispatch_barrier_async.md), no retain is performed on the target queue. Because calls to this function are synchronous, it “borrows” the reference of the caller. Moreover, no `Block_copy` is performed on the block.

As an optimization, this function invokes the barrier block on the current thread when possible.

## See Also

### Creating a Barrier Synchronously

- [dispatch_barrier_sync_f](dispatch_barrier_sync_f.md) — Submits a barrier function for execution and waits until that function completes.
- [dispatch_barrier_async_and_wait](dispatch_barrier_async_and_wait.md) — Submits a work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
- [dispatch_barrier_async_and_wait_f](dispatch_barrier_async_and_wait_f.md) — Submits a function-based work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
