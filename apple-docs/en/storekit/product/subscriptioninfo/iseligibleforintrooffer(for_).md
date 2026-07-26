---
title: 'isEligibleForIntroOffer(for:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/subscriptioninfo/iseligibleforintrooffer(for:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/iseligibleforintrooffer(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/iseligibleforintrooffer%28for%3A%29.json'
content_hash: 'sha256:eac6add97bf65409'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# isEligibleForIntroOffer(for:)

<sub>Type Method</sub>

Returns a Boolean value that determines the customer’s eligibility for an introductory offer within the provided subscription group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func isEligibleForIntroOffer(for groupID: String) async -> Bool
```

## Parameters

- `groupID` — The subscription group identifier to check eligibility for an introductory offer.

## Return Value

`true` if the customer is eligible for an introductory offer on any auto-renewable subscription within the subscription group; `false` otherwise.

## Discussion

This value may be `true` even if you haven’t set up an introductory offer in App Store Connect.

## See Also

### Getting introductory offer details

- [isEligibleForIntroOffer](iseligibleforintrooffer.md) — A Boolean value that indicates whether the customer is eligible for an introductory offer.
- [introductoryOffer](introductoryoffer.md) — Information about the introductory offer available for the auto-renewable subscription.
- [SubscriptionOffer](../subscriptionoffer.md) — Information about a subscription offer that you configure in App Store Connect.
