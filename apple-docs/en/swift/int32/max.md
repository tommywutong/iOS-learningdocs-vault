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
doc_path: /documentation/swift/int32/max
source_url: 'https://developer.apple.com/documentation/swift/int32/max'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int32/max.json'
content_hash: 'sha256:3cc35badb8e6becb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int32](../int32.md)

# max

<sub>Type Property</sub>

The maximum representable integer in this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var max: Self { get }
```

## Discussion

For signed integer types, this value is `(2 ** (bitWidth - 1)) - 1`, where `**` is exponentiation.
