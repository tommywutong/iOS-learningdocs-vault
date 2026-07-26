---
title: dispatch_function_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_function_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_function_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_function_t.json'
content_hash: 'sha256:6c467a5a9ce12e1e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_function_t

<sub>Type Alias</sub>

The prototype of functions submitted to dispatch queues.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef void (*)(void *) dispatch_function_t;
```

## Discussion

Functions that take a `dispatch_function_t` type as a parameter also take a pointer to contextual data that you provide. When your dispatch function is called, the pointer to that contextual data is passed as the parameter to the function. The pointer to the contextual data is passed unmodified to your function and it is your responsibility to ensure that the pointer is valid.

## See Also

### Executing Tasks Asynchronously

- [dispatch_async](dispatch_async.md) — Submits a block for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_async_f](dispatch_async_f.md) — Submits an app-defined function for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_after](dispatch_after.md) — Enqueues a block for execution at the specified time.
- [dispatch_after_f](dispatch_after_f.md) — Enqueues an app-defined function for execution at the specified time.
- [dispatch_block_t](dispatch_block_t.md) — The prototype of blocks submitted to dispatch queues, which take no arguments and have no return value.
