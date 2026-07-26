---
title: 'integerLength(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatstyleconfiguration/precision/integerlength(_:)-u8ua'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision/integerlength(_:)-u8ua'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration/precision/integerlength%28_%3A%29-u8ua.json'
content_hash: 'sha256:9dc41a3ca380b3af'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) · [Precision](../precision.md)

# integerLength(_:)

<sub>Type Method</sub>

Returns a precision that constrains formatted values to a range of allowed digits in the integer part.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func integerLength<R>(_ limits: R) -> NumberFormatStyleConfiguration.Precision where R : RangeExpression
```

## Parameters

- `limits` — A range from the minimum to the maximum number of digits to use when formatting the integer part of a number.

## Return Value

A precision that constrains formatted values to ranges of digits in the integer part.

## See Also

### Precision configurations

- [significantDigits(_:)](<significantdigits(__)-2rp7g.md>) — Returns a precision that constrains formatted values to a range of significant digits.
- [significantDigits(_:)](<significantdigits(__)-9dvpr.md>) — Returns a precision that constrains formatted values to a given number of significant digits.
- [integerAndFractionLength(integerLimits:fractionLimits:)](<integerandfractionlength(integerlimits_fractionlimits_).md>) — Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.
- [integerAndFractionLength(integer:fraction:)](<integerandfractionlength(integer_fraction_).md>) — Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.
- [integerLength(_:)](<integerlength(__)-1njyz.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.
- [fractionLength(_:)](<fractionlength(__)-w6fk.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
- [fractionLength(_:)](<fractionlength(__)-3wkd9.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.
