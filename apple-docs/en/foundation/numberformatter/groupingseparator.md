---
title: groupingSeparator
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/groupingseparator
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/groupingseparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/groupingseparator.json'
content_hash: 'sha256:642c0e9983074079'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# groupingSeparator

<sub>Instance Property</sub>

The string used by the receiver for a grouping separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var groupingSeparator: String! { get set }
```

## Discussion

For example, the grouping separator used in the United States is the comma (“10,000”) whereas in France it is the space (“10 000”).

## See Also

### Configuring Separators and Grouping Size

- [usesGroupingSeparator](usesgroupingseparator.md) — Determines whether the receiver displays the group separator.
- [thousandSeparator](thousandseparator.md) — The character the receiver uses as a thousand separator.
- [hasThousandSeparators](hasthousandseparators.md) — Determines whether the receiver uses thousand separators.
- [decimalSeparator](decimalseparator.md) — The character the receiver uses as a decimal separator.
- [alwaysShowsDecimalSeparator](alwaysshowsdecimalseparator.md) — Determines whether the receiver always shows the decimal separator, even for integer numbers.
- [currencyDecimalSeparator](currencydecimalseparator.md) — The string used by the receiver as a currency decimal separator.
- [groupingSize](groupingsize.md) — The grouping size of the receiver.
- [secondaryGroupingSize](secondarygroupingsize.md) — The secondary grouping size of the receiver.
