---
title: paymentMode
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.2+, iPadOS 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.property.json'
content_hash: 'sha256:b94ab79898b4f938'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Transaction](../../transaction.md) · [Offer](../offer-swift.struct.md)

# paymentMode

<sub>Instance Property</sub>

The payment mode for a subscription offer on an auto-renewable subscription that applies to the transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let paymentMode: Transaction.Offer.PaymentMode?
```

## Discussion

You set up subscription offers and determine the payment mode when you configure subscriptions in App Store Connect. For more information about the Free Trial ([freeTrial](paymentmode-swift.struct/freetrial.md)), Pay As You Go ([payAsYouGo](paymentmode-swift.struct/payasyougo.md)), and Pay Up Front ([payUpFront](paymentmode-swift.struct/payupfront.md)) payment modes, see [Pricing and availability](https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability).

## See Also

### Getting offer details

- [id](id.md) — A string that identifies an offer that applies to the transaction.
- [type](type.md) — The type of offer that applies to the transaction.
- [OfferType](../offertype-swift.struct.md) — The types of offers that apply to a transaction.
- [PaymentMode](paymentmode-swift.struct.md) — The payment modes for offers that apply to a transaction.
- [period](period.md) — The duration of the offer applied to a transaction.
