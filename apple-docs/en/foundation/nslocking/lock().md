---
title: lock()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocking/lock()
source_url: 'https://developer.apple.com/documentation/foundation/nslocking/lock()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocking/lock%28%29.json'
content_hash: 'sha256:23588b01087f0e77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocking](../nslocking.md)

# lock()

<sub>Instance Method</sub>

Attempts to acquire a lock, blocking a thread’s execution until the lock can be acquired.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lock()
```

## Discussion

An application protects a critical section of code by requiring a thread to acquire a lock before executing the code. Once the critical section is completed, the thread relinquishes the lock by invoking [- unlock](<unlock().md>).

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)

### Working with Locks

- [- unlock](<unlock().md>) — Relinquishes a previously acquired lock.
