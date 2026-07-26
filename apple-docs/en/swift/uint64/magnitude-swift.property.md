---
title: magnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint64/magnitude-swift.property
source_url: 'https://developer.apple.com/documentation/swift/uint64/magnitude-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64/magnitude-swift.property.json'
content_hash: 'sha256:0d28c54df71a3993'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt64](../uint64.md)

# magnitude

<sub>Instance Property</sub>

The magnitude of this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var magnitude: Self { get }
```

## Discussion

Every unsigned integer is its own magnitude, so for any value `x`, `x == x.magnitude`.

The global `abs(_:)` function provides more familiar syntax when you need to find an absolute value. In addition, because `abs(_:)` always returns a value of the same type, even in a generic context, using the function instead of the `magnitude` property is encouraged.
