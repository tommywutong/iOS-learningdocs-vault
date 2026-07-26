---
title: 'init(productIDs:content:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstoreview/init(productids:content:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(productids:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstoreview/init%28productids%3Acontent%3A%29.json'
content_hash: 'sha256:4826ab36737e9181'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreView](../subscriptionstoreview.md)

# init(productIDs:content:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<C>(productIDs: some Collection<String>, @StoreContentBuilder content: () -> C) where Content == SubscriptionStoreContentView<C>, C : StoreContent
```

## See Also

### Creating subscription store views with a hierarchichal structure

- [init(groupID:visibleRelationships:content:)](<init(groupid_visiblerelationships_content_).md>)
- [init(subscriptions:content:)](<init(subscriptions_content_).md>)
