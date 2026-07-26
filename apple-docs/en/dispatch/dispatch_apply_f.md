---
title: dispatch_apply_f
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_apply_f
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_apply_f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_apply_f.json'
content_hash: 'sha256:dea5b6a97b7be945'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_apply_f

<sub>Function</sub>

Submits a single function to the dispatch queue and causes the function to be executed the specified number of times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_apply_f(size_t iterations, dispatch_queue_t queue, void *context, void (*)(void *, unsigned long)work);
```

## Parameters

- `iterations` — The number of iterations to perform.

- `queue` — The queue on which to submit the function. It is recommended that you specify [DISPATCH_APPLY_AUTO](dispatch_apply_auto.md) for this parameter, as that causes the block to run on a queue whose quality-of-service class is most appropriate for the current execution context.

- `context` — The application-defined context parameter to pass to the function.

- `work` — The application-defined function to invoke on the target queue. This parameter cannot be NULL. The block has no return value and takes the following parameters: - **data** — The pointer you specified in the `context` parameter. - **iteration** — The current iteration index.

## Discussion

This function submits an application-defined function to a dispatch queue for multiple invocations and waits for all iterations of the function to complete before returning. If the target queue is a concurrent queue returned by [dispatch_get_global_queue](dispatch_get_global_queue.md), the function can be invoked concurrently, and it must therefore be reentrant-safe. Using this function with a concurrent queue can be useful as an efficient parallel `for` loop.

The current index of iteration is passed to each invocation of the function.

## See Also

### Executing a Task in Parallel

- [dispatch_apply](dispatch_apply.md) — Submits a single block to the dispatch queue and causes the block to be executed the specified number of times.
- [DISPATCH_APPLY_AUTO](dispatch_apply_auto.md)
