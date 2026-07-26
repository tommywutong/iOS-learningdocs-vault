---
title: currency
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/currency
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/currency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/currency.json'
content_hash: 'sha256:5c03280984db4f5e'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# currency

<sub>Instance Property</sub>

The currency of the subscription’s renewal price.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.0, macOS 15.0, tvOS 18.0, watchOS 11.0, visionOS 2.0)
var currency: Locale.Currency? { get }
```

## Discussion

The [currency](currency.md) value applies to the product’s [renewalPrice](renewalprice.md) instance.

> [!important] Important
> For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [Download financial reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [Overview of reporting tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use [currency](currency.md) to infer the storefront. Use the [storefront](../../../transaction/storefront.md) value in the transaction instead.

To access the renewal price currency on systems earlier than iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9, use [currencyCode](currencycode.md).

## See Also

### Getting the renewal price and currency

- [renewalPrice](renewalprice.md) — The renewal price of the auto-renewable subscription that renews at the next billing period.
