---
title: updates
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/status-swift.struct/updates
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/updates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/status-swift.struct/updates.json'
content_hash: 'sha256:f4b9fff1fcee8652'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [Status](../status-swift.struct.md)

# updates

<sub>Type Property</sub>

The asynchronous sequence that emits status information when a subscription’s status changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var updates: Product.SubscriptionInfo.Status.Statuses { get }
```

## See Also

### Monitoring subscription status changes

- [all](all.md)
- [Statuses](statuses.md) — An asynchronous sequence that listens for new subscription status information.
