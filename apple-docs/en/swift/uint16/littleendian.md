---
title: littleEndian
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint16/littleendian
source_url: 'https://developer.apple.com/documentation/swift/uint16/littleendian'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint16/littleendian.json'
content_hash: 'sha256:5660ba5752b53a39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt16](../uint16.md)

# littleEndian

<sub>Instance Property</sub>

The little-endian representation of this integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var littleEndian: Self { get }
```

## Discussion

If necessary, the byte order of this value is reversed from the typical byte order of this integer type. On a little-endian platform, for any integer `x`, `x == x.littleEndian`.
