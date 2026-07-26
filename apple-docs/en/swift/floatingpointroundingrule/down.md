---
title: FloatingPointRoundingRule.down
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpointroundingrule/down
source_url: 'https://developer.apple.com/documentation/swift/floatingpointroundingrule/down'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointroundingrule/down.json'
content_hash: 'sha256:ffec5a0f3241ae73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPointRoundingRule](../floatingpointroundingrule.md)

# FloatingPointRoundingRule.down

<sub>Case</sub>

Round to the closest allowed value that is less than or equal to the source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case down
```

## Discussion

The following example shows the results of rounding numbers using this rule:

```swift
(5.2).rounded(.down)
// 5.0
(5.5).rounded(.down)
// 5.0
(-5.2).rounded(.down)
// -6.0
(-5.5).rounded(.down)
// -6.0
```

This rule is equivalent to the C `floor` function and implements the `roundToIntegralTowardNegative` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
