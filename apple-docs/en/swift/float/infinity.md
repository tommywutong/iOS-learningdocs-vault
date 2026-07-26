---
title: infinity
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/infinity
source_url: 'https://developer.apple.com/documentation/swift/float/infinity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/infinity.json'
content_hash: 'sha256:1976e6d0738cd62c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# infinity

<sub>Type Property</sub>

Positive infinity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var infinity: Float { get }
```

## Discussion

Infinity compares greater than all finite numbers and equal to other infinite values.

```swift
let x = Double.greatestFiniteMagnitude
let y = x * 2
// y == Double.infinity
// y > x
```

## See Also

### Accessing Numeric Constants

- [pi](pi.md) — The mathematical constant pi (π), approximately equal to 3.14159.
- [greatestFiniteMagnitude](greatestfinitemagnitude.md) — The greatest finite number representable by this type.
- [nan](nan.md) — A quiet NaN (“not a number”).
- [signalingNaN](signalingnan.md) — A signaling NaN (“not a number”).
- [ulpOfOne](ulpofone.md) — The unit in the last place of 1.0.
- [leastNormalMagnitude](leastnormalmagnitude.md) — The least positive normal number.
- [leastNonzeroMagnitude](leastnonzeromagnitude.md) — The least positive number.
- [zero](zero.md) — The zero value.
