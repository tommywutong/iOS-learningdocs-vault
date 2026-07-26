---
title: AutomaticSubscriptionStoreMarketingContent
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/automaticsubscriptionstoremarketingcontent
source_url: 'https://developer.apple.com/documentation/storekit/automaticsubscriptionstoremarketingcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/automaticsubscriptionstoremarketingcontent.json'
content_hash: 'sha256:3e767b46e5e82608'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# AutomaticSubscriptionStoreMarketingContent

<sub>Structure</sub>

A view that represents the default marketing content for a subscription store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct AutomaticSubscriptionStoreMarketingContent
```

## Overview

You don’t use this type directly. Instead, create a [SubscriptionStoreView](subscriptionstoreview.md) using an initializer that doesn’t include a `marketingContent` parameter for providing custom marketing content.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## See Also

### Supporting types

- [SubscriptionStoreContentView](subscriptionstorecontentview.md)
