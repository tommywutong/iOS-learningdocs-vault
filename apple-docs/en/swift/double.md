---
title: Double
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double
source_url: 'https://developer.apple.com/documentation/swift/double'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double.json'
content_hash: 'sha256:99f3f8552602960a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Double

<sub>Structure</sub>

A double-precision (64-bit), floating-point value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Double
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [Animatable](../swiftui/animatable.md), [AnimatableData](../realitykit/animatabledata.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BinaryFloatingPoint](binaryfloatingpoint.md), [BindableData](../realitykit/bindabledata.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleFromGeneratedContent](../foundationmodels/convertiblefromgeneratedcontent.md), [ConvertibleToBytes](convertibletobytes.md), [ConvertibleToGeneratedContent](../foundationmodels/convertibletogeneratedcontent.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FloatingPoint](floatingpoint.md), [Generable](../foundationmodels/generable.md), [Hashable](hashable.md), [InstructionsRepresentable](../foundationmodels/instructionsrepresentable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLDataValueConvertible](../createml/mldatavalueconvertible.md), [MLShapedArrayScalar](../coreml/mlshapedarrayscalar.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [PromptRepresentable](../foundationmodels/promptrepresentable.md), [RangeComparableProperty](../appintents/rangecomparableproperty.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [SignedNumeric](signednumeric.md), [Strideable](strideable.md), [TextOutputStreamable](textoutputstreamable.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md), [VectorArithmetic](../swiftui/vectorarithmetic.md), [vDSP_DiscreteFourierTransformable](../accelerate/vdsp_discretefouriertransformable.md), [vDSP_FloatingPointBiquadFilterable](../accelerate/vdsp_floatingpointbiquadfilterable.md), [vDSP_FloatingPointConvertable](../accelerate/vdsp_floatingpointconvertable.md), [vDSP_FloatingPointDiscreteFourierTransformable](../accelerate/vdsp_floatingpointdiscretefouriertransformable.md), [vDSP_FloatingPointGeneratable](../accelerate/vdsp_floatingpointgeneratable.md)

## Topics

### Converting Integers

- [init(_:)](<double/init(__)-5blrp.md>) — Creates a new value, rounded to the closest possible representation.
- [init(_:)](<double/init(__)-84ohu.md>) — Creates a new value, rounded to the closest possible representation.

### Converting Strings

- [init(_:)](<double/init(__)-5wmm8.md>) — Creates a new instance from the given string.
- [init(_:)](<double/init(__)-15kej.md>)

### Converting Floating-Point Values

- [init(_:)](<double/init(__)-1488d.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<double/init(__)-o1k9.md>) — Creates a new instance initialized to the given value.
- [init(_:)](<double/init(__)-5h7qh.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<double/init(__)-aeox.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<double/init(__)-9z7ob.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<double/init(__)-7ag2w.md>)
- [init(sign:exponent:significand:)](<double/init(sign_exponent_significand_).md>) — Creates a new value from the given sign, exponent, and significand.
- [init(signOf:magnitudeOf:)](<double/init(signof_magnitudeof_).md>) — Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(_:)](<double/init(__)-1oh9r.md>) — Creates a new value, rounded to the closest possible representation.
- [init(truncating:)](<double/init(truncating_).md>)

### Converting with No Loss of Precision

- [init(exactly:)](<double/init(exactly_)-8esra.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<double/init(exactly_)-1h1oc.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<double/init(exactly_)-2uexo.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<double/init(exactly_)-2l6p1.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<double/init(exactly_)-7cl0t.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<double/init(exactly_)-50ofc.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<double/init(exactly_)-63925.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<double/init(exactly_)-8e00y.md>)

### Creating a Random Value

- [random(in:)](<double/random(in_)-6idef.md>) — Returns a random value within the specified range.
- [random(in:using:)](<double/random(in_using_)-1m6gd.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:)](<double/random(in_)-5o5ha.md>) — Returns a random value within the specified range.
- [random(in:using:)](<double/random(in_using_)-613hz.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.

### Performing Calculations

- [Floating-Point Operators for Double](floating-point-operators-for-double.md) — Perform arithmetic and bitwise operations or compare values.
- [addingProduct(_:_:)](<double/addingproduct(____).md>) — Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [addProduct(_:_:)](<double/addproduct(____).md>) — Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [squareRoot()](<double/squareroot().md>) — Returns the square root of the value, rounded to a representable value.
- [formSquareRoot()](<double/formsquareroot().md>) — Replaces this value with its square root, rounded to a representable value.
- [remainder(dividingBy:)](<double/remainder(dividingby_).md>) — Returns the remainder of this value divided by the given value.
- [formRemainder(dividingBy:)](<double/formremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value.
- [truncatingRemainder(dividingBy:)](<double/truncatingremainder(dividingby_).md>) — Returns the remainder of this value divided by the given value using truncating division.
- [formTruncatingRemainder(dividingBy:)](<double/formtruncatingremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value using truncating division.
- [negate()](<double/negate().md>) — Replaces this value with its additive inverse.

### Rounding Values

- [rounded()](<double/rounded().md>)
- [rounded(_:)](<double/rounded(__).md>) — Returns this value rounded to an integral value using the specified rounding rule.
- [round()](<double/round().md>)
- [round(_:)](<double/round(__).md>) — Rounds the value to an integral value using the specified rounding rule.

### Comparing Values

- [Floating-Point Operators for Double](floating-point-operators-for-double.md) — Perform arithmetic and bitwise operations or compare values.
- [isEqual(to:)](<double/isequal(to_).md>) — Returns a Boolean value indicating whether this instance is equal to the given value.
- [isLess(than:)](<double/isless(than_).md>) — Returns a Boolean value indicating whether this instance is less than the given value.
- [isLessThanOrEqualTo(_:)](<double/islessthanorequalto(__).md>) — Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [isTotallyOrdered(belowOrEqualTo:)](<double/istotallyordered(beloworequalto_).md>) — Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [minimum(_:_:)](<double/minimum(____).md>) — Returns the lesser of the two given values.
- [minimumMagnitude(_:_:)](<double/minimummagnitude(____).md>) — Returns the value with lesser magnitude.
- [maximum(_:_:)](<double/maximum(____).md>) — Returns the greater of the two given values.
- [maximumMagnitude(_:_:)](<double/maximummagnitude(____).md>) — Returns the value with greater magnitude.

### Finding the Sign and Magnitude

- [magnitude](double/magnitude-swift.property.md) — The magnitude of this value.
- [sign](double/sign.md) — The sign of the floating-point value.
- [Magnitude](double/magnitude-swift.typealias.md) — A type that can represent the absolute value of any possible value of the conforming type.

### Querying a Double

- [ulp](double/ulp.md) — The unit in the last place of this value.
- [significand](double/significand.md) — The significand of the floating-point value.
- [exponent](double/exponent-swift.property.md) — The exponent of the floating-point value.
- [nextUp](double/nextup.md) — The least representable value that compares greater than this value.
- [nextDown](double/nextdown.md) — The greatest representable value that compares less than this value.
- [binade](double/binade.md) — The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.

### Accessing Numeric Constants

- [pi](double/pi.md) — The mathematical constant pi (π), approximately equal to 3.14159.
- [infinity](double/infinity.md) — Positive infinity.
- [greatestFiniteMagnitude](double/greatestfinitemagnitude.md) — The greatest finite number representable by this type.
- [nan](double/nan.md) — A quiet NaN (“not a number”).
- [signalingNaN](double/signalingnan.md) — A signaling NaN (“not a number”).
- [ulpOfOne](double/ulpofone.md) — The unit in the last place of 1.0.
- [leastNonzeroMagnitude](double/leastnonzeromagnitude.md) — The least positive number.
- [leastNormalMagnitude](double/leastnormalmagnitude.md) — The least positive normal number.
- [zero](double/zero.md) — The zero value.

### Working with Binary Representation

- [bitPattern](double/bitpattern.md) — The bit pattern of the value’s encoding.
- [significandBitPattern](double/significandbitpattern.md) — The raw encoding of the value’s significand field.
- [significandWidth](double/significandwidth.md) — The number of bits required to represent the value’s significand.
- [exponentBitPattern](double/exponentbitpattern.md) — The raw encoding of the value’s exponent field.
- [significandBitCount](double/significandbitcount.md) — The available number of fractional significand bits.
- [exponentBitCount](double/exponentbitcount.md) — The number of bits used to represent the type’s exponent.
- [radix](double/radix.md) — The radix, or base of exponentiation, for a floating-point type.
- [init(bitPattern:)](<double/init(bitpattern_).md>) — Creates a new value with the given bit pattern.
- [init(sign:exponentBitPattern:significandBitPattern:)](<double/init(sign_exponentbitpattern_significandbitpattern_).md>) — Creates a new instance from the specified sign and bit patterns.
- [init(nan:signaling:)](<double/init(nan_signaling_).md>) — Creates a NaN (“not a number”) value with the specified payload.
- [Exponent](double/exponent-swift.typealias.md) — A type that can represent any written exponent.
- [RawSignificand](double/rawsignificand.md) — A type that represents the encoded significand of a value.
- [RawExponent](double/rawexponent.md) — A type that represents the encoded exponent of a value.

### Querying a Double’s State

- [isZero](double/iszero.md) — A Boolean value indicating whether the instance is equal to zero.
- [isFinite](double/isfinite.md) — A Boolean value indicating whether this instance is finite.
- [isInfinite](double/isinfinite.md) — A Boolean value indicating whether the instance is infinite.
- [isNaN](double/isnan.md) — A Boolean value indicating whether the instance is NaN (“not a number”).
- [isSignalingNaN](double/issignalingnan.md) — A Boolean value indicating whether the instance is a signaling NaN.
- [isNormal](double/isnormal.md) — A Boolean value indicating whether this instance is normal.
- [isSubnormal](double/issubnormal.md) — A Boolean value indicating whether the instance is subnormal.
- [isCanonical](double/iscanonical.md) — A Boolean value indicating whether the instance’s representation is in its canonical form.
- [floatingPointClass](double/floatingpointclass.md) — The classification of this value.

### Encoding and Decoding Values

- [encode(to:)](<double/encode(to_).md>) — Encodes this value into the given encoder.
- [init(from:)](<double/init(from_).md>) — Creates a new instance by decoding from the given decoder.

### Creating a Range

- [...(_:_:)](<double/'...(____).md>) — Returns a closed range that contains both of its bounds.

### Describing a Double

- [description](double/description.md) — A textual representation of the value.
- [debugDescription](double/debugdescription.md) — A textual representation of the value, suitable for debugging.
- [customMirror](double/custommirror.md) — A mirror that reflects the `Double` instance.
- [hash(into:)](<double/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Infrequently Used Functionality

- [init()](<double/init().md>)
- [init(floatLiteral:)](<double/init(floatliteral_).md>) — Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral:)](<double/init(integerliteral_).md>) — Creates an instance initialized to the specified integer value.
- [init(integerLiteral:)](<double/init(integerliteral_)-6hc7j.md>)
- [FloatLiteralType](double/floatliteraltype.md) — A type that represents a floating-point literal.
- [IntegerLiteralType](double/integerliteraltype.md) — A type that represents an integer literal.
- [advanced(by:)](<double/advanced(by_).md>) — Returns a value that is offset the specified distance from this value.
- [distance(to:)](<double/distance(to_).md>) — Returns the distance from this value to the given value, expressed as a stride.
- [Stride](double/stride.md) — A type that represents the distance between two values.
- [write(to:)](<double/write(to_).md>) — Writes a textual representation of this instance into the given output stream.
- [hashValue](double/hashvalue.md) — The hash value.

### SIMD-Supporting Types

- [SIMDMaskScalar](double/simdmaskscalar.md)
- [SIMD2Storage](double/simd2storage.md) — Storage for a vector of two floating-point values.
- [SIMD4Storage](double/simd4storage.md) — Storage for a vector of four floating-point values.
- [SIMD8Storage](double/simd8storage.md) — Storage for a vector of eight floating-point values.
- [SIMD16Storage](double/simd16storage.md) — Storage for a vector of 16 floating-point values.
- [SIMD32Storage](double/simd32storage.md) — Storage for a vector of 32 floating-point values.
- [SIMD64Storage](double/simd64storage.md) — Storage for a vector of 64 floating-point values.

### Deprecated

- [customPlaygroundQuickLook](double/customplaygroundquicklook.md) — A custom playground Quick Look for the `Double` instance. _(deprecated)_
- [init(_:)](<double/init(__)-8kme5.md>)

### Type Aliases

- [Specification](double/specification.md)
- [UnwrappedType](double/unwrappedtype.md)
- [ValueType](double/valuetype.md)

### Type Properties

- [defaultResolverSpecification](double/defaultresolverspecification.md)
- [mlMultiArrayDataType](double/mlmultiarraydatatype.md)

### Default Implementations

- [AdditiveArithmetic Implementations](double/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](double/atomicrepresentable-implementations.md)
- [BinaryFloatingPoint Implementations](double/binaryfloatingpoint-implementations.md)
- [Comparable Implementations](double/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](double/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](double/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](double/customstringconvertible-implementations.md)
- [Decodable Implementations](double/decodable-implementations.md)
- [Encodable Implementations](double/encodable-implementations.md)
- [Equatable Implementations](double/equatable-implementations.md)
- [ExpressibleByFloatLiteral Implementations](double/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](double/expressiblebyintegerliteral-implementations.md)
- [FloatingPoint Implementations](double/floatingpoint-implementations.md)
- [Hashable Implementations](double/hashable-implementations.md)
- [LosslessStringConvertible Implementations](double/losslessstringconvertible-implementations.md)
- [Numeric Implementations](double/numeric-implementations.md)
- [SIMDScalar Implementations](double/simdscalar-implementations.md)
- [SignedNumeric Implementations](double/signednumeric-implementations.md)
- [Strideable Implementations](double/strideable-implementations.md)
- [TextOutputStreamable Implementations](double/textoutputstreamable-implementations.md)

## See Also

### Standard Library

- [Int](int.md) — A signed integer value type.
- [String](string.md) — A Unicode string value that is a collection of characters.
- [Array](array.md) — An ordered, random-access collection.
- [Dictionary](dictionary.md) — A collection whose elements are key-value pairs.
- [Swift Standard Library](swift-standard-library.md) — Solve complex problems and write high-performance, readable code.
