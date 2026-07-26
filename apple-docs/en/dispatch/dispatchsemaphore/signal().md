---
title: signal()
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsemaphore/signal()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsemaphore/signal()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsemaphore/signal%28%29.json'
content_hash: 'sha256:8c20a1e7a88bc14c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSemaphore](../dispatchsemaphore.md)

# signal()

<sub>Instance Method</sub>

Signals (increments) a semaphore.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func signal() -> Int
```

## Return Value

This function returns non-zero if a thread is woken. Otherwise, zero is returned.

## Discussion

Increment the counting semaphore. If the previous value was less than zero, this function wakes a thread currently waiting in [dispatch_semaphore_wait](../dispatch_semaphore_wait.md).
