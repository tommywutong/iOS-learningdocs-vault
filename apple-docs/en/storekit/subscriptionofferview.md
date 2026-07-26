---
title: SubscriptionOfferView
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionofferview
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionofferview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionofferview.json'
content_hash: 'sha256:745e784b3d1d9056'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionOfferView

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency struct SubscriptionOfferView<Icon, PlaceholderIcon> where Icon : View, PlaceholderIcon : View
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Initializers

- [init(_:)](<subscriptionofferview/init(__).md>)
- [init(groupID:visibleRelationship:)](<subscriptionofferview/init(groupid_visiblerelationship_).md>)
- [init(groupID:visibleRelationship:icon:)](<subscriptionofferview/init(groupid_visiblerelationship_icon_).md>)
- [init(groupID:visibleRelationship:icon:placeholderIcon:)](<subscriptionofferview/init(groupid_visiblerelationship_icon_placeholdericon_).md>)
- [init(groupID:visibleRelationship:useAppIcon:)](<subscriptionofferview/init(groupid_visiblerelationship_useappicon_).md>)
- [init(id:icon:placeholderIcon:)](<subscriptionofferview/init(id_icon_placeholdericon_).md>)
- [init(id:prefersPromotionalIcon:)](<subscriptionofferview/init(id_preferspromotionalicon_).md>)
- [init(id:prefersPromotionalIcon:icon:)](<subscriptionofferview/init(id_preferspromotionalicon_icon_).md>)
- [init(id:prefersPromotionalIcon:icon:placeholderIcon:)](<subscriptionofferview/init(id_preferspromotionalicon_icon_placeholdericon_).md>)
- [init(_:icon:)](<subscriptionofferview/init(__icon_).md>)
- [init(_:prefersPromotionalIcon:)](<subscriptionofferview/init(__preferspromotionalicon_).md>)
- [init(_:prefersPromotionalIcon:icon:)](<subscriptionofferview/init(__preferspromotionalicon_icon_).md>)

## See Also

### Merchandising In-App Purchases, subscriptions, and offers

- [ProductView](productview.md) — A view that merchandises an individual In-App Purchase product.
- [StoreView](storeview.md) — A view that merchandises a collection of In-App Purchase products.
- [SubscriptionStoreView](subscriptionstoreview.md) — A view that merchandises a collection of auto-renewable subscription options that belong to the same subscription group.
- [Backyard Birds: Building an app with SwiftData and widgets](../swiftui/backyard-birds-sample.md) — Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.
