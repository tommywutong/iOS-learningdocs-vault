---
title: currencyCode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/currencycode
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/currencycode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/currencycode.json'
content_hash: 'sha256:09e26a5a87cf31fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# currencyCode

<sub>Instance Property</sub>

The receiver’s currency code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currencyCode: String! { get set }
```

## Discussion

A currency code is a three-letter code that is, in most cases, composed of a region’s two-character Internet region code plus an extra character to denote the currency unit. For example, the currency code for the Australian dollar is “AUD”. Currency codes are based on the ISO 4217 standard.

## See Also

### Configuring the Format of Currency

- [currencySymbol](currencysymbol.md) — The string used by the receiver as a local currency symbol.
- [internationalCurrencySymbol](internationalcurrencysymbol.md) — The international currency symbol used by the receiver.
- [currencyGroupingSeparator](currencygroupingseparator.md) — The currency grouping separator for the receiver.
