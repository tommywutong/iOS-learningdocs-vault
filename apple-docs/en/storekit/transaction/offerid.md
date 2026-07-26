---
title: offerID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（17.2 起废弃）, iPadOS 15.0+（17.2 起废弃）, macOS 12.0+（14.2 起废弃）, tvOS 15.0+（17.2 起废弃）, visionOS 1.0+（1.1 起废弃）, watchOS 8.0+（10.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/transaction/offerid
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offerid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offerid.json'
content_hash: 'sha256:b71ee6f096a7552b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# offerID

<sub>Instance Property</sub>

A string that identifies an offer applied to the current subscription.

> [!warning] Deprecated
> Use [offer](offer-swift.property.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var offerID: String? { get }
```

## Discussion

This value is `nil` if there isn’t an offer, or if the offer type is [introductory](offertype-swift.struct/introductory.md).

If the offer type is [promotional](offertype-swift.struct/promotional.md), this value contains the promotional offer identifier you set up in App Store Connect. For more information about promotional offers, see [Set up promotional offers for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev16dfca448).

If the offer type is [code](offertype-swift.struct/code.md), this value contains the reference name of the offer code you set up in App Store Connect. For more information about offer codes, see [Set up offer codes](https://help.apple.com/app-store-connect/#/dev6a098e4b1).

## See Also

### Deprecated

- [currencyCode](currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [environmentStringRepresentation](environmentstringrepresentation.md) — A string representation of the server environment. _(deprecated)_
- [offerPaymentModeStringRepresentation](offerpaymentmodestringrepresentation.md) — The string representation of the payment mode for a subscription offer. _(deprecated)_
- [offerType](offertype-swift.property.md) — The subscription offer type for the current subscription period. _(deprecated)_
- [reasonStringRepresentation](reasonstringrepresentation.md) — The string representation of the transaction reason. _(deprecated)_
- [storefrontCountryCode](storefrontcountrycode.md) — The three-letter code that represents the country or region associated with the App Store storefront of the purchase. _(deprecated)_
