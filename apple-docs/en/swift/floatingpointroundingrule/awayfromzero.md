---
title: FloatingPointRoundingRule.awayFromZero
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpointroundingrule/awayfromzero
source_url: 'https://developer.apple.com/documentation/swift/floatingpointroundingrule/awayfromzero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointroundingrule/awayfromzero.json'
content_hash: 'sha256:c4a57177d0335878'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPointRoundingRule](../floatingpointroundingrule.md)

# FloatingPointRoundingRule.awayFromZero

<sub>Case</sub>

Round to the closest allowed value whose magnitude is greater than or equal to that of the source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case awayFromZero
```

## Discussion

The following example shows the results of rounding numbers using this rule:

```swift
(5.2).rounded(.awayFromZero)
// 6.0
(5.5).rounded(.awayFromZero)
// 6.0
(-5.2).rounded(.awayFromZero)
// -6.0
(-5.5).rounded(.awayFromZero)
// -6.0
```
