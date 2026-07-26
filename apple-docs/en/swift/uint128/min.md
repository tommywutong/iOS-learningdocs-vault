---
title: min
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint128/min
source_url: 'https://developer.apple.com/documentation/swift/uint128/min'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/min.json'
content_hash: 'sha256:5e37dcacbbd38fe5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# min

<sub>Type Property</sub>

The minimum representable integer in this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var min: UInt128 { get }
```

## Discussion

For unsigned integer types, this value is always `0`. For signed integer types, this value is `-(2 ** (bitWidth - 1))`, where `**` is exponentiation.
