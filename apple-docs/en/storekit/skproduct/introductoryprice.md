---
title: introductoryPrice
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/introductoryprice
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/introductoryprice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/introductoryprice.json'
content_hash: 'sha256:f34aa835a8bd5a79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# introductoryPrice

<sub>Instance Property</sub>

The object containing introductory price information for the product.

> [!warning] Deprecated
> Use Product.subscription.introductionaryOffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var introductoryPrice: SKProductDiscount? { get }
```

## Discussion

If you’ve set up introductory prices in App Store Connect, the introductory price property will be populated. This property is `nil` if the product has no introductory price.

Before displaying UI that offers the introductory price, you must first determine if the user is eligible to receive it. See [Implementing introductory offers in your app](../implementing-introductory-offers-in-your-app.md) for information on determining eligibility and displaying introductory prices.

## See Also

### Getting Pricing Information

- [price](price.md) — The cost of the product in the local currency. _(deprecated)_
- [priceLocale](pricelocale.md) — The locale used to format the price of the product. _(deprecated)_
- [discounts](discounts.md) — An array of subscription offers available for the auto-renewable subscription. _(deprecated)_
- [SKProductDiscount](../skproductdiscount.md) — The details of an introductory offer or a promotional offer for an auto-renewable subscription. _(deprecated)_
