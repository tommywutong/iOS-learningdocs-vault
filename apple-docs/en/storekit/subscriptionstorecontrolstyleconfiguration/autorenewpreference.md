---
title: autoRenewPreference
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/autorenewpreference
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/autorenewpreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/autorenewpreference.json'
content_hash: 'sha256:89fc6fb7acc96e74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md)

# autoRenewPreference

<sub>Instance Property</sub>

The auto-renewable subscripton product that renews at the next billing cycle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var autoRenewPreference: Product? { get }
```

## Discussion

Use the [autoRenewPreference](autorenewpreference.md) property to identify the subscription that renews in the next billing cycle, if there is one. The property is `nil` if the customer doesn’t have an auto-renewable subscription that renews in the next billing period. This indicates that the customer turned off the auto-renew preference, or that they don’t have a current subscription.

Display the subscription in the auto-renew preference only if it appears in the [options](options.md) or [sections](sections.md) arrays. However, disable its [subscribe()](<option/subscribe().md>) control so the customer doesn’t try to subscribe to it again, to prevent a system dialog that explains that the customer is already subscribed. The following code example shows how to check for the auto-renew preference and disable the subscribe functionality:

```swift
ForEach(configuration.options) { option in 
    Button(option.displayName, action: option.subscribe)
        .disabled(option.id == configuration.autoRenewPreference?.id)
}
```

> [!important] Important
> Don’t use the [autoRenewPreference](autorenewpreference.md) property to determine whether to grant access to a service. Always check the full transaction information before granting access to a paid service.

## See Also

### Getting subscription group properties

- [groupDisplayName](groupdisplayname.md) — The localized display name of the subscription group that the subscription store view merchandises.
- [allOptions](alloptions.md) — All subscription options in the subscription group.
