---
title: NumberFormatter.Style.currency
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/style/currency
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/style/currency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/style/currency.json'
content_hash: 'sha256:0b08a3a23d1646cc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatter](../../numberformatter.md) · [Style](../style.md)

# NumberFormatter.Style.currency

<sub>Case</sub>

A currency style format that uses the currency symbol defined by the number formatter locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case currency
```

## Discussion

For example, in the en_US locale, the number 1234.5678 is represented as $1,234.57; in the fr_FR locale, the number 1234.5678 is represented as 1 234,57 €.

## See Also

### Formatting Styles

- [NSNumberFormatterNoStyle](none.md) — An integer representation.
- [NSNumberFormatterDecimalStyle](decimal.md) — A decimal style format.
- [NSNumberFormatterPercentStyle](percent.md) — A percent style format.
- [NSNumberFormatterScientificStyle](scientific.md) — A scientific style format.
- [NSNumberFormatterSpellOutStyle](spellout.md) — A style format in which numbers are spelled out in the language defined by the number formatter locale.
- [NSNumberFormatterOrdinalStyle](ordinal.md) — An ordinal style format.
- [NSNumberFormatterCurrencyAccountingStyle](currencyaccounting.md) — An accounting currency style format that uses the currency symbol defined by the number formatter locale.
- [NSNumberFormatterCurrencyISOCodeStyle](currencyisocode.md) — A currency style format that uses the ISO 4217 currency code defined by the number formatter locale.
- [NSNumberFormatterCurrencyPluralStyle](currencyplural.md) — A currency style format that uses the pluralized denomination defined by the number formatter locale.
