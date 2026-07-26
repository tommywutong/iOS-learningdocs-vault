---
title: SKProductDiscount.PaymentMode.payUpFront
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductdiscount/paymentmode-swift.enum/payupfront
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum/payupfront'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount/paymentmode-swift.enum/payupfront.json'
content_hash: 'sha256:bcac26ea9a84e066'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKProductDiscount](../../skproductdiscount.md) · [PaymentMode](../paymentmode-swift.enum.md)

# SKProductDiscount.PaymentMode.payUpFront

<sub>Case</sub>

A constant that indicates that the system applies the product discount up front.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.PaymentMode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case payUpFront
```

## Discussion

With a pay up front payment mode, users pay the discounted price one time, and receive the product for duration of the discount period.

![Example of a subscription timeline with a pay up front payment mode. The introductory price is billed one time.](../../../../../attachments/d4efc45f4203f1875f488fa0f304656f/media-2942133@2x.png)

## See Also

### Discount Price Payment Modes

- [SKProductDiscountPaymentModePayAsYouGo](payasyougo.md) — A constant that indicates a product discount that applies over a single billing period or multiple billing periods. _(deprecated)_
- [SKProductDiscountPaymentModeFreeTrial](freetrial.md) — A constant that indicates that the payment mode is a free trial. _(deprecated)_
