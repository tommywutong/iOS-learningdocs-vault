---
title: NumberFormatter.Style.spellOut
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/style/spellout
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/style/spellout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/style/spellout.json'
content_hash: 'sha256:369e102b18a84a34'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatter](../../numberformatter.md) · [Style](../style.md)

# NumberFormatter.Style.spellOut

<sub>Case</sub>

A style format in which numbers are spelled out in the language defined by the number formatter locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case spellOut
```

## Discussion

For example, in the en_US locale, the number 1234.5678 is represented as one thousand two hundred thirty-four point five six seven eight; in the fr_FR locale, the number 1234.5678 is represented as mille deux cent trente-quatre virgule cinq six sept huit.

This style is supported for most user locales. If this style doesn’t support the number formatter locale, the en_US locale is used as a fallback.

## See Also

### Formatting Styles

- [NSNumberFormatterNoStyle](none.md) — An integer representation.
- [NSNumberFormatterDecimalStyle](decimal.md) — A decimal style format.
- [NSNumberFormatterPercentStyle](percent.md) — A percent style format.
- [NSNumberFormatterScientificStyle](scientific.md) — A scientific style format.
- [NSNumberFormatterOrdinalStyle](ordinal.md) — An ordinal style format.
- [NSNumberFormatterCurrencyStyle](currency.md) — A currency style format that uses the currency symbol defined by the number formatter locale.
- [NSNumberFormatterCurrencyAccountingStyle](currencyaccounting.md) — An accounting currency style format that uses the currency symbol defined by the number formatter locale.
- [NSNumberFormatterCurrencyISOCodeStyle](currencyisocode.md) — A currency style format that uses the ISO 4217 currency code defined by the number formatter locale.
- [NSNumberFormatterCurrencyPluralStyle](currencyplural.md) — A currency style format that uses the pluralized denomination defined by the number formatter locale.
