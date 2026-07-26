---
title: Product.SubscriptionInfo.Status
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/status-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/status-swift.struct.json'
content_hash: 'sha256:4453b932f47f7ead'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# Product.SubscriptionInfo.Status

<sub>Structure</sub>

The renewal status information for an auto-renewable subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Status
```

## Overview

The subscription status provides renewal information signed by the App Store for subscriptions that a customer purchases.

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Monitoring subscription status changes

- [updates](status-swift.struct/updates.md) — The asynchronous sequence that emits status information when a subscription’s status changes.
- [all](status-swift.struct/all.md)
- [Statuses](status-swift.struct/statuses.md) — An asynchronous sequence that listens for new subscription status information.

### Getting subscription status information

- [state](status-swift.struct/state.md) — The renewal state of the auto-renewable subscription.
- [renewalInfo](status-swift.struct/renewalinfo.md) — The signed renewal information for the auto-renewable subscription.
- [transaction](status-swift.struct/transaction.md) — The latest transaction for the subscription group.
- [RenewalInfo](renewalinfo.md) — The renewal information for an auto-renewable subscription.
- [RenewalState](renewalstate.md) — The renewal states of auto-renewable subscriptions.

## See Also

### Subscription status and renewal information

- [RenewalInfo](renewalinfo.md) — The renewal information for an auto-renewable subscription.
- [SubscriptionRenewalInfo](../../subscriptionrenewalinfo.md) — Represents the renewal information for an auto-renewable subscription.
- [RenewalState](renewalstate.md) — The renewal states of auto-renewable subscriptions.
- [SubscriptionRenewalState](../../subscriptionrenewalstate.md) — The renewal states of auto-renewable subscriptions.
- [SubscriptionPeriod](../../subscriptionperiod.md) — Represents the duration of time between subscription renewals.
