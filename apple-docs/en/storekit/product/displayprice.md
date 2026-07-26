---
title: displayPrice
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/displayprice
source_url: 'https://developer.apple.com/documentation/storekit/product/displayprice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/displayprice.json'
content_hash: 'sha256:837c5c1ff5a74219'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# displayPrice

<sub>Instance Property</sub>

The localized string representation of the product price, suitable for display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let displayPrice: String
```

## Discussion

Use this string to display the price, formatted for the locale. The storefront that the user’s device is connected to determines the locale. For more information, see [Storefront](../storefront.md).

To perform arithmetic calculations with the price, use the [price](price.md) property instead.

## See Also

### Displaying a product description and price

- [displayName](displayname.md) — The localized display name of the product, if it exists.
- [description](description.md) — The localized description of the product.
- [price](price.md) — The decimal representation of the cost of the product, in local currency.
- [priceFormatStyle](priceformatstyle.md) — The format style for the numbers in the price of the product.
- [subscriptionPeriodFormatStyle](subscriptionperiodformatstyle.md) — The format style for the date components related to a subscription’s duration.
- [subscriptionPeriodUnitFormatStyle](subscriptionperiodunitformatstyle.md) — The format style for subscription period units, such as week, month, or year.
