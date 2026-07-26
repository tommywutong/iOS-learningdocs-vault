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
doc_path: /documentation/swift/uint64/binaryinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/uint64/binaryinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64/binaryinteger-implementations.json'
content_hash: 'sha256:e4a762de972cbcf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [Special-Use Numeric Types](../special-use-numeric-types.md) · [UInt64](../uint64.md)

# BinaryInteger Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [!=(_:_:)](<!=(____)-67tzk.md>) — Returns a Boolean value indicating whether the two given values are not equal.
- [&(_:_:)](<&(____).md>) — Returns the result of performing a bitwise AND operation on the two given values.
- [&(_:_:)](<&(____)-3x1yh.md>) — Returns the result of performing a bitwise AND operation on the two given values.
- [*(_:_:)](<_(____).md>) — Multiplies two values and produces their product.
- [+(_:_:)](<+(____).md>) — Adds two values and produces their sum.
- [-(_:_:)](<-(____).md>) — Subtracts one value from another and produces their difference.
- [==(_:_:)](<==(____)-6ra49.md>) — Returns a Boolean value indicating whether the two given values are equal.
- [^(_:_:)](<_(____)-1kwg2.md>) — Returns the result of performing a bitwise XOR operation on the two given values.
- [|(_:_:)](<_(____)-2girh.md>) — Returns the result of performing a bitwise OR operation on the two given values.
- [^(_:_:)](<_(____)-5hgaz.md>) — Returns the result of performing a bitwise XOR operation on the two given values.
- [\>(_:_:)](<_(____)-5jero.md>)
- [%(_:_:)](<_(____)-68vrk.md>) — Returns the remainder of dividing the first value by the second.
- [|(_:_:)](<_(____)-6ykmm.md>) — Returns the result of performing a bitwise OR operation on the two given values.
- [\<(_:_:)](<_(____)-75vtz.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [/(_:_:)](<_(____)-8b3l2.md>) — Returns the quotient of dividing the first value by the second.
- [\>(_:_:)](<_(____)-9xpv.md>) — Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [\<=(_:_:)](<_=(____)-1clb5.md>) — Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [\<=(_:_:)](<_=(____)-4pbv7.md>)
- [\>=(_:_:)](<_=(____)-5p2f4.md>) — Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [\>=(_:_:)](<_=(____)-5sy3d.md>)
- [\>\>(_:_:)](<__(____)-25f5d.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [\<\<(_:_:)](<__(____)-5so09.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [\>\>(_:_:)](<__(____)-7rk6f.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [\<\<(_:_:)](<__(____)-83yhh.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [\>\>=(_:_:)](<__=(____)-25p32.md>) — Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [\<\<=(_:_:)](<__=(____)-7usr.md>) — Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
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
