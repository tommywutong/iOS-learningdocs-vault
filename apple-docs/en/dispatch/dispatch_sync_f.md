---
title: dispatch_sync_f
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_sync_f
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_sync_f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_sync_f.json'
content_hash: 'sha256:2530d5477abc46bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_sync_f

<sub>Function</sub>

Submits an app-defined function for synchronous execution on a dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_sync_f(dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Parameters

- `queue` — The queue on which to submit the function.  This parameter cannot be `NULL`.

- `context` — The app-defined context parameter to pass to the function.

- `work` — The app-defined function to invoke on the target queue. The first parameter passed to this function is the value in the `context` parameter. This parameter cannot be `NULL`.

## See Also

### Executing Tasks Synchronously

- [dispatch_sync](<dispatchqueue/sync(execute_)-3segw.md>) — Submits a block object for execution and returns after that block finishes executing.
- [dispatch_async_and_wait](<dispatchqueue/asyncandwait(execute_)-1udeu.md>) — Submits a work item for execution and returns only after it finishes executing.
- [dispatch_async_and_wait_f](dispatch_async_and_wait_f.md) — Submits a function-based work item for execution and returns only after it finishes executing.
- [dispatch_barrier_async_and_wait](dispatch_barrier_async_and_wait.md) — Submits a work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
- [dispatch_barrier_async_and_wait_f](dispatch_barrier_async_and_wait_f.md) — Submits a function-based work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
