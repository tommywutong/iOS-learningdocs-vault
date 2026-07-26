---
title: AutomaticSubscriptionStoreControlStyle
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/automaticsubscriptionstorecontrolstyle
source_url: 'https://developer.apple.com/documentation/storekit/automaticsubscriptionstorecontrolstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/automaticsubscriptionstorecontrolstyle.json'
content_hash: 'sha256:20e6f8761de5fefa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# AutomaticSubscriptionStoreControlStyle

<sub>Structure</sub>

The default in-app subscription store control style that resolves its appearance based on the view’s context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct AutomaticSubscriptionStoreControlStyle
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## Topics

### Getting the automatic subscription store control style

- [automatic](subscriptionstorecontrolstyle/automatic.md) — A subscription store control style that resolves its appearance automatically, based on the current context.

### Creating the style

- [init()](<automaticsubscriptionstorecontrolstyle/init().md>) — Creates an automatic subscription store control style.

## See Also

### Placement types

- [ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
