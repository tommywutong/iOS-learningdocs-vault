---
title: dispatch_apply
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_apply
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_apply'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_apply.json'
content_hash: 'sha256:da9d612f1d6b4650'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_apply

<sub>Function</sub>

Submits a single block to the dispatch queue and causes the block to be executed the specified number of times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_apply(size_t iterations, dispatch_queue_t queue, void (^block)(size_t iteration));
```

## Parameters

- `iterations` — The number of times to execute the block.

- `queue` — The queue on which to submit the block. It is recommended that you specify [DISPATCH_APPLY_AUTO](dispatch_apply_auto.md) for this parameter, as that causes the block to run on a queue whose quality-of-service class is most appropriate for the current execution context.

- `block` — The application-defined function to be submitted. This parameter cannot be `NULL`. This block has no return value and takes one parameter: - **iteration** — The current iteration index.

## Discussion

This function submits a block to a dispatch queue for multiple invocations and waits for all iterations of the task block to complete before returning. If the target queue is a concurrent queue returned by [dispatch_get_global_queue](dispatch_get_global_queue.md), the block can be invoked concurrently, and it must therefore be reentrant-safe. Using this function with a concurrent queue can be useful as an efficient parallel `for` loop.

The current index of iteration is passed to each invocation of the block.

## See Also

### Executing a Task in Parallel

- [dispatch_apply_f](dispatch_apply_f.md) — Submits a single function to the dispatch queue and causes the function to be executed the specified number of times.
- [DISPATCH_APPLY_AUTO](dispatch_apply_auto.md)
