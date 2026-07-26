---
title: Integer Operators
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/integer-operators
source_url: 'https://developer.apple.com/documentation/swift/integer-operators'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/integer-operators.json'
content_hash: 'sha256:e62a10744dae182c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Int](int.md)

# Integer Operators

<sub>API Collection</sub>

Perform arithmetic and bitwise operations or compare values.

## Topics

### Arithmetic

- [+(_:_:)](<int/+(____).md>) — Adds two values and produces their sum.
- [-(_:_:)](<int/-(____).md>) — Subtracts one value from another and produces their difference.
- [*(_:_:)](<int/_(____).md>) — Multiplies two values and produces their product.
- [/(_:_:)](<int/_(____)-7j9bj.md>) — Returns the quotient of dividing the first value by the second.

### Arithmetic with Assignment

- [+=(_:_:)](<int/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable.
- [*=(_:_:)](<int/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable.
- [/=(_:_:)](<int/_=(____)-9lzpe.md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable.

### Masked Arithmetic

- [&+(_:_:)](<int/&+(____).md>) — Returns the sum of the two given values, wrapping the result in case of any overflow.
- [&-(_:_:)](<int/&-(____).md>) — Returns the difference of the two given values, wrapping the result in case of any overflow.
- [&*(_:_:)](<int/&_(____).md>) — Returns the product of the two given values, wrapping the result in case of any overflow.
- [&+=(_:_:)](<int/&+=(____).md>) — Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [&-=(_:_:)](<int/&-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [&*=(_:_:)](<int/&_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.

### Bitwise Operations

- [&(_:_:)](<int/&(____).md>) — Returns the result of performing a bitwise AND operation on the two given values.
- [&=(_:_:)](<int/&=(____).md>) — Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [~(_:)](<int/~(__).md>) — Returns the inverse of the bits set in the argument.

### Negation

- [-(_:)](<int/-(__).md>) — Returns the additive inverse of the specified value.
- [+(_:)](<int/+(__).md>) — Returns the given number unchanged.

### Comparison

- [==(_:_:)](<int/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [==(_:_:)](<int/==(____)-1zalu.md>) — Returns a Boolean value indicating whether the two given values are equal.
- [!=(_:_:)](<int/!=(____)-4jphg.md>) — Returns a Boolean value indicating whether the two given values are not equal.

### Range Expressions

- [...(_:_:)](<int/'...(____).md>) — Returns a closed range that contains both of its bounds.
- [...(_:)](<int/'...(__)-6ct66.md>) — Returns a partial range extending upward from a lower bound.
- [...(_:)](<int/'...(__)-4mm5u.md>) — Returns a partial range up to, and including, its upper bound.

### Deprecated

- [-=(_:_:)](<int/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable.

## See Also

### Performing Calculations

- [negate()](<int/negate().md>) — Replaces this value with its additive inverse.
- [quotientAndRemainder(dividingBy:)](<int/quotientandremainder(dividingby_).md>) — Returns the quotient and remainder of this value divided by the given value.
- [isMultiple(of:)](<int/ismultiple(of_).md>) — Returns `true` if this value is a multiple of the given value, and `false` otherwise.
