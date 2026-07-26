---
title: 'status(for:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/subscriptioninfo/status(for:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/status%28for%3A%29.json'
content_hash: 'sha256:2a6bda83e064160b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# status(for:)

<sub>Type Method</sub>

Gets the subscription status for a subscription group identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func status(for groupID: String) async throws -> [Product.SubscriptionInfo.Status]
```

## Parameters

- `groupID` — The subscription group identifier of the subscription to get status for.

## Return Value

An array of [Status](status-swift.struct.md). This array is empty if the customer has never subscribed to a product in this subscription group.

## Discussion

To get the subscription group identifier of a subscription, see [subscriptionGroupID](subscriptiongroupid.md) in [SubscriptionInfo](../subscriptioninfo.md), or [subscriptionGroupID](../../transaction/subscriptiongroupid.md) in [Transaction](../../transaction.md). You originally create subscription group identifiers when you set up in-app purchases in App Store Connect. For more information, see [Offer auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev75708c031).

Users can only buy one auto-renewable subscription within a group at a time. However, the returned array may contain multiple status values if your subscription supports Family Sharing, and the person has access to other subscriptions in the group through Family Sharing. For more information about Family Sharing, see [Enable Family Sharing for your subscriptions](https://developer.apple.com/news/?id=ksfkdwpr).

## See Also

### Determining the subscription status

- [status](status-swift.property.md) — An array that contains status information for a subscription group, including renewal and transaction information.
- [status(transactionID:)](<status(transactionid_).md>) — Gets the subscription status for a transaction ID.
- [Status](status-swift.struct.md) — The renewal status information for an auto-renewable subscription.
