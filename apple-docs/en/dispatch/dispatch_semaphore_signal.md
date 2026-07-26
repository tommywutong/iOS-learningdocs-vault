---
title: dispatch_semaphore_signal
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_semaphore_signal
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_semaphore_signal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_semaphore_signal.json'
content_hash: 'sha256:83f0c03fa7b650dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_semaphore_signal

<sub>Function</sub>

Signals (increments) a semaphore.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern intptr_t dispatch_semaphore_signal(dispatch_semaphore_t dsema);
```

## Return Value

If the previous value was less than zero, this function wakes a process currently waiting.

## Discussion

Increment the counting semaphore. If the previous value was less than zero, this function wakes a thread currently waiting in [dispatch_semaphore_wait](dispatch_semaphore_wait.md).
