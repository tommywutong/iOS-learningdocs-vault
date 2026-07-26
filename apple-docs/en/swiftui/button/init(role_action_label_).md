---
title: 'init(role:action:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(role:action:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(role:action:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28role%3Aaction%3Alabel%3A%29.json'
content_hash: 'sha256:363ff55885cff54b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(role:action:label:)

<sub>Initializer</sub>

Creates a button with a specified role that displays a custom label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency nonisolated init(role: ButtonRole?, action: @escaping @MainActor () -> Void, @ContentBuilder label: () -> Label)
```

## Parameters

- `role` — An optional semantic role that describes the button. A value of `nil` means that the button doesn’t have an assigned role.

- `action` — The action to perform when the user interacts with the button.

- `label` — A view that describes the purpose of the button’s `action`.

## See Also

### Creating a button with a role

- [init(_:role:action:)](<init(__role_action_).md>) — Creates a button with a specified role that generates its label from a localized string resource.
- [init(_:image:role:action:)](<init(__image_role_action_).md>) — Creates a button with a specified role that generates its label from a localized string resource and an image resource.
- [init(_:systemImage:role:action:)](<init(__systemimage_role_action_).md>) — Creates a button with a specified role that generates its label from a localized string key and a system image.
