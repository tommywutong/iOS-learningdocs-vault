---
title: Number Formatter Styles
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/number-formatter-styles
source_url: 'https://developer.apple.com/documentation/corefoundation/number-formatter-styles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/number-formatter-styles.json'
content_hash: 'sha256:418e76d15b671fb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFNumberFormatter](cfnumberformatter.md)

# Number Formatter Styles

<sub>API Collection</sub>

Predefined number format styles.

## Overview

The format for these number styles is not exact because they depend on the locale, user preference settings, and operating system version. Do not use these constants if you want an exact format (for example, if you are parsing data in a given format). In general, however, you are encouraged to use these styles to accommodate user preferences.

## Topics

### Constants

- [kCFNumberFormatterNoStyle](cfnumberformatterstyle/nostyle.md) — Specifies no style.
- [kCFNumberFormatterDecimalStyle](cfnumberformatterstyle/decimalstyle.md) — Specifies a decimal style format.
- [kCFNumberFormatterCurrencyStyle](cfnumberformatterstyle/currencystyle.md) — Specifies a currency style format.
- [kCFNumberFormatterPercentStyle](cfnumberformatterstyle/percentstyle.md) — Specifies a percent style format.
- [kCFNumberFormatterScientificStyle](cfnumberformatterstyle/scientificstyle.md) — Specifies a scientific style format.
- [kCFNumberFormatterSpellOutStyle](cfnumberformatterstyle/spelloutstyle.md) — Specifies a spelled out format.

## See Also

### Constants

- [Number Formatter Property Keys](number-formatter-property-keys.md) — The keys used in key-value pairs to specify the value of number formatter properties.
- [Number Format Options](number_format_options.md) — These constants are used to specify how numbers should be parsed.
- [CFNumberFormatterRoundingMode](cfnumberformatterroundingmode.md) — These constants are used to specify how numbers should be rounded.
- [Padding Positions](padding-positions.md) — These constants are used to specify how numbers should be padded.
