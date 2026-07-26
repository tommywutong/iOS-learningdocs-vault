---
title: 'init(action:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(action:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(action:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28action%3Alabel%3A%29.json'
content_hash: 'sha256:dd6e5d4aebd6e961'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(action:label:)

<sub>Initializer</sub>

Creates a button that displays a custom label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency nonisolated init(action: @escaping @MainActor () -> Void, @ContentBuilder label: () -> Label)
```

## Parameters

- `action` — The action to perform when the user triggers the button.

- `label` — A view that describes the purpose of the button’s `action`.

## See Also

### Creating a button

- [init(_:action:)](<init(__action_).md>) — Creates a button that generates its label from a localized string resource.
- [init(_:image:action:)](<init(__image_action_).md>) — Creates a button that generates its label from a localized string resource and image resource.
- [init(_:systemImage:action:)](<init(__systemimage_action_).md>) — Creates a button that generates its label from a localized string key and system image name.
