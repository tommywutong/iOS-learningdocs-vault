---
title: groupDisplayName
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/groupdisplayname
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/groupdisplayname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/groupdisplayname.json'
content_hash: 'sha256:1478e5f0a96828d7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# groupDisplayName

<sub>Instance Property</sub>

The localized name of the subscription group, suitable for display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0)
var groupDisplayName: String { get }
```

## Discussion

You provide a group display name in App Store Connect when you set up a subscription group. For more information, see [Offer auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev75708c031).

The [SubscriptionStoreView](../../subscriptionstoreview.md) uses this value as part of the automatic marketing content if you don’t provide a marketing content view.

> [!note] Note
> When you create a new product in App Store Connect or in a StoreKit configuration file, you can test it before you add a product localization. The [groupDisplayName](groupdisplayname.md) value is an empty string until you add a localization. For more information on localizations, see [Add localizations](https://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions#add-localizations).

## See Also

### Identifying the subscription group

- [subscriptionGroupID](subscriptiongroupid.md) — The subscription group identifier for this subscription.
- [groupLevel](grouplevel.md) — The rank of the subscription relative to other subscriptions in the same subscription group.
