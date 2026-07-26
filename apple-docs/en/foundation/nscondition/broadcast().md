---
title: broadcast()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscondition/broadcast()
source_url: 'https://developer.apple.com/documentation/foundation/nscondition/broadcast()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscondition/broadcast%28%29.json'
content_hash: 'sha256:83e90914493258b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCondition](../nscondition.md)

# broadcast()

<sub>Instance Method</sub>

Signals the condition, waking up all threads waiting on it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func broadcast()
```

## Discussion

If no threads are waiting on the condition, this method does nothing.

To avoid race conditions, you should invoke this method only while the receiver is locked.

## See Also

### Signaling Waiting Threads

- [- signal](<signal().md>) — Signals the condition, waking up one thread waiting on it.
