---
title: currency
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/currency
source_url: 'https://developer.apple.com/documentation/storekit/transaction/currency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/currency.json'
content_hash: 'sha256:5f8b7a83489fe12e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# currency

<sub>Instance Property</sub>

The currency of the price of the product.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2, visionOS 1.1)
var currency: Locale.Currency? { get }
```

## Discussion

The [currency](currency.md) property represents the currency of the product’s [price](price.md) that the system records at the time of purchase.

> [!important] Important
> For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [Download financial reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [Overview of reporting tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use [currency](currency.md) to infer the storefront. Use the [storefront](storefront.md) value in the transaction instead.

To access the transaction’s currency on systems earlier than iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9, use [currencyCode](../product/subscriptioninfo/renewalinfo/currencycode.md).

## See Also

### Getting the product price and currency

- [price](price.md) — The price of the in-app purchase that the system records in the transaction.
