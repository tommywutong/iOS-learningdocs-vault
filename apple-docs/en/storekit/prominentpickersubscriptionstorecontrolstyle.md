---
title: ProminentPickerSubscriptionStoreControlStyle
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/prominentpickersubscriptionstorecontrolstyle
source_url: 'https://developer.apple.com/documentation/storekit/prominentpickersubscriptionstorecontrolstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/prominentpickersubscriptionstorecontrolstyle.json'
content_hash: 'sha256:a26252b0f55ddd7d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# ProminentPickerSubscriptionStoreControlStyle

<sub>Structure</sub>

A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@MainActor @preconcurrency struct ProminentPickerSubscriptionStoreControlStyle
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## Topics

### Getting the prominent picker control style

- [pagedProminentPicker](subscriptionstorecontrolstyle/pagedprominentpicker.md) — A subscription store control style that displays subscription plans as a prominent paged picker control, with a single button to subscribe.

### Creating the style

- [init()](<prominentpickersubscriptionstorecontrolstyle/init().md>) — Creates a prominent picker subscription store control style.

### Placing the controls

- [Placement](subscriptionstorecontrolstyle/placement.md) — The placement of subscription controls in a subscription store.

## See Also

### Supporting types

- [AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md) — The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
- [PagedProminentPickerSubscriptionStoreControlStyle](pagedprominentpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a paged prominent picker control, with a single button to subscribe.
- [AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement.md) — A system-defined placement for a subscription store view.
