---
title: Floating-Point Operators for Float
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floating-point-operators-for-float
source_url: 'https://developer.apple.com/documentation/swift/floating-point-operators-for-float'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floating-point-operators-for-float.json'
content_hash: 'sha256:e01a00bbf1717f5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md) · [Numbers and Basic Values](numbers-and-basic-values.md) · [Float](float.md)

# Floating-Point Operators for Float

<sub>API Collection</sub>

Perform arithmetic and bitwise operations or compare values.

## Topics

### Arithmetic

- [+(_:_:)](<float/+(____).md>) — Adds two values and produces their sum, rounded to a representable value.
- [-(_:_:)](<float/-(____).md>) — Subtracts one value from another and produces their difference, rounded to a representable value.
- [*(_:_:)](<float/_(____).md>) — Multiplies two values and produces their product, rounding to a representable value.
- [/(_:_:)](<float/_(____).md>) — Returns the quotient of dividing the first value by the second, rounded to a representable value.

### Arithmetic with Assignment

- [+=(_:_:)](<float/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [-=(_:_:)](<float/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [*=(_:_:)](<float/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [/=(_:_:)](<float/_=(____).md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.

### Comparison

- [==(_:_:)](<float/==(____)-12hdt.md>) — Returns a Boolean value indicating whether two values are equal.
- [!=(_:_:)](<float/!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.
- [\<(_:_:)](<float/_(____)-7lwp7.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [\<=(_:_:)](<float/_=(____)-5yoz5.md>)
- [\>(_:_:)](<float/_(____)-552jr.md>)
- [\>=(_:_:)](<float/_=(____)-9o6ha.md>)

### Negation

- [-(_:)](<float/-(__).md>) — Calculates the additive inverse of a value.
- [+(_:)](<float/+(__).md>) — Returns the given number unchanged.

### Range Expressions

- [..\<(_:)](<float/'.._(__).md>) — Returns a partial range up to, but not including, its upper bound.
- [...(_:)](<float/'...(__)-4mm65.md>) — Returns a partial range up to, and including, its upper bound.
- [...(_:)](<float/'...(__)-6ct5t.md>) — Returns a partial range extending upward from a lower bound.

## See Also

### Performing Calculations

- [addingProduct(_:_:)](<float/addingproduct(____).md>) — Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [addProduct(_:_:)](<float/addproduct(____).md>) — Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [squareRoot()](<float/squareroot().md>) — Returns the square root of the value, rounded to a representable value.
- [formSquareRoot()](<float/formsquareroot().md>) — Replaces this value with its square root, rounded to a representable value.
- [remainder(dividingBy:)](<float/remainder(dividingby_).md>) — Returns the remainder of this value divided by the given value.
- [formRemainder(dividingBy:)](<float/formremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value.
- [truncatingRemainder(dividingBy:)](<float/truncatingremainder(dividingby_).md>) — Returns the remainder of this value divided by the given value using truncating division.
- [formTruncatingRemainder(dividingBy:)](<float/formtruncatingremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value using truncating division.
- [negate()](<float/negate().md>) — Replaces this value with its additive inverse.
