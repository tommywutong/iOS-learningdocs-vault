---
title: 'init(groupID:visibleRelationships:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstoreview/init(groupid:visiblerelationships:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(groupid:visiblerelationships:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstoreview/init%28groupid%3Avisiblerelationships%3A%29.json'
content_hash: 'sha256:6559a67c6dca750b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreView](../subscriptionstoreview.md)

# init(groupID:visibleRelationships:)

<sub>Initializer</sub>

Creates a view that loads all subscriptions in a subscription group from the App Store, and merchandises them with automatic marketing content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(groupID: String, visibleRelationships: Product.SubscriptionRelationship = .all) where Content == AutomaticSubscriptionStoreMarketingContent
```

## Parameters

- `groupID` — The subscription group identifier to load from the App Store.

- `visibleRelationships` — The kinds of subscription option relationships the view makes visible when someone is already subscribed to the subscription.

## See Also

### Creating subscription store views with automatic marketing content

- [init(productIDs:)](<init(productids_).md>) — Creates a view that loads subscriptions based on a collection of product identifiers, and merchandises them with automatic marketing content.
- [init(subscriptions:)](<init(subscriptions_).md>) — Creates a view that displays a collection of subscription options, and merchandises them with automatic marketing content.
