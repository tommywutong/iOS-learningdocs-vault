---
title: 'addProduct(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/addproduct(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/float/addproduct(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/addproduct%28_%3A_%3A%29.json'
content_hash: 'sha256:5d338ea0a3e89b05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# addProduct(_:_:)

<sub>Instance Method</sub>

Adds the product of the two given values to this value in place, computed without intermediate rounding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addProduct(_ lhs: Float, _ rhs: Float)
```

## Parameters

- `lhs` — One of the values to multiply before adding to this value.

- `rhs` — The other value to multiply.

## See Also

### Performing Calculations

- [Floating-Point Operators for Float](../floating-point-operators-for-float.md) — Perform arithmetic and bitwise operations or compare values.
- [addingProduct(_:_:)](<addingproduct(____).md>) — Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [squareRoot()](<squareroot().md>) — Returns the square root of the value, rounded to a representable value.
- [formSquareRoot()](<formsquareroot().md>) — Replaces this value with its square root, rounded to a representable value.
- [remainder(dividingBy:)](<remainder(dividingby_).md>) — Returns the remainder of this value divided by the given value.
- [formRemainder(dividingBy:)](<formremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value.
- [truncatingRemainder(dividingBy:)](<truncatingremainder(dividingby_).md>) — Returns the remainder of this value divided by the given value using truncating division.
- [formTruncatingRemainder(dividingBy:)](<formtruncatingremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value using truncating division.
- [negate()](<negate().md>) — Replaces this value with its additive inverse.
