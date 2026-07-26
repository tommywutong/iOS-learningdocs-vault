---
title: offerPaymentModeStringRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（17.2 起废弃）, iPadOS 15.0+（17.2 起废弃）, macOS 12.0+（14.2 起废弃）, tvOS 15.0+（17.2 起废弃）, visionOS 1.0+（1.1 起废弃）, watchOS 8.0+（10.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/transaction/offerpaymentmodestringrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offerpaymentmodestringrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offerpaymentmodestringrepresentation.json'
content_hash: 'sha256:5bdac019d850b9b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# offerPaymentModeStringRepresentation

<sub>Instance Property</sub>

The string representation of the payment mode for a subscription offer.

> [!warning] Deprecated
> Use `paymentMode` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2)
var offerPaymentModeStringRepresentation: String? { get }
```

## See Also

### Deprecated

- [currencyCode](currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [environmentStringRepresentation](environmentstringrepresentation.md) — A string representation of the server environment. _(deprecated)_
- [offerID](offerid.md) — A string that identifies an offer applied to the current subscription. _(deprecated)_
- [offerType](offertype-swift.property.md) — The subscription offer type for the current subscription period. _(deprecated)_
- [reasonStringRepresentation](reasonstringrepresentation.md) — The string representation of the transaction reason. _(deprecated)_
- [storefrontCountryCode](storefrontcountrycode.md) — The three-letter code that represents the country or region associated with the App Store storefront of the purchase. _(deprecated)_
