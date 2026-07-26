---
title: NumberFormatStyleConfiguration.Precision
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatstyleconfiguration/precision
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration/precision.json'
content_hash: 'sha256:702ffc9c2c8890c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md)

# NumberFormatStyleConfiguration.Precision

<sub>Structure</sub>

A structure that an integer format style uses to configure precision.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Precision
```

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Precision configurations

- [significantDigits(_:)](<precision/significantdigits(__)-2rp7g.md>) — Returns a precision that constrains formatted values to a range of significant digits.
- [significantDigits(_:)](<precision/significantdigits(__)-9dvpr.md>) — Returns a precision that constrains formatted values to a given number of significant digits.
- [integerAndFractionLength(integerLimits:fractionLimits:)](<precision/integerandfractionlength(integerlimits_fractionlimits_).md>) — Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.
- [integerAndFractionLength(integer:fraction:)](<precision/integerandfractionlength(integer_fraction_).md>) — Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.
- [integerLength(_:)](<precision/integerlength(__)-u8ua.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the integer part.
- [integerLength(_:)](<precision/integerlength(__)-1njyz.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.
- [fractionLength(_:)](<precision/fractionlength(__)-w6fk.md>) — Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
- [fractionLength(_:)](<precision/fractionlength(__)-3wkd9.md>) — Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.

## See Also

### Specifying Configuration

- [DecimalSeparatorDisplayStrategy](decimalseparatordisplaystrategy.md) — A structure that an integer format style uses to configure a decimal separator display strategy.
- [Grouping](grouping.md) — A structure that an integer format style uses to configure grouping.
- [RoundingRule](roundingrule.md) — The type used for rounding rule values.
- [SignDisplayStrategy](signdisplaystrategy.md) — A structure that an integer format style uses to configure a sign display strategy.
- [Notation](notation.md) — A structure that an integer format style uses to configure notation.
