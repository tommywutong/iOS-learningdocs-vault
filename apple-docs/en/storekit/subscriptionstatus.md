---
title: SubscriptionStatus
framework: StoreKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstatus
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstatus.json'
content_hash: 'sha256:ef77d4e8b6bcae74'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionStatus

<sub>Type Alias</sub>

Represents the renewal status information for an auto-renewable subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SubscriptionStatus = Product.SubscriptionInfo.Status
```

## See Also

### Product and subscription information

- [Implementing a store in your app using the StoreKit API](implementing-a-store-in-your-app-using-the-storekit-api.md) — Offer In-App Purchases and manage entitlements using signed transactions and status information.
- [Supporting monthly subscriptions with a 12-month commitment](supporting-monthly-subscriptions-with-a-12-month-commitment.md) — Configure, merchandise, and grant access to a monthly subscription with a 12-month commitment.
- [Managing the life cycle of monthly subscriptions with a 12-month commitment](managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment-.md) — Handle renewals, cancellations, billing issues, refund requests, and price changes, and test subscriptions with a commitment plan.
- [Product](product.md) — Information about a product that you configure in App Store Connect.
- [SubscriptionInfo](product/subscriptioninfo.md) — Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [SubscriptionInfo](subscriptioninfo.md) — Information about an auto-renewable subscription.
