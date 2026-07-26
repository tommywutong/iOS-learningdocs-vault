---
title: Floating-Point Operators for Double
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floating-point-operators-for-double
source_url: 'https://developer.apple.com/documentation/swift/floating-point-operators-for-double'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floating-point-operators-for-double.json'
content_hash: 'sha256:a0abc42b274ab140'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Double](double.md)

# Floating-Point Operators for Double

<sub>API Collection</sub>

Perform arithmetic and bitwise operations or compare values.

## Topics

### Arithmetic

- [+(_:_:)](<double/+(____).md>) — Adds two values and produces their sum, rounded to a representable value.
- [-(_:_:)](<double/-(____).md>) — Subtracts one value from another and produces their difference, rounded to a representable value.
- [*(_:_:)](<double/_(____).md>) — Multiplies two values and produces their product, rounding to a representable value.
- [/(_:_:)](<double/_(____).md>) — Returns the quotient of dividing the first value by the second, rounded to a representable value.

### Arithmetic with Assignment

- [+=(_:_:)](<double/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [-=(_:_:)](<double/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [*=(_:_:)](<double/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [/=(_:_:)](<double/_=(____).md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.

### Comparison

- [==(_:_:)](<double/==(____)-12hdv.md>) — Returns a Boolean value indicating whether two values are equal.
- [!=(_:_:)](<double/!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.

### Negation

- [-(_:)](<double/-(__).md>) — Calculates the additive inverse of a value.
- [+(_:)](<double/+(__).md>) — Returns the given number unchanged.

### Range Expressions

- [...(_:)](<double/'...(__)-4mm67.md>) — Returns a partial range up to, and including, its upper bound.
- [...(_:)](<double/'...(__)-6ct5v.md>) — Returns a partial range extending upward from a lower bound.

## See Also

### Performing Calculations

- [addingProduct(_:_:)](<double/addingproduct(____).md>) — Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [addProduct(_:_:)](<double/addproduct(____).md>) — Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [squareRoot()](<double/squareroot().md>) — Returns the square root of the value, rounded to a representable value.
- [formSquareRoot()](<double/formsquareroot().md>) — Replaces this value with its square root, rounded to a representable value.
- [remainder(dividingBy:)](<double/remainder(dividingby_).md>) — Returns the remainder of this value divided by the given value.
- [formRemainder(dividingBy:)](<double/formremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value.
- [truncatingRemainder(dividingBy:)](<double/truncatingremainder(dividingby_).md>) — Returns the remainder of this value divided by the given value using truncating division.
- [formTruncatingRemainder(dividingBy:)](<double/formtruncatingremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value using truncating division.
- [negate()](<double/negate().md>) — Replaces this value with its additive inverse.
