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
doc_path: /documentation/swift/int128/binaryinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/int128/binaryinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/binaryinteger-implementations.json'
content_hash: 'sha256:83ee3576915f0cbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [Special-Use Numeric Types](../special-use-numeric-types.md) · [Int128](../int128.md)

# BinaryInteger Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [!=(_:_:)](<!=(____)-4l6xf.md>) — Returns a Boolean value indicating whether the two given values are not equal.
- [&(_:_:)](<&(____).md>) — Returns the result of performing a bitwise AND operation on the two given values.
- [&=(_:_:)](<&=(____).md>) — Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [==(_:_:)](<==(____)-31spp.md>) — Returns a Boolean value indicating whether the two given values are equal.
- [|(_:_:)](<_(____)-120rc.md>) — Returns the result of performing a bitwise OR operation on the two given values.
- [\>(_:_:)](<_(____)-3jxf8.md>) — Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [/(_:_:)](<_(____)-3u29x.md>) — Returns the quotient of dividing the first value by the second.
- [%(_:_:)](<_(____)-4kr9j.md>) — Returns the remainder of dividing the first value by the second.
- [^(_:_:)](<_(____)-4wqvr.md>) — Returns the result of performing a bitwise XOR operation on the two given values.
- [\<(_:_:)](<_(____)-6c38s.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [\>(_:_:)](<_(____)-71bfg.md>)
- [\>=(_:_:)](<_=(____)-2rq25.md>)
- [\<=(_:_:)](<_=(____)-3tzf9.md>)
- [/=(_:_:)](<_=(____)-4hmtz.md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [%=(_:_:)](<_=(____)-58nmj.md>) — Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [|=(_:_:)](<_=(____)-791af.md>) — Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [\>=(_:_:)](<_=(____)-90wyd.md>) — Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [\<=(_:_:)](<_=(____)-9kicv.md>) — Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [^=(_:_:)](<_=(____)-ckwk.md>) — Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [\>\>(_:_:)](<__(____)-10plt.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [\<\<(_:_:)](<__(____)-30yed.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [\<\<(_:_:)](<__(____)-6jhs3.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [\>\>(_:_:)](<__(____)-80gwd.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [\<\<=(_:_:)](<__=(____)-195op.md>) — Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [\>\>=(_:_:)](<__=(____)-3w1qu.md>) — Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [~(_:)](<~(__).md>) — Returns the inverse of the bits set in the argument.

### Initializers

- [init()](<init().md>) — Creates a new value equal to zero.
- [init(_:)](<init(__)-7ib60.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<init(__)-95d5.md>) — Creates a new instance from the given integer.
- [init(clamping:)](<init(clamping_).md>) — Creates a new instance with the representable value that’s closest to the given integer.
- [init(clamping:)](<init(clamping_)-4ogm3.md>) — Creates a new instance with the representable value that’s closest to the given integer.
- [init(exactly:)](<init(exactly_)-7ybhb.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_).md>) — Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_)-9tq25.md>) — Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.

### Instance Properties

- [bitWidth](bitwidth-swift.property.md) — The number of bits in the current binary representation of this value.
- [description](description.md) — A textual representation of this value.
- [trailingZeroBitCount](trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

### Instance Methods

- [advanced(by:)](<advanced(by_).md>) — Returns a value that is offset the specified distance from this value.
- [distance(to:)](<distance(to_).md>) — Returns the distance from this value to the given value, expressed as a stride.
- [isMultiple(of:)](<ismultiple(of_).md>) — Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [quotientAndRemainder(dividingBy:)](<quotientandremainder(dividingby_).md>) — Returns the quotient and remainder of this value divided by the given value.
- [signum()](<signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.

### Type Aliases

- [Words](words-swift.typealias.md) — A type that represents the words of a binary integer.
