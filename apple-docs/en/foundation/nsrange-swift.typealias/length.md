---
title: length
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsrange-swift.typealias/length
source_url: 'https://developer.apple.com/documentation/foundation/nsrange-swift.typealias/length'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrange-swift.typealias/length.json'
content_hash: 'sha256:a122e55f4b6930c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRange](../nsrange-swift.typealias.md)

# length

<sub>Instance Property</sub>

The number of items in the range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var length: Int
```

## Discussion

This value can be `0` to represent an empty range. For type compatibility with the rest of the system, the maximum value you should use for length is `LONG_MAX`.

## See Also

### Accessing range properties

- [location](location.md) — The index of the first member of the range.
