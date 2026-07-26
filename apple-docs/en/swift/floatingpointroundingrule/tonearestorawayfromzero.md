---
title: FloatingPointRoundingRule.toNearestOrAwayFromZero
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpointroundingrule/tonearestorawayfromzero
source_url: 'https://developer.apple.com/documentation/swift/floatingpointroundingrule/tonearestorawayfromzero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointroundingrule/tonearestorawayfromzero.json'
content_hash: 'sha256:e389ff5a57cbde8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPointRoundingRule](../floatingpointroundingrule.md)

# FloatingPointRoundingRule.toNearestOrAwayFromZero

<sub>Case</sub>

Round to the closest allowed value; if two values are equally close, the one with greater magnitude is chosen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case toNearestOrAwayFromZero
```

## Discussion

This rounding rule is also known as “schoolbook rounding.” The following example shows the results of rounding numbers using this rule:

```swift
(5.2).rounded(.toNearestOrAwayFromZero)
// 5.0
(5.5).rounded(.toNearestOrAwayFromZero)
// 6.0
(-5.2).rounded(.toNearestOrAwayFromZero)
// -5.0
(-5.5).rounded(.toNearestOrAwayFromZero)
// -6.0
```

This rule is equivalent to the C `round` function and implements the `roundToIntegralTiesToAway` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
