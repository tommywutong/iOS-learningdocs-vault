---
title: status
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/status-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/status-swift.property.json'
content_hash: 'sha256:d82e8b9bec9e2328'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# status

<sub>Instance Property</sub>

An array that contains status information for a subscription group, including renewal and transaction information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var status: [Product.SubscriptionInfo.Status] { get async throws }
```

## Discussion

This array is empty if the customer was never subscribed to a product in this subscription group.

The array can have more than one subscription status if your subscription supports Family Sharing. Provide the customer with service for the subscription based on the highest level of service where the state is [subscribed](renewalstate/subscribed.md).

## See Also

### Determining the subscription status

- [status(for:)](<status(for_).md>) — Gets the subscription status for a subscription group identifier.
- [status(transactionID:)](<status(transactionid_).md>) — Gets the subscription status for a transaction ID.
- [Status](status-swift.struct.md) — The renewal status information for an auto-renewable subscription.
