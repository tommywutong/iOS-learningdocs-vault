---
title: 'init(productIDs:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstoreview/init(productids:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(productids:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstoreview/init%28productids%3A%29.json'
content_hash: 'sha256:821b9e65950913a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreView](../subscriptionstoreview.md)

# init(productIDs:)

<sub>Initializer</sub>

Creates a view that loads subscriptions based on a collection of product identifiers, and merchandises them with automatic marketing content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(productIDs: some Collection<String>) where Content == AutomaticSubscriptionStoreMarketingContent
```

## Parameters

- `productIDs` — The product identifiers to load from the App Store.

## See Also

### Creating subscription store views with automatic marketing content

- [init(groupID:visibleRelationships:)](<init(groupid_visiblerelationships_).md>) — Creates a view that loads all subscriptions in a subscription group from the App Store, and merchandises them with automatic marketing content.
- [init(subscriptions:)](<init(subscriptions_).md>) — Creates a view that displays a collection of subscription options, and merchandises them with automatic marketing content.
