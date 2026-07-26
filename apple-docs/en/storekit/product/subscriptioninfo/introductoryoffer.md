---
title: introductoryOffer
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/introductoryoffer
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/introductoryoffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/introductoryoffer.json'
content_hash: 'sha256:6fc4e5eaa18613dc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# introductoryOffer

<sub>Instance Property</sub>

Information about the introductory offer available for the auto-renewable subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let introductoryOffer: Product.SubscriptionOffer?
```

## Discussion

This value is `nil` if you don’t set up an introductory offer in App Store Connect. Use [isEligibleForIntroOffer](iseligibleforintrooffer.md) to determine whether the customer is eligible for an introductory offer.

## See Also

### Getting introductory offer details

- [isEligibleForIntroOffer](iseligibleforintrooffer.md) — A Boolean value that indicates whether the customer is eligible for an introductory offer.
- [isEligibleForIntroOffer(for:)](<iseligibleforintrooffer(for_).md>) — Returns a Boolean value that determines the customer’s eligibility for an introductory offer within the provided subscription group.
- [SubscriptionOffer](../subscriptionoffer.md) — Information about a subscription offer that you configure in App Store Connect.
