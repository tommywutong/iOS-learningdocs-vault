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
doc_path: /documentation/swift/uint8/binaryinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/uint8/binaryinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint8/binaryinteger-implementations.json'
content_hash: 'sha256:c34b99cfd01f56aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [Special-Use Numeric Types](../special-use-numeric-types.md) · [UInt8](../uint8.md)

# BinaryInteger Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [!=(_:_:)](<!=(____)-99bok.md>) — Returns a Boolean value indicating whether the two given values are not equal.
- [&(_:_:)](<&(____).md>) — Returns the result of performing a bitwise AND operation on the two given values.
- [&(_:_:)](<&(____)-4psmt.md>) — Returns the result of performing a bitwise AND operation on the two given values.
- [*(_:_:)](<_(____).md>) — Multiplies two values and produces their product.
- [+(_:_:)](<+(____).md>) — Adds two values and produces their sum.
- [-(_:_:)](<-(____).md>) — Subtracts one value from another and produces their difference.
- [==(_:_:)](<==(____)-156b9.md>) — Returns a Boolean value indicating whether the two given values are equal.
- [|(_:_:)](<_(____)-17p9c.md>) — Returns the result of performing a bitwise OR operation on the two given values.
- [^(_:_:)](<_(____)-2kgmz.md>) — Returns the result of performing a bitwise XOR operation on the two given values.
- [/(_:_:)](<_(____)-327b5.md>) — Returns the quotient of dividing the first value by the second.
- [^(_:_:)](<_(____)-4eiav.md>) — Returns the result of performing a bitwise XOR operation on the two given values.
- [\<(_:_:)](<_(____)-5kmc9.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [\>(_:_:)](<_(____)-6ieix.md>)
- [\>(_:_:)](<_(____)-7nbqc.md>) — Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [|(_:_:)](<_(____)-865lu.md>) — Returns the result of performing a bitwise OR operation on the two given values.
- [%(_:_:)](<_(____)-9tmal.md>) — Returns the remainder of dividing the first value by the second.
- [\<=(_:_:)](<_=(____)-6b690.md>) — Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [\<=(_:_:)](<_=(____)-7efxq.md>)
- [\>=(_:_:)](<_=(____)-8oubr.md>)
- [\>=(_:_:)](<_=(____)-9rm29.md>) — Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [\>\>(_:_:)](<__(____)-2qqlb.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [\>\>(_:_:)](<__(____)-56eg9.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [\<\<(_:_:)](<__(____)-7yxgh.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [\<\<(_:_:)](<__(____)-jtqk.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [\<\<=(_:_:)](<__=(____)-1p711.md>) — Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [\>\>=(_:_:)](<__=(____)-8pj4c.md>) — Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
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
