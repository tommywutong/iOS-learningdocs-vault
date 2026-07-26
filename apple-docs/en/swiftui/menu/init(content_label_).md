---
title: 'init(content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menu/init(content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menu/init(content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menu/init%28content%3Alabel%3A%29.json'
content_hash: 'sha256:4d9a9f62ff7255db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Menu](../menu.md)

# init(content:label:)

<sub>Initializer</sub>

Creates a menu with a custom label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `content` — A group of menu items.

- `label` — A view describing the content of the menu.

## See Also

### Creating a menu from content

- [init(_:content:)](<init(__content_).md>) — Creates a menu that generates its label from a localized string resource.
- [init(_:image:content:)](<init(__image_content_).md>) — Creates a menu that generates its label from a localized string resource and image resource.
- [init(_:systemImage:content:)](<init(__systemimage_content_).md>) — Creates a menu that generates its label from a localized string key and system image.
