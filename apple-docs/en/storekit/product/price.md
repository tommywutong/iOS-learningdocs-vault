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
doc_path: /documentation/storekit/product/price
source_url: 'https://developer.apple.com/documentation/storekit/product/price'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/price.json'
content_hash: 'sha256:2595ff561e7bf747'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# price

<sub>Instance Property</sub>

The decimal representation of the cost of the product, in local currency.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let price: Decimal
```

## Discussion

Use this property to perform arithmetic calculations with the price of the product. For a localized string representation of the price to display to customers, use the [displayPrice](displayprice.md) property instead.

## See Also

### Displaying a product description and price

- [displayName](displayname.md) — The localized display name of the product, if it exists.
- [description](description.md) — The localized description of the product.
- [displayPrice](displayprice.md) — The localized string representation of the product price, suitable for display.
- [priceFormatStyle](priceformatstyle.md) — The format style for the numbers in the price of the product.
- [subscriptionPeriodFormatStyle](subscriptionperiodformatstyle.md) — The format style for the date components related to a subscription’s duration.
- [subscriptionPeriodUnitFormatStyle](subscriptionperiodunitformatstyle.md) — The format style for subscription period units, such as week, month, or year.
