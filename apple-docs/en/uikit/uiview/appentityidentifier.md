---
title: appEntityIdentifier
framework: AppIntents
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+, tvOS 18.4+, visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/appentityidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiview/appentityidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/appentityidentifier.json'
content_hash: 'sha256:979c0fb4f2a4cc7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# appEntityIdentifier

<sub>Instance Property</sub>

The identifier of an app entity that you associate with a custom view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var appEntityIdentifier: EntityIdentifier? { get set }
```

## Discussion

Associate your view with one app entity to make it discoverable by Apple Intelligence and Siri when the view appears onscreen. For example, when a person taps an item in a list to view the detail view for the item, expose the item to Apple Intelligence and Siri using the `appEntityIdentifier`. If your custom view shows several separate items; for example, if you use a custom list implementation that manages selection states itself; use [appEntityUIElementProvider](appentityuielementprovider.md) to provide the system with a list of items.

To clear the association with the app entity, set `appEntityIdentifier` to `nil`.

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [App Intents](../../appintents.md).
