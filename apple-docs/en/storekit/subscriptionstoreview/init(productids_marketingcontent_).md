---
title: 'init(productIDs:marketingContent:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstoreview/init(productids:marketingcontent:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(productids:marketingcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstoreview/init%28productids%3Amarketingcontent%3A%29.json'
content_hash: 'sha256:df1b03db4383318a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreView](../subscriptionstoreview.md)

# init(productIDs:marketingContent:)

<sub>Initializer</sub>

Creates a view that loads a collection of subscriptions from the App Store, and merchandises them with custom marketing content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(productIDs: some Collection<String>, @ViewBuilder marketingContent: () -> Content)
```

## Parameters

- `productIDs` — The product identifiers to load from the App Store.

- `marketingContent` — The view that contains marketing content to display above the store controls.

## See Also

### Creating subscription store views with custom marketing content

- [init(groupID:visibleRelationships:marketingContent:)](<init(groupid_visiblerelationships_marketingcontent_).md>) — Creates a view that loads all the subscriptions in a subscription group from the App Store, and merchandises them with custom marketing content.
- [init(subscriptions:marketingContent:)](<init(subscriptions_marketingcontent_).md>) — Creates a view that displays a collection of subscription options, and merchandises them with custom marketing content.
