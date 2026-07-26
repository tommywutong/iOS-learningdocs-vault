---
title: PagedPickerSubscriptionStoreControlStyle
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/pagedpickersubscriptionstorecontrolstyle
source_url: 'https://developer.apple.com/documentation/storekit/pagedpickersubscriptionstorecontrolstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/pagedpickersubscriptionstorecontrolstyle.json'
content_hash: 'sha256:5c4b9654edf76183'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# PagedPickerSubscriptionStoreControlStyle

<sub>Structure</sub>

A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct PagedPickerSubscriptionStoreControlStyle
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## Topics

### Getting the paged picker control style

- [pagedPicker](subscriptionstorecontrolstyle/pagedpicker.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.

### Creating the style

- [init()](<pagedpickersubscriptionstorecontrolstyle/init().md>) — Creates a paged picker control style.

### Placing the controls

- [Placement](pagedpickersubscriptionstorecontrolstyle/placement.md) — The placement of paged subscription picker in a subscription store view.

## See Also

### Placement types

- [AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md) — The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
