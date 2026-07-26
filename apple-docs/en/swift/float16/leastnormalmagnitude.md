---
title: leastNormalMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/leastnormalmagnitude
source_url: 'https://developer.apple.com/documentation/swift/float16/leastnormalmagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/leastnormalmagnitude.json'
content_hash: 'sha256:77ce38de20b47d4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# leastNormalMagnitude

<sub>Type Property</sub>

The least positive normal number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var leastNormalMagnitude: Float16 { get }
```

## Discussion

This value compares less than or equal to all positive normal numbers. There may be smaller positive numbers, but they are _subnormal_, meaning that they are represented with less precision than normal numbers.

This value corresponds to type-specific C macros such as `FLT_MIN` and `DBL_MIN`. The naming of those macros is slightly misleading, because subnormals, zeros, and negative numbers are smaller than this value.
