---
title: significandWidth
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/significandwidth
source_url: 'https://developer.apple.com/documentation/swift/float80/significandwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/significandwidth.json'
content_hash: 'sha256:53ef34a1ef472cf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# significandWidth

<sub>Instance Property</sub>

The number of bits required to represent the value’s significand.

<sub>macOS</sub>

```swift
var significandWidth: Int { get }
```

## Discussion

If this value is a finite nonzero number, `significandWidth` is the number of fractional bits required to represent the value of `significand`; otherwise, `significandWidth` is -1. The value of `significandWidth` is always -1 or between zero and `significandBitCount`. For example:

- For any representable power of two, `significandWidth` is zero, because `significand` is `1.0`.
- If `x` is 10, `x.significand` is `1.01` in binary, so `x.significandWidth` is 2.
- If `x` is Float.pi, `x.significand` is `1.10010010000111111011011` in binary, and `x.significandWidth` is 23.
