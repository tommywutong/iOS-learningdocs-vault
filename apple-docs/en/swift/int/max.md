---
title: max
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/max
source_url: 'https://developer.apple.com/documentation/swift/int/max'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/max.json'
content_hash: 'sha256:d54ec3388b9d10ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# max

<sub>Type Property</sub>

The maximum representable integer in this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var max: Self { get }
```

## Discussion

For signed integer types, this value is `(2 ** (bitWidth - 1)) - 1`, where `**` is exponentiation.

## See Also

### Accessing Numeric Constants

- [zero](zero.md) — The zero value.
- [min](min.md) — The minimum representable integer in this type.
- [isSigned](issigned.md) — A Boolean value indicating whether this type is a signed integer type.
