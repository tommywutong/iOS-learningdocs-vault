---
title: willUnbundle
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/willunbundle
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/willunbundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/willunbundle.json'
content_hash: 'sha256:35482d04fa9eff38'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# willUnbundle

<sub>Instance Property</sub>

Whether the subscription will leave the bundle at the next renewal and renew as a standalone product.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
var willUnbundle: Bool { get }
```

## Discussion

> [!note] Note
> Only for renewals of subscriptions included in a bundle.
