---
title: icon
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/icon
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/icon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/icon.json'
content_hash: 'sha256:dca367485f4f1fa3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../../subscriptionstorecontrolstyleconfiguration.md) · [PickerOption](../pickeroption.md)

# icon

<sub>Instance Property</sub>

The subscription option’s icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var icon: SubscriptionStoreControlStyleConfiguration.Icon? { get }
```

## Discussion

Use this property to access the icon you configure for a subscription option using the [subscriptionStoreControlIcon(icon:)](<../../../swiftui/view/subscriptionstorecontrolicon(icon_).md>) view modifier.

## See Also

### Getting properties of the subscription picker option

- [subscription](subscription.md) — The auto-renewable subscription that the picker option represents.
- [activeOffer](activeoffer.md)
- [isSelected](isselected.md) — A Boolean value that indicates whether the picker option is in a selected state.
- [id](id.md)
