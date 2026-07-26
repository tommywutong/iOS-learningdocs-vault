---
title: StringInterpolation
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebystringinterpolation/stringinterpolation
source_url: 'https://developer.apple.com/documentation/swift/expressiblebystringinterpolation/stringinterpolation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebystringinterpolation/stringinterpolation.json'
content_hash: 'sha256:3a5afbff25f27a68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ExpressibleByStringInterpolation](../expressiblebystringinterpolation.md)

# StringInterpolation

<sub>Associated Type</sub>

The type each segment of a string literal containing interpolations should be appended to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype StringInterpolation : StringInterpolationProtocol = DefaultStringInterpolation where Self.StringLiteralType == Self.StringInterpolation.StringLiteralType
```

## Discussion

The `StringLiteralType` of an interpolation type must match the `StringLiteralType` of the conforming type.
