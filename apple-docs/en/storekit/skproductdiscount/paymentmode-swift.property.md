---
title: paymentMode
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductdiscount/paymentmode-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount/paymentmode-swift.property.json'
content_hash: 'sha256:095ebfebc6171d14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductDiscount](../skproductdiscount.md)

# paymentMode

<sub>Instance Property</sub>

The payment mode for this product discount.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.paymentMode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var paymentMode: SKProductDiscount.PaymentMode { get }
```

## Discussion

The payment mode indicates how the product discount [price](price.md) is charged:

- One or more times, for [SKProductDiscountPaymentModePayAsYouGo](paymentmode-swift.enum/payasyougo.md) mode
- Once in advance, for [SKProductDiscountPaymentModePayUpFront](paymentmode-swift.enum/payupfront.md) mode
- No initial charge, for [SKProductDiscountPaymentModeFreeTrial](paymentmode-swift.enum/freetrial.md) mode.

Use the payment mode to display an accurate description of the product discount in your UI. For design guidance, see [Human Interface Guidelines \> In-App Purchase](https://developer.apple.com/ios/human-interface-guidelines/technologies/in-app-purchase/).

## See Also

### Getting Price and Payment Mode

- [price](price.md) — The discount price of the product in the local currency. _(deprecated)_
- [priceLocale](pricelocale.md) — The locale used to format the discount price of the product. _(deprecated)_
- [PaymentMode](paymentmode-swift.enum.md) — Values representing the payment modes for a product discount. _(deprecated)_
