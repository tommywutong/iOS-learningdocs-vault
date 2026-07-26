---
title: greatestFiniteMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/greatestfinitemagnitude
source_url: 'https://developer.apple.com/documentation/swift/float16/greatestfinitemagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/greatestfinitemagnitude.json'
content_hash: 'sha256:6d415fa46f63b0c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# greatestFiniteMagnitude

<sub>Type Property</sub>

The greatest finite number representable by this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var greatestFiniteMagnitude: Float16 { get }
```

## Discussion

This value compares greater than or equal to all finite numbers, but less than `infinity`.

This value corresponds to type-specific C macros such as `FLT_MAX` and `DBL_MAX`. The naming of those macros is slightly misleading, because `infinity` is greater than this value.
