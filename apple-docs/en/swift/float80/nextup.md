---
title: nextUp
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/nextup
source_url: 'https://developer.apple.com/documentation/swift/float80/nextup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/nextup.json'
content_hash: 'sha256:2cc01b4f9fbf1ec9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# nextUp

<sub>Instance Property</sub>

The least representable value that compares greater than this value.

<sub>macOS</sub>

```swift
var nextUp: Float80 { get }
```

## Discussion

For any finite value `x`, `x.nextUp` is greater than `x`. For `nan` or `infinity`, `x.nextUp` is `x` itself. The following special cases also apply:

- If `x` is `-infinity`, then `x.nextUp` is `-greatestFiniteMagnitude`.
- If `x` is `-leastNonzeroMagnitude`, then `x.nextUp` is `-0.0`.
- If `x` is zero, then `x.nextUp` is `leastNonzeroMagnitude`.
- If `x` is `greatestFiniteMagnitude`, then `x.nextUp` is `infinity`.
