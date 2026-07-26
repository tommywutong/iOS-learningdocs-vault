---
title: UInt64
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint64
source_url: 'https://developer.apple.com/documentation/swift/uint64'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64.json'
content_hash: 'sha256:b8c47ffabe01d56d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UInt64

<sub>Structure</sub>

A 64-bit unsigned integer value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UInt64
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSScalar](../accelerate/bnnsscalar.md), [BinaryInteger](binaryinteger.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FixedWidthInteger](fixedwidthinteger.md), [Hashable](hashable.md), [LosslessStringConvertible](losslessstringconvertible.md), [NetworkFixedWidthInteger](../network/networkfixedwidthinteger.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Strideable](strideable.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md), [UnsignedInteger](unsignedinteger.md)

## Topics

### Structures

- [Words](uint64/words-swift.struct.md) — A type that represents the words of this integer.

### Operators

- [!=(_:_:)](<uint64/!=(____).md>)
- [&=(_:_:)](<uint64/&=(____).md>) — Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [&\>\>=(_:_:)](<uint64/&__=(____)-9z0pp.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\<\<=(_:_:)](<uint64/&__=(____)-p2fc.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [*=(_:_:)](<uint64/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable.
- [+=(_:_:)](<uint64/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable.
- [-=(_:_:)](<uint64/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [==(_:_:)](<uint64/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [\<(_:_:)](<uint64/_(____)-1zzq5.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [%=(_:_:)](<uint64/_=(____)-20phr.md>) — Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [|=(_:_:)](<uint64/_=(____)-3oy72.md>) — Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [^=(_:_:)](<uint64/_=(____)-7dm2a.md>) — Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [/=(_:_:)](<uint64/_=(____)-9jhbb.md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable.

### Initializers

- [init(_:)](<uint64/init(__)-31scj.md>)
- [init(_:)](<uint64/init(__)-6bhfg.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint64/init(__)-71bjo.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint64/init(__)-7pz4t.md>)
- [init(_:)](<uint64/init(__)-7yfzu.md>) — Construct with value `v.value`.
- [init(_:)](<uint64/init(__)-86c9y.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint64/init(__)-8hpyb.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern:)](<uint64/init(bitpattern_).md>) — Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](<uint64/init(exactly_)-1laz5.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint64/init(exactly_)-1rz30.md>)
- [init(exactly:)](<uint64/init(exactly_)-4pdnv.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint64/init(exactly_)-92on5.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint64/init(exactly_)-gsjs.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating:)](<uint64/init(truncating_).md>)

### Instance Properties

- [byteSwapped](uint64/byteswapped.md) — A representation of this integer with the byte order swapped.
- [customPlaygroundQuickLook](uint64/customplaygroundquicklook.md) — A custom playground Quick Look for the `UInt64` instance. _(deprecated)_
- [leadingZeroBitCount](uint64/leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [nonzeroBitCount](uint64/nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [trailingZeroBitCount](uint64/trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](uint64/words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

### Instance Methods

- [addingReportingOverflow(_:)](<uint64/addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<uint64/dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividingFullWidth(_:)](<uint64/dividingfullwidth(__).md>) — Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [multipliedFullWidth(by:)](<uint64/multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [multipliedReportingOverflow(by:)](<uint64/multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<uint64/remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [signum()](<uint64/signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [subtractingReportingOverflow(_:)](<uint64/subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

### Type Aliases

- [IntegerLiteralType](uint64/integerliteraltype.md) — A type that represents an integer literal.
- [Magnitude](uint64/magnitude.md) — A type that can represent the absolute value of any possible value of this type.
- [Stride](uint64/stride.md) — A type that represents the distance between two values.

### Type Properties

- [bitWidth](uint64/bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.

### Default Implementations

- [AdditiveArithmetic Implementations](uint64/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](uint64/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](uint64/binaryinteger-implementations.md)
- [Comparable Implementations](uint64/comparable-implementations.md)
- [CustomReflectable Implementations](uint64/customreflectable-implementations.md)
- [Decodable Implementations](uint64/decodable-implementations.md)
- [Encodable Implementations](uint64/encodable-implementations.md)
- [Equatable Implementations](uint64/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](uint64/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](uint64/fixedwidthinteger-implementations.md)
- [Hashable Implementations](uint64/hashable-implementations.md)
- [SIMDScalar Implementations](uint64/simdscalar-implementations.md)
- [UnsignedInteger Implementations](uint64/unsignedinteger-implementations.md)

## See Also

### Unsigned Integers

- [UInt](uint.md) — An unsigned integer value type.
- [UInt8](uint8.md) — An 8-bit unsigned integer value type.
- [UInt16](uint16.md) — A 16-bit unsigned integer value type.
- [UInt32](uint32.md) — A 32-bit unsigned integer value type.
- [UInt128](uint128.md) — A 128-bit unsigned integer value type.
