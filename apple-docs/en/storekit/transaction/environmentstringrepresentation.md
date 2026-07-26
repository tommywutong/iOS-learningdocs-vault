---
title: environmentStringRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（16.0 起废弃）, iPadOS 15.0+（16.0 起废弃）, Mac Catalyst 15.0+（16.0 起废弃）, macOS 12.0+（13.0 起废弃）, tvOS 15.0+（16.0 起废弃）, watchOS 8.0+（9.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/transaction/environmentstringrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/transaction/environmentstringrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/environmentstringrepresentation.json'
content_hash: 'sha256:9993b25e23d9d31a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# environmentStringRepresentation

<sub>Instance Property</sub>

A string representation of the server environment.

> [!warning] Deprecated
> Use [environment](environment.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
var environmentStringRepresentation: String { get }
```

## See Also

### Deprecated

- [currencyCode](currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [offerID](offerid.md) — A string that identifies an offer applied to the current subscription. _(deprecated)_
- [offerPaymentModeStringRepresentation](offerpaymentmodestringrepresentation.md) — The string representation of the payment mode for a subscription offer. _(deprecated)_
- [offerType](offertype-swift.property.md) — The subscription offer type for the current subscription period. _(deprecated)_
- [reasonStringRepresentation](reasonstringrepresentation.md) — The string representation of the transaction reason. _(deprecated)_
- [storefrontCountryCode](storefrontcountrycode.md) — The three-letter code that represents the country or region associated with the App Store storefront of the purchase. _(deprecated)_
