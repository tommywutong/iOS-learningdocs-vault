---
title: Product.SubscriptionOffer
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptionoffer
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionoffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionoffer.json'
content_hash: 'sha256:d248e1e3fcc16b89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# Product.SubscriptionOffer

<sub>Structure</sub>

Information about a subscription offer that you configure in App Store Connect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SubscriptionOffer
```

## Overview

You set up subscription offers, such as introductory offers and win-back offers, in App Store Connect.

For more information about subscription offers, see [Providing subscription offers](https://developer.apple.com/app-store/subscriptions/#providing-subscription-offers). For information about configuring the various types of subscription offers in App Store Connect, see:

- [Set up offer codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes/)
- [Set up introductory offers for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions)
- [Set up promotional offers for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions)
- [Set up win-back offers](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers)

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the subscription offer identifier

- [id](subscriptionoffer/id.md) — The offer identifier.

### Getting the subscription offer type

- [type](subscriptionoffer/type.md) — The type of subscription offer, which can be introductory, promotional, or win-back.
- [OfferType](subscriptionoffer/offertype.md) — The types of offers for auto-renewable subscriptions.

### Getting price information

- [displayPrice](subscriptionoffer/displayprice.md) — The localized string representation of the discounted price of the subscription offer.
- [price](subscriptionoffer/price.md) — The decimal representation of the discounted price of the subscription offer.
- [paymentMode](subscriptionoffer/paymentmode-swift.property.md) — The offer’s payment mode.
- [PaymentMode](subscriptionoffer/paymentmode-swift.struct.md) — The payment modes for subscription offers that apply to a transaction.

### Getting the subscription duration

- [period](subscriptionoffer/period.md) — The subscription period for the subscription offer.
- [periodCount](subscriptionoffer/periodcount.md) — The number of periods that the subscription offer renews for.

### Creating a subscription offer signature

- [Signature](subscriptionoffer/signature.md) — A cryptographic signature for a promotional offer. _(deprecated)_

## See Also

### Offers

- [Supporting offer codes in your app](../supporting-offer-codes-in-your-app.md) — Enable customers to redeem offer codes through the App Store or within your app.
- [Supporting win-back offers in your app](../supporting-win-back-offers-in-your-app.md) — Re-engage previous subscribers with a free or discounted offer for an auto-renewable subscription, for a specific duration.
- [Merchandising win-back offers in your app](../merchandising-win-back-offers-in-your-app.md) — Present win-back offers to eligible customers in your app with the win-back offer sheet or by implementing custom merchandising.
- [OfferType](subscriptionoffer/offertype.md) — The types of offers for auto-renewable subscriptions.
