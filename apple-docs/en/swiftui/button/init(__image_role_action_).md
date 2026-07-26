---
title: 'init(_:image:role:action:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(_:image:role:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(_:image:role:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28_%3Aimage%3Arole%3Aaction%3A%29.json'
content_hash: 'sha256:7d6f2aee5add2b2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(_:image:role:action:)

<sub>Initializer</sub>

Creates a button with a specified role that generates its label from a localized string resource and an image resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency @export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

## Parameters

- `titleResource` — Text resource for the button’s localized title, that describes the purpose of the button’s `action`.

- `image` — The image resource to lookup.

- `role` — An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.

- `action` — The action to perform when the user triggers the button.

## Discussion

This initializer creates a [Label](../label.md) view on your behalf. See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a button with a role

- [init(role:action:label:)](<init(role_action_label_).md>) — Creates a button with a specified role that displays a custom label.
- [init(_:role:action:)](<init(__role_action_).md>) — Creates a button with a specified role that generates its label from a localized string resource.
- [init(_:systemImage:role:action:)](<init(__systemimage_role_action_).md>) — Creates a button with a specified role that generates its label from a localized string key and a system image.
