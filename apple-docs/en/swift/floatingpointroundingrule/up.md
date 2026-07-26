---
title: FloatingPointRoundingRule.up
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpointroundingrule/up
source_url: 'https://developer.apple.com/documentation/swift/floatingpointroundingrule/up'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointroundingrule/up.json'
content_hash: 'sha256:925d0c727ff2eed9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPointRoundingRule](../floatingpointroundingrule.md)

# FloatingPointRoundingRule.up

<sub>Case</sub>

Round to the closest allowed value that is greater than or equal to the source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case up
```

## Discussion

The following example shows the results of rounding numbers using this rule:

```swift
(5.2).rounded(.up)
// 6.0
(5.5).rounded(.up)
// 6.0
(-5.2).rounded(.up)
// -5.0
(-5.5).rounded(.up)
// -5.0
```

This rule is equivalent to the C `ceil` function and implements the `roundToIntegralTowardPositive` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
