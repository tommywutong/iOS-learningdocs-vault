---
title: max
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int128/max
source_url: 'https://developer.apple.com/documentation/swift/int128/max'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/max.json'
content_hash: 'sha256:1621a97d02014a39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# max

<sub>Type Property</sub>

The maximum representable integer in this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var max: Int128 { get }
```

## Discussion

For unsigned integer types, this value is `(2 ** bitWidth) - 1`, where `**` is exponentiation. For signed integer types, this value is `(2 ** (bitWidth - 1)) - 1`.
