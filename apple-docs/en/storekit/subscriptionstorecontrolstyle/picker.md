---
title: picker
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyle/picker
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle/picker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyle/picker.json'
content_hash: 'sha256:82244e4d3bdfea78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyle](../subscriptionstorecontrolstyle.md)

# picker

<sub>Type Property</sub>

A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency static var picker: PickerSubscriptionStoreControlStyle { get }
```

## Discussion

You can also use [subscriptionStoreControlStyle(_:)](<../../swiftui/view/subscriptionstorecontrolstyle(__).md>) with [picker](picker.md) as the parameter to construct this style.

## See Also

### Getting built-in subscription store control styles

- [automatic](automatic.md) — A subscription store control style that resolves its appearance automatically, based on the current context.
- [buttons](buttons.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [prominentPicker](prominentpicker.md) — A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.
- [pagedPicker](pagedpicker.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
- [pagedProminentPicker](pagedprominentpicker.md) — A subscription store control style that displays subscription plans as a prominent paged picker control, with a single button to subscribe.
- [compactPicker](compactpicker.md) — A subscription store control style that displays subscription plans as a compact control, with a single button to subscribe.
