---
title: promotionalOffers
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/promotionaloffers
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/promotionaloffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/promotionaloffers.json'
content_hash: 'sha256:a7f2ff6d2baecb17'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# promotionalOffers

<sub>Instance Property</sub>

An array of promotional offers available for the auto-renewable subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let promotionalOffers: [Product.SubscriptionOffer]
```

## Discussion

This array is empty if you haven’t set up promotional offers in App Store Connect.

For more information about promotional offers, see [Set up promotional offers for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev16dfca448).
