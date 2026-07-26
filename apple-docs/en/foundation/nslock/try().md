---
title: try()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslock/try()
source_url: 'https://developer.apple.com/documentation/foundation/nslock/try()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslock/try%28%29.json'
content_hash: 'sha256:508a72ad559cc55a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLock](../nslock.md)

# try()

<sub>Instance Method</sub>

Attempts to acquire a lock and immediately returns a Boolean value that indicates whether the attempt was successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func `try`() -> Bool
```

## Return Value

[true](../../swift/true.md) if the lock was acquired, otherwise [false](../../swift/false.md).

## See Also

### Acquiring a Lock

- [- lockBeforeDate:](<lock(before_).md>) — Attempts to acquire a lock before a given time and returns a Boolean value indicating whether the attempt was successful.
