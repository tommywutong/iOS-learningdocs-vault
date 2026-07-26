---
title: NSDecimalNumber.CalculationError
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumber/calculationerror
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/calculationerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/calculationerror.json'
content_hash: 'sha256:04b48773b2004e9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# NSDecimalNumber.CalculationError

<sub>Enumeration</sub>

Calculation error constants used to describe an error in [- exceptionDuringOperation:error:leftOperand:rightOperand:](<../nsdecimalnumberbehaviors/exceptionduringoperation(__error_leftoperand_rightoperand_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CalculationError
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSCalculationNoError](calculationerror/noerror.md) — No error occurred.
- [NSCalculationLossOfPrecision](calculationerror/lossofprecision.md) — The number can’t be represented in 38 significant digits.
- [NSCalculationOverflow](calculationerror/overflow.md) — The number is too large to represent.
- [NSCalculationUnderflow](calculationerror/underflow.md) — The number is too small to represent.
- [NSCalculationDivideByZero](calculationerror/dividebyzero.md) — The caller tried to divide by `0`.

### Initializers

- [init(rawValue:)](<calculationerror/init(rawvalue_).md>)

## See Also

### Performing arithmetic using references

- [NSDecimalCompact](<../nsdecimalcompact(__).md>) — Compacts the decimal structure for efficiency.
- [NSDecimalAdd](<../nsdecimaladd(________).md>) — Adds two decimal values.
- [NSDecimalSubtract](<../nsdecimalsubtract(________).md>) — Subtracts one decimal value from another.
- [NSDecimalDivide](<../nsdecimaldivide(________).md>) — Divides one decimal value by another.
- [NSDecimalMultiply](<../nsdecimalmultiply(________).md>) — Multiplies two decimal numbers together.
- [NSDecimalMultiplyByPowerOf10](<../nsdecimalmultiplybypowerof10(________).md>) — Multiplies a decimal by the specified power of 10.
- [NSDecimalRound](<../nsdecimalround(________).md>) — Rounds off the decimal value.
- [NSDecimalPower](<../nsdecimalpower(________).md>) — Raises the decimal value to the specified power.
- [NSDecimalNormalize](<../nsdecimalnormalize(______).md>) — Normalizes the internal format of two decimal numbers to simplify later operations.
- [RoundingMode](../decimal/roundingmode.md) — An alias for an enumeration that specifies possible rounding modes.
- [RoundingMode](roundingmode.md) — These constants specify rounding behaviors.
- [CalculationError](../decimal/calculationerror.md) — An alias for a type that specifies possible calculation errors.
