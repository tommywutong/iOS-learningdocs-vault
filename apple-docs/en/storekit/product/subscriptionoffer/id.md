---
title: id
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptionoffer/id
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionoffer/id'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionoffer/id.json'
content_hash: 'sha256:79837e8bdb9b6626'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionOffer](../subscriptionoffer.md)

# id

<sub>Instance Property</sub>

The offer identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let id: String?
```

## Discussion

The [id](id.md) is a string that contains the alphanumeric offer identifier you provide when you configure an offer in App Store Connect.

This value is `nil` if the offer is an [introductory](offertype/introductory.md) offer.

Pass the [id](id.md) to a method in [purchase(options:)](<../purchase(options_).md>) to create a purchase option based on the offer’s [type](type.md). For example, pass the [id](id.md) for a promotional offer to the [promotionalOffer(offerID:signature:)](<../purchaseoption/promotionaloffer(offerid_signature_).md>) to apply the promotion to a purchase.

For more information about configuring offers in App Store Connect, see [SubscriptionOffer](../subscriptionoffer.md).
