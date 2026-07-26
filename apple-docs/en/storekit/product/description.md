---
title: description
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/description
source_url: 'https://developer.apple.com/documentation/storekit/product/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/description.json'
content_hash: 'sha256:33e61b7da0bdf3d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# description

<sub>Instance Property</sub>

The localized description of the product.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let description: String
```

## Discussion

The storefront of the device determines the language of the [description](description.md), not the preferred language set on the device. For more information, see [Storefront](../storefront.md).

> [!note] Note
> When you create a new product in App Store Connect or in a StoreKit configuration file, you can test it before you add a product localization. The [description](description.md) value is an empty string until you add a localization. For more information on localizations, see [Add and remove localizations](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information#add-and-remove-localizations).

## See Also

### Displaying a product description and price

- [displayName](displayname.md) — The localized display name of the product, if it exists.
- [displayPrice](displayprice.md) — The localized string representation of the product price, suitable for display.
- [price](price.md) — The decimal representation of the cost of the product, in local currency.
- [priceFormatStyle](priceformatstyle.md) — The format style for the numbers in the price of the product.
- [subscriptionPeriodFormatStyle](subscriptionperiodformatstyle.md) — The format style for the date components related to a subscription’s duration.
- [subscriptionPeriodUnitFormatStyle](subscriptionperiodunitformatstyle.md) — The format style for subscription period units, such as week, month, or year.
