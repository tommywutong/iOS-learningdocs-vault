---
title: priceLocale
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/pricelocale
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/pricelocale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/pricelocale.json'
content_hash: 'sha256:ae1421cf0f2a8f45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# priceLocale

<sub>Instance Property</sub>

The locale used to format the price of the product.

> [!warning] Deprecated
> Use Product.displayPrice.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var priceLocale: Locale { get }
```

## Discussion

Use the locale to format the [price](price.md).

## See Also

### Getting Pricing Information

- [price](price.md) — The cost of the product in the local currency. _(deprecated)_
- [introductoryPrice](introductoryprice.md) — The object containing introductory price information for the product. _(deprecated)_
- [discounts](discounts.md) — An array of subscription offers available for the auto-renewable subscription. _(deprecated)_
- [SKProductDiscount](../skproductdiscount.md) — The details of an introductory offer or a promotional offer for an auto-renewable subscription. _(deprecated)_
