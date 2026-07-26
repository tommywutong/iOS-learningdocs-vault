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
doc_path: /documentation/swift/unsignedinteger/max
source_url: 'https://developer.apple.com/documentation/swift/unsignedinteger/max'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsignedinteger/max.json'
content_hash: 'sha256:f43371b73bfb004f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsignedInteger](../unsignedinteger.md)

# max

<sub>Type Property</sub>

The maximum representable integer in this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var max: Self { get }
```

## Discussion

For unsigned integer types, this value is `(2 ** bitWidth) - 1`, where `**` is exponentiation.
