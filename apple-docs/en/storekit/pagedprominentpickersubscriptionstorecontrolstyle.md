---
title: PagedProminentPickerSubscriptionStoreControlStyle
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/pagedprominentpickersubscriptionstorecontrolstyle
source_url: 'https://developer.apple.com/documentation/storekit/pagedprominentpickersubscriptionstorecontrolstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/pagedprominentpickersubscriptionstorecontrolstyle.json'
content_hash: 'sha256:562cef23712de070'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# PagedProminentPickerSubscriptionStoreControlStyle

<sub>Structure</sub>

A subscription store control style that displays subscription plans as a paged prominent picker control, with a single button to subscribe.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct PagedProminentPickerSubscriptionStoreControlStyle
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## Topics

### Getting the paged prominent picker control style

- [pagedProminentPicker](subscriptionstorecontrolstyle/pagedprominentpicker.md) — A subscription store control style that displays subscription plans as a prominent paged picker control, with a single button to subscribe.

### Creating the style

- [init()](<pagedprominentpickersubscriptionstorecontrolstyle/init().md>) — Creates the paged prominent picker control style.

### Placing the controls

- [Placement](pagedprominentpickersubscriptionstorecontrolstyle/placement.md)

## See Also

### Supporting types

- [AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md) — The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [ProminentPickerSubscriptionStoreControlStyle](prominentpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.
- [CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
- [AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement.md) — A system-defined placement for a subscription store view.
