---
title: bundledSubscriptions
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/bundledsubscriptions
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/bundledsubscriptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/bundledsubscriptions.json'
content_hash: 'sha256:5eeb96452ce55fa8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# bundledSubscriptions

<sub>Instance Property</sub>

Properties and functionality specific to auto-renewable subscriptions included in a subscription bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let bundledSubscriptions: [Product.SubscriptionInfo.BundledSubscription]
```

## Discussion

This list is only populated if `type` is `.subscriptionBundle`, and always empty for all other product types.
