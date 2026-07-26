---
title: paymentDiscount
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+（18.0 起废弃）, iPadOS 12.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14.4+（15.0 起废弃）, tvOS 12.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpayment/paymentdiscount
source_url: 'https://developer.apple.com/documentation/storekit/skpayment/paymentdiscount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpayment/paymentdiscount.json'
content_hash: 'sha256:da15cd6c5af4316c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPayment](../skpayment.md)

# paymentDiscount

<sub>Instance Property</sub>

The details of the discount offer to apply to the payment.

> [!warning] Deprecated
> Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var paymentDiscount: SKPaymentDiscount? { get }
```

## See Also

### Getting Discount Details

- [SKPaymentDiscount](../skpaymentdiscount.md) — The signed discount to apply to a payment. _(deprecated)_
