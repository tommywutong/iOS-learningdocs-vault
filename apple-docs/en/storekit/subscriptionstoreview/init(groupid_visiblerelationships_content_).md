---
title: 'init(groupID:visibleRelationships:content:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstoreview/init(groupid:visiblerelationships:content:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(groupid:visiblerelationships:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstoreview/init%28groupid%3Avisiblerelationships%3Acontent%3A%29.json'
content_hash: 'sha256:0c0fd6c2d8f09911'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreView](../subscriptionstoreview.md)

# init(groupID:visibleRelationships:content:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<C>(groupID: String, visibleRelationships: Product.SubscriptionRelationship = .all, @StoreContentBuilder content: () -> C) where Content == SubscriptionStoreContentView<C>, C : StoreContent
```

## See Also

### Creating subscription store views with a hierarchichal structure

- [init(productIDs:content:)](<init(productids_content_).md>)
- [init(subscriptions:content:)](<init(subscriptions_content_).md>)
