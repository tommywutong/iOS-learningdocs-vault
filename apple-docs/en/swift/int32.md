---
title: Int32
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int32
source_url: 'https://developer.apple.com/documentation/swift/int32'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int32.json'
content_hash: 'sha256:006cdf3faecc42f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Int32

<sub>Structure</sub>

A 32-bit signed integer value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Int32
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSScalar](../accelerate/bnnsscalar.md), [BinaryInteger](binaryinteger.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FixedWidthInteger](fixedwidthinteger.md), [Hashable](hashable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLShapedArrayScalar](../coreml/mlshapedarrayscalar.md), [MLTensorScalar](../coreml/mltensorscalar.md), [NetworkFixedWidthInteger](../network/networkfixedwidthinteger.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [SignedInteger](signedinteger.md), [SignedNumeric](signednumeric.md), [Strideable](strideable.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md), [vDSP_IntegerConvertable](../accelerate/vdsp_integerconvertable.md)

## Topics

### Structures

- [Words](int32/words-swift.struct.md) — A type that represents the words of this integer.

### Operators

- [!=(_:_:)](<int32/!=(____).md>)
- [&=(_:_:)](<int32/&=(____).md>) — Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [&\<\<=(_:_:)](<int32/&__=(____)-5xpt1.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\>\>=(_:_:)](<int32/&__=(____)-9l16.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [*=(_:_:)](<int32/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable.
- [+=(_:_:)](<int32/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable.
- [-=(_:_:)](<int32/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [==(_:_:)](<int32/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [\<(_:_:)](<int32/_(____)-3k2xk.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [^=(_:_:)](<int32/_=(____)-46xu7.md>) — Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [|=(_:_:)](<int32/_=(____)-6hsuo.md>) — Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [%=(_:_:)](<int32/_=(____)-8flrz.md>) — Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [/=(_:_:)](<int32/_=(____)-997bi.md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable.

### Initializers

- [init(_:)](<int32/init(__)-1817u.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int32/init(__)-2px8y.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int32/init(__)-34fue.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int32/init(__)-3zpp6.md>)
- [init(_:)](<int32/init(__)-5nznu.md>)
- [init(_:)](<int32/init(__)-k0sh.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern:)](<int32/init(bitpattern_).md>) — Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](<int32/init(exactly_)-3dltv.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int32/init(exactly_)-5hlj9.md>)
- [init(exactly:)](<int32/init(exactly_)-79vj5.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int32/init(exactly_)-7dio6.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int32/init(exactly_)-9tpyy.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating:)](<int32/init(truncating_).md>)

### Instance Properties

- [byteSwapped](int32/byteswapped.md) — A representation of this integer with the byte order swapped.
- [customPlaygroundQuickLook](int32/customplaygroundquicklook.md) — A custom playground Quick Look for the `Int32` instance. _(deprecated)_
- [leadingZeroBitCount](int32/leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [magnitude](int32/magnitude-swift.property.md) — The magnitude of this value.
- [nonzeroBitCount](int32/nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [trailingZeroBitCount](int32/trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](int32/words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

### Instance Methods

- [addingReportingOverflow(_:)](<int32/addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<int32/dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividingFullWidth(_:)](<int32/dividingfullwidth(__).md>) — Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [multipliedFullWidth(by:)](<int32/multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [multipliedReportingOverflow(by:)](<int32/multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<int32/remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [signum()](<int32/signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [subtractingReportingOverflow(_:)](<int32/subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

### Type Aliases

- [IntegerLiteralType](int32/integerliteraltype.md) — A type that represents an integer literal.
- [Magnitude](int32/magnitude-swift.typealias.md) — A type that can represent the absolute value of any possible value of this type.
- [Stride](int32/stride.md) — A type that represents the distance between two values.

### Type Properties

- [bitWidth](int32/bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.
- [mlMultiArrayDataType](int32/mlmultiarraydatatype.md)

### Default Implementations

- [AdditiveArithmetic Implementations](int32/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](int32/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](int32/binaryinteger-implementations.md)
- [Comparable Implementations](int32/comparable-implementations.md)
- [CustomReflectable Implementations](int32/customreflectable-implementations.md)
- [Decodable Implementations](int32/decodable-implementations.md)
- [Encodable Implementations](int32/encodable-implementations.md)
- [Equatable Implementations](int32/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](int32/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](int32/fixedwidthinteger-implementations.md)
- [Hashable Implementations](int32/hashable-implementations.md)
- [SIMDScalar Implementations](int32/simdscalar-implementations.md)
- [SignedInteger Implementations](int32/signedinteger-implementations.md)
- [SignedNumeric Implementations](int32/signednumeric-implementations.md)

## See Also

### Signed Integers

- [Int8](int8.md) — An 8-bit signed integer value type.
- [Int16](int16.md) — A 16-bit signed integer value type.
- [Int64](int64.md) — A 64-bit signed integer value type.
- [Int128](int128.md) — A 128-bit signed integer value type.
