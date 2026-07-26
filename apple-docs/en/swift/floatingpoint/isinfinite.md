---
title: isInfinite
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/isinfinite
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/isinfinite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/isinfinite.json'
content_hash: 'sha256:c37ae83b36cc8235'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# isInfinite

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is infinite.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isInfinite: Bool { get }
```

## Discussion

For NaN, both `isFinite` and `isInfinite` are false.
