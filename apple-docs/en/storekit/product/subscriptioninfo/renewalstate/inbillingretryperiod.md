---
title: inBillingRetryPeriod
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalstate/inbillingretryperiod
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalstate/inbillingretryperiod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalstate/inbillingretryperiod.json'
content_hash: 'sha256:1d64c9e0b2362803'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalState](../renewalstate.md)

# inBillingRetryPeriod

<sub>Type Property</sub>

The subscription is in a billing retry period.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState
```

## See Also

### Getting the renewal state

- [subscribed](subscribed.md) — The customer is currently subscribed.
- [expired](expired.md) — The subscription expired.
- [inGracePeriod](ingraceperiod.md) — The subscription is in a billing grace period state.
- [revoked](revoked.md) — The App Store has revoked the customer’s access to the subscription group.
