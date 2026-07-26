---
title: CompactPickerSubscriptionStoreControlStyle
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/compactpickersubscriptionstorecontrolstyle
source_url: 'https://developer.apple.com/documentation/storekit/compactpickersubscriptionstorecontrolstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/compactpickersubscriptionstorecontrolstyle.json'
content_hash: 'sha256:0333db33d72e41fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# CompactPickerSubscriptionStoreControlStyle

<sub>Structure</sub>

A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct CompactPickerSubscriptionStoreControlStyle
```

## Overview

This style lays out the picker options in a horizontal stack, and it can scroll horizontally if the contents are wider than the container. This style is recommended when you expect your store to display two or three subscription options.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## Topics

### Getting the compact picker control style

- [compactPicker](subscriptionstorecontrolstyle/compactpicker.md) — A subscription store control style that displays subscription plans as a compact control, with a single button to subscribe.

### Creating the style

- [init()](<compactpickersubscriptionstorecontrolstyle/init().md>) — Creates a compact picker subscription store control style.

### Placing the controls

- [Placement](compactpickersubscriptionstorecontrolstyle/placement.md) — The placement of the compact subscription picker in a subscription store view.

## See Also

### Placement types

- [AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md) — The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
