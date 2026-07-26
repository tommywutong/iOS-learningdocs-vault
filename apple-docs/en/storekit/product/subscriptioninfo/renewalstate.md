---
title: Product.SubscriptionInfo.RenewalState
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalstate
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalstate.json'
content_hash: 'sha256:ac6e9add276792b8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# Product.SubscriptionInfo.RenewalState

<sub>Structure</sub>

The renewal states of auto-renewable subscriptions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RenewalState
```

## Overview

A subscription’s renewal state indicates whether an auto-renewable subscription is entitled to service. Subscriptions in the [subscribed](renewalstate/subscribed.md) and [inGracePeriod](renewalstate/ingraceperiod.md) states are entitled to service.

Subscriptions in the [expired](renewalstate/expired.md), [inBillingRetryPeriod](renewalstate/inbillingretryperiod.md), and [revoked](renewalstate/revoked.md) states aren’t entitled to service if the customer doesn’t have other [Status](status-swift.struct.md) items that give them entitlement to service for that subscription. For example, a customer may have a status in the [expired](renewalstate/expired.md) state for a subscription that they purchased individually, and another status in the [subscribed](renewalstate/subscribed.md) state for the same subscription, which they get through Family Sharing. In that case, the customer has an entitlement to service for that subscription.

For more information about Family Sharing, see [Supporting Family Sharing in your app](../../supporting-family-sharing-in-your-app.md). For more information about entitlements, see [currentEntitlements](../../transaction/currententitlements.md).

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Getting the renewal state

- [subscribed](renewalstate/subscribed.md) — The customer is currently subscribed.
- [expired](renewalstate/expired.md) — The subscription expired.
- [inBillingRetryPeriod](renewalstate/inbillingretryperiod.md) — The subscription is in a billing retry period.
- [inGracePeriod](renewalstate/ingraceperiod.md) — The subscription is in a billing grace period state.
- [revoked](renewalstate/revoked.md) — The App Store has revoked the customer’s access to the subscription group.

### Getting a localized description

- [localizedDescription](renewalstate/localizeddescription.md) — A string containing the localized description of the renewal state.

## See Also

### Subscription status and renewal information

- [Status](status-swift.struct.md) — The renewal status information for an auto-renewable subscription.
- [RenewalInfo](renewalinfo.md) — The renewal information for an auto-renewable subscription.
- [SubscriptionRenewalInfo](../../subscriptionrenewalinfo.md) — Represents the renewal information for an auto-renewable subscription.
- [SubscriptionRenewalState](../../subscriptionrenewalstate.md) — The renewal states of auto-renewable subscriptions.
- [SubscriptionPeriod](../../subscriptionperiod.md) — Represents the duration of time between subscription renewals.
