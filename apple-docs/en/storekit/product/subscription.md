---
title: subscription
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscription
source_url: 'https://developer.apple.com/documentation/storekit/product/subscription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscription.json'
content_hash: 'sha256:7a9ed790d16d8131'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# subscription

<sub>Instance Property</sub>

The subscription information for an auto-renewable subscripton.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let subscription: Product.SubscriptionInfo?
```

## Discussion

A `nil` value indicates that this product isn’t an auto-renewable subscription.

For more information about subscriptions, see [Auto-renewable Subscriptions](https://developer.apple.com/app-store/subscriptions/#groups).

## See Also

### Getting subscription information

- [SubscriptionInfo](subscriptioninfo.md) — Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [SubscriptionPeriod](subscriptionperiod.md) — Values that represent the duration of time between subscription renewals.
- [SubscriptionOffer](subscriptionoffer.md) — Information about a subscription offer that you configure in App Store Connect.
- [Status](subscriptioninfo/status-swift.struct.md) — The renewal status information for an auto-renewable subscription.
