---
title: 'NSDecimalNormalize(_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnormalize(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnormalize(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnormalize%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3f5736d0bd21e3be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalNormalize(_:_:_:)

<sub>Function</sub>

Normalizes the internal format of two decimal numbers to simplify later operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSDecimalNormalize(_ number1: UnsafeMutablePointer<Decimal>, _ number2: UnsafeMutablePointer<Decimal>, _ roundingMode: NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError
```

## Discussion

[Decimal](decimal.md) instances are represented in memory as a mantissa and an exponent, expressing the value mantissa x 10^exponent. A number can have many representations; for example, the following table lists several valid representations for the number 100:

| Mantissa | Exponent |
|---|---|
| 100 | 0 |
| 10 | 1 |
| 1 | 2 |

Format `number1` and `number2` so that they have equal exponents. This format makes addition and subtraction very convenient. Both [NSDecimalAdd](<nsdecimaladd(________).md>) and [NSDecimalSubtract](<nsdecimalsubtract(________).md>) call [NSDecimalNormalize](<nsdecimalnormalize(______).md>). You may want to use it if you write more complicated addition or subtraction routines.

For explanations of the possible return values, see [NSDecimalAdd](<nsdecimaladd(________).md>).

For more information, see [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).

## See Also

### Performing arithmetic using references

- [NSDecimalCompact](<nsdecimalcompact(__).md>) — Compacts the decimal structure for efficiency.
- [NSDecimalAdd](<nsdecimaladd(________).md>) — Adds two decimal values.
- [NSDecimalSubtract](<nsdecimalsubtract(________).md>) — Subtracts one decimal value from another.
- [NSDecimalDivide](<nsdecimaldivide(________).md>) — Divides one decimal value by another.
- [NSDecimalMultiply](<nsdecimalmultiply(________).md>) — Multiplies two decimal numbers together.
- [NSDecimalMultiplyByPowerOf10](<nsdecimalmultiplybypowerof10(________).md>) — Multiplies a decimal by the specified power of 10.
- [NSDecimalRound](<nsdecimalround(________).md>) — Rounds off the decimal value.
- [NSDecimalPower](<nsdecimalpower(________).md>) — Raises the decimal value to the specified power.
- [RoundingMode](decimal/roundingmode.md) — An alias for an enumeration that specifies possible rounding modes.
- [RoundingMode](nsdecimalnumber/roundingmode.md) — These constants specify rounding behaviors.
- [CalculationError](decimal/calculationerror.md) — An alias for a type that specifies possible calculation errors.
- [CalculationError](nsdecimalnumber/calculationerror.md) — Calculation error constants used to describe an error in [- exceptionDuringOperation:error:leftOperand:rightOperand:](<nsdecimalnumberbehaviors/exceptionduringoperation(__error_leftoperand_rightoperand_).md>).
