---
title: greatestFiniteMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/greatestfinitemagnitude
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/greatestfinitemagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/greatestfinitemagnitude.json'
content_hash: 'sha256:0a31d7189ffe4117'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# greatestFiniteMagnitude

<sub>Type Property</sub>

The greatest finite number representable by this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var greatestFiniteMagnitude: Self { get }
```

## Discussion

This value compares greater than or equal to all finite numbers, but less than `infinity`.

This value corresponds to type-specific C macros such as `FLT_MAX` and `DBL_MAX`. The naming of those macros is slightly misleading, because `infinity` is greater than this value.
