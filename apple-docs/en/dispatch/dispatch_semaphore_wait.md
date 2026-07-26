---
title: dispatch_semaphore_wait
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_semaphore_wait
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_semaphore_wait'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_semaphore_wait.json'
content_hash: 'sha256:0fc8936c9e3fa64c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_semaphore_wait

<sub>Function</sub>

Waits for (decrements) a semaphore.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern intptr_t dispatch_semaphore_wait(dispatch_semaphore_t dsema, dispatch_time_t timeout);
```

## Parameters

- `dsema` — The semaphore. This parameter cannot be `NULL`.

- `timeout` — When to timeout (see [dispatch_time](dispatch_time.md)). The constants [DISPATCH_TIME_NOW](dispatch_time_now.md) and [DISPATCH_TIME_FOREVER](dispatch_time_forever.md) are available as a convenience.

## Return Value

Returns zero on success, or non-zero if the timeout occurred.

## Discussion

Decrement the counting semaphore. If the resulting value is less than zero, this function waits for a signal to occur before returning.
