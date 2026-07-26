---
title: allOptions
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/alloptions
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/alloptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/alloptions.json'
content_hash: 'sha256:9934fe1c6bfd7c60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md)

# allOptions

<sub>Instance Property</sub>

All subscription options in the subscription group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allOptions: [Product] { get }
```

## Discussion

The [allOptions](alloptions.md) property is an array that contains all the subscription options in a subscription group. Use the [allOptions](alloptions.md) property to access the subscription options that the [options](options.md) and [sections](sections.md) properties may not contain.

For example, use the [allOptions](alloptions.md) property if your control style displays comparisons between available subscription options. A [SubscriptionPeriodGroupSet](../subscriptionperiodgroupset.md) can compare the value of a yearly renewing subscription to a monthly subscription. Because each instance of your control style displays only subscriptions with matching renewal periods, you can’t compute such a comparison using the [options](options.md) property. The [allOptions](alloptions.md) value is always a superset of the [options](options.md) property.

> [!note] Note
> Don’t use the [allOptions](alloptions.md) property to determine the subscription options your control style view displays. Instead, only display the subscription options that the [options](options.md) or [sections](sections.md) properties contain.

It’s possible for a subscription store control to display only a subset of the options available within a subscription group. For example, if you use a store content builder to declare the content of a [SubscriptionStoreView](../subscriptionstoreview.md), the store may create multiple instances of your control with different configuration values. These instances may each display a different subset of the subscripton options.

## See Also

### Getting subscription group properties

- [groupDisplayName](groupdisplayname.md) — The localized display name of the subscription group that the subscription store view merchandises.
- [autoRenewPreference](autorenewpreference.md) — The auto-renewable subscripton product that renews at the next billing cycle.
