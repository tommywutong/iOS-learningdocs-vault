---
title: 'wait(until:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscondition/wait(until:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscondition/wait(until:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscondition/wait%28until%3A%29.json'
content_hash: 'sha256:b3ff66624d64b744'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCondition](../nscondition.md)

# wait(until:)

<sub>Instance Method</sub>

Blocks the current thread until the condition is signaled or the specified time limit is reached.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wait(until limit: Date) -> Bool
```

## Parameters

- `limit` — The time at which to wake up the thread if the condition has not been signaled.

## Return Value

[true](../../swift/true.md) if the condition was signaled; otherwise, [false](../../swift/false.md) if the time limit was reached.

## Discussion

You must lock the receiver prior to calling this method.

## See Also

### Related Documentation

- [- lock](<../nslocking/lock().md>) — Attempts to acquire a lock, blocking a thread’s execution until the lock can be acquired.

### Waiting for the Lock

- [- wait](<wait().md>) — Blocks the current thread until the condition is signaled.
