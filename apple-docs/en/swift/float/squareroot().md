---
title: squareRoot()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/squareroot()
source_url: 'https://developer.apple.com/documentation/swift/float/squareroot()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/squareroot%28%29.json'
content_hash: 'sha256:3a1505f677b7aa15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# squareRoot()

<sub>Instance Method</sub>

Returns the square root of the value, rounded to a representable value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func squareRoot() -> Self
```

## Return Value

The square root of the value.

## Discussion

The following example declares a function that calculates the length of the hypotenuse of a right triangle given its two perpendicular sides.

```swift
func hypotenuse(_ a: Double, _ b: Double) -> Double {
    return (a * a + b * b).squareRoot()
}

let (dx, dy) = (3.0, 4.0)
let distance = hypotenuse(dx, dy)
// distance == 5.0
```

## See Also

### Performing Calculations

- [Floating-Point Operators for Float](../floating-point-operators-for-float.md) — Perform arithmetic and bitwise operations or compare values.
- [addingProduct(_:_:)](<addingproduct(____).md>) — Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [addProduct(_:_:)](<addproduct(____).md>) — Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [formSquareRoot()](<formsquareroot().md>) — Replaces this value with its square root, rounded to a representable value.
- [remainder(dividingBy:)](<remainder(dividingby_).md>) — Returns the remainder of this value divided by the given value.
- [formRemainder(dividingBy:)](<formremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value.
- [truncatingRemainder(dividingBy:)](<truncatingremainder(dividingby_).md>) — Returns the remainder of this value divided by the given value using truncating division.
- [formTruncatingRemainder(dividingBy:)](<formtruncatingremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value using truncating division.
- [negate()](<negate().md>) — Replaces this value with its additive inverse.
