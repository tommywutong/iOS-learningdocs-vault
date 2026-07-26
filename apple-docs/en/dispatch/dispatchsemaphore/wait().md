---
title: wait()
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsemaphore/wait()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsemaphore/wait()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsemaphore/wait%28%29.json'
content_hash: 'sha256:0d971b51d73e5f80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSemaphore](../dispatchsemaphore.md)

# wait()

<sub>Instance Method</sub>

Waits for, or decrements, a semaphore.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wait()
```

## Discussion

Decrement the counting semaphore. If the resulting value is less than zero, this function waits for a signal to occur before returning.

## See Also

### Blocking on the Semaphore

- [wait(timeout:)](<wait(timeout_).md>) — Waits for, or decrements, a semaphore.
- [wait(wallTimeout:)](<wait(walltimeout_).md>) — Waits for, or decrements, a semaphore.
