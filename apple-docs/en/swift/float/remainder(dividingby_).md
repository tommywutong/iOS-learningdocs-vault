---
title: 'remainder(dividingBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/remainder(dividingby:)'
source_url: 'https://developer.apple.com/documentation/swift/float/remainder(dividingby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/remainder%28dividingby%3A%29.json'
content_hash: 'sha256:7d37304d7e95658a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# remainder(dividingBy:)

<sub>Instance Method</sub>

Returns the remainder of this value divided by the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remainder(dividingBy other: Self) -> Self
```

## Parameters

- `other` — The value to use when dividing this value.

## Return Value

The remainder of this value divided by `other`.

## Discussion

For two finite values `x` and `y`, the remainder `r` of dividing `x` by `y` satisfies `x == y * q + r`, where `q` is the integer nearest to `x / y`. If `x / y` is exactly halfway between two integers, `q` is chosen to be even. Note that `q` is _not_ `x / y` computed in floating-point arithmetic, and that `q` may not be representable in any available integer type.

The following example calculates the remainder of dividing 8.625 by 0.75:

```swift
let x = 8.625
print(x / 0.75)
// Prints "11.5"

let q = (x / 0.75).rounded(.toNearestOrEven)
// q == 12.0
let r = x.remainder(dividingBy: 0.75)
// r == -0.375

let x1 = 0.75 * q + r
// x1 == 8.625
```

If this value and `other` are finite numbers, the remainder is in the closed range `-abs(other / 2)...abs(other / 2)`. The `remainder(dividingBy:)` method is always exact. This method implements the remainder operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## See Also

### Performing Calculations

- [Floating-Point Operators for Float](../floating-point-operators-for-float.md) — Perform arithmetic and bitwise operations or compare values.
- [addingProduct(_:_:)](<addingproduct(____).md>) — Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [addProduct(_:_:)](<addproduct(____).md>) — Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [squareRoot()](<squareroot().md>) — Returns the square root of the value, rounded to a representable value.
- [formSquareRoot()](<formsquareroot().md>) — Replaces this value with its square root, rounded to a representable value.
- [formRemainder(dividingBy:)](<formremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value.
- [truncatingRemainder(dividingBy:)](<truncatingremainder(dividingby_).md>) — Returns the remainder of this value divided by the given value using truncating division.
- [formTruncatingRemainder(dividingBy:)](<formtruncatingremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value using truncating division.
- [negate()](<negate().md>) — Replaces this value with its additive inverse.
