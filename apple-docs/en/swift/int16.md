---
title: Int16
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int16
source_url: 'https://developer.apple.com/documentation/swift/int16'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int16.json'
content_hash: 'sha256:8f586fc77c9af5f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Int16

<sub>Structure</sub>

A 16-bit signed integer value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Int16
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSScalar](../accelerate/bnnsscalar.md), [BinaryInteger](binaryinteger.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FixedWidthInteger](fixedwidthinteger.md), [Hashable](hashable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLTensorScalar](../coreml/mltensorscalar.md), [NetworkFixedWidthInteger](../network/networkfixedwidthinteger.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [SignedInteger](signedinteger.md), [SignedNumeric](signednumeric.md), [Strideable](strideable.md), [vDSP_IntegerConvertable](../accelerate/vdsp_integerconvertable.md)

## Topics

### Structures

- [Words](int16/words-swift.struct.md) — A type that represents the words of this integer.

### Operators

- [!=(_:_:)](<int16/!=(____).md>)
- [&=(_:_:)](<int16/&=(____).md>) — Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [&\<\<=(_:_:)](<int16/&__=(____)-99pwo.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\>\>=(_:_:)](<int16/&__=(____)-p5ty.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [*=(_:_:)](<int16/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable.
- [+=(_:_:)](<int16/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable.
- [-=(_:_:)](<int16/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [==(_:_:)](<int16/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [\<(_:_:)](<int16/_(____)-47ytd.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [/=(_:_:)](<int16/_=(____)-15qjk.md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [%=(_:_:)](<int16/_=(____)-1zcaj.md>) — Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [^=(_:_:)](<int16/_=(____)-3hk1a.md>) — Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [|=(_:_:)](<int16/_=(____)-9yk6s.md>) — Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.

### Initializers

- [init(_:)](<int16/init(__)-192r7.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int16/init(__)-4h6i5.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int16/init(__)-5r9gw.md>)
- [init(_:)](<int16/init(__)-6paha.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int16/init(__)-8tp32.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int16/init(__)-9hqpm.md>)
- [init(bitPattern:)](<int16/init(bitpattern_).md>) — Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](<int16/init(exactly_)-1zxj5.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int16/init(exactly_)-3vet0.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int16/init(exactly_)-5zk1.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int16/init(exactly_)-8omg3.md>)
- [init(exactly:)](<int16/init(exactly_)-8v4ka.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating:)](<int16/init(truncating_).md>)

### Instance Properties

- [byteSwapped](int16/byteswapped.md) — A representation of this integer with the byte order swapped.
- [customPlaygroundQuickLook](int16/customplaygroundquicklook.md) — A custom playground Quick Look for the `Int16` instance. _(deprecated)_
- [leadingZeroBitCount](int16/leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [magnitude](int16/magnitude-swift.property.md) — The magnitude of this value.
- [nonzeroBitCount](int16/nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [trailingZeroBitCount](int16/trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](int16/words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

### Instance Methods

- [addingReportingOverflow(_:)](<int16/addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<int16/dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividingFullWidth(_:)](<int16/dividingfullwidth(__).md>) — Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [multipliedFullWidth(by:)](<int16/multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [multipliedReportingOverflow(by:)](<int16/multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<int16/remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [signum()](<int16/signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [subtractingReportingOverflow(_:)](<int16/subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

### Type Aliases

- [IntegerLiteralType](int16/integerliteraltype.md) — A type that represents an integer literal.
- [Magnitude](int16/magnitude-swift.typealias.md) — A type that can represent the absolute value of any possible value of this type.
- [Stride](int16/stride.md) — A type that represents the distance between two values.

### Type Properties

- [bitWidth](int16/bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.

### Default Implementations

- [AdditiveArithmetic Implementations](int16/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](int16/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](int16/binaryinteger-implementations.md)
- [Comparable Implementations](int16/comparable-implementations.md)
- [CustomReflectable Implementations](int16/customreflectable-implementations.md)
- [Decodable Implementations](int16/decodable-implementations.md)
- [Encodable Implementations](int16/encodable-implementations.md)
- [Equatable Implementations](int16/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](int16/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](int16/fixedwidthinteger-implementations.md)
- [Hashable Implementations](int16/hashable-implementations.md)
- [SIMDScalar Implementations](int16/simdscalar-implementations.md)
- [SignedInteger Implementations](int16/signedinteger-implementations.md)
- [SignedNumeric Implementations](int16/signednumeric-implementations.md)

## See Also

### Signed Integers

- [Int8](int8.md) — An 8-bit signed integer value type.
- [Int32](int32.md) — A 32-bit signed integer value type.
- [Int64](int64.md) — A 64-bit signed integer value type.
- [Int128](int128.md) — A 128-bit signed integer value type.
