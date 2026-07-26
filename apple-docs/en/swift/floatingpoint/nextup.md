---
title: nextUp
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/nextup
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/nextup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/nextup.json'
content_hash: 'sha256:87c2e70d5e09bb8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# nextUp

<sub>Instance Property</sub>

The least representable value that compares greater than this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nextUp: Self { get }
```

## Discussion

For any finite value `x`, `x.nextUp` is greater than `x`. For `nan` or `infinity`, `x.nextUp` is `x` itself. The following special cases also apply:

- If `x` is `-infinity`, then `x.nextUp` is `-greatestFiniteMagnitude`.
- If `x` is `-leastNonzeroMagnitude`, then `x.nextUp` is `-0.0`.
- If `x` is zero, then `x.nextUp` is `leastNonzeroMagnitude`.
- If `x` is `greatestFiniteMagnitude`, then `x.nextUp` is `infinity`.
