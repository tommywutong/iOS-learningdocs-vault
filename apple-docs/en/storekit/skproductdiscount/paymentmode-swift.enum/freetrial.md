---
title: SKProductDiscount.PaymentMode.freeTrial
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductdiscount/paymentmode-swift.enum/freetrial
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum/freetrial'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount/paymentmode-swift.enum/freetrial.json'
content_hash: 'sha256:f354c1b2ece459b8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKProductDiscount](../../skproductdiscount.md) · [PaymentMode](../paymentmode-swift.enum.md)

# SKProductDiscount.PaymentMode.freeTrial

<sub>Case</sub>

A constant that indicates that the payment mode is a free trial.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.PaymentMode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case freeTrial
```

## Discussion

With a free trial payment mode, the price is 0, so users pay nothing during the discount period.

![](../../../../../attachments/0ee556ad1cee3517fb03233a341235b3/media-2942195@2x.png)

<sub>Example of a subscription timeline starting with a free trial. After the free introductory period, the subscription renews at regular price. </sub>

## See Also

### Discount Price Payment Modes

- [SKProductDiscountPaymentModePayAsYouGo](payasyougo.md) — A constant that indicates a product discount that applies over a single billing period or multiple billing periods. _(deprecated)_
- [SKProductDiscountPaymentModePayUpFront](payupfront.md) — A constant that indicates that the system applies the product discount up front. _(deprecated)_
