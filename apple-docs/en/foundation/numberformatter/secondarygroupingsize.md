---
title: secondaryGroupingSize
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/secondarygroupingsize
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/secondarygroupingsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/secondarygroupingsize.json'
content_hash: 'sha256:5b2cc1efc2e0a690'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# secondaryGroupingSize

<sub>Instance Property</sub>

The secondary grouping size of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var secondaryGroupingSize: Int { get set }
```

## Discussion

Some locales allow the specification of another grouping size for larger numbers. For example, some locales may represent a number such as 61, 242, 378.46 (as in the United States) as 6,12,42,378.46. In this case, the secondary grouping size (covering the groups of digits furthest from the decimal point) is 2.

## See Also

### Configuring Separators and Grouping Size

- [groupingSeparator](groupingseparator.md) — The string used by the receiver for a grouping separator.
- [usesGroupingSeparator](usesgroupingseparator.md) — Determines whether the receiver displays the group separator.
- [thousandSeparator](thousandseparator.md) — The character the receiver uses as a thousand separator.
- [hasThousandSeparators](hasthousandseparators.md) — Determines whether the receiver uses thousand separators.
- [decimalSeparator](decimalseparator.md) — The character the receiver uses as a decimal separator.
- [alwaysShowsDecimalSeparator](alwaysshowsdecimalseparator.md) — Determines whether the receiver always shows the decimal separator, even for integer numbers.
- [currencyDecimalSeparator](currencydecimalseparator.md) — The string used by the receiver as a currency decimal separator.
- [groupingSize](groupingsize.md) — The grouping size of the receiver.
