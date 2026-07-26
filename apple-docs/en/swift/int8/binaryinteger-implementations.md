---
title: BinaryInteger Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int8/binaryinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/int8/binaryinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/binaryinteger-implementations.json'
content_hash: 'sha256:13194a6be38972c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [Special-Use Numeric Types](../special-use-numeric-types.md) · [Int8](../int8.md)

# BinaryInteger Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [!=(_:_:)](<!=(____)-5cims.md>) — Returns a Boolean value indicating whether the two given values are not equal.
- [&(_:_:)](<&(____).md>) — Returns the result of performing a bitwise AND operation on the two given values.
- [&(_:_:)](<&(____)-6jf06.md>) — Returns the result of performing a bitwise AND operation on the two given values.
- [*(_:_:)](<_(____).md>) — Multiplies two values and produces their product.
- [+(_:_:)](<+(____).md>) — Adds two values and produces their sum.
- [-(_:_:)](<-(____).md>) — Subtracts one value from another and produces their difference.
- [==(_:_:)](<==(____)-exky.md>) — Returns a Boolean value indicating whether the two given values are equal.
- [\>(_:_:)](<_(____)-1jlfi.md>)
- [^(_:_:)](<_(____)-346io.md>) — Returns the result of performing a bitwise XOR operation on the two given values.
- [\>(_:_:)](<_(____)-53qq.md>) — Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [|(_:_:)](<_(____)-5p6eu.md>) — Returns the result of performing a bitwise OR operation on the two given values.
- [\<(_:_:)](<_(____)-615a6.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [|(_:_:)](<_(____)-662qp.md>) — Returns the result of performing a bitwise OR operation on the two given values.
- [%(_:_:)](<_(____)-6tefc.md>) — Returns the remainder of dividing the first value by the second.
- [^(_:_:)](<_(____)-a3sx.md>) — Returns the result of performing a bitwise XOR operation on the two given values.
- [/(_:_:)](<_(____)-aic4.md>) — Returns the quotient of dividing the first value by the second.
- [\<=(_:_:)](<_=(____)-10tl1.md>) — Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [\>=(_:_:)](<_=(____)-3nz2d.md>)
- [\>=(_:_:)](<_=(____)-41bgc.md>) — Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [\<=(_:_:)](<_=(____)-5bita.md>)
- [\<\<(_:_:)](<__(____)-3z21o.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [\>\>(_:_:)](<__(____)-7wosz.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [\<\<(_:_:)](<__(____)-9i518.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [\>\>(_:_:)](<__(____)-moua.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [\>\>=(_:_:)](<__=(____)-40egk.md>) — Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [\<\<=(_:_:)](<__=(____)-53mkr.md>) — Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [~(_:)](<~(__).md>) — Returns the inverse of the bits set in the argument.

### Initializers

- [init()](<init().md>) — Creates a new value equal to zero.
- [init(clamping:)](<init(clamping_).md>) — Creates a new instance with the representable value that’s closest to the given integer.
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_).md>) — Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.

### Instance Properties

- [bitWidth](bitwidth-swift.property.md) — The number of bits in the current binary representation of this value.
- [description](description.md) — A textual representation of this value.

### Instance Methods

- [advanced(by:)](<advanced(by_).md>) — Returns a value that is offset the specified distance from this value.
- [distance(to:)](<distance(to_).md>) — Returns the distance from this value to the given value, expressed as a stride.
- [isMultiple(of:)](<ismultiple(of_).md>) — Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [quotientAndRemainder(dividingBy:)](<quotientandremainder(dividingby_).md>) — Returns the quotient and remainder of this value divided by the given value.
