---
title: 'init(_:systemImage:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menu/init(_:systemimage:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menu/init(_:systemimage:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menu/init%28_%3Asystemimage%3Acontent%3A%29.json'
content_hash: 'sha256:ba0394b15ec58192'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Menu](../menu.md)

# init(_:systemImage:content:)

<sub>Initializer</sub>

Creates a menu that generates its label from a localized string key and system image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleKey` — The key for the link’s localized title, which describes the contents of the menu.

- `systemImage` — The name of the image resource to lookup.

- `content` — A group of menu items.

## See Also

### Creating a menu from content

- [init(_:content:)](<init(__content_).md>) — Creates a menu that generates its label from a localized string resource.
- [init(content:label:)](<init(content_label_).md>) — Creates a menu with a custom label.
- [init(_:image:content:)](<init(__image_content_).md>) — Creates a menu that generates its label from a localized string resource and image resource.
