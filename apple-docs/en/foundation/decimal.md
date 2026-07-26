---
title: Decimal
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/decimal
source_url: 'https://developer.apple.com/documentation/foundation/decimal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal.json'
content_hash: 'sha256:442254b5643cc910'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Decimal

<sub>Structure</sub>

A structure representing a base-10 number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Decimal
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](../swift/additivearithmetic.md), [Comparable](../swift/comparable.md), [ConvertibleFromGeneratedContent](../foundationmodels/convertiblefromgeneratedcontent.md), [ConvertibleToGeneratedContent](../foundationmodels/convertibletogeneratedcontent.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md), [Generable](../foundationmodels/generable.md), [Hashable](../swift/hashable.md), [InstructionsRepresentable](../foundationmodels/instructionsrepresentable.md), [Numeric](../swift/numeric.md), [Plottable](../charts/plottable.md), [PromptRepresentable](../foundationmodels/promptrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SignedNumeric](../swift/signednumeric.md), [Strideable](../swift/strideable.md)

## Topics

### Creating an empty decimal

- [init()](<decimal/init().md>) — Creates a decimal initialized to `0`.

### Creating a decimal from components

- [init(sign:exponent:significand:)](<decimal/init(sign_exponent_significand_).md>) — Creates a decimal initialized with the given sign, exponent, and significand.

### Creating a decimal from a floating point number

- [init(_:)](<decimal/init(__)-6wgru.md>) — Creates and initializes a decimal with the provided floating point value.
- [init(floatLiteral:)](<decimal/init(floatliteral_).md>) — Creates and initializes a decimal with the provided floating point value.

### Creating a decimal from an integer

- [init(exactly:)](<decimal/init(exactly_).md>) — Creates a new decimal value exactly representing the provided integer.
- [init(_:)](<decimal/init(__)-2tcho.md>) — Creates and initializes a decimal with the provided integer value.
- [init(_:)](<decimal/init(__)-4gk29.md>) — Creates and initializes a decimal with the provided integer value.
- [init(_:)](<decimal/init(__)-5aznh.md>) — Creates and initializes a decimal with the provided integer value.
- [init(_:)](<decimal/init(__)-7dmlc.md>) — Creates and initializes a decimal with the provided integer value.
- [init(_:)](<decimal/init(__)-7a033.md>) — Creates and initializes a decimal with the provided integer value.
- [init(integerLiteral:)](<decimal/init(integerliteral_).md>) — Creates and initializes a decimal with the provided integer value.

### Creating a decimal from an unsigned integer

- [init(_:)](<decimal/init(__)-2lxxy.md>) — Creates and initializes a decimal with the provided unsigned integer value.
- [init(_:)](<decimal/init(__)-4gbgq.md>) — Creates and initializes a decimal with the provided unsigned integer value.
- [init(_:)](<decimal/init(__)-9lio1.md>) — Creates and initializes a decimal with the provided unsigned integer value.
- [init(_:)](<decimal/init(__)-9okou.md>) — Creates and initializes a decimal with the provided unsigned integer value.
- [init(_:)](<decimal/init(__)-43cx6.md>) — Creates and initializes a decimal with the provided unsigned integer value.

### Creating a decimal from another decimal

- [init(signOf:magnitudeOf:)](<decimal/init(signof_magnitudeof_).md>) — Creates and initializes a decimal with the sign and magnitude of the given decimals.
- [NSDecimalCopy](<nsdecimalcopy(____).md>) — Copies the value of a decimal number.

### Creating a decimal by parsing a string

- [init(_:format:lenient:)](<decimal/init(__format_lenient_)-6fk71.md>) — Creates and initializes a decimal by parsing a string according to the provided format style.
- [init(_:format:lenient:)](<decimal/init(__format_lenient_)-8t5o2.md>) — Creates and initializes a decimal by parsing a string according to the provided currency format style.
- [init(_:format:lenient:)](<decimal/init(__format_lenient_)-3u6o6.md>) — Creates and initializes a percentage decimal by parsing a string according to the provided format style.
- [init(string:locale:)](<decimal/init(string_locale_).md>) — Creates and initializes a decimal by parsing a string according to the provided locale’s conventions.
- [init(_:strategy:)](<decimal/init(__strategy_).md>) — Creates and initializes a decimal by parsing an arbitrary type according to the provided parse strategy.
- [ParseStrategy](decimal/parsestrategy.md) — A parse strategy for creating decimal values from formatted strings.

### Performing arithmetic

- [pow(_:_:)](<pow(____).md>) — Returns a decimal number raised to a given power.

### Performing arithmetic using references

- [NSDecimalCompact](<nsdecimalcompact(__).md>) — Compacts the decimal structure for efficiency.
- [NSDecimalAdd](<nsdecimaladd(________).md>) — Adds two decimal values.
- [NSDecimalSubtract](<nsdecimalsubtract(________).md>) — Subtracts one decimal value from another.
- [NSDecimalDivide](<nsdecimaldivide(________).md>) — Divides one decimal value by another.
- [NSDecimalMultiply](<nsdecimalmultiply(________).md>) — Multiplies two decimal numbers together.
- [NSDecimalMultiplyByPowerOf10](<nsdecimalmultiplybypowerof10(________).md>) — Multiplies a decimal by the specified power of 10.
- [NSDecimalRound](<nsdecimalround(________).md>) — Rounds off the decimal value.
- [NSDecimalPower](<nsdecimalpower(________).md>) — Raises the decimal value to the specified power.
- [NSDecimalNormalize](<nsdecimalnormalize(______).md>) — Normalizes the internal format of two decimal numbers to simplify later operations.
- [RoundingMode](decimal/roundingmode.md) — An alias for an enumeration that specifies possible rounding modes.
- [RoundingMode](nsdecimalnumber/roundingmode.md) — These constants specify rounding behaviors.
- [CalculationError](decimal/calculationerror.md) — An alias for a type that specifies possible calculation errors.
- [CalculationError](nsdecimalnumber/calculationerror.md) — Calculation error constants used to describe an error in [- exceptionDuringOperation:error:leftOperand:rightOperand:](<nsdecimalnumberbehaviors/exceptionduringoperation(__error_leftoperand_rightoperand_).md>).

### Getting a decimal’s characteristics

- [sign](decimal/sign.md) — The sign of the decimal.
- [exponent](decimal/exponent.md) — The exponent of the decimal.
- [significand](decimal/significand.md) — The significand of the decimal.
- [magnitude](decimal/magnitude.md) — The magnitude of this decimal.
- [floatingPointClass](decimal/floatingpointclass.md) — The IEEE 754 class of this type.
- [isCanonical](decimal/iscanonical.md) — A Boolean value indicating whether the representation of this decimal is canonical.
- [isFinite](decimal/isfinite.md) — A Boolean value indicating whether this decimal is zero, subnormal, or normal (not infinity or NaN).
- [isInfinite](decimal/isinfinite.md) — A Boolean value indicating whether this decimal is infinity.
- [isNaN](decimal/isnan.md) — A Boolean value indicating whether this decimal is NaN.
- [isNormal](decimal/isnormal.md) — A Boolean value indicating whether this decimal is normal (not zero, subnormal, infinity, or NaN).
- [isSignMinus](decimal/issignminus.md) — A Boolean value indicating whether this decimal has a negative sign.
- [isSignaling](decimal/issignaling.md) — A Boolean value indicating whether this decimal is a signaling NaN.``
- [isSignalingNaN](decimal/issignalingnan.md) — A Boolean value indicating whether this decimal is a signaling NaN.
- [isSubnormal](decimal/issubnormal.md) — A Boolean value indicating whether this decimal is subnormal.
- [isZero](decimal/iszero.md) — A Boolean value indicating whether this value is zero.
- [nextDown](decimal/nextdown.md) — The greatest representable value that is less than this decimal.
- [nextUp](decimal/nextup.md) — The least representable value that is greater than this decimal.
- [ulp](decimal/ulp.md) — The unit in the last place of the decimal.

### Getting particular decimals

- [greatestFiniteMagnitude](decimal/greatestfinitemagnitude.md) — The decimal that contains the largest possible non-infinite magnitude for the underlying representation.
- [leastFiniteMagnitude](decimal/leastfinitemagnitude.md) — The decimal that contains the smallest possible non-infinite magnitude for the underlying representation.
- [leastNonzeroMagnitude](decimal/leastnonzeromagnitude.md) — The decimal value that represents the smallest possible non-zero value for the underlying representation.
- [leastNormalMagnitude](decimal/leastnormalmagnitude.md) — The decimal value that represents the smallest possible normal magnitude for the underlying representation.
- [pi](decimal/pi.md) — The mathematical constant pi.
- [nan](decimal/nan.md) — The value that represents “not a number.”
- [quietNaN](decimal/quietnan.md) — A quiet representation of not-a-number.
- [radix](decimal/radix.md) — The radix used by decimal numbers.
- [NSDecimalMaxSize](nsdecimalmaxsize.md) — The maximum size of [Decimal](decimal.md).
- [NSDecimalNoScale](nsdecimalnoscale.md) — Specifies that the number of digits allowed after the decimal separator in a decimal number should not be limited.

### Formatting decimals

- [formatted()](<decimal/formatted().md>) — Formats the decimal using a default localized format style.
- [formatted(_:)](<decimal/formatted(__).md>) — Formats the decimal using the provided format style.
- [FormatStyle](decimal/formatstyle.md) — A structure that converts between decimal values and their textual representations.

### Converting between decimals and strings

- [NSDecimalString](<nsdecimalstring(____).md>) — Returns a string representation of the decimal value appropriate for the specified locale.

### Comparing decimals

- [isEqual(to:)](<decimal/isequal(to_).md>) — Indicates whether this decimal is equal to the specified one.
- [isLess(than:)](<decimal/isless(than_).md>) — Indicates whether this decimal is less than the specified one.
- [isLessThanOrEqualTo(_:)](<decimal/islessthanorequalto(__).md>) — Indicates whether this decimal is less than or equal to the specified one.
- [isTotallyOrdered(belowOrEqualTo:)](<decimal/istotallyordered(beloworequalto_).md>) — Returns a Boolean value indicating whether this instance should precede the given value in an ascending sort.
- [distance(to:)](<decimal/distance(to_).md>) — Returns the distance from this value to the specified value.
- [advanced(by:)](<decimal/advanced(by_).md>) — Returns a new value advanced by the given distance.
- [NSDecimalCompare](<nsdecimalcompare(____).md>) — Compares two decimal values.

### Using reference types

- [NSDecimalNumber](nsdecimalnumber.md) — An object for representing and performing arithmetic on base-10 numbers.

### Supporting Types

- [FormatStyle](decimal/formatstyle.md) — A structure that converts between decimal values and their textual representations.

### Operators

- [/(_:_:)](<decimal/_(____).md>) — Divides one decimal number by another.
- [/=(_:_:)](<decimal/_=(____).md>) — Divides one decimal number by another, storing the result in the first number.

### Default Implementations

- [AdditiveArithmetic Implementations](decimal/additivearithmetic-implementations.md)
- [ExpressibleByFloatLiteral Implementations](decimal/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](decimal/expressiblebyintegerliteral-implementations.md)
- [Numeric Implementations](decimal/numeric-implementations.md)
- [SignedNumeric Implementations](decimal/signednumeric-implementations.md)
- [Strideable Implementations](decimal/strideable-implementations.md)

## See Also

### Numbers

- [Int](../swift/int.md) — A signed integer value type.
- [Double](../swift/double.md) — A double-precision (64-bit), floating-point value type.
- [NumberFormatter](numberformatter.md) — A formatter that converts between numeric values and their textual representations.
