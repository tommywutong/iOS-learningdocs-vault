---
title: all
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/status-swift.struct/all
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/all'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/status-swift.struct/all.json'
content_hash: 'sha256:9b8d7c8787180724'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [Status](../status-swift.struct.md)

# all

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var all: AsyncStream<(groupID: String, statuses: [Product.SubscriptionInfo.Status])> { get }
```

## See Also

### Monitoring subscription status changes

- [updates](updates.md) — The asynchronous sequence that emits status information when a subscription’s status changes.
- [Statuses](statuses.md) — An asynchronous sequence that listens for new subscription status information.
