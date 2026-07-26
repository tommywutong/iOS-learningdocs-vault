---
title: significandBitCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/binaryfloatingpoint/significandbitcount
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/significandbitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/significandbitcount.json'
content_hash: 'sha256:903d699202b71425'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# significandBitCount

<sub>Type Property</sub>

The available number of fractional significand bits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var significandBitCount: Int { get }
```

## Discussion

For fixed-width floating-point types, this is the actual number of fractional significand bits.

For extensible floating-point types, `significandBitCount` should be the maximum allowed significand width (without counting any leading integral bit of the significand). If there is no upper limit, then `significandBitCount` should be `Int.max`.

Note that `Float80.significandBitCount` is 63, even though 64 bits are used to store the significand in the memory representation of a `Float80` (unlike other floating-point types, `Float80` explicitly stores the leading integral significand bit, but the `BinaryFloatingPoint` APIs provide an abstraction so that users don’t need to be aware of this detail).

## See Also

### Working with Binary Representation

- [binade](binade.md) — The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [exponentBitPattern](exponentbitpattern.md) — The raw encoding of the value’s exponent field.
- [significandBitPattern](significandbitpattern.md) — The raw encoding of the value’s significand field.
- [significandWidth](significandwidth.md) — The number of bits required to represent the value’s significand.
- [exponentBitCount](exponentbitcount.md) — The number of bits used to represent the type’s exponent.
- [init(sign:exponentBitPattern:significandBitPattern:)](<init(sign_exponentbitpattern_significandbitpattern_).md>) — Creates a new instance from the specified sign and bit patterns.
- [RawExponent](rawexponent.md) — A type that represents the encoded exponent of a value.
- [RawSignificand](rawsignificand.md) — A type that represents the encoded significand of a value.
