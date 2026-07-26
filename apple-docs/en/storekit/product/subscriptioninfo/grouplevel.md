---
title: groupLevel
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/grouplevel
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/grouplevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/grouplevel.json'
content_hash: 'sha256:2cb9919460ab0394'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# groupLevel

<sub>Instance Property</sub>

The rank of the subscription relative to other subscriptions in the same subscription group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0)
var groupLevel: Int { get }
```

## Discussion

If you offer multiple auto-renewable subscriptions with different price tiers, you can assign each to a level in App Store Connect. Ranking your subscriptions determines the upgrade, downgrade, and crossgrade paths available.

Subscriptions with the highest level of service within a subscription group have a [groupLevel](grouplevel.md) value of `1`. Subscriptions with lower levels of service or content have [groupLevel](grouplevel.md) values of `2` or greater. For example, when comparing two subscriptions, moving from a subscription with a [groupLevel](grouplevel.md) of `2` to a subscription with a [groupLevel](grouplevel.md) of `1` represents an upgrade.

For more information on ranking, see [Ranking subscriptions within the group](https://developer.apple.com/app-store/subscriptions/#ranking). For information on assigning subscription levels in App Store Connect, see [Assign subscription levels](https://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions/#assign-subscription-levels).

> [!note] Note
> On systems earlier than iOS 17, macOS 14, tvOS 17, and watchOS 10, this property returns a sentinel value of `0` when you test your app using StoreKit Testing in Xcode or if there’s an unexpected server error.

## See Also

### Identifying the subscription group

- [subscriptionGroupID](subscriptiongroupid.md) — The subscription group identifier for this subscription.
- [groupDisplayName](groupdisplayname.md) — The localized name of the subscription group, suitable for display.
