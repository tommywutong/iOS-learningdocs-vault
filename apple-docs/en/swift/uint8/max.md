---
title: max
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint8/max
source_url: 'https://developer.apple.com/documentation/swift/uint8/max'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint8/max.json'
content_hash: 'sha256:4769670d568720d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt8](../uint8.md)

# max

<sub>Type Property</sub>

The maximum representable integer in this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var max: Self { get }
```

## Discussion

For unsigned integer types, this value is `(2 ** bitWidth) - 1`, where `**` is exponentiation.
