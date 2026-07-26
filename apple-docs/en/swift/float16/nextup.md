---
title: nextUp
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/nextup
source_url: 'https://developer.apple.com/documentation/swift/float16/nextup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/nextup.json'
content_hash: 'sha256:64cf8b05d7e98099'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# nextUp

<sub>Instance Property</sub>

The least representable value that compares greater than this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nextUp: Float16 { get }
```

## Discussion

For any finite value `x`, `x.nextUp` is greater than `x`. For `nan` or `infinity`, `x.nextUp` is `x` itself. The following special cases also apply:

- If `x` is `-infinity`, then `x.nextUp` is `-greatestFiniteMagnitude`.
- If `x` is `-leastNonzeroMagnitude`, then `x.nextUp` is `-0.0`.
- If `x` is zero, then `x.nextUp` is `leastNonzeroMagnitude`.
- If `x` is `greatestFiniteMagnitude`, then `x.nextUp` is `infinity`.
