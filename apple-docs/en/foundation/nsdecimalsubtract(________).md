---
title: 'NSDecimalSubtract(_:_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalsubtract(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalsubtract(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalsubtract%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:083ad67fc62ed412'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalSubtract(_:_:_:_:)

<sub>Function</sub>

Subtracts one decimal value from another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSDecimalSubtract(_ result: UnsafeMutablePointer<Decimal>, _ leftOperand: UnsafePointer<Decimal>, _ rightOperand: UnsafePointer<Decimal>, _ roundingMode: NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError
```

## Discussion

Subtracts `rightOperand` from `leftOperand` and stores the difference, possibly rounded off according to `roundingMode`, in `result`.

For explanations of the possible return values and rounding modes, see [NSDecimalAdd](<nsdecimaladd(________).md>).

For more information, see [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).

## See Also

### Performing arithmetic using references

- [NSDecimalCompact](<nsdecimalcompact(__).md>) — Compacts the decimal structure for efficiency.
- [NSDecimalAdd](<nsdecimaladd(________).md>) — Adds two decimal values.
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
