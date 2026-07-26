---
title: exponentBitCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/exponentbitcount
source_url: 'https://developer.apple.com/documentation/swift/float80/exponentbitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/exponentbitcount.json'
content_hash: 'sha256:80f36ab544864590'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# exponentBitCount

<sub>Type Property</sub>

The number of bits used to represent the type’s exponent.

<sub>macOS</sub>

```swift
static var exponentBitCount: Int { get }
```

## Discussion

A binary floating-point type’s `exponentBitCount` imposes a limit on the range of the exponent for normal, finite values. The _exponent bias_ of a type `F` can be calculated as the following, where `**` is exponentiation:

```swift
let bias = 2 ** (F.exponentBitCount - 1) - 1
```

The least normal exponent for values of the type `F` is `1 - bias`, and the largest finite exponent is `bias`. An all-zeros exponent is reserved for subnormals and zeros, and an all-ones exponent is reserved for infinity and NaN.

For example, the `Float` type has an `exponentBitCount` of 8, which gives an exponent bias of `127` by the calculation above.

```swift
let bias = 2 ** (Float.exponentBitCount - 1) - 1
// bias == 127
print(Float.greatestFiniteMagnitude.exponent)
// Prints "127"
print(Float.leastNormalMagnitude.exponent)
// Prints "-126"
```
