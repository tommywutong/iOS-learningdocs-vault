---
title: signalingNaN
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/signalingnan
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/signalingnan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/signalingnan.json'
content_hash: 'sha256:944b097345af863e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# signalingNaN

<sub>Type Property</sub>

A signaling NaN (“not a number”).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var signalingNaN: Self { get }
```

## Discussion

The default IEEE 754 behavior of operations involving a signaling NaN is to raise the Invalid flag in the floating-point environment and return a quiet NaN.

Operations on types conforming to the `FloatingPoint` protocol should support this behavior, but they might also support other options. For example, it would be reasonable to implement alternative operations in which operating on a signaling NaN triggers a runtime error or results in a diagnostic for debugging purposes. Types that implement alternative behaviors for a signaling NaN must document the departure.

Other than these signaling operations, a signaling NaN behaves in the same manner as a quiet NaN.
