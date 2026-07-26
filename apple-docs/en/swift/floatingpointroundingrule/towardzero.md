---
title: FloatingPointRoundingRule.towardZero
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpointroundingrule/towardzero
source_url: 'https://developer.apple.com/documentation/swift/floatingpointroundingrule/towardzero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointroundingrule/towardzero.json'
content_hash: 'sha256:c4cb6599426f2826'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPointRoundingRule](../floatingpointroundingrule.md)

# FloatingPointRoundingRule.towardZero

<sub>Case</sub>

Round to the closest allowed value whose magnitude is less than or equal to that of the source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case towardZero
```

## Discussion

The following example shows the results of rounding numbers using this rule:

```swift
(5.2).rounded(.towardZero)
// 5.0
(5.5).rounded(.towardZero)
// 5.0
(-5.2).rounded(.towardZero)
// -5.0
(-5.5).rounded(.towardZero)
// -5.0
```

This rule is equivalent to the C `trunc` function and implements the `roundToIntegralTowardZero` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
