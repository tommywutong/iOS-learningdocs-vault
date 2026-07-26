---
title: activeOffer
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/activeoffer
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/activeoffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/activeoffer.json'
content_hash: 'sha256:484e4b11429af17f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../../subscriptionstorecontrolstyleconfiguration.md) · [Option](../option.md)

# activeOffer

<sub>Instance Property</sub>

The subscription offer the customer is eligible for, and that applies to the subscription option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var activeOffer: Product.SubscriptionOffer? { get }
```

## Discussion

Always display the terms of this subscription offer along with your control because it represents the offer that StoreKit automatically applies when you call the [subscribe()](<subscribe().md>) method. If the [activeOffer](activeoffer.md) property is `nil`, there’s no subscription offer.

> [!important] Important
> Don’t display offers from properties of [subscription](subscription.md), such as [introductoryOffer](../../product/subscriptioninfo/introductoryoffer.md).

The [preferredSubscriptionOffer(_:)](<../../../swiftui/view/preferredsubscriptionoffer(__).md>) and [subscriptionPromotionalOffer(offer:signature:)](<../../../swiftui/view/subscriptionpromotionaloffer(offer_signature_).md>) view modifiers influence the [offer](../../purchaseintent/offer.md) property.

## See Also

### Getting the subscription product and offer

- [subscription](subscription.md) — The auto-renewable subscription to merchandise.
- [id](id.md) — The product ID of the auto-renewable subscription.
