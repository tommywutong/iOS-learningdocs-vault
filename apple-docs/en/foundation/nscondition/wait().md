---
title: wait()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscondition/wait()
source_url: 'https://developer.apple.com/documentation/foundation/nscondition/wait()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscondition/wait%28%29.json'
content_hash: 'sha256:dc740d0edc926ace'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCondition](../nscondition.md)

# wait()

<sub>Instance Method</sub>

Blocks the current thread until the condition is signaled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wait()
```

## Discussion

You must lock the receiver prior to calling this method.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [- lock](<../nslocking/lock().md>) — Attempts to acquire a lock, blocking a thread’s execution until the lock can be acquired.

### Waiting for the Lock

- [- waitUntilDate:](<wait(until_).md>) — Blocks the current thread until the condition is signaled or the specified time limit is reached.
