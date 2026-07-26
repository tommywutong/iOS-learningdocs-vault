---
title: bundleSubscriptionGroupID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/bundlesubscriptiongroupid
source_url: 'https://developer.apple.com/documentation/storekit/transaction/bundlesubscriptiongroupid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/bundlesubscriptiongroupid.json'
content_hash: 'sha256:dc1b0018071ae043'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# bundleSubscriptionGroupID

<sub>Instance Property</sub>

Identifies the subscription bundle group the transaction is for.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
var bundleSubscriptionGroupID: String? { get }
```

## Discussion

> [!note] Note
> Only for transactions of subscriptions included in a bundle.
