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
doc_path: /documentation/swift/uint128/max-7lxqa
source_url: 'https://developer.apple.com/documentation/swift/uint128/max-7lxqa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/max-7lxqa.json'
content_hash: 'sha256:e56de577f32c9762'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# max

<sub>Type Property</sub>

The maximum representable integer in this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var max: Self { get }
```

## Discussion

For unsigned integer types, this value is `(2 ** bitWidth) - 1`, where `**` is exponentiation.
