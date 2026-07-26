---
title: 'init(_:systemImage:content:primaryAction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menu/init(_:systemimage:content:primaryaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menu/init(_:systemimage:content:primaryaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menu/init%28_%3Asystemimage%3Acontent%3Aprimaryaction%3A%29.json'
content_hash: 'sha256:0296351cdec764fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Menu](../menu.md)

# init(_:systemImage:content:primaryAction:)

<sub>Initializer</sub>

Creates a menu with a custom primary action that generates its label from a localized string key and system image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void)
```

## Parameters

- `titleKey` — The key for the link’s localized title, which describes the contents of the menu.

- `systemImage` — The name of the image resource to lookup.

- `content` — A group of menu items.

- `primaryAction` — The action to perform on primary interaction with the menu.

## See Also

### Creating a menu with a primary action

- [init(_:content:primaryAction:)](<init(__content_primaryaction_).md>) — Creates a menu with a custom primary action that generates its label from a localized string resource.
- [init(content:label:primaryAction:)](<init(content_label_primaryaction_).md>) — Creates a menu with a custom primary action and custom label.
- [init(_:image:content:primaryAction:)](<init(__image_content_primaryaction_).md>) — Creates a menu with a custom primary action that generates its label from a localized string resource.
