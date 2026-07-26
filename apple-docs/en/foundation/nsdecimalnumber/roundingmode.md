---
title: NSDecimalNumber.RoundingMode
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumber/roundingmode
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/roundingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/roundingmode.json'
content_hash: 'sha256:07892aea7947f93c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# NSDecimalNumber.RoundingMode

<sub>Enumeration</sub>

These constants specify rounding behaviors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum RoundingMode
```

## Overview

The rounding mode matters only if the [- scale](<../nsdecimalnumberbehaviors/scale().md>) method sets a limit on the precision of `NSDecimalNumber` return values. It has no effect if [- scale](<../nsdecimalnumberbehaviors/scale().md>) returns `NSDecimalNoScale`. Assuming that [- scale](<../nsdecimalnumberbehaviors/scale().md>) returns 1, the rounding mode has the following effects on various original values:

| Original Value | NSRoundPlain | NSRoundDown & NS RoundUp | NSRoundBankers |
|---|---|---|---|
| 1.24 | 1.2 | 1.2 & 1.3 | 1.2 |
| 1.26 | 1.3 | 1.2 & 1.3 | 1.3 |
| 1.25 | 1.3 | 1.2 & 1.3 | 1.2 |
| 1.35 | 1.4 | 1.3  & 1.4 | 1.4 |
| –1.35 | –1.4 | –1.4  & -1.3 | –1.4 |

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSRoundPlain](roundingmode/plain.md) — Round to the closest possible return value; when caught halfway between two positive numbers, round up; when caught between two negative numbers, round down.
- [NSRoundDown](roundingmode/down.md) — Round return values down.
- [NSRoundUp](roundingmode/up.md) — Round return values up.
- [NSRoundBankers](roundingmode/bankers.md) — Round to the closest possible return value; when halfway between two possibilities, return the possibility whose last digit is even.

### Initializers

- [init(rawValue:)](<roundingmode/init(rawvalue_).md>)

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
- [CalculationError](../decimal/calculationerror.md) — An alias for a type that specifies possible calculation errors.
- [CalculationError](calculationerror.md) — Calculation error constants used to describe an error in [- exceptionDuringOperation:error:leftOperand:rightOperand:](<../nsdecimalnumberbehaviors/exceptionduringoperation(__error_leftoperand_rightoperand_).md>).
