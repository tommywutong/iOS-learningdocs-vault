---
title: 'status(transactionID:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/subscriptioninfo/status(transactionid:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status(transactionid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/status%28transactionid%3A%29.json'
content_hash: 'sha256:35c236f26e7ff835'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# status(transactionID:)

<sub>Type Method</sub>

Gets the subscription status for a transaction ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func status(transactionID: UInt64) async throws -> SubscriptionStatus?
```

## See Also

### Determining the subscription status

- [status](status-swift.property.md) — An array that contains status information for a subscription group, including renewal and transaction information.
- [status(for:)](<status(for_).md>) — Gets the subscription status for a subscription group identifier.
- [Status](status-swift.struct.md) — The renewal status information for an auto-renewable subscription.
