---
title: subscription
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/subscription
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/subscription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/subscription.json'
content_hash: 'sha256:f3782d5058b45cc2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../../subscriptionstorecontrolstyleconfiguration.md) · [PickerOption](../pickeroption.md)

# subscription

<sub>Instance Property</sub>

The auto-renewable subscription that the picker option represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var subscription: Product { get }
```

## Discussion

[PickerOption](../pickeroption.md) is a dynamic member lookup type, so you don’t need to use this property directly to access the properties of the [Product](../../product.md) value. Instead, access any properties of [Product](../../product.md) or [SubscriptionInfo](../../product/subscriptioninfo.md) directly on the `PickerOption` value.

> [!important] Important
> Don’t use [purchase(confirmIn:options:)](<../../product/purchase(confirmin_options_)-6dj6y.md>) or related purchase methods on this property to initiate a purchase. Use a picker option only for selecting a subscription option, which requires additional confirmation before initiating a purchase.

## See Also

### Getting properties of the subscription picker option

- [activeOffer](activeoffer.md)
- [isSelected](isselected.md) — A Boolean value that indicates whether the picker option is in a selected state.
- [icon](icon.md) — The subscription option’s icon.
- [id](id.md)
