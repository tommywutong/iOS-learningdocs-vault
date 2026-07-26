---
title: 'addingProduct(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/addingproduct(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/double/addingproduct(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/addingproduct%28_%3A_%3A%29.json'
content_hash: 'sha256:8d3a2a5f80b8308e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# addingProduct(_:_:)

<sub>Instance Method</sub>

Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addingProduct(_ lhs: Self, _ rhs: Self) -> Self
```

## Parameters

- `lhs` — One of the values to multiply before adding to this value.

- `rhs` — The other value to multiply.

## Return Value

The product of `lhs` and `rhs`, added to this value.

## Discussion

This method is equivalent to the C `fma` function and implements the `fusedMultiplyAdd` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## See Also

### Performing Calculations

- [Floating-Point Operators for Double](../floating-point-operators-for-double.md) — Perform arithmetic and bitwise operations or compare values.
- [addProduct(_:_:)](<addproduct(____).md>) — Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [squareRoot()](<squareroot().md>) — Returns the square root of the value, rounded to a representable value.
- [formSquareRoot()](<formsquareroot().md>) — Replaces this value with its square root, rounded to a representable value.
- [remainder(dividingBy:)](<remainder(dividingby_).md>) — Returns the remainder of this value divided by the given value.
- [formRemainder(dividingBy:)](<formremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value.
- [truncatingRemainder(dividingBy:)](<truncatingremainder(dividingby_).md>) — Returns the remainder of this value divided by the given value using truncating division.
- [formTruncatingRemainder(dividingBy:)](<formtruncatingremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value using truncating division.
- [negate()](<negate().md>) — Replaces this value with its additive inverse.
