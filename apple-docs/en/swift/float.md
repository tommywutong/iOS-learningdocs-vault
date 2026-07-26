---
title: Float
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float
source_url: 'https://developer.apple.com/documentation/swift/float'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float.json'
content_hash: 'sha256:94c2dc9a98d5608e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Float

<sub>Structure</sub>

A single-precision (32-bit), floating-point value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Float
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AnimatableData](../realitykit/animatabledata.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSGraph.Builder.OperationParameter](../accelerate/bnnsgraph/builder/operationparameter.md), [BNNSScalar](../accelerate/bnnsscalar.md), [BinaryFloatingPoint](binaryfloatingpoint.md), [BindableData](../realitykit/bindabledata.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleFromGeneratedContent](../foundationmodels/convertiblefromgeneratedcontent.md), [ConvertibleToBytes](convertibletobytes.md), [ConvertibleToGeneratedContent](../foundationmodels/convertibletogeneratedcontent.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [EntityIdentifierConvertible](../appintents/entityidentifierconvertible.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FloatingPoint](floatingpoint.md), [Generable](../foundationmodels/generable.md), [Hashable](hashable.md), [InstructionsRepresentable](../foundationmodels/instructionsrepresentable.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLShapedArrayScalar](../coreml/mlshapedarrayscalar.md), [MLTensorScalar](../coreml/mltensorscalar.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [PromptRepresentable](../foundationmodels/promptrepresentable.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [SignedNumeric](signednumeric.md), [Strideable](strideable.md), [TextOutputStreamable](textoutputstreamable.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md), [VectorArithmetic](../swiftui/vectorarithmetic.md), [vDSP_DiscreteFourierTransformable](../accelerate/vdsp_discretefouriertransformable.md), [vDSP_FloatingPointBiquadFilterable](../accelerate/vdsp_floatingpointbiquadfilterable.md), [vDSP_FloatingPointConvertable](../accelerate/vdsp_floatingpointconvertable.md), [vDSP_FloatingPointDiscreteFourierTransformable](../accelerate/vdsp_floatingpointdiscretefouriertransformable.md), [vDSP_FloatingPointGeneratable](../accelerate/vdsp_floatingpointgeneratable.md)

## Topics

### Converting Integers

- [init(_:)](<float/init(__)-7e965.md>) — Creates a new value, rounded to the closest possible representation.
- [init(_:)](<float/init(__)-6cvkq.md>) — Creates a new value, rounded to the closest possible representation.

### Converting Strings

- [init(_:)](<float/init(__)-h2f4.md>) — Creates a new instance from the given string.
- [init(_:)](<float/init(__)-4xsj6.md>)

### Converting Floating-Point Values

- [init(_:)](<float/init(__)-1488f.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<float/init(__)-1oh9p.md>) — Creates a new value, rounded to the closest possible representation.
- [init(_:)](<float/init(__)-1kp2p.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<float/init(__)-975tv.md>) — Creates a new instance initialized to the given value.
- [init(_:)](<float/init(__)-11orc.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<float/init(__)-5soww.md>)
- [init(_:)](<float/init(__)-ussz.md>) — Creates a new instance that approximates the given value.
- [init(signOf:magnitudeOf:)](<float/init(signof_magnitudeof_).md>) — Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(sign:exponent:significand:)](<float/init(sign_exponent_significand_).md>) — Creates a new value from the given sign, exponent, and significand.
- [init(truncating:)](<float/init(truncating_).md>)

### Converting with No Loss of Precision

- [init(exactly:)](<float/init(exactly_)-8esr8.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<float/init(exactly_)-89na7.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<float/init(exactly_)-89pn7.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<float/init(exactly_)-6l5fa.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<float/init(exactly_)-zknq.md>)
- [init(exactly:)](<float/init(exactly_)-1h1oe.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<float/init(exactly_)-8ho5q.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.

### Creating a Random Value

- [random(in:)](<float/random(in_)-6ided.md>) — Returns a random value within the specified range.
- [random(in:using:)](<float/random(in_using_)-1m6gf.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:)](<float/random(in_)-5o5h8.md>) — Returns a random value within the specified range.
- [random(in:using:)](<float/random(in_using_)-613hx.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.

### Performing Calculations

- [Floating-Point Operators for Float](floating-point-operators-for-float.md) — Perform arithmetic and bitwise operations or compare values.
- [addingProduct(_:_:)](<float/addingproduct(____).md>) — Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [addProduct(_:_:)](<float/addproduct(____).md>) — Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [squareRoot()](<float/squareroot().md>) — Returns the square root of the value, rounded to a representable value.
- [formSquareRoot()](<float/formsquareroot().md>) — Replaces this value with its square root, rounded to a representable value.
- [remainder(dividingBy:)](<float/remainder(dividingby_).md>) — Returns the remainder of this value divided by the given value.
- [formRemainder(dividingBy:)](<float/formremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value.
- [truncatingRemainder(dividingBy:)](<float/truncatingremainder(dividingby_).md>) — Returns the remainder of this value divided by the given value using truncating division.
- [formTruncatingRemainder(dividingBy:)](<float/formtruncatingremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value using truncating division.
- [negate()](<float/negate().md>) — Replaces this value with its additive inverse.

### Rounding Values

- [rounded()](<float/rounded().md>)
- [rounded(_:)](<float/rounded(__).md>) — Returns this value rounded to an integral value using the specified rounding rule.
- [round()](<float/round().md>)
- [round(_:)](<float/round(__).md>) — Rounds the value to an integral value using the specified rounding rule.

### Comparing Values

- [Floating-Point Operators for Float](floating-point-operators-for-float.md) — Perform arithmetic and bitwise operations or compare values.
- [isEqual(to:)](<float/isequal(to_).md>) — Returns a Boolean value indicating whether this instance is equal to the given value.
- [isLess(than:)](<float/isless(than_).md>) — Returns a Boolean value indicating whether this instance is less than the given value.
- [isLessThanOrEqualTo(_:)](<float/islessthanorequalto(__).md>) — Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [isTotallyOrdered(belowOrEqualTo:)](<float/istotallyordered(beloworequalto_).md>) — Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [maximum(_:_:)](<float/maximum(____).md>) — Returns the greater of the two given values.
- [maximumMagnitude(_:_:)](<float/maximummagnitude(____).md>) — Returns the value with greater magnitude.
- [minimum(_:_:)](<float/minimum(____).md>) — Returns the lesser of the two given values.
- [minimumMagnitude(_:_:)](<float/minimummagnitude(____).md>) — Returns the value with lesser magnitude.

### Finding the Sign and Magnitude

- [magnitude](float/magnitude-swift.property.md) — The magnitude of this value.
- [sign](float/sign.md) — The sign of the floating-point value.
- [Magnitude](float/magnitude-swift.typealias.md) — A type that can represent the absolute value of any possible value of the conforming type.

### Querying a Float

- [ulp](float/ulp.md) — The unit in the last place of this value.
- [significand](float/significand.md) — The significand of the floating-point value.
- [exponent](float/exponent-swift.property.md) — The exponent of the floating-point value.
- [nextUp](float/nextup.md) — The least representable value that compares greater than this value.
- [nextDown](float/nextdown.md) — The greatest representable value that compares less than this value.
- [binade](float/binade.md) — The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.

### Accessing Numeric Constants

- [pi](float/pi.md) — The mathematical constant pi (π), approximately equal to 3.14159.
- [infinity](float/infinity.md) — Positive infinity.
- [greatestFiniteMagnitude](float/greatestfinitemagnitude.md) — The greatest finite number representable by this type.
- [nan](float/nan.md) — A quiet NaN (“not a number”).
- [signalingNaN](float/signalingnan.md) — A signaling NaN (“not a number”).
- [ulpOfOne](float/ulpofone.md) — The unit in the last place of 1.0.
- [leastNormalMagnitude](float/leastnormalmagnitude.md) — The least positive normal number.
- [leastNonzeroMagnitude](float/leastnonzeromagnitude.md) — The least positive number.
- [zero](float/zero.md) — The zero value.

### Working with Binary Representation

- [bitPattern](float/bitpattern.md) — The bit pattern of the value’s encoding.
- [significandBitPattern](float/significandbitpattern.md) — The raw encoding of the value’s significand field.
- [significandWidth](float/significandwidth.md) — The number of bits required to represent the value’s significand.
- [exponentBitPattern](float/exponentbitpattern.md) — The raw encoding of the value’s exponent field.
- [significandBitCount](float/significandbitcount.md) — The available number of fractional significand bits.
- [exponentBitCount](float/exponentbitcount.md) — The number of bits used to represent the type’s exponent.
- [radix](float/radix.md) — The radix, or base of exponentiation, for a floating-point type.
- [init(bitPattern:)](<float/init(bitpattern_).md>) — Creates a new value with the given bit pattern.
- [init(sign:exponentBitPattern:significandBitPattern:)](<float/init(sign_exponentbitpattern_significandbitpattern_).md>) — Creates a new instance from the specified sign and bit patterns.
- [init(nan:signaling:)](<float/init(nan_signaling_).md>) — Creates a NaN (“not a number”) value with the specified payload.
- [Exponent](float/exponent-swift.typealias.md) — A type that can represent any written exponent.
- [RawSignificand](float/rawsignificand.md) — A type that represents the encoded significand of a value.

### Querying a Float’s State

- [isZero](float/iszero.md) — A Boolean value indicating whether the instance is equal to zero.
- [isFinite](float/isfinite.md) — A Boolean value indicating whether this instance is finite.
- [isInfinite](float/isinfinite.md) — A Boolean value indicating whether the instance is infinite.
- [isNaN](float/isnan.md) — A Boolean value indicating whether the instance is NaN (“not a number”).
- [isSignalingNaN](float/issignalingnan.md) — A Boolean value indicating whether the instance is a signaling NaN.
- [isNormal](float/isnormal.md) — A Boolean value indicating whether this instance is normal.
- [isSubnormal](float/issubnormal.md) — A Boolean value indicating whether the instance is subnormal.
- [isCanonical](float/iscanonical.md) — A Boolean value indicating whether the instance’s representation is in its canonical form.
- [floatingPointClass](float/floatingpointclass.md) — The classification of this value.

### Encoding and Decoding Values

- [encode(to:)](<float/encode(to_).md>) — Encodes this value into the given encoder.
- [init(from:)](<float/init(from_).md>) — Creates a new instance by decoding from the given decoder.

### Creating a Range

- [...(_:_:)](<float/'...(____).md>) — Returns a closed range that contains both of its bounds.

### Describing a Float

- [hash(into:)](<float/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
- [description](float/description.md) — A textual representation of the value.
- [debugDescription](float/debugdescription.md) — A textual representation of the value, suitable for debugging.
- [customMirror](float/custommirror.md) — A mirror that reflects the `Float` instance.
- [hashValue](float/hashvalue.md) — The hash value.

### SIMD-Supporting Types

- [SIMDMaskScalar](float/simdmaskscalar.md)
- [SIMD2Storage](float/simd2storage.md) — Storage for a vector of two floating-point values.
- [SIMD4Storage](float/simd4storage.md) — Storage for a vector of four floating-point values.
- [SIMD8Storage](float/simd8storage.md) — Storage for a vector of eight floating-point values.
- [SIMD16Storage](float/simd16storage.md) — Storage for a vector of 16 floating-point values.
- [SIMD32Storage](float/simd32storage.md) — Storage for a vector of 32 floating-point values.
- [SIMD64Storage](float/simd64storage.md) — Storage for a vector of 64 floating-point values.

### Infrequently Used Functionality

- [init()](<float/init().md>)
- [init(integerLiteral:)](<float/init(integerliteral_).md>) — Creates an instance initialized to the specified integer value.
- [init(floatLiteral:)](<float/init(floatliteral_).md>) — Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral:)](<float/init(integerliteral_)-6hc7h.md>)
- [advanced(by:)](<float/advanced(by_).md>) — Returns a value that is offset the specified distance from this value.
- [distance(to:)](<float/distance(to_).md>) — Returns the distance from this value to the given value, expressed as a stride.
- [write(to:)](<float/write(to_).md>) — Writes a textual representation of this instance into the given output stream.

### Deprecated

- [init(_:)](<float/init(__)-7dbrz.md>)
- [customPlaygroundQuickLook](float/customplaygroundquicklook.md) — A custom playground Quick Look for the `Float` instance. _(deprecated)_

### Type Properties

- [mlMultiArrayDataType](float/mlmultiarraydatatype.md)

### Default Implementations

- [AdditiveArithmetic Implementations](float/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](float/atomicrepresentable-implementations.md)
- [BinaryFloatingPoint Implementations](float/binaryfloatingpoint-implementations.md)
- [Comparable Implementations](float/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](float/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](float/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](float/customstringconvertible-implementations.md)
- [Decodable Implementations](float/decodable-implementations.md)
- [Encodable Implementations](float/encodable-implementations.md)
- [Equatable Implementations](float/equatable-implementations.md)
- [ExpressibleByFloatLiteral Implementations](float/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](float/expressiblebyintegerliteral-implementations.md)
- [FloatingPoint Implementations](float/floatingpoint-implementations.md)
- [Hashable Implementations](float/hashable-implementations.md)
- [LosslessStringConvertible Implementations](float/losslessstringconvertible-implementations.md)
- [Numeric Implementations](float/numeric-implementations.md)
- [OperationParameter Implementations](float/operationparameter-implementations.md)
- [SIMDScalar Implementations](float/simdscalar-implementations.md)
- [SignedNumeric Implementations](float/signednumeric-implementations.md)
- [Strideable Implementations](float/strideable-implementations.md)
- [TextOutputStreamable Implementations](float/textoutputstreamable-implementations.md)

## See Also

### Numeric Values

- [Int](int.md) — A signed integer value type.
- [Double](double.md) — A double-precision (64-bit), floating-point value type.
