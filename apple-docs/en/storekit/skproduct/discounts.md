---
title: discounts
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+（18.0 起废弃）, iPadOS 12.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14.4+（15.0 起废弃）, tvOS 12.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/discounts
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/discounts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/discounts.json'
content_hash: 'sha256:646439b270ec52fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# discounts

<sub>Instance Property</sub>

An array of subscription offers available for the auto-renewable subscription.

> [!warning] Deprecated
> Use Product.subscription.promotionalOffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var discounts: [SKProductDiscount] { get }
```

## Discussion

The [discounts](discounts.md) array contains all of the introductory offers and promotional offers that you set up in App Store Connect for this subscription ([productIdentifier](productidentifier.md)).  It’s up to the logic in your app to decide which offer to present to the user.

For more information about offers, see [Implementing promotional offers in your app](../implementing-promotional-offers-in-your-app.md), and [Implementing introductory offers in your app](../implementing-introductory-offers-in-your-app.md).

## See Also

### Getting Pricing Information

- [price](price.md) — The cost of the product in the local currency. _(deprecated)_
- [priceLocale](pricelocale.md) — The locale used to format the price of the product. _(deprecated)_
- [introductoryPrice](introductoryprice.md) — The object containing introductory price information for the product. _(deprecated)_
- [SKProductDiscount](../skproductdiscount.md) — The details of an introductory offer or a promotional offer for an auto-renewable subscription. _(deprecated)_
