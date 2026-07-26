---
title: 'integerAndFractionLength(integer:fraction:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatstyleconfiguration/precision/integerandfractionlength(integer:fraction:)'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision/integerandfractionlength(integer:fraction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration/precision/integerandfractionlength%28integer%3Afraction%3A%29.json'
content_hash: 'sha256:8bdb21e0932b120d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) · [Precision](../precision.md)

# integerAndFractionLength(integer:fraction:)

<sub>Type Method</sub>

Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func integerAndFractionLength(integer: Int, fraction: Int) -> NumberFormatStyleConfiguration.Precision
```

## Parameters

- `integer` — The number of digits to use when formatting the integer part of a number.

- `fraction` — The number of digits to use when formatting the fraction part of a number.

## Return Value

A precision that constrains formatted values a given number of digits in the integer and fraction parts.

## Discussion

When using this precision, the formatter pads values with fewer digits than the specified digits for the integer or fraction parts. Similarly, it rounds values that have more digits than specified. The following example shows this behavior, padding the integer part while rounding the fraction:

```swift
let myNum = 12345.6789.formatted(.number
    .precision(.integerAndFractionLength(integer: 6,
                                         fraction: 3))
    .rounded(rule: .down)) // "012,345.678"
```

## See Also

### Precision configurations

- [significantDigits(_:)](<significantdigits(__)-2rp7g.md>) — Returns a precision that constrains formatted values to a range of significant digits.
- [significantDigits(_:)](<significantdigits(__)-9dvpr.md>) — Returns a precision that constrains formatted values to a given number of significant digits.
- [integerAndFractionLength(integerLimits:fractionLimits:)](<integerandfractionlength(integerlimits_fractionlimits_).md>) — Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.
- [integerLength(_:)](<integerlength(__)-u8ua.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the integer part.
- [integerLength(_:)](<integerlength(__)-1njyz.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.
- [fractionLength(_:)](<fractionlength(__)-w6fk.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
- [fractionLength(_:)](<fractionlength(__)-3wkd9.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.
