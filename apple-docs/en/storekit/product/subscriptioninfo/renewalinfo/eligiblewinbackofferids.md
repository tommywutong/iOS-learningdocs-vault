---
title: eligibleWinBackOfferIDs
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/eligiblewinbackofferids
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/eligiblewinbackofferids'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/eligiblewinbackofferids.json'
content_hash: 'sha256:a0e8922338f25f8d'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# eligibleWinBackOfferIDs

<sub>Instance Property</sub>

An array of strings that represent identifiers of win-back offers that the customer is eligible to redeem, sorted with the best offers first.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let eligibleWinBackOfferIDs: [String]
```

## Discussion

Use this list to select an eligible win-back offer for a customer. The array contains strings that represent offer identifiers for win-back offers. You provide the offer identifier in App Store Connect when you configure a win-back offer.

The App Store sets the order of the eligible win-back offer IDs for each customer, with the best offer first. The order takes into account the available offers you configure in App Store Connect for the customer’s most recent subscription in the subscription group. Subscriptions in a Billing Grace Period or billing retry state aren’t eligible for win-back offers.

Get the complete offer details by searching for the identifier in the [winBackOffers](../winbackoffers.md) property of the [SubscriptionInfo](../../subscriptioninfo.md) instance. To add the offer to a purchase when a customer accepts the offer, use the [winBackOffer(_:)](<../../purchaseoption/winbackoffer(__).md>) purchase option. For more information, see [Supporting win-back offers in your app](../../../supporting-win-back-offers-in-your-app.md).

When you test win-back offers with StoreKit Testing in Xcode, the system lists the offers in no particular order. For more information, see [Testing win-back offers in Xcode](../../../testing-win-back-offers-in-xcode.md).

You can also use the [App Store Server API](../../../../appstoreserverapi.md) to get a list of eligible win-back offers, on your server. For more information, see [Get All Subscription Statuses](../../../../appstoreserverapi/get-all-subscription-statuses.md) and [eligibleWinBackOfferIds](../../../../appstoreserverapi/eligiblewinbackofferids.md).

For information about configuring win-back offers in App Store Connect, see [Set up win-back offers](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers).

## See Also

### Getting offers

- [offer](offer.md) — A subscription offer that applies to the transaction at the next renewal period.
- [Offer](../../../transaction/offer-swift.struct.md) — Discounts or promotions that apply to a transaction.
