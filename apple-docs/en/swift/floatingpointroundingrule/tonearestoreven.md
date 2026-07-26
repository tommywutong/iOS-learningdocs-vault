---
title: FloatingPointRoundingRule.toNearestOrEven
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpointroundingrule/tonearestoreven
source_url: 'https://developer.apple.com/documentation/swift/floatingpointroundingrule/tonearestoreven'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointroundingrule/tonearestoreven.json'
content_hash: 'sha256:abc0e77312a62499'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPointRoundingRule](../floatingpointroundingrule.md)

# FloatingPointRoundingRule.toNearestOrEven

<sub>Case</sub>

Round to the closest allowed value; if two values are equally close, the even one is chosen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case toNearestOrEven
```

## Discussion

This rounding rule is also known as “bankers rounding,” and is the default IEEE 754 rounding mode for arithmetic. The following example shows the results of rounding numbers using this rule:

```swift
(5.2).rounded(.toNearestOrEven)
// 5.0
(5.5).rounded(.toNearestOrEven)
// 6.0
(4.5).rounded(.toNearestOrEven)
// 4.0
```

This rule implements the `roundToIntegralTiesToEven` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
