---
title: offerType
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（17.2 起废弃）, iPadOS 15.0+（17.2 起废弃）, macOS 12.0+（14.2 起废弃）, tvOS 15.0+（17.2 起废弃）, visionOS 1.0+（1.1 起废弃）, watchOS 8.0+（10.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/transaction/offertype-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offertype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offertype-swift.property.json'
content_hash: 'sha256:656605db905f7176'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# offerType

<sub>Instance Property</sub>

The subscription offer type for the current subscription period.

> [!warning] Deprecated
> Use [offer](offer-swift.property.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var offerType: Transaction.OfferType? { get }
```

## Discussion

If this value is `nil`, there’s no offer applied.

## See Also

### Deprecated

- [currencyCode](currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [environmentStringRepresentation](environmentstringrepresentation.md) — A string representation of the server environment. _(deprecated)_
- [offerID](offerid.md) — A string that identifies an offer applied to the current subscription. _(deprecated)_
- [offerPaymentModeStringRepresentation](offerpaymentmodestringrepresentation.md) — The string representation of the payment mode for a subscription offer. _(deprecated)_
- [reasonStringRepresentation](reasonstringrepresentation.md) — The string representation of the transaction reason. _(deprecated)_
- [storefrontCountryCode](storefrontcountrycode.md) — The three-letter code that represents the country or region associated with the App Store storefront of the purchase. _(deprecated)_
