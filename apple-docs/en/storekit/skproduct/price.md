---
title: price
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/price
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/price'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/price.json'
content_hash: 'sha256:50f8c32a5bbacbfc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# price

<sub>Instance Property</sub>

The cost of the product in the local currency.

> [!warning] Deprecated
> Use Product.displayPrice.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var price: NSDecimalNumber { get }
```

## Discussion

Your app can format the price using a number formatter, as shown in the following sample code:

**Swift**

```swift
let numberFormatter = NumberFormatter()
numberFormatter.numberStyle = .currency
numberFormatter.locale = product.priceLocale
let formattedString = numberFormatter.string(from: product.price)
```

**Objective-C**

```objc
NSNumberFormatter *numberFormatter = [[NSNumberFormatter alloc] init];
[numberFormatter setFormatterBehavior:NSNumberFormatterBehavior10_4];
[numberFormatter setNumberStyle:NSNumberFormatterCurrencyStyle];
[numberFormatter setLocale:product.priceLocale];
NSString *formattedString = [numberFormatter stringFromNumber:product.price];
```

## See Also

### Getting Pricing Information

- [priceLocale](pricelocale.md) — The locale used to format the price of the product. _(deprecated)_
- [introductoryPrice](introductoryprice.md) — The object containing introductory price information for the product. _(deprecated)_
- [discounts](discounts.md) — An array of subscription offers available for the auto-renewable subscription. _(deprecated)_
- [SKProductDiscount](../skproductdiscount.md) — The details of an introductory offer or a promotional offer for an auto-renewable subscription. _(deprecated)_
