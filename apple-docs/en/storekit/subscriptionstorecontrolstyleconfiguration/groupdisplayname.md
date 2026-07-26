---
title: groupDisplayName
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/groupdisplayname
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/groupdisplayname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/groupdisplayname.json'
content_hash: 'sha256:bbed6045bb6b9e8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md)

# groupDisplayName

<sub>Instance Property</sub>

The localized display name of the subscription group that the subscription store view merchandises.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var groupDisplayName: String { get }
```

## Discussion

This property is the same as accessing [groupDisplayName](../product/subscriptioninfo/groupdisplayname.md) on a [SubscriptionInfo](../product/subscriptioninfo.md) value. Because all options within a subscription store view belong to the same subscription group, using the [groupDisplayName](groupdisplayname.md) property is more convenient than getting the group display name from an arbitrary subscription option.

## See Also

### Getting subscription group properties

- [autoRenewPreference](autorenewpreference.md) — The auto-renewable subscripton product that renews at the next billing cycle.
- [allOptions](alloptions.md) — All subscription options in the subscription group.
