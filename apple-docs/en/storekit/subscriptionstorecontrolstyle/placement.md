---
title: Placement
framework: StoreKit
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyle/placement
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle/placement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyle/placement.json'
content_hash: 'sha256:dbcec18f83cb4bff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyle](../subscriptionstorecontrolstyle.md)

# Placement

<sub>Associated Type</sub>

The placement of subscription controls in a subscription store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Placement : SubscriptionStoreControlPlacement = AutomaticSubscriptionStoreControlPlacement
```

## See Also

### Creating custom subscription store control styles

- [makeBody(configuration:)](<makebody(configuration_).md>) — Creates a view that represents the body of a subscription store control.
- [Configuration](configuration.md) — The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.
- [SubscribeButton](subscribebutton.md) — A button for subscribing to an in-app subscription.
- [SubscriptionPicker](subscriptionpicker.md) — A composite control for selecting a subscription option and confirming the subscription.
- [SubscriptionPickerOption](subscriptionpickeroption.md) — A subscription option within a subscription picker control.
- [SubscriptionStoreControlPlacementKey](../subscriptionstorecontrolplacementkey.md) — A placement for a subscription store control in a store view.
- [Body](body.md) — A view that represents the body of a subscription store control.
