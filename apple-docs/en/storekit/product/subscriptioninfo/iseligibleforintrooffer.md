---
title: isEligibleForIntroOffer
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/iseligibleforintrooffer
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/iseligibleforintrooffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/iseligibleforintrooffer.json'
content_hash: 'sha256:a9d5eaeb5cfb6032'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# isEligibleForIntroOffer

<sub>Instance Property</sub>

A Boolean value that indicates whether the customer is eligible for an introductory offer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEligibleForIntroOffer: Bool { get async }
```

## Discussion

This value is `true` if the customer is eligible for an introductory offer on this auto-renewable subscription, or any auto-renewable subscription in the same subscription group; this value is `false` otherwise. This value may be `true` even if you haven’t set up an introductory offer in App Store Connect. The following example illustrates checking the [subscription](../subscription.md) property of a product to determine whether the user is eligible for an introductory offer.

```swift
func eligibleForIntro(product: Product) async throws -> Bool {
    guard let renewableSubscription = product.subscription else {
        // No renewable subscription is available for this product.
        return false
    }
    if await renewableSubscription.isEligibleForIntroOffer {
        // The product is eligible for an introductory offer.
        return true
    }
    return false
}
```

To specify a customer’s eligibility for an introductory offer, see [introductoryOfferEligibility(compactJWS:)](<../purchaseoption/introductoryoffereligibility(compactjws_).md>).

## See Also

### Getting introductory offer details

- [isEligibleForIntroOffer(for:)](<iseligibleforintrooffer(for_).md>) — Returns a Boolean value that determines the customer’s eligibility for an introductory offer within the provided subscription group.
- [introductoryOffer](introductoryoffer.md) — Information about the introductory offer available for the auto-renewable subscription.
- [SubscriptionOffer](../subscriptionoffer.md) — Information about a subscription offer that you configure in App Store Connect.
