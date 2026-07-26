---
title: signalingNaN
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/signalingnan
source_url: 'https://developer.apple.com/documentation/swift/float80/signalingnan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/signalingnan.json'
content_hash: 'sha256:b6fce7ff288b51d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# signalingNaN

<sub>Type Property</sub>

A signaling NaN (“not a number”).

<sub>macOS</sub>

```swift
static var signalingNaN: Float80 { get }
```

## Discussion

The default IEEE 754 behavior of operations involving a signaling NaN is to raise the Invalid flag in the floating-point environment and return a quiet NaN.

Operations on types conforming to the `FloatingPoint` protocol should support this behavior, but they might also support other options. For example, it would be reasonable to implement alternative operations in which operating on a signaling NaN triggers a runtime error or results in a diagnostic for debugging purposes. Types that implement alternative behaviors for a signaling NaN must document the departure.

Other than these signaling operations, a signaling NaN behaves in the same manner as a quiet NaN.
