---
title: internationalCurrencySymbol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/internationalcurrencysymbol
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/internationalcurrencysymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/internationalcurrencysymbol.json'
content_hash: 'sha256:39469eef8bceaf5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# internationalCurrencySymbol

<sub>Instance Property</sub>

The international currency symbol used by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var internationalCurrencySymbol: String! { get set }
```

## Discussion

A region typically has a local currency symbol and an international currency symbol. The local symbol is used within the region, while the international currency symbol is used in international contexts to specify that region’s currency unambiguously. The international currency symbol is often represented by a Unicode code point.

## See Also

### Configuring the Format of Currency

- [currencySymbol](currencysymbol.md) — The string used by the receiver as a local currency symbol.
- [currencyCode](currencycode.md) — The receiver’s currency code.
- [currencyGroupingSeparator](currencygroupingseparator.md) — The currency grouping separator for the receiver.
