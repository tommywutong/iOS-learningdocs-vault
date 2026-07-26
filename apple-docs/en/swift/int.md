---
title: Int
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int
source_url: 'https://developer.apple.com/documentation/swift/int'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int.json'
content_hash: 'sha256:d1e69145fffac726'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Int

<sub>Structure</sub>

A signed integer value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Int
```

## Overview

On 32-bit platforms, `Int` is the same size as `Int32`, and on 64-bit platforms, `Int` is the same size as `Int64`.

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSGraph.Builder.SliceIndex](../accelerate/bnnsgraph/builder/sliceindex.md), [BinaryInteger](binaryinteger.md), [BindableData](../realitykit/bindabledata.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [CodingKeyRepresentable](codingkeyrepresentable.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleFromGeneratedContent](../foundationmodels/convertiblefromgeneratedcontent.md), [ConvertibleToBytes](convertibletobytes.md), [ConvertibleToGeneratedContent](../foundationmodels/convertibletogeneratedcontent.md), [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [CustomURLRepresentationParameterConvertible](../appintents/customurlrepresentationparameterconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [EntityIdentifierConvertible](../appintents/entityidentifierconvertible.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FixedWidthInteger](fixedwidthinteger.md), [Generable](../foundationmodels/generable.md), [Hashable](hashable.md), [InstructionsRepresentable](../foundationmodels/instructionsrepresentable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLDataValueConvertible](../createml/mldatavalueconvertible.md), [MLIdentifier](../createml/mlidentifier.md), [MLTensorRangeExpression](../coreml/mltensorrangeexpression.md), [MirrorPath](mirrorpath.md), [NDArray.RangeExpression](../coreai/ndarray/rangeexpression.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [PromptRepresentable](../foundationmodels/promptrepresentable.md), [RangeComparableProperty](../appintents/rangecomparableproperty.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [SignedInteger](signedinteger.md), [SignedNumeric](signednumeric.md), [Strideable](strideable.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md)

## Topics

### Converting Integers

- [init(_:)](<int/init(__)-4ekvl.md>) — Creates a new instance from the given integer.
- [init(exactly:)](<int/init(exactly_)-b1dy.md>)
- [init(clamping:)](<int/init(clamping_).md>) — Creates a new instance with the representable value that’s closest to the given integer.
- [init(truncatingIfNeeded:)](<int/init(truncatingifneeded_).md>) — Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init(bitPattern:)](<int/init(bitpattern_)-72037.md>) — Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](<int/init(exactly_)-177ax.md>)
- [init(truncating:)](<int/init(truncating_).md>)

### Converting Floating-Point Values

- [init(_:)](<int/init(__)-6gt9z.md>)
- [init(_:)](<int/init(__)-8vbwo.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int/init(__)-2oscb.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int/init(__)-3huv0.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int/init(__)-66i0w.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<int/init(__)-5q6q5.md>)

### Converting with No Loss of Precision

- [init(exactly:)](<int/init(exactly_)-7yhn6.md>)
- [init(exactly:)](<int/init(exactly_)-77kq8.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int/init(exactly_)-7qdwf.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int/init(exactly_)-5xh2s.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<int/init(exactly_)-5kot1.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.

### Converting Strings

- [init(_:)](<int/init(__)-2hmii.md>) — Creates a new integer value from the given string.
- [init(_:radix:)](<int/init(__radix_).md>) — Creates a new integer value from the given string and radix.

### Creating a Random Integer

- [random(in:)](<int/random(in_)-9mjpw.md>) — Returns a random value within the specified range.
- [random(in:using:)](<int/random(in_using_)-4lsb5.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:)](<int/random(in_)-8zzqh.md>) — Returns a random value within the specified range.
- [random(in:using:)](<int/random(in_using_)-3dwv4.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.

### Performing Calculations

- [Integer Operators](integer-operators.md) — Perform arithmetic and bitwise operations or compare values.
- [negate()](<int/negate().md>) — Replaces this value with its additive inverse.
- [quotientAndRemainder(dividingBy:)](<int/quotientandremainder(dividingby_).md>) — Returns the quotient and remainder of this value divided by the given value.
- [isMultiple(of:)](<int/ismultiple(of_).md>) — Returns `true` if this value is a multiple of the given value, and `false` otherwise.

### Performing Calculations with Overflow

- [addingReportingOverflow(_:)](<int/addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [subtractingReportingOverflow(_:)](<int/subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
- [multipliedReportingOverflow(by:)](<int/multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<int/dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<int/remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.

### Performing Double-Width Calculations

- [multipliedFullWidth(by:)](<int/multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [dividingFullWidth(_:)](<int/dividingfullwidth(__).md>) — Returns a tuple containing the quotient and remainder of dividing the given value by this value.

### Finding the Sign and Magnitude

- [magnitude](int/magnitude-swift.property.md) — The magnitude of this value.
- [Magnitude](int/magnitude-swift.typealias.md) — A type that can represent the absolute value of any possible value of this type.
- [abs(_:)](<abs(__).md>) — Returns the absolute value of the given number.
- [signum()](<int/signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.

### Accessing Numeric Constants

- [zero](int/zero.md) — The zero value.
- [min](int/min.md) — The minimum representable integer in this type.
- [max](int/max.md) — The maximum representable integer in this type.
- [isSigned](int/issigned.md) — A Boolean value indicating whether this type is a signed integer type.

### Working with Byte Order

- [byteSwapped](int/byteswapped.md) — A representation of this integer with the byte order swapped.
- [littleEndian](int/littleendian.md) — The little-endian representation of this integer.
- [bigEndian](int/bigendian.md) — The big-endian representation of this integer.
- [init(littleEndian:)](<int/init(littleendian_).md>) — Creates an integer from its little-endian representation, changing the byte order if necessary.
- [init(bigEndian:)](<int/init(bigendian_).md>) — Creates an integer from its big-endian representation, changing the byte order if necessary.

### Working with Binary Representation

- [bitWidth](int/bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.
- [bitWidth](int/bitwidth-swift.property.md) — The number of bits in the current binary representation of this value.
- [nonzeroBitCount](int/nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [leadingZeroBitCount](int/leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [trailingZeroBitCount](int/trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](int/words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [Words](int/words-swift.struct.md) — A type that represents the words of this integer.

### Working with Memory Addresses

- [init(bitPattern:)](<int/init(bitpattern_)-2i0qy.md>) — Creates a new value with the bit pattern of the given pointer.
- [init(bitPattern:)](<int/init(bitpattern_)-2o9co.md>) — Creates an integer that captures the full value of the given object identifier.
- [init(bitPattern:)](<int/init(bitpattern_)-5qm7a.md>) — Creates a new value with the bit pattern of the given pointer.

### Encoding and Decoding Values

- [encode(to:)](<int/encode(to_).md>) — Encodes this value into the given encoder.
- [init(from:)](<int/init(from_).md>) — Creates a new instance by decoding from the given decoder.

### Describing an Integer

- [description](int/description.md) — A textual representation of this value.
- [hash(into:)](<int/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
- [customMirror](int/custommirror.md) — A mirror that reflects the `Int` instance.

### Infrequently Used Functionality

- [init()](<int/init().md>) — Creates a new value equal to zero.
- [init(integerLiteral:)](<int/init(integerliteral_).md>)
- [IntegerLiteralType](int/integerliteraltype.md) — A type that represents an integer literal.
- [distance(to:)](<int/distance(to_).md>) — Returns the distance from this value to the given value, expressed as a stride.
- [advanced(by:)](<int/advanced(by_).md>) — Returns a value that is offset the specified distance from this value.
- [Stride](int/stride.md) — A type that represents the distance between two values.
- [hashValue](int/hashvalue.md) — The hash value.

### Deprecated

- [customPlaygroundQuickLook](int/customplaygroundquicklook.md) — A custom playground Quick Look for the `Int` instance. _(deprecated)_
- [init(_:)](<int/init(__)-3mb3q.md>)

### SIMD-Supporting Types

- [SIMDMaskScalar](int/simdmaskscalar.md)
- [SIMD2Storage](int/simd2storage.md) — Storage for a vector of two integers.
- [SIMD4Storage](int/simd4storage.md) — Storage for a vector of four integers.
- [SIMD8Storage](int/simd8storage.md) — Storage for a vector of eight integers.
- [SIMD16Storage](int/simd16storage.md) — Storage for a vector of 16 integers.
- [SIMD32Storage](int/simd32storage.md) — Storage for a vector of 32 integers.
- [SIMD64Storage](int/simd64storage.md) — Storage for a vector of 64 integers.

### Operators

- [!=(_:_:)](<int/!=(____).md>)
- [&\>\>=(_:_:)](<int/&__=(____)-2i06i.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\<\<=(_:_:)](<int/&__=(____)-58orm.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [\<(_:_:)](<int/_(____)-3wpum.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [^=(_:_:)](<int/_=(____)-1ypi9.md>) — Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [%=(_:_:)](<int/_=(____)-30t77.md>) — Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [|=(_:_:)](<int/_=(____)-4b29i.md>) — Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.

### Type Aliases

- [Specification](int/specification.md)
- [UnwrappedType](int/unwrappedtype.md)
- [ValueType](int/valuetype.md)

### Type Properties

- [defaultResolverSpecification](int/defaultresolverspecification.md)

### Default Implementations

- [AdditiveArithmetic Implementations](int/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](int/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](int/binaryinteger-implementations.md)
- [CodingKeyRepresentable Implementations](int/codingkeyrepresentable-implementations.md)
- [Comparable Implementations](int/comparable-implementations.md)
- [CustomReflectable Implementations](int/customreflectable-implementations.md)
- [Decodable Implementations](int/decodable-implementations.md)
- [Encodable Implementations](int/encodable-implementations.md)
- [Equatable Implementations](int/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](int/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](int/fixedwidthinteger-implementations.md)
- [Hashable Implementations](int/hashable-implementations.md)
- [SIMDScalar Implementations](int/simdscalar-implementations.md)
- [SignedInteger Implementations](int/signedinteger-implementations.md)
- [SignedNumeric Implementations](int/signednumeric-implementations.md)
- [Strideable Implementations](int/strideable-implementations.md)

## See Also

### Standard Library

- [Double](double.md) — A double-precision (64-bit), floating-point value type.
- [String](string.md) — A Unicode string value that is a collection of characters.
- [Array](array.md) — An ordered, random-access collection.
- [Dictionary](dictionary.md) — A collection whose elements are key-value pairs.
- [Swift Standard Library](swift-standard-library.md) — Solve complex problems and write high-performance, readable code.
