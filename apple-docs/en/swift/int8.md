---
title: Int8
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int8
source_url: 'https://developer.apple.com/documentation/swift/int8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8.json'
content_hash: 'sha256:d867f2081aaf0dad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Int8

<sub>Structure</sub>

An 8-bit signed integer value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Int8
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSScalar](../accelerate/bnnsscalar.md), [BinaryInteger](binaryinteger.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FixedWidthInteger](fixedwidthinteger.md), [Hashable](hashable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLShapedArrayScalar](../coreml/mlshapedarrayscalar.md), [MLTensorScalar](../coreml/mltensorscalar.md), [NetworkFixedWidthInteger](../network/networkfixedwidthinteger.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [SignedInteger](signedinteger.md), [SignedNumeric](signednumeric.md), [Strideable](strideable.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md), [vDSP_IntegerConvertable](../accelerate/vdsp_integerconvertable.md)

## Topics

### Structures

- [Words](int8/words-swift.struct.md) — A type that represents the words of this integer.

### Operators

- [!=(_:_:)](<int8/!=(____).md>)
- [&=(_:_:)](<int8/&=(____).md>) — Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [&\>\>=(_:_:)](<int8/&__=(____)-17e9w.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\<\<=(_:_:)](<int8/&__=(____)-7gdrc.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [*=(_:_:)](<int8/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable.
- [+=(_:_:)](<int8/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable.
- [-=(_:_:)](<int8/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [==(_:_:)](<int8/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [\<(_:_:)](<int8/_(____)-1kdfe.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [|=(_:_:)](<int8/_=(____)-19gzu.md>) — Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [/=(_:_:)](<int8/_=(____)-2auqb.md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [^=(_:_:)](<int8/_=(____)-2mpgr.md>) — Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [%=(_:_:)](<int8/_=(____)-3o9cs.md>) — Divides the first value by the second and stores the remainder in the left-hand-side variable.

### Initializers

- [init(_:)](<int8/init(__)-2vdru.md>)
- [init(_:)](<int8/init(__)-44cer.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int8/init(__)-47zy8.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int8/init(__)-4erk2.md>)
- [init(_:)](<int8/init(__)-6g8q9.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int8/init(__)-7renq.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern:)](<int8/init(bitpattern_).md>) — Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](<int8/init(exactly_)-1vh5j.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int8/init(exactly_)-6zkv6.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int8/init(exactly_)-72z4.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int8/init(exactly_)-78es1.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int8/init(exactly_)-9cjj7.md>)
- [init(truncating:)](<int8/init(truncating_).md>)

### Instance Properties

- [byteSwapped](int8/byteswapped.md) — A representation of this integer with the byte order swapped.
- [customPlaygroundQuickLook](int8/customplaygroundquicklook.md) — A custom playground Quick Look for the `Int8` instance. _(deprecated)_
- [leadingZeroBitCount](int8/leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [magnitude](int8/magnitude-swift.property.md) — The magnitude of this value.
- [nonzeroBitCount](int8/nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [trailingZeroBitCount](int8/trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](int8/words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

### Instance Methods

- [addingReportingOverflow(_:)](<int8/addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<int8/dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividingFullWidth(_:)](<int8/dividingfullwidth(__).md>) — Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [multipliedFullWidth(by:)](<int8/multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [multipliedReportingOverflow(by:)](<int8/multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<int8/remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [signum()](<int8/signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [subtractingReportingOverflow(_:)](<int8/subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

### Type Aliases

- [IntegerLiteralType](int8/integerliteraltype.md) — A type that represents an integer literal.
- [Magnitude](int8/magnitude-swift.typealias.md) — A type that can represent the absolute value of any possible value of this type.
- [Stride](int8/stride.md) — A type that represents the distance between two values.

### Type Properties

- [bitWidth](int8/bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.

### Default Implementations

- [AdditiveArithmetic Implementations](int8/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](int8/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](int8/binaryinteger-implementations.md)
- [Comparable Implementations](int8/comparable-implementations.md)
- [CustomReflectable Implementations](int8/customreflectable-implementations.md)
- [Decodable Implementations](int8/decodable-implementations.md)
- [Encodable Implementations](int8/encodable-implementations.md)
- [Equatable Implementations](int8/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](int8/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](int8/fixedwidthinteger-implementations.md)
- [Hashable Implementations](int8/hashable-implementations.md)
- [SIMDScalar Implementations](int8/simdscalar-implementations.md)
- [SignedInteger Implementations](int8/signedinteger-implementations.md)
- [SignedNumeric Implementations](int8/signednumeric-implementations.md)

## See Also

### Signed Integers

- [Int16](int16.md) — A 16-bit signed integer value type.
- [Int32](int32.md) — A 32-bit signed integer value type.
- [Int64](int64.md) — A 64-bit signed integer value type.
- [Int128](int128.md) — A 128-bit signed integer value type.
