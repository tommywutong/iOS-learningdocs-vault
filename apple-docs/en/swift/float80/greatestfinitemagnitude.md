---
title: greatestFiniteMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/greatestfinitemagnitude
source_url: 'https://developer.apple.com/documentation/swift/float80/greatestfinitemagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/greatestfinitemagnitude.json'
content_hash: 'sha256:bde0bcd3740c70e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# greatestFiniteMagnitude

<sub>Type Property</sub>

The greatest finite number representable by this type.

<sub>macOS</sub>

```swift
static var greatestFiniteMagnitude: Float80 { get }
```

## Discussion

This value compares greater than or equal to all finite numbers, but less than `infinity`.

This value corresponds to type-specific C macros such as `FLT_MAX` and `DBL_MAX`. The naming of those macros is slightly misleading, because `infinity` is greater than this value.
