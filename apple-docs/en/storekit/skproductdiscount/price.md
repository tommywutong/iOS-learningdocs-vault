---
title: price
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductdiscount/price
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount/price'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount/price.json'
content_hash: 'sha256:da41c8a47575f488'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductDiscount](../skproductdiscount.md)

# price

<sub>Instance Property</sub>

The discount price of the product in the local currency.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.displayPrice.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var price: NSDecimalNumber { get }
```

## Discussion

Use the [priceLocale](pricelocale.md) to format the price.

## See Also

### Getting Price and Payment Mode

- [priceLocale](pricelocale.md) — The locale used to format the discount price of the product. _(deprecated)_
- [paymentMode](paymentmode-swift.property.md) — The payment mode for this product discount. _(deprecated)_
- [PaymentMode](paymentmode-swift.enum.md) — Values representing the payment modes for a product discount. _(deprecated)_
