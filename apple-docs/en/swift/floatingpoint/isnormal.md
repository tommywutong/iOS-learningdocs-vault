---
title: isNormal
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/isnormal
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/isnormal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/isnormal.json'
content_hash: 'sha256:59cf2b55f5c5ed08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# isNormal

<sub>Instance Property</sub>

A Boolean value indicating whether this instance is normal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isNormal: Bool { get }
```

## Discussion

A _normal_ value is a finite number that uses the full precision available to values of a type. Zero is neither a normal nor a subnormal number.
