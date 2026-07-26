---
title: significandBitCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/significandbitcount
source_url: 'https://developer.apple.com/documentation/swift/float16/significandbitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/significandbitcount.json'
content_hash: 'sha256:62998fd68449e3aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

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
