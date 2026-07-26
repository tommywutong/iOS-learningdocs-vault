---
title: SubscriptionStoreControlPlacementKey
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolplacementkey
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolplacementkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolplacementkey.json'
content_hash: 'sha256:dd5e548547399a86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionStoreControlPlacementKey

<sub>Structure</sub>

A placement for a subscription store control in a store view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SubscriptionStoreControlPlacementKey
```

## Overview

This type represents all available control placements. You typically don’t interact with this type directly. Use it if you create a custom control style that conforms to the [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md) protocol to restrict the supported placements for your style. By default, a custom control style supports all placements. For more information, see [SubscriptionStoreControlPlacement](subscriptionstorecontrolplacement.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Placing subscription store controls

- [bottom](subscriptionstorecontrolplacementkey/bottom.md) — A placement that anchors the subscription controls to the bottom edge of the view.
- [leading](subscriptionstorecontrolplacementkey/leading.md) — A placement that anchors the subscription controls to the leading edge of the view.
- [scrollView](subscriptionstorecontrolplacementkey/scrollview.md) — A placement that locates the subscription controls within the main scroll view of a subscription store view.
- [trailing](subscriptionstorecontrolplacementkey/trailing.md) — A placement that anchors the subscription controls to the trailing edge of the view.
- [bottomBar](subscriptionstorecontrolplacementkey/bottombar.md) — A placement that locates the subscription controls in a bar near the bottom of the main scroll view in a subscription store view.
- [buttonsInBottomBar](subscriptionstorecontrolplacementkey/buttonsinbottombar.md) — A hybrid placement that positions subscription controls within the main scroll view, and places auxiliary buttons in the bottom bar.

## See Also

### Creating custom subscription store control styles

- [makeBody(configuration:)](<subscriptionstorecontrolstyle/makebody(configuration_).md>) — Creates a view that represents the body of a subscription store control.
- [Configuration](subscriptionstorecontrolstyle/configuration.md) — The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.
- [SubscribeButton](subscriptionstorecontrolstyle/subscribebutton.md) — A button for subscribing to an in-app subscription.
- [SubscriptionPicker](subscriptionstorecontrolstyle/subscriptionpicker.md) — A composite control for selecting a subscription option and confirming the subscription.
- [SubscriptionPickerOption](subscriptionstorecontrolstyle/subscriptionpickeroption.md) — A subscription option within a subscription picker control.
- [Placement](subscriptionstorecontrolstyle/placement.md) — The placement of subscription controls in a subscription store.
- [Body](subscriptionstorecontrolstyle/body.md) — A view that represents the body of a subscription store control.
