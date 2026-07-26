---
title: dispatch_barrier_sync_f
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_barrier_sync_f
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_barrier_sync_f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_barrier_sync_f.json'
content_hash: 'sha256:b13327b024604129'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_barrier_sync_f

<sub>Function</sub>

Submits a barrier function for execution and waits until that function completes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_barrier_sync_f(dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Parameters

- `queue` — The dispatch queue on which to execute the barrier function. This parameter cannot be `NULL`.

- `context` — The app-defined context parameter to pass to the barrier function.

- `work` — The app-defined barrier function to execute. The first parameter passed to this function is the value in the `context` parameter. This parameter cannot be `NULL`.

## Discussion

This function submits a barrier function to a dispatch queue for synchronous execution. Unlike [dispatch_barrier_async_f](dispatch_barrier_async_f.md), this function does not return until the barrier function has finished. Calling this function and targeting the current queue results in deadlock.

When the barrier function reaches the front of a private concurrent queue, it is not executed immediately. Instead, the queue waits until its currently executing blocks finish executing. At that point, the queue executes the barrier function by itself. Any blocks submitted after the barrier function are not executed until the barrier function completes.

The queue you specify should be a concurrent queue that you create yourself using the [dispatch_queue_create](dispatch_queue_create.md) function. If the queue you pass to this function is a serial queue or one of the global concurrent queues, this function behaves like the [dispatch_sync_f](dispatch_sync_f.md) function.

Unlike with [dispatch_barrier_async_f](dispatch_barrier_async_f.md), no retain is performed on the target queue. Because calls to this function are synchronous, it “borrows” the reference of the caller.

As an optimization, this function invokes the barrier function on the current thread when possible.

## See Also

### Creating a Barrier Synchronously

- [dispatch_barrier_sync](dispatch_barrier_sync.md) — Submits a barrier block object for execution and waits until that block completes.
- [dispatch_barrier_async_and_wait](dispatch_barrier_async_and_wait.md) — Submits a work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
- [dispatch_barrier_async_and_wait_f](dispatch_barrier_async_and_wait_f.md) — Submits a function-based work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
