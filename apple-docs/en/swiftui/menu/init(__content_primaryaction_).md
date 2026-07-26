---
title: 'init(_:content:primaryAction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menu/init(_:content:primaryaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menu/init(_:content:primaryaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menu/init%28_%3Acontent%3Aprimaryaction%3A%29.json'
content_hash: 'sha256:7294847ca6b84dae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Menu](../menu.md)

# init(_:content:primaryAction:)

<sub>Initializer</sub>

Creates a menu with a custom primary action that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void) where Label == Text
```

## Parameters

- `titleResource` — Text resource for the link’s localized title, which describes the contents of the menu.

- `content` — A group of menu items.

- `primaryAction` — The action to perform on primary interaction with the menu.

## See Also

### Creating a menu with a primary action

- [init(content:label:primaryAction:)](<init(content_label_primaryaction_).md>) — Creates a menu with a custom primary action and custom label.
- [init(_:image:content:primaryAction:)](<init(__image_content_primaryaction_).md>) — Creates a menu with a custom primary action that generates its label from a localized string resource.
- [init(_:systemImage:content:primaryAction:)](<init(__systemimage_content_primaryaction_).md>) — Creates a menu with a custom primary action that generates its label from a localized string key and system image.
