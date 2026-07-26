---
title: 'maximumMagnitude(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpoint/maximummagnitude(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/maximummagnitude(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/maximummagnitude%28_%3A_%3A%29.json'
content_hash: 'sha256:3a6c743721e89647'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# maximumMagnitude(_:_:)

<sub>Type Method</sub>

Returns the value with greater magnitude.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func maximumMagnitude(_ x: Self, _ y: Self) -> Self
```

## Parameters

- `x` — A floating-point value.

- `y` — Another floating-point value.

## Return Value

Whichever of `x` or `y` has greater magnitude, or whichever is a number if the other is NaN.

## Discussion

This method returns the value with greater magnitude of the two given values, preserving order and eliminating NaN when possible. For two values `x` and `y`, the result of `maximumMagnitude(x, y)` is `x` if `x.magnitude > y.magnitude`, `y` if `x.magnitude <= y.magnitude`, or whichever of `x` or `y` is a number if the other is a quiet NaN. If both `x` and `y` are NaN, or either `x` or `y` is a signaling NaN, the result is NaN.

```swift
Double.maximumMagnitude(10.0, -25.0)
// -25.0
Double.maximumMagnitude(10.0, .nan)
// 10.0
Double.maximumMagnitude(.nan, -25.0)
// -25.0
Double.maximumMagnitude(.nan, .nan)
// nan
```

The `maximumMagnitude` method implements the `maxNumMag` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Default Implementations

### FloatingPoint Implementations

- [maximumMagnitude(_:_:)](<maximummagnitude(____)-1e1x7.md>) — Returns the value with greater magnitude.
