---
title: 'init(content:label:primaryAction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menu/init(content:label:primaryaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menu/init(content:label:primaryaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menu/init%28content%3Alabel%3Aprimaryaction%3A%29.json'
content_hash: 'sha256:89b98c9638681c16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Menu](../menu.md)

# init(content:label:primaryAction:)

<sub>Initializer</sub>

Creates a menu with a custom primary action and custom label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label, primaryAction: @escaping () -> Void)
```

## Parameters

- `content` — A group of menu items.

- `label` — A view describing the content of the menu.

- `primaryAction` — The action to perform on primary interaction with the menu.

## See Also

### Creating a menu with a primary action

- [init(_:content:primaryAction:)](<init(__content_primaryaction_).md>) — Creates a menu with a custom primary action that generates its label from a localized string resource.
- [init(_:image:content:primaryAction:)](<init(__image_content_primaryaction_).md>) — Creates a menu with a custom primary action that generates its label from a localized string resource.
- [init(_:systemImage:content:primaryAction:)](<init(__systemimage_content_primaryaction_).md>) — Creates a menu with a custom primary action that generates its label from a localized string key and system image.
