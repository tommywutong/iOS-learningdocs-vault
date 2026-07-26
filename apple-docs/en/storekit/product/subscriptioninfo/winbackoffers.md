---
title: winBackOffers
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/winbackoffers
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/winbackoffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/winbackoffers.json'
content_hash: 'sha256:1723789689346e9a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# winBackOffers

<sub>Instance Property</sub>

An array of available win-back offers for the auto-renewable subscription that you configured in App Store Connect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let winBackOffers: [Product.SubscriptionOffer]
```

## Discussion

This list of win-back offers doesn’t take customer eligibility into account, and includes the available offers you’ve configured for the subscription. The customer may not be eligible for all the win-back offers in this array. To get the win-back offers that the customer is eligible for, use [eligibleWinBackOfferIDs](renewalinfo/eligiblewinbackofferids.md) in the subscription renewal information.

For more information about win-back offers, see [Supporting win-back offers in your app](../../supporting-win-back-offers-in-your-app.md).
