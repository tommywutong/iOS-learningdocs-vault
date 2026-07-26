---
title: 'init(subscriptions:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstoreview/init(subscriptions:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(subscriptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstoreview/init%28subscriptions%3A%29.json'
content_hash: 'sha256:4ce53a7d2dd5198c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreView](../subscriptionstoreview.md)

# init(subscriptions:)

<sub>Initializer</sub>

Creates a view that displays a collection of subscription options, and merchandises them with automatic marketing content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(subscriptions: some Collection<Product>) where Content == AutomaticSubscriptionStoreMarketingContent
```

## Parameters

- `subscriptions` — A collection of auto-renewable subscription [Product](../product.md) instances to merchandise. The auto-renewable subscriptions need to belong to the same subscription group.

## See Also

### Creating subscription store views with automatic marketing content

- [init(groupID:visibleRelationships:)](<init(groupid_visiblerelationships_).md>) — Creates a view that loads all subscriptions in a subscription group from the App Store, and merchandises them with automatic marketing content.
- [init(productIDs:)](<init(productids_).md>) — Creates a view that loads subscriptions based on a collection of product identifiers, and merchandises them with automatic marketing content.
