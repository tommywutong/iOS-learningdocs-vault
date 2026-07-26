---
title: isFinite
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/isfinite
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/isfinite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/isfinite.json'
content_hash: 'sha256:00259d013a84aefb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# isFinite

<sub>Instance Property</sub>

A Boolean value indicating whether this instance is finite.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFinite: Bool { get }
```

## Discussion

All values other than NaN and infinity are considered finite, whether normal or subnormal.  For NaN, both `isFinite` and `isInfinite` are false.
