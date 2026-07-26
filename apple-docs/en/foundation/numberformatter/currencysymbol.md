---
title: currencySymbol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/currencysymbol
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/currencysymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/currencysymbol.json'
content_hash: 'sha256:940994938288cd04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# currencySymbol

<sub>Instance Property</sub>

The string used by the receiver as a local currency symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currencySymbol: String! { get set }
```

## Discussion

A region typically has a local currency symbol and an international currency symbol. The local symbol is used within the region, while the international currency symbol is used in international contexts to specify that region’s currency unambiguously. The local currency symbol is often represented by a Unicode code point.

## See Also

### Configuring the Format of Currency

- [currencyCode](currencycode.md) — The receiver’s currency code.
- [internationalCurrencySymbol](internationalcurrencysymbol.md) — The international currency symbol used by the receiver.
- [currencyGroupingSeparator](currencygroupingseparator.md) — The currency grouping separator for the receiver.
