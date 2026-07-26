---
title: Int64
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int64
source_url: 'https://developer.apple.com/documentation/swift/int64'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int64.json'
content_hash: 'sha256:5af167df37065440'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Int64

<sub>Structure</sub>

A 64-bit signed integer value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Int64
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSScalar](../accelerate/bnnsscalar.md), [BinaryInteger](binaryinteger.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FixedWidthInteger](fixedwidthinteger.md), [Hashable](hashable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLDataValueConvertible](../createml/mldatavalueconvertible.md), [NetworkFixedWidthInteger](../network/networkfixedwidthinteger.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [SignedInteger](signedinteger.md), [SignedNumeric](signednumeric.md), [Strideable](strideable.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md)

## Topics

### Structures

- [Words](int64/words-swift.struct.md) — A type that represents the words of this integer.

### Operators

- [!=(_:_:)](<int64/!=(____).md>)
- [&=(_:_:)](<int64/&=(____).md>) — Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [&\<\<=(_:_:)](<int64/&__=(____)-3hmto.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\>\>=(_:_:)](<int64/&__=(____)-7f5t8.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [*=(_:_:)](<int64/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable.
- [+=(_:_:)](<int64/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable.
- [-=(_:_:)](<int64/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [==(_:_:)](<int64/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [\<(_:_:)](<int64/_(____)-15gfv.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [%=(_:_:)](<int64/_=(____)-6kyxv.md>) — Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [^=(_:_:)](<int64/_=(____)-8wdie.md>) — Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [|=(_:_:)](<int64/_=(____)-8xard.md>) — Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [/=(_:_:)](<int64/_=(____)-9q89m.md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable.

### Initializers

- [init(_:)](<int64/init(__)-1d7o4.md>)
- [init(_:)](<int64/init(__)-4goni.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int64/init(__)-5aiim.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int64/init(__)-87ipw.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int64/init(__)-ia49.md>)
- [init(_:)](<int64/init(__)-ro3j.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern:)](<int64/init(bitpattern_).md>) — Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](<int64/init(exactly_)-5w39p.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int64/init(exactly_)-74h3v.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int64/init(exactly_)-87idz.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int64/init(exactly_)-8nn2c.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int64/init(exactly_)-mpiy.md>)
- [init(truncating:)](<int64/init(truncating_).md>)

### Instance Properties

- [byteSwapped](int64/byteswapped.md) — A representation of this integer with the byte order swapped.
- [customPlaygroundQuickLook](int64/customplaygroundquicklook.md) — A custom playground Quick Look for the `Int64` instance. _(deprecated)_
- [leadingZeroBitCount](int64/leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [magnitude](int64/magnitude-swift.property.md) — The magnitude of this value.
- [nonzeroBitCount](int64/nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [trailingZeroBitCount](int64/trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](int64/words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

### Instance Methods

- [addingReportingOverflow(_:)](<int64/addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<int64/dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividingFullWidth(_:)](<int64/dividingfullwidth(__).md>) — Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [multipliedFullWidth(by:)](<int64/multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [multipliedReportingOverflow(by:)](<int64/multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<int64/remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [signum()](<int64/signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [subtractingReportingOverflow(_:)](<int64/subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

### Type Aliases

- [IntegerLiteralType](int64/integerliteraltype.md) — A type that represents an integer literal.
- [Magnitude](int64/magnitude-swift.typealias.md) — A type that can represent the absolute value of any possible value of this type.
- [Stride](int64/stride.md) — A type that represents the distance between two values.

### Type Properties

- [bitWidth](int64/bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.

### Default Implementations

- [AdditiveArithmetic Implementations](int64/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](int64/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](int64/binaryinteger-implementations.md)
- [Comparable Implementations](int64/comparable-implementations.md)
- [CustomReflectable Implementations](int64/customreflectable-implementations.md)
- [Decodable Implementations](int64/decodable-implementations.md)
- [Encodable Implementations](int64/encodable-implementations.md)
- [Equatable Implementations](int64/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](int64/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](int64/fixedwidthinteger-implementations.md)
- [Hashable Implementations](int64/hashable-implementations.md)
- [SIMDScalar Implementations](int64/simdscalar-implementations.md)
- [SignedInteger Implementations](int64/signedinteger-implementations.md)
- [SignedNumeric Implementations](int64/signednumeric-implementations.md)

## See Also

### Signed Integers

- [Int8](int8.md) — An 8-bit signed integer value type.
- [Int16](int16.md) — A 16-bit signed integer value type.
- [Int32](int32.md) — A 32-bit signed integer value type.
- [Int128](int128.md) — A 128-bit signed integer value type.
