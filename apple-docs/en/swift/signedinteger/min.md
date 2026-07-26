---
title: min
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/signedinteger/min
source_url: 'https://developer.apple.com/documentation/swift/signedinteger/min'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/signedinteger/min.json'
content_hash: 'sha256:bb3ae121d79fb96d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SignedInteger](../signedinteger.md)

# min

<sub>Type Property</sub>

The minimum representable integer in this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var min: Self { get }
```

## Discussion

For signed integer types, this value is `-(2 ** (bitWidth - 1))`, where `**` is exponentiation.
