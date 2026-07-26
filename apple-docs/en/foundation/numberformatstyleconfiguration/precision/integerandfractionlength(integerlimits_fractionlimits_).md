---
title: 'integerAndFractionLength(integerLimits:fractionLimits:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatstyleconfiguration/precision/integerandfractionlength(integerlimits:fractionlimits:)'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision/integerandfractionlength(integerlimits:fractionlimits:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration/precision/integerandfractionlength%28integerlimits%3Afractionlimits%3A%29.json'
content_hash: 'sha256:29c3e7f90d6b2c7c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) · [Precision](../precision.md)

# integerAndFractionLength(integerLimits:fractionLimits:)

<sub>Type Method</sub>

Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func integerAndFractionLength<R1, R2>(integerLimits: R1, fractionLimits: R2) -> NumberFormatStyleConfiguration.Precision where R1 : RangeExpression, R2 : RangeExpression, R1.Bound == Int, R2.Bound == Int
```

## Parameters

- `integerLimits` — A range from the minimum to the maximum number of digits to use when formatting the integer part of a number.

- `fractionLimits` — A range from the minimum to the maximum number of digits to use when formatting the fraction part of a number.

## Return Value

A precision that constrains formatted values to ranges of digits in the integer and fraction parts.

## Discussion

When using this precision, the formatter rounds values that have more digits than the maximum of the range, as seen in the following example:

```swift
let myNum = 12345.6789.formatted(.number
    .precision(.integerAndFractionLength(integerLimits: 2...,
                                         fractionLimits: 2...3))
    .rounded(rule: .down)) // "12,345.678"
```

## See Also

### Precision configurations

- [significantDigits(_:)](<significantdigits(__)-2rp7g.md>) — Returns a precision that constrains formatted values to a range of significant digits.
- [significantDigits(_:)](<significantdigits(__)-9dvpr.md>) — Returns a precision that constrains formatted values to a given number of significant digits.
- [integerAndFractionLength(integer:fraction:)](<integerandfractionlength(integer_fraction_).md>) — Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.
- [integerLength(_:)](<integerlength(__)-u8ua.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the integer part.
- [integerLength(_:)](<integerlength(__)-1njyz.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.
- [fractionLength(_:)](<fractionlength(__)-w6fk.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
- [fractionLength(_:)](<fractionlength(__)-3wkd9.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.
