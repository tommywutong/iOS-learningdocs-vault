---
title: currencyCode
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（16.0 起废弃）, iPadOS 15.0+（16.0 起废弃）, macOS 12.0+（13.0 起废弃）, tvOS 15.0+（16.0 起废弃）, watchOS 8.0+（9.0 起废弃）]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/currencycode
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/currencycode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/currencycode.json'
content_hash: 'sha256:8345560ef4ab9ae7'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# currencyCode

<sub>Instance Property</sub>

The three-letter ISO 4217 currency code for the price of the product.

> [!warning] Deprecated
> Use [currency](currency.md) instead. To get the currency code as a string, use the [identifier](../../../../foundation/locale/currency-swift.struct/identifier.md) property of [currency](currency.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0)
var currencyCode: String? { get }
```

## Discussion

Use [currencyCode](currencycode.md) to access the currency of the price on systems earlier than iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9. Otherwise, use [currency](currency.md).

> [!important] Important
> For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [Download financial reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [Overview of reporting tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use [currencyCode](../../../transaction/currencycode.md) to infer the storefront. Use the [storefront](../../../transaction/storefront.md) value in the transaction instead.

For more information on how you set prices, see [Set a price for an in-app purchase](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

### Deprecated

- [environmentStringRepresentation](environmentstringrepresentation.md) — The string representation of the server environment that signs the renewal information for an auto-renewable subscription. _(deprecated)_
- [offerID](offerid.md) — A string that identifies an offer that applies to the next subscription period. _(deprecated)_
- [offerType](offertype.md) — The subscription offer type for the next subscription period. _(deprecated)_
- [offerPaymentModeStringRepresentation](offerpaymentmodestringrepresentation.md) _(deprecated)_
- [offerPeriodStringRepresentation](offerperiodstringrepresentation.md) — The string representation of the subscription offer period applied to the next billing period. _(deprecated)_
