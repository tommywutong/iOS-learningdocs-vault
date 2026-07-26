---
title: thousandSeparator
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/thousandseparator
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/thousandseparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/thousandseparator.json'
content_hash: 'sha256:a3b645a2fabb7035'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# thousandSeparator

<sub>Instance Property</sub>

The character the receiver uses as a thousand separator.

<sub>macOS</sub>

```swift
var thousandSeparator: String! { get set }
```

## Discussion

If you don’t have thousand separators enabled through any other means (such as [format](format.md)), using this method enables them.

### Special Considerations

This method is for use with formatters using `NSNumberFormatterBehavior10_0` behavior.

## See Also

### Configuring Separators and Grouping Size

- [groupingSeparator](groupingseparator.md) — The string used by the receiver for a grouping separator.
- [usesGroupingSeparator](usesgroupingseparator.md) — Determines whether the receiver displays the group separator.
- [hasThousandSeparators](hasthousandseparators.md) — Determines whether the receiver uses thousand separators.
- [decimalSeparator](decimalseparator.md) — The character the receiver uses as a decimal separator.
- [alwaysShowsDecimalSeparator](alwaysshowsdecimalseparator.md) — Determines whether the receiver always shows the decimal separator, even for integer numbers.
- [currencyDecimalSeparator](currencydecimalseparator.md) — The string used by the receiver as a currency decimal separator.
- [groupingSize](groupingsize.md) — The grouping size of the receiver.
- [secondaryGroupingSize](secondarygroupingsize.md) — The secondary grouping size of the receiver.
