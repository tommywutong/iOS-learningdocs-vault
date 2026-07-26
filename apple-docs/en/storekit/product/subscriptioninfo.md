---
title: Product.SubscriptionInfo
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo.json'
content_hash: 'sha256:72f0b0b1a877b1a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# Product.SubscriptionInfo

<sub>Structure</sub>

Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SubscriptionInfo
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Determining the subscription status

- [status](subscriptioninfo/status-swift.property.md) — An array that contains status information for a subscription group, including renewal and transaction information.
- [status(for:)](<subscriptioninfo/status(for_).md>) — Gets the subscription status for a subscription group identifier.
- [status(transactionID:)](<subscriptioninfo/status(transactionid_).md>) — Gets the subscription status for a transaction ID.
- [Status](subscriptioninfo/status-swift.struct.md) — The renewal status information for an auto-renewable subscription.

### Identifying the subscription group

- [subscriptionGroupID](subscriptioninfo/subscriptiongroupid.md) — The subscription group identifier for this subscription.
- [groupDisplayName](subscriptioninfo/groupdisplayname.md) — The localized name of the subscription group, suitable for display.
- [groupLevel](subscriptioninfo/grouplevel.md) — The rank of the subscription relative to other subscriptions in the same subscription group.

### Getting the subscription period

- [subscriptionPeriod](subscriptioninfo/subscriptionperiod.md) — The duration of time between subscription renewals.
- [SubscriptionPeriod](subscriptionperiod.md) — Values that represent the duration of time between subscription renewals.

### Getting introductory offer details

- [isEligibleForIntroOffer](subscriptioninfo/iseligibleforintrooffer.md) — A Boolean value that indicates whether the customer is eligible for an introductory offer.
- [isEligibleForIntroOffer(for:)](<subscriptioninfo/iseligibleforintrooffer(for_).md>) — Returns a Boolean value that determines the customer’s eligibility for an introductory offer within the provided subscription group.
- [introductoryOffer](subscriptioninfo/introductoryoffer.md) — Information about the introductory offer available for the auto-renewable subscription.
- [SubscriptionOffer](subscriptionoffer.md) — Information about a subscription offer that you configure in App Store Connect.

### Getting win-back offer details

- [winBackOffers](subscriptioninfo/winbackoffers.md) — An array of available win-back offers for the auto-renewable subscription that you configured in App Store Connect.

### Getting promotional offer details

- [promotionalOffers](subscriptioninfo/promotionaloffers.md) — An array of promotional offers available for the auto-renewable subscription.

### Getting subscription renewal information

- [RenewalInfo](subscriptioninfo/renewalinfo.md) — The renewal information for an auto-renewable subscription.
- [RenewalState](subscriptioninfo/renewalstate.md) — The renewal states of auto-renewable subscriptions.

### Structures

- [BillingPlanType](subscriptioninfo/billingplantype.md)
- [BundledSubscription](subscriptioninfo/bundledsubscription.md) — Properties and functionality specific to auto-renewable subscriptions included in a subscription bundle. _(beta)_
- [CommitmentInfo](subscriptioninfo/commitmentinfo.md)
- [PricingTerms](subscriptioninfo/pricingterms-swift.struct.md)

### Instance Properties

- [bundledSubscriptions](subscriptioninfo/bundledsubscriptions.md) — Properties and functionality specific to auto-renewable subscriptions included in a subscription bundle. _(beta)_
- [pricingTerms](subscriptioninfo/pricingterms-swift.property.md)

### Type Aliases

- [BillingPeriod](subscriptioninfo/billingperiod.md)

## See Also

### Product and subscription information

- [Implementing a store in your app using the StoreKit API](../implementing-a-store-in-your-app-using-the-storekit-api.md) — Offer In-App Purchases and manage entitlements using signed transactions and status information.
- [Supporting monthly subscriptions with a 12-month commitment](../supporting-monthly-subscriptions-with-a-12-month-commitment.md) — Configure, merchandise, and grant access to a monthly subscription with a 12-month commitment.
- [Managing the life cycle of monthly subscriptions with a 12-month commitment](../managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment-.md) — Handle renewals, cancellations, billing issues, refund requests, and price changes, and test subscriptions with a commitment plan.
- [Product](../product.md) — Information about a product that you configure in App Store Connect.
- [SubscriptionInfo](../subscriptioninfo.md) — Information about an auto-renewable subscription.
- [SubscriptionStatus](../subscriptionstatus.md) — Represents the renewal status information for an auto-renewable subscription.
