---
title: 'minimum(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpoint/minimum(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/minimum(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/minimum%28_%3A_%3A%29.json'
content_hash: 'sha256:60fe95769abc2a7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# minimum(_:_:)

<sub>Type Method</sub>

Returns the lesser of the two given values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func minimum(_ x: Self, _ y: Self) -> Self
```

## Parameters

- `x` — A floating-point value.

- `y` — Another floating-point value.

## Return Value

The minimum of `x` and `y`, or whichever is a number if the other is NaN.

## Discussion

This method returns the minimum of two values, preserving order and eliminating NaN when possible. For two values `x` and `y`, the result of `minimum(x, y)` is `x` if `x <= y`, `y` if `y < x`, or whichever of `x` or `y` is a number if the other is a quiet NaN. If both `x` and `y` are NaN, or either `x` or `y` is a signaling NaN, the result is NaN.

```swift
Double.minimum(10.0, -25.0)
// -25.0
Double.minimum(10.0, .nan)
// 10.0
Double.minimum(.nan, -25.0)
// -25.0
Double.minimum(.nan, .nan)
// nan
```

The `minimum` method implements the `minNum` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Default Implementations

### FloatingPoint Implementations

- [minimum(_:_:)](<minimum(____)-cb9c.md>) — Returns the lesser of the two given values.
