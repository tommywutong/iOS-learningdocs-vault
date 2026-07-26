---
title: Transaction.Offer
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.2+, iPadOS 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/offer-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offer-swift.struct.json'
content_hash: 'sha256:13c157648fa6b34d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# Transaction.Offer

<sub>Structure</sub>

Discounts or promotions that apply to a transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Offer
```

## Overview

You set up offers for auto-renewable subscriptions and other In-App Purchase types in App Store Connect. If a customer redeems an offer, it appears in the [offer](offer-swift.property.md) property of the transaction. For auto-renewable subscriptions, if the offer applies to one or more renewal periods, it also appears in the [offer](../product/subscriptioninfo/renewalinfo/offer.md) property of [RenewalInfo](../product/subscriptioninfo/renewalinfo.md).

For more information on configuring the various offers in App Store Connect, see:

- [Create offer codes for In-App Purchases](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases)
- [Providing subscription offers](https://developer.apple.com/app-store/subscriptions/#providing-subscription-offers).
- [Set up offer codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes/)
- [Set up introductory offers for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions)
- [Set up promotional offers for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions)
- [Set up win-back offers](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers)

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting offer details

- [id](offer-swift.struct/id.md) — A string that identifies an offer that applies to the transaction.
- [type](offer-swift.struct/type.md) — The type of offer that applies to the transaction.
- [OfferType](offertype-swift.struct.md) — The types of offers that apply to a transaction.
- [paymentMode](offer-swift.struct/paymentmode-swift.property.md) — The payment mode for a subscription offer on an auto-renewable subscription that applies to the transaction.
- [PaymentMode](offer-swift.struct/paymentmode-swift.struct.md) — The payment modes for offers that apply to a transaction.
- [period](offer-swift.struct/period.md) — The duration of the offer applied to a transaction.

## See Also

### Getting offers

- [offer](../product/subscriptioninfo/renewalinfo/offer.md) — A subscription offer that applies to the transaction at the next renewal period.
- [eligibleWinBackOfferIDs](../product/subscriptioninfo/renewalinfo/eligiblewinbackofferids.md) — An array of strings that represent identifiers of win-back offers that the customer is eligible to redeem, sorted with the best offers first.
