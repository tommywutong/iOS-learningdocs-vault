---
title: radix
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/radix-322z3
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/radix-322z3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/radix-322z3.json'
content_hash: 'sha256:55fdd27d2adbbaf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# radix

<sub>Type Property</sub>

The radix, or base of exponentiation, for a floating-point type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var radix: Int { get }
```

## Discussion

The magnitude of a floating-point value `x` of type `F` can be calculated by using the following formula, where `**` is exponentiation:

```swift
x.significand * (F.radix ** x.exponent)
```

A conforming type may use any integer radix, but values other than 2 (for binary floating-point types) or 10 (for decimal floating-point types) are extraordinarily rare in practice.
