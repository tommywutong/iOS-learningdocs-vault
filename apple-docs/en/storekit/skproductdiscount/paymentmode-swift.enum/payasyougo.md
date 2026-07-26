---
title: SKProductDiscount.PaymentMode.payAsYouGo
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductdiscount/paymentmode-swift.enum/payasyougo
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum/payasyougo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount/paymentmode-swift.enum/payasyougo.json'
content_hash: 'sha256:3d569dff5f616a51'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKProductDiscount](../../skproductdiscount.md) · [PaymentMode](../paymentmode-swift.enum.md)

# SKProductDiscount.PaymentMode.payAsYouGo

<sub>Case</sub>

A constant that indicates a product discount that applies over a single billing period or multiple billing periods.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.PaymentMode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case payAsYouGo
```

## Discussion

With a pay as you go payment mode, users pay the discounted price at each billing period during the discount period.

![Example of a subscription timeline with a pay as you go payment mode. The  introductory price is billed three times.](../../../../../attachments/cdf7424c589eb68fe7962e3c551ebba1/media-2942132@2x.png)

## See Also

### Discount Price Payment Modes

- [SKProductDiscountPaymentModePayUpFront](payupfront.md) — A constant that indicates that the system applies the product discount up front. _(deprecated)_
- [SKProductDiscountPaymentModeFreeTrial](freetrial.md) — A constant that indicates that the payment mode is a free trial. _(deprecated)_
