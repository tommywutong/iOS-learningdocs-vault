---
title: automatic
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyle/automatic
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyle/automatic.json'
content_hash: 'sha256:d1ae366898af9f4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyle](../subscriptionstorecontrolstyle.md)

# automatic

<sub>Type Property</sub>

A subscription store control style that resolves its appearance automatically, based on the current context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency static var automatic: AutomaticSubscriptionStoreControlStyle { get }
```

## Discussion

You can also use [subscriptionStoreControlStyle(_:)](<../../swiftui/view/subscriptionstorecontrolstyle(__).md>) with [automatic](automatic.md) as the parameter to construct this style.

## See Also

### Getting built-in subscription store control styles

- [buttons](buttons.md) — A subscription store control style that displays a subscribe button for each subscription plan.
- [picker](picker.md) — A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [prominentPicker](prominentpicker.md) — A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.
- [pagedPicker](pagedpicker.md) — A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
- [pagedProminentPicker](pagedprominentpicker.md) — A subscription store control style that displays subscription plans as a prominent paged picker control, with a single button to subscribe.
- [compactPicker](compactpicker.md) — A subscription store control style that displays subscription plans as a compact control, with a single button to subscribe.
