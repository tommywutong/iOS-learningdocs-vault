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
doc_path: /documentation/foundation/nsrecursivelock/try()
source_url: 'https://developer.apple.com/documentation/foundation/nsrecursivelock/try()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrecursivelock/try%28%29.json'
content_hash: 'sha256:cd910b5a0b3fbcfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRecursiveLock](../nsrecursivelock.md)

# try()

<sub>Instance Method</sub>

Attempts to acquire a lock, and immediately returns a Boolean value that indicates whether the attempt was successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func `try`() -> Bool
```

## Return Value

[true](../../swift/true.md) if successful, otherwise [false](../../swift/false.md).

## See Also

### Acquiring a Lock

- [- lockBeforeDate:](<lock(before_).md>) — Attempts to acquire a lock before a given date.
