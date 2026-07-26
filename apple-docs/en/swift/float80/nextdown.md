---
title: nextDown
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/nextdown
source_url: 'https://developer.apple.com/documentation/swift/float80/nextdown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/nextdown.json'
content_hash: 'sha256:f1d404652e91ee52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# nextDown

<sub>Instance Property</sub>

The greatest representable value that compares less than this value.

<sub>macOS</sub>

```swift
var nextDown: Self { get }
```

## Discussion

For any finite value `x`, `x.nextDown` is less than `x`. For `nan` or `-infinity`, `x.nextDown` is `x` itself. The following special cases also apply:

- If `x` is `infinity`, then `x.nextDown` is `greatestFiniteMagnitude`.
- If `x` is `leastNonzeroMagnitude`, then `x.nextDown` is `0.0`.
- If `x` is zero, then `x.nextDown` is `-leastNonzeroMagnitude`.
- If `x` is `-greatestFiniteMagnitude`, then `x.nextDown` is `-infinity`.
