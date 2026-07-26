---
title: 'fractionLength(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatstyleconfiguration/precision/fractionlength(_:)-3wkd9'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision/fractionlength(_:)-3wkd9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration/precision/fractionlength%28_%3A%29-3wkd9.json'
content_hash: 'sha256:97f149ea2fb49b50'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) · [Precision](../precision.md)

# fractionLength(_:)

<sub>Type Method</sub>

Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func fractionLength(_ length: Int) -> NumberFormatStyleConfiguration.Precision
```

## Parameters

- `length` — The number of digits to use when formatting the fraction part of a number.

## Return Value

A precision that constrains formatted values to a given number of allowed digits in the fraction part.

## See Also

### Precision configurations

- [significantDigits(_:)](<significantdigits(__)-2rp7g.md>) — Returns a precision that constrains formatted values to a range of significant digits.
- [significantDigits(_:)](<significantdigits(__)-9dvpr.md>) — Returns a precision that constrains formatted values to a given number of significant digits.
- [integerAndFractionLength(integerLimits:fractionLimits:)](<integerandfractionlength(integerlimits_fractionlimits_).md>) — Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.
- [integerAndFractionLength(integer:fraction:)](<integerandfractionlength(integer_fraction_).md>) — Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.
- [integerLength(_:)](<integerlength(__)-u8ua.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the integer part.
- [integerLength(_:)](<integerlength(__)-1njyz.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.
- [fractionLength(_:)](<fractionlength(__)-w6fk.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
