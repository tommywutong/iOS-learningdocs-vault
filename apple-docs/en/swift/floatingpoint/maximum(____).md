---
title: 'maximum(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpoint/maximum(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/maximum(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/maximum%28_%3A_%3A%29.json'
content_hash: 'sha256:ad3eb0426d99689e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# maximum(_:_:)

<sub>Type Method</sub>

Returns the greater of the two given values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func maximum(_ x: Self, _ y: Self) -> Self
```

## Parameters

- `x` — A floating-point value.

- `y` — Another floating-point value.

## Return Value

The greater of `x` and `y`, or whichever is a number if the other is NaN.

## Discussion

This method returns the maximum of two values, preserving order and eliminating NaN when possible. For two values `x` and `y`, the result of `maximum(x, y)` is `x` if `x > y`, `y` if `x <= y`, or whichever of `x` or `y` is a number if the other is a quiet NaN. If both `x` and `y` are NaN, or either `x` or `y` is a signaling NaN, the result is NaN.

```swift
Double.maximum(10.0, -25.0)
// 10.0
Double.maximum(10.0, .nan)
// 10.0
Double.maximum(.nan, -25.0)
// -25.0
Double.maximum(.nan, .nan)
// nan
```

The `maximum` method implements the `maxNum` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Default Implementations

### FloatingPoint Implementations

- [maximum(_:_:)](<maximum(____)-1dfa.md>) — Returns the greater of the two given values.
