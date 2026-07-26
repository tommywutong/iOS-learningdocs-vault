---
title: PickerSubscriptionStoreControlStyle
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/pickersubscriptionstorecontrolstyle
source_url: 'https://developer.apple.com/documentation/storekit/pickersubscriptionstorecontrolstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/pickersubscriptionstorecontrolstyle.json'
content_hash: 'sha256:ee4606012a4105a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# PickerSubscriptionStoreControlStyle

<sub>Structure</sub>

A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct PickerSubscriptionStoreControlStyle
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## Topics

### Getting the picker control style

- [picker](subscriptionstorecontrolstyle/picker.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.

### Placing the controls

- [Placement](subscriptionstorecontrolstyle/placement.md) — The placement of subscription controls in a subscription store.

### Creating the style

- [init()](<pickersubscriptionstorecontrolstyle/init().md>) — Creates a picker subscription store control style.

## See Also

### Placement types

- [AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md) — The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
