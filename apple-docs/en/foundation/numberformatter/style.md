---
title: NumberFormatter.Style
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/style
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/style'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/style.json'
content_hash: 'sha256:b3d29cb69f74c6a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# NumberFormatter.Style

<sub>Enumeration</sub>

The predefined number format styles used by the [numberStyle](numberstyle.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Style
```

## Overview

The table below provides examples of each formatting style for the U.S., France, and China.

| Style | en_US Locale | fr_FR Locale | zh_CN Locale |
|---|---|---|---|
| [NSNumberFormatterNoStyle](style/none.md) | 1235 | 1235 | 1235 |
| [NSNumberFormatterDecimalStyle](style/decimal.md) | 1,234.568 | 1 234,568 | 1,234.568 |
| [NSNumberFormatterPercentStyle](style/percent.md) | 12% | 12 % | 12% |
| [NSNumberFormatterScientificStyle](style/scientific.md) | 1.2345678E3 | 1,2345678E3 | 1.2345678E3 |
| [NSNumberFormatterSpellOutStyle](style/spellout.md) | one hundred twenty-three | cent vingt-trois | 一百二十三 |
| [NSNumberFormatterOrdinalStyle](style/ordinal.md) | 3rd | 3e | 第3 |
| [NSNumberFormatterCurrencyStyle](style/currency.md) | $1,234.57 | 1 234,57 € | ￥1,234.57 |
| [NSNumberFormatterCurrencyAccountingStyle](style/currencyaccounting.md) | ($1,234.57) | (1 234,57 €) | (￥1,234.57) |
| [NSNumberFormatterCurrencyISOCodeStyle](style/currencyisocode.md) | USD1,234.57 | 1 234,57 EUR | CNY1,234.57 |
| [NSNumberFormatterCurrencyPluralStyle](style/currencyplural.md) | 1,234.57 US dollars | 1 234,57 euros | 1,234.57人民币 |

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Formatting Styles

- [NSNumberFormatterNoStyle](style/none.md) — An integer representation.
- [NSNumberFormatterDecimalStyle](style/decimal.md) — A decimal style format.
- [NSNumberFormatterPercentStyle](style/percent.md) — A percent style format.
- [NSNumberFormatterScientificStyle](style/scientific.md) — A scientific style format.
- [NSNumberFormatterSpellOutStyle](style/spellout.md) — A style format in which numbers are spelled out in the language defined by the number formatter locale.
- [NSNumberFormatterOrdinalStyle](style/ordinal.md) — An ordinal style format.
- [NSNumberFormatterCurrencyStyle](style/currency.md) — A currency style format that uses the currency symbol defined by the number formatter locale.
- [NSNumberFormatterCurrencyAccountingStyle](style/currencyaccounting.md) — An accounting currency style format that uses the currency symbol defined by the number formatter locale.
- [NSNumberFormatterCurrencyISOCodeStyle](style/currencyisocode.md) — A currency style format that uses the ISO 4217 currency code defined by the number formatter locale.
- [NSNumberFormatterCurrencyPluralStyle](style/currencyplural.md) — A currency style format that uses the pluralized denomination defined by the number formatter locale.

### Initializers

- [init(rawValue:)](<style/init(rawvalue_).md>)

## See Also

### Constants

- [Behavior](behavior.md) — These constants specify the behavior of a number formatter. These constants are returned by the [+ defaultFormatterBehavior](<defaultformatterbehavior().md>) class method and the [formatterBehavior](formatterbehavior.md) property.
- [PadPosition](padposition.md) — These constants are used to specify how numbers should be padded. These constants are used by the [paddingPosition](paddingposition.md) property.
- [RoundingMode](roundingmode-swift.enum.md) — These constants are used to specify how numbers should be rounded. These constants are used by the [roundingMode](roundingmode-swift.property.md) property.
