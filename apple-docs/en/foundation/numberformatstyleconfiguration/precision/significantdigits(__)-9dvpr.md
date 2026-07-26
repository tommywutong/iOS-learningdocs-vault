---
title: 'significantDigits(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatstyleconfiguration/precision/significantdigits(_:)-9dvpr'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision/significantdigits(_:)-9dvpr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration/precision/significantdigits%28_%3A%29-9dvpr.json'
content_hash: 'sha256:d7d2ca7bcbfb0914'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) · [Precision](../precision.md)

# significantDigits(_:)

<sub>Type Method</sub>

Returns a precision that constrains formatted values to a given number of significant digits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func significantDigits(_ digits: Int) -> NumberFormatStyleConfiguration.Precision
```

## Parameters

- `digits` — The maximum number of significant digits to use when formatting values.

## Return Value

A precision that constrains formatted values to a given number of significant digits.

## Discussion

When using this precision, the formatter rounds values that have more sigificant digits than the maximum of the range, as seen in the following example:

```swift
let myNum = 123456.formatted(.number
    .precision(.significantDigits(4))
    .rounded(rule: .down)) // "123,400"
```

## See Also

### Precision configurations

- [significantDigits(_:)](<significantdigits(__)-2rp7g.md>) — Returns a precision that constrains formatted values to a range of significant digits.
- [integerAndFractionLength(integerLimits:fractionLimits:)](<integerandfractionlength(integerlimits_fractionlimits_).md>) — Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.
- [integerAndFractionLength(integer:fraction:)](<integerandfractionlength(integer_fraction_).md>) — Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.
- [integerLength(_:)](<integerlength(__)-u8ua.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the integer part.
- [integerLength(_:)](<integerlength(__)-1njyz.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.
- [fractionLength(_:)](<fractionlength(__)-w6fk.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
- [fractionLength(_:)](<fractionlength(__)-3wkd9.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.
