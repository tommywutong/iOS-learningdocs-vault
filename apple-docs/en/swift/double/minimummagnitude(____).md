---
title: 'minimumMagnitude(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/minimummagnitude(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/double/minimummagnitude(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/minimummagnitude%28_%3A_%3A%29.json'
content_hash: 'sha256:7ad2b74c24262aa3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# minimumMagnitude(_:_:)

<sub>Type Method</sub>

Returns the value with lesser magnitude.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func minimumMagnitude(_ x: Self, _ y: Self) -> Self
```

## Parameters

- `x` — A floating-point value.

- `y` — Another floating-point value.

## Return Value

Whichever of `x` or `y` has lesser magnitude, or whichever is a number if the other is NaN.

## Discussion

This method returns the value with lesser magnitude of the two given values, preserving order and eliminating NaN when possible. For two values `x` and `y`, the result of `minimumMagnitude(x, y)` is `x` if `x.magnitude <= y.magnitude`, `y` if `y.magnitude < x.magnitude`, or whichever of `x` or `y` is a number if the other is a quiet NaN. If both `x` and `y` are NaN, or either `x` or `y` is a signaling NaN, the result is NaN.

```swift
Double.minimumMagnitude(10.0, -25.0)
// 10.0
Double.minimumMagnitude(10.0, .nan)
// 10.0
Double.minimumMagnitude(.nan, -25.0)
// -25.0
Double.minimumMagnitude(.nan, .nan)
// nan
```

The `minimumMagnitude` method implements the `minNumMag` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## See Also

### Comparing Values

- [Floating-Point Operators for Double](../floating-point-operators-for-double.md) — Perform arithmetic and bitwise operations or compare values.
- [isEqual(to:)](<isequal(to_).md>) — Returns a Boolean value indicating whether this instance is equal to the given value.
- [isLess(than:)](<isless(than_).md>) — Returns a Boolean value indicating whether this instance is less than the given value.
- [isLessThanOrEqualTo(_:)](<islessthanorequalto(__).md>) — Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [isTotallyOrdered(belowOrEqualTo:)](<istotallyordered(beloworequalto_).md>) — Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [minimum(_:_:)](<minimum(____).md>) — Returns the lesser of the two given values.
- [maximum(_:_:)](<maximum(____).md>) — Returns the greater of the two given values.
- [maximumMagnitude(_:_:)](<maximummagnitude(____).md>) — Returns the value with greater magnitude.
