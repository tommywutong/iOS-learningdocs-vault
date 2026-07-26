---
title: pi
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/pi
source_url: 'https://developer.apple.com/documentation/swift/float80/pi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/pi.json'
content_hash: 'sha256:b0ed37c909f28a12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# pi

<sub>Type Property</sub>

The mathematical constant pi (π), approximately equal to 3.14159.

<sub>macOS</sub>

```swift
static var pi: Float80 { get }
```

## Discussion

When measuring an angle in radians, π is equivalent to a half-turn.

This value is rounded toward zero to keep user computations with angles from inadvertently ending up in the wrong quadrant. A type that conforms to the `FloatingPoint` protocol provides the value for `pi` at its best possible precision.

```swift
print(Double.pi)
// Prints "3.14159265358979"
```
