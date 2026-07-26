---
title: signal()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscondition/signal()
source_url: 'https://developer.apple.com/documentation/foundation/nscondition/signal()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscondition/signal%28%29.json'
content_hash: 'sha256:496b8c8b5f1d0cba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCondition](../nscondition.md)

# signal()

<sub>Instance Method</sub>

Signals the condition, waking up one thread waiting on it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func signal()
```

## Discussion

You use this method to wake up one thread that is waiting on the condition. You may call this method multiple times to wake up multiple threads. If no threads are waiting on the condition, this method does nothing.

To avoid race conditions, you should invoke this method only while the receiver is locked.

## See Also

### Signaling Waiting Threads

- [- broadcast](<broadcast().md>) — Signals the condition, waking up all threads waiting on it.
