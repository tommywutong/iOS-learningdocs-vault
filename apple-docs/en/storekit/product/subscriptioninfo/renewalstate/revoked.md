---
title: revoked
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalstate/revoked
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalstate/revoked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalstate/revoked.json'
content_hash: 'sha256:95a030ad6cb40dc6'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalState](../renewalstate.md)

# revoked

<sub>Type Property</sub>

The App Store has revoked the customer’s access to the subscription group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let revoked: Product.SubscriptionInfo.RenewalState
```

## See Also

### Getting the renewal state

- [subscribed](subscribed.md) — The customer is currently subscribed.
- [expired](expired.md) — The subscription expired.
- [inBillingRetryPeriod](inbillingretryperiod.md) — The subscription is in a billing retry period.
- [inGracePeriod](ingraceperiod.md) — The subscription is in a billing grace period state.
