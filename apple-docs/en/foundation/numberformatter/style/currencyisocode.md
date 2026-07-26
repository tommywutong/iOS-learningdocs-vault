---
title: NumberFormatter.Style.currencyISOCode
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/style/currencyisocode
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/style/currencyisocode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/style/currencyisocode.json'
content_hash: 'sha256:31674be8db3d39f1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatter](../../numberformatter.md) · [Style](../style.md)

# NumberFormatter.Style.currencyISOCode

<sub>Case</sub>

A currency style format that uses the ISO 4217 currency code defined by the number formatter locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case currencyISOCode
```

## Discussion

This style behaves like the [NSNumberFormatterCurrencyStyle](currency.md) style, except that the currency symbol is replaced by the corresponding ISO 4217 currency code. For example, in the en_US locale, the number 1234.5678 is represented as USD1,234.57; in the fr_FR locale, the number 1234.5678 is represented as 1 234,57 EUR.

## See Also

### Formatting Styles

- [NSNumberFormatterNoStyle](none.md) — An integer representation.
- [NSNumberFormatterDecimalStyle](decimal.md) — A decimal style format.
- [NSNumberFormatterPercentStyle](percent.md) — A percent style format.
- [NSNumberFormatterScientificStyle](scientific.md) — A scientific style format.
- [NSNumberFormatterSpellOutStyle](spellout.md) — A style format in which numbers are spelled out in the language defined by the number formatter locale.
- [NSNumberFormatterOrdinalStyle](ordinal.md) — An ordinal style format.
- [NSNumberFormatterCurrencyStyle](currency.md) — A currency style format that uses the currency symbol defined by the number formatter locale.
- [NSNumberFormatterCurrencyAccountingStyle](currencyaccounting.md) — An accounting currency style format that uses the currency symbol defined by the number formatter locale.
- [NSNumberFormatterCurrencyPluralStyle](currencyplural.md) — A currency style format that uses the pluralized denomination defined by the number formatter locale.
