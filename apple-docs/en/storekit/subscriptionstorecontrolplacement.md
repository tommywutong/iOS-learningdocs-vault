---
title: SubscriptionStoreControlPlacement
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolplacement
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolplacement.json'
content_hash: 'sha256:193588d90caebd32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionStoreControlPlacement

<sub>Protocol</sub>

A type that specifies the placement of a subscription control in a subscription store view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SubscriptionStoreControlPlacement : RawRepresentable where Self.RawValue == SubscriptionStoreControlPlacementKey
```

## Overview

A placement indicates a position for placing a control in a view. Specifically, a subscription store control placement indicates a postion for placing a subscription control in a subscription store view. You typically don’t need to implement your own control placement; instead, use the conforming placement types. To see the available control placements for a type, such as a [PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md), check the `Placement` associated type on a control style.

Not all subscription store control styles support all placements. For example, the picker control styles don’t support the bottom bar placement because the height obscures the scroll view.

## Relationships

- **Inherits From**: [RawRepresentable](../swift/rawrepresentable.md)

- **Conforming Types**: [AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement.md), [Placement](compactpickersubscriptionstorecontrolstyle/placement.md), [Placement](pagedpickersubscriptionstorecontrolstyle/placement.md)

## Topics

### Getting a placement

- [automatic](subscriptionstorecontrolplacement/automatic.md) — The default placement for a subscription store control.

### Placement types

- [AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md) — The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.

## See Also

### Styling subscription store controls

- [subscriptionStoreControlStyle(_:)](<../swiftui/view/subscriptionstorecontrolstyle(__).md>) — Sets the control style for subscription store views within a view.
- [subscriptionStoreControlStyle(_:placement:)](<../swiftui/view/subscriptionstorecontrolstyle(__placement_).md>) — Sets the control style and control placement for subscription store views within a view.
- [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md) — A type that specifies the appearance and interaction of controls in the subscription store view instances within the view hierarchy.
- [SubscriptionStoreControlStyleConfiguration](subscriptionstorecontrolstyleconfiguration.md) — The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.
