---
title: bigEndian
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int128/bigendian
source_url: 'https://developer.apple.com/documentation/swift/int128/bigendian'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/bigendian.json'
content_hash: 'sha256:8d4fe3d7a25ee639'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# bigEndian

<sub>Instance Property</sub>

The big-endian representation of this integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bigEndian: Self { get }
```

## Discussion

If necessary, the byte order of this value is reversed from the typical byte order of this integer type. On a big-endian platform, for any integer `x`, `x == x.bigEndian`.
