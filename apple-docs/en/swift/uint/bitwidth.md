---
title: bitWidth
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint/bitwidth
source_url: 'https://developer.apple.com/documentation/swift/uint/bitwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint/bitwidth.json'
content_hash: 'sha256:6a59be140bfccda2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt](../uint.md)

# bitWidth

<sub>Type Property</sub>

The number of bits used for the underlying binary representation of values of this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var bitWidth: Int { get }
```

## Discussion

The bit width of a `UInt` instance is 32 on 32-bit platforms and 64 on 64-bit platforms.
