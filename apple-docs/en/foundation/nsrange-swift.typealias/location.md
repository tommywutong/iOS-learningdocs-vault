---
title: location
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsrange-swift.typealias/location
source_url: 'https://developer.apple.com/documentation/foundation/nsrange-swift.typealias/location'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrange-swift.typealias/location.json'
content_hash: 'sha256:9396e4816cc8cc74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRange](../nsrange-swift.typealias.md)

# location

<sub>Instance Property</sub>

The index of the first member of the range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var location: Int
```

## Discussion

The minimum first index is `0`, as in C arrays. For type compatibility with the rest of the system, the maximum value you should use for the location is `LONG_MAX`.

## See Also

### Accessing range properties

- [length](length.md) — The number of items in the range.
