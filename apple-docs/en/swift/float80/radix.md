---
title: radix
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/radix
source_url: 'https://developer.apple.com/documentation/swift/float80/radix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/radix.json'
content_hash: 'sha256:90505cdce2d41fe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# radix

<sub>Type Property</sub>

The radix, or base of exponentiation, for a floating-point type.

<sub>macOS</sub>

```swift
static var radix: Int { get }
```

## Discussion

The magnitude of a floating-point value `x` of type `F` can be calculated by using the following formula, where `**` is exponentiation:

```swift
x.significand * (F.radix ** x.exponent)
```

A conforming type may use any integer radix, but values other than 2 (for binary floating-point types) or 10 (for decimal floating-point types) are extraordinarily rare in practice.
