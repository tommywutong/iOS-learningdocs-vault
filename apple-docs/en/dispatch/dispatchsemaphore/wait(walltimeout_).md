---
title: 'wait(wallTimeout:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsemaphore/wait(walltimeout:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsemaphore/wait(walltimeout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsemaphore/wait%28walltimeout%3A%29.json'
content_hash: 'sha256:36e35e5b3301639d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSemaphore](../dispatchsemaphore.md)

# wait(wallTimeout:)

<sub>Instance Method</sub>

Waits for, or decrements, a semaphore.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult
```

## Parameters

- `wallTimeout` — The latest time to wait for a signal.

## Discussion

Decrement the counting semaphore. If the resulting value is less than zero, this function waits for a signal to occur before returning.

## See Also

### Blocking on the Semaphore

- [wait()](<wait().md>) — Waits for, or decrements, a semaphore.
- [wait(timeout:)](<wait(timeout_).md>) — Waits for, or decrements, a semaphore.
