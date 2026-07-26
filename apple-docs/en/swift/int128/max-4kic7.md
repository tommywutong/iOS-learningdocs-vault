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
doc_path: /documentation/swift/int128/max-4kic7
source_url: 'https://developer.apple.com/documentation/swift/int128/max-4kic7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/max-4kic7.json'
content_hash: 'sha256:b300b478f3500b25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# max

<sub>Type Property</sub>

The maximum representable integer in this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var max: Self { get }
```

## Discussion

For signed integer types, this value is `(2 ** (bitWidth - 1)) - 1`, where `**` is exponentiation.
