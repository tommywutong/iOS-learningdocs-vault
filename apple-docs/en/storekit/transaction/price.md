---
title: price
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/price
source_url: 'https://developer.apple.com/documentation/storekit/transaction/price'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/price.json'
content_hash: 'sha256:279111d3d94eeeab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# price

<sub>Instance Property</sub>

The price of the in-app purchase that the system records in the transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2, visionOS 1.1)
var price: Decimal? { get }
```

## Discussion

This value represents the price of the in-app purchase, in units of the [currency](currency.md), that the system records in the transaction. The [price](price.md) value reflects all of the following:

- The price you configured in App Store Connect, which the system records on the purchase date ([purchaseDate](purchasedate.md)).
- The discount from a subscription offer in the [offer](offer-swift.property.md) property, if the transaction includes an offer.
- The [purchasedQuantity](purchasedquantity.md) of a consumable in-app purchase. The price value shows the total amount of the transaction for the quantity that the customer purchased.

> [!important] Important
> For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [Download financial reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [Overview of reporting tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

The decoded payloads of [jwsRepresentation](../verificationresult/jwsrepresentation-21vgo.md) and the [JWSTransaction](../../appstoreserverapi/jwstransaction.md) strings from the App Store server APIs contain [price](../../appstoreserverapi/price.md) fields specified in _milliunits_ of the currency. StoreKit represents the [price](price.md) value in _units_ of the currency. Take care not to confuse these two representations when working with both APIs.

You configure prices in App Store Connect. For more information, see [Set a price for an in-app purchase](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

### Getting the product price and currency

- [currency](currency.md) — The currency of the price of the product.
