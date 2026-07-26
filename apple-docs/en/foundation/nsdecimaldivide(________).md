---
title: 'NSDecimalDivide(_:_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimaldivide(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimaldivide(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimaldivide%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:36c1bd35eb23ec82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalDivide(_:_:_:_:)

<sub>Function</sub>

Divides one decimal value by another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSDecimalDivide(_ result: UnsafeMutablePointer<Decimal>, _ leftOperand: UnsafePointer<Decimal>, _ rightOperand: UnsafePointer<Decimal>, _ roundingMode: NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError
```

## Discussion

Divides `leftOperand` by `rightOperand` and stores the quotient, possibly rounded off according to `roundingMode`, in `result`. If `rightOperand` is 0, returns `NSDivideByZero`.

For explanations of the possible return values and rounding modes, see [NSDecimalAdd](<nsdecimaladd(________).md>).

Note that repeating decimals or numbers with a mantissa larger than 38 digits cannot be represented precisely.

For more information, see [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).

## See Also

### Performing arithmetic using references

- [NSDecimalCompact](<nsdecimalcompact(__).md>) — Compacts the decimal structure for efficiency.
- [NSDecimalAdd](<nsdecimaladd(________).md>) — Adds two decimal values.
- [NSDecimalSubtract](<nsdecimalsubtract(________).md>) — Subtracts one decimal value from another.
- [NSDecimalMultiply](<nsdecimalmultiply(________).md>) — Multiplies two decimal numbers together.
- [NSDecimalMultiplyByPowerOf10](<nsdecimalmultiplybypowerof10(________).md>) — Multiplies a decimal by the specified power of 10.
- [NSDecimalRound](<nsdecimalround(________).md>) — Rounds off the decimal value.
- [NSDecimalPower](<nsdecimalpower(________).md>) — Raises the decimal value to the specified power.
- [NSDecimalNormalize](<nsdecimalnormalize(______).md>) — Normalizes the internal format of two decimal numbers to simplify later operations.
- [RoundingMode](decimal/roundingmode.md) — An alias for an enumeration that specifies possible rounding modes.
- [RoundingMode](nsdecimalnumber/roundingmode.md) — These constants specify rounding behaviors.
- [CalculationError](decimal/calculationerror.md) — An alias for a type that specifies possible calculation errors.
- [CalculationError](nsdecimalnumber/calculationerror.md) — Calculation error constants used to describe an error in [- exceptionDuringOperation:error:leftOperand:rightOperand:](<nsdecimalnumberbehaviors/exceptionduringoperation(__error_leftoperand_rightoperand_).md>).
