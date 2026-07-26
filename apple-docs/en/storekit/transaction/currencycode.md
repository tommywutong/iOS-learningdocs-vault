---
title: currencyCode
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（16.0 起废弃）, iPadOS 15.0+（16.0 起废弃）, macOS 12.0+（13.0 起废弃）, tvOS 15.0+（16.0 起废弃）, visionOS 1.0+（1.1 起废弃）, watchOS 8.0+（9.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/transaction/currencycode
source_url: 'https://developer.apple.com/documentation/storekit/transaction/currencycode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/currencycode.json'
content_hash: 'sha256:2521918d3a0b026e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# currencyCode

<sub>Instance Property</sub>

The three-letter ISO 4217 currency code for the price of the product.

> [!warning] Deprecated
> Use [currency](currency.md) instead. To get the currency code as a string, use the [identifier](../../foundation/locale/currency-swift.struct/identifier.md) property of [currency](../product/subscriptioninfo/renewalinfo/currency.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0)
var currencyCode: String? { get }
```

## Discussion

The [currencyCode](currencycode.md) property contains an ISO 4217 alpha-3 string that represents the currency of the price of the product. Use [currencyCode](../product/subscriptioninfo/renewalinfo/currencycode.md) to access the currency of the price on systems earlier than iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9. Otherwise, use [currency](../product/subscriptioninfo/renewalinfo/currency.md).

> [!important] Important
> For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [Download financial reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [Overview of reporting tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use [currencyCode](currencycode.md) to infer the storefront. Use the [storefront](storefront.md) value in the transaction instead.

For more information on how you set prices, see [Set a price for an in-app purchase](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

### Deprecated

- [environmentStringRepresentation](environmentstringrepresentation.md) — A string representation of the server environment. _(deprecated)_
- [offerID](offerid.md) — A string that identifies an offer applied to the current subscription. _(deprecated)_
- [offerPaymentModeStringRepresentation](offerpaymentmodestringrepresentation.md) — The string representation of the payment mode for a subscription offer. _(deprecated)_
- [offerType](offertype-swift.property.md) — The subscription offer type for the current subscription period. _(deprecated)_
- [reasonStringRepresentation](reasonstringrepresentation.md) — The string representation of the transaction reason. _(deprecated)_
- [storefrontCountryCode](storefrontcountrycode.md) — The three-letter code that represents the country or region associated with the App Store storefront of the purchase. _(deprecated)_
