---
title: dispatch_async_f
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_async_f
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_async_f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_async_f.json'
content_hash: 'sha256:057d13031b37d2d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_async_f

<sub>Function</sub>

Submits an app-defined function for asynchronous execution on a dispatch queue and returns immediately.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_async_f(dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Parameters

- `queue` — The queue on which to submit the function. The system retains the queue until the function runs to completion. This parameter cannot be `NULL`.

- `context` — The app-defined context parameter to pass to the function.

- `work` — The app-defined function to invoke on the target queue. The first parameter passed to this function is the value of the `context` parameter. This parameter cannot be `NULL`.

## Discussion

This function is the fundamental mechanism for submitting app-defined functions to a dispatch queue. Calls to this function always return immediately after the function is submitted and never wait for it to be invoked. The target queue determines whether the function is invoked serially or concurrently with respect to other tasks submitted to that same queue. Serial queues are processed concurrently with respect to each other.

## See Also

### Executing Tasks Asynchronously

- [dispatch_async](dispatch_async.md) — Submits a block for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_after](dispatch_after.md) — Enqueues a block for execution at the specified time.
- [dispatch_after_f](dispatch_after_f.md) — Enqueues an app-defined function for execution at the specified time.
- [dispatch_function_t](dispatch_function_t.md) — The prototype of functions submitted to dispatch queues.
- [dispatch_block_t](dispatch_block_t.md) — The prototype of blocks submitted to dispatch queues, which take no arguments and have no return value.
