---
title: nextDown
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/nextdown-92vef
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/nextdown-92vef'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/nextdown-92vef.json'
content_hash: 'sha256:4a4cd1f0d8289468'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# nextDown

<sub>Instance Property</sub>

The greatest representable value that compares less than this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nextDown: Self { get }
```

## Discussion

For any finite value `x`, `x.nextDown` is less than `x`. For `nan` or `-infinity`, `x.nextDown` is `x` itself. The following special cases also apply:

- If `x` is `infinity`, then `x.nextDown` is `greatestFiniteMagnitude`.
- If `x` is `leastNonzeroMagnitude`, then `x.nextDown` is `0.0`.
- If `x` is zero, then `x.nextDown` is `-leastNonzeroMagnitude`.
- If `x` is `-greatestFiniteMagnitude`, then `x.nextDown` is `-infinity`.
