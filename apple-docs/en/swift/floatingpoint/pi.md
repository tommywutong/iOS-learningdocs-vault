---
title: pi
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/pi
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/pi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/pi.json'
content_hash: 'sha256:a0c68662c161b094'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# pi

<sub>Type Property</sub>

The mathematical constant pi (π), approximately equal to 3.14159.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var pi: Self { get }
```

## Discussion

When measuring an angle in radians, π is equivalent to a half-turn.

This value is rounded toward zero to keep user computations with angles from inadvertently ending up in the wrong quadrant. A type that conforms to the `FloatingPoint` protocol provides the value for `pi` at its best possible precision.

```swift
print(Double.pi)
// Prints "3.14159265358979"
```
