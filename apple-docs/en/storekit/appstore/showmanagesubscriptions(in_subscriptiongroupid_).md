---
title: 'showManageSubscriptions(in:subscriptionGroupID:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/appstore/showmanagesubscriptions(in:subscriptiongroupid:)'
source_url: 'https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:subscriptiongroupid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/showmanagesubscriptions%28in%3Asubscriptiongroupid%3A%29.json'
content_hash: 'sha256:2b7e123137b97ef3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# showManageSubscriptions(in:subscriptionGroupID:)

<sub>Type Method</sub>

Presents the App Store sheet for managing subscriptions for a subscription group.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor static func showManageSubscriptions(in scene: UIWindowScene, subscriptionGroupID: String) async throws
```

## Parameters

- `scene` — The [UIWindowScene](../../uikit/uiwindowscene.md) that the system displays the sheet on.

- `subscriptionGroupID` — The subscription group identifier that the subscription belongs to.

## See Also

### Managing subscriptions

- [showManageSubscriptions(in:)](<showmanagesubscriptions(in_).md>) — Presents the App Store sheet for managing subscriptions.
