---
title: UInt
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint
source_url: 'https://developer.apple.com/documentation/swift/uint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint.json'
content_hash: 'sha256:cb0b5bffe6763bc4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UInt

<sub>Structure</sub>

An unsigned integer value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UInt
```

## Overview

On 32-bit platforms, `UInt` is the same size as `UInt32`, and on 64-bit platforms, `UInt` is the same size as `UInt64`.

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BinaryInteger](binaryinteger.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FixedWidthInteger](fixedwidthinteger.md), [Hashable](hashable.md), [LosslessStringConvertible](losslessstringconvertible.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Strideable](strideable.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md), [UnsignedInteger](unsignedinteger.md)

## Topics

### Structures

- [Words](uint/words-swift.struct.md) — A type that represents the words of this integer.

### Operators

- [!=(_:_:)](<uint/!=(____).md>)
- [&=(_:_:)](<uint/&=(____).md>) — Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [&\<\<=(_:_:)](<uint/&__=(____)-5hags.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\>\>=(_:_:)](<uint/&__=(____)-69f19.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [*=(_:_:)](<uint/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable.
- [+=(_:_:)](<uint/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable.
- [-=(_:_:)](<uint/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [==(_:_:)](<uint/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [\<(_:_:)](<uint/_(____)-9v225.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [/=(_:_:)](<uint/_=(____)-22lsj.md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [^=(_:_:)](<uint/_=(____)-2p0vs.md>) — Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [|=(_:_:)](<uint/_=(____)-4bs9t.md>) — Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [%=(_:_:)](<uint/_=(____)-85oek.md>) — Divides the first value by the second and stores the remainder in the left-hand-side variable.

### Initializers

- [init(_:)](<uint/init(__)-117g.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint/init(__)-5lcnv.md>)
- [init(_:)](<uint/init(__)-7mzx8.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint/init(__)-8jtgk.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint/init(__)-9lrzt.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint/init(__)-jl4r.md>)
- [init(bitPattern:)](<uint/init(bitpattern_)-3qf8b.md>) — Creates a new value with the bit pattern of the given pointer.
- [init(bitPattern:)](<uint/init(bitpattern_)-7sd72.md>) — Creates a new value with the bit pattern of the given pointer.
- [init(bitPattern:)](<uint/init(bitpattern_)-9qvv7.md>) — Creates a new instance with the same memory representation as the given value.
- [init(bitPattern:)](<uint/init(bitpattern_)-gk5x.md>) — Creates an integer that captures the full value of the given object identifier.
- [init(exactly:)](<uint/init(exactly_)-22ddn.md>)
- [init(exactly:)](<uint/init(exactly_)-8zm2w.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint/init(exactly_)-9cl5x.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint/init(exactly_)-9ve7w.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint/init(exactly_)-wmyv.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating:)](<uint/init(truncating_).md>)

### Instance Properties

- [byteSwapped](uint/byteswapped.md) — A representation of this integer with the byte order swapped.
- [customPlaygroundQuickLook](uint/customplaygroundquicklook.md) — A custom playground Quick Look for the `UInt` instance. _(deprecated)_
- [leadingZeroBitCount](uint/leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [nonzeroBitCount](uint/nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [trailingZeroBitCount](uint/trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](uint/words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

### Instance Methods

- [addingReportingOverflow(_:)](<uint/addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<uint/dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividingFullWidth(_:)](<uint/dividingfullwidth(__).md>) — Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [multipliedFullWidth(by:)](<uint/multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [multipliedReportingOverflow(by:)](<uint/multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<uint/remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [signum()](<uint/signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [subtractingReportingOverflow(_:)](<uint/subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

### Type Aliases

- [IntegerLiteralType](uint/integerliteraltype.md) — A type that represents an integer literal.
- [Magnitude](uint/magnitude.md) — A type that can represent the absolute value of any possible value of this type.
- [Stride](uint/stride.md) — A type that represents the distance between two values.

### Type Properties

- [bitWidth](uint/bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.

### Default Implementations

- [AdditiveArithmetic Implementations](uint/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](uint/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](uint/binaryinteger-implementations.md)
- [Comparable Implementations](uint/comparable-implementations.md)
- [CustomReflectable Implementations](uint/customreflectable-implementations.md)
- [Decodable Implementations](uint/decodable-implementations.md)
- [Encodable Implementations](uint/encodable-implementations.md)
- [Equatable Implementations](uint/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](uint/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](uint/fixedwidthinteger-implementations.md)
- [Hashable Implementations](uint/hashable-implementations.md)
- [SIMDScalar Implementations](uint/simdscalar-implementations.md)
- [UnsignedInteger Implementations](uint/unsignedinteger-implementations.md)

## See Also

### Unsigned Integers

- [UInt8](uint8.md) — An 8-bit unsigned integer value type.
- [UInt16](uint16.md) — A 16-bit unsigned integer value type.
- [UInt32](uint32.md) — A 32-bit unsigned integer value type.
- [UInt64](uint64.md) — A 64-bit unsigned integer value type.
- [UInt128](uint128.md) — A 128-bit unsigned integer value type.
