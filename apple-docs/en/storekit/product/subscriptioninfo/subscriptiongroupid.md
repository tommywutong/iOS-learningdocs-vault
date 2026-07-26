---
title: subscriptionGroupID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/subscriptiongroupid
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/subscriptiongroupid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/subscriptiongroupid.json'
content_hash: 'sha256:65f23c5ac57e8b21'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# subscriptionGroupID

<sub>Instance Property</sub>

The subscription group identifier for this subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let subscriptionGroupID: String
```

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create the subscription group identifiers in App Store Connect before you create and add an auto-renewable subscription. For more information about subscription groups, see [Offer auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev75708c031).

## See Also

### Identifying the subscription group

- [groupDisplayName](groupdisplayname.md) — The localized name of the subscription group, suitable for display.
- [groupLevel](grouplevel.md) — The rank of the subscription relative to other subscriptions in the same subscription group.
