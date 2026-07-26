---
title: type
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.2+, iPadOS 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/offer-swift.struct/type
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offer-swift.struct/type.json'
content_hash: 'sha256:ee4250e71d2ffe45'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Transaction](../../transaction.md) · [Offer](../offer-swift.struct.md)

# type

<sub>Instance Property</sub>

The type of offer that applies to the transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let type: Transaction.OfferType
```

## Discussion

See [OfferType](../offertype-swift.struct.md) for the complete list of offer types.

For more information about introductory offers, see [Set an introductory offer for an auto-renewable subscription](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions).

For more information about promotional offers, see [Set up promotional offers for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions).

For more information about offer codes, see [Set up offer codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes).

## See Also

### Getting offer details

- [id](id.md) — A string that identifies an offer that applies to the transaction.
- [OfferType](../offertype-swift.struct.md) — The types of offers that apply to a transaction.
- [paymentMode](paymentmode-swift.property.md) — The payment mode for a subscription offer on an auto-renewable subscription that applies to the transaction.
- [PaymentMode](paymentmode-swift.struct.md) — The payment modes for offers that apply to a transaction.
- [period](period.md) — The duration of the offer applied to a transaction.
