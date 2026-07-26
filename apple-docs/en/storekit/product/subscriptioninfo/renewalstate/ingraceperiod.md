---
title: inGracePeriod
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalstate/ingraceperiod
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalstate/ingraceperiod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalstate/ingraceperiod.json'
content_hash: 'sha256:76835f1073b7ad6b'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalState](../renewalstate.md)

# inGracePeriod

<sub>Type Property</sub>

The subscription is in a billing grace period state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let inGracePeriod: Product.SubscriptionInfo.RenewalState
```

## Discussion

An auto-renewable subscription in this state is entitled to service.

## See Also

### Getting the renewal state

- [subscribed](subscribed.md) — The customer is currently subscribed.
- [expired](expired.md) — The subscription expired.
- [inBillingRetryPeriod](inbillingretryperiod.md) — The subscription is in a billing retry period.
- [revoked](revoked.md) — The App Store has revoked the customer’s access to the subscription group.
