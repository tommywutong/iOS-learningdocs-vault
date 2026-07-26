---
title: ButtonsSubscriptionStoreControlStyle
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/buttonssubscriptionstorecontrolstyle
source_url: 'https://developer.apple.com/documentation/storekit/buttonssubscriptionstorecontrolstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/buttonssubscriptionstorecontrolstyle.json'
content_hash: 'sha256:933d78c9fd7254f1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# ButtonsSubscriptionStoreControlStyle

<sub>Structure</sub>

A subscription store control style that displays a subscribe button for each subscription plan.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct ButtonsSubscriptionStoreControlStyle
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## Topics

### Getting the button subscription store style

- [buttons](subscriptionstorecontrolstyle/buttons.md) — A subscription store control style that displays a subscribe button for each subscription plan.

### Creating the style

- [init()](<buttonssubscriptionstorecontrolstyle/init().md>) — Creates a button subscription store control style.

## See Also

### Placement types

- [AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md) — The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
