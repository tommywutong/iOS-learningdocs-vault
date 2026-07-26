---
title: 'init(_:image:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menu/init(_:image:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menu/init(_:image:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menu/init%28_%3Aimage%3Acontent%3A%29.json'
content_hash: 'sha256:1a911f47d121d6e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Menu](../menu.md)

# init(_:image:content:)

<sub>Initializer</sub>

Creates a menu that generates its label from a localized string resource and image resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource` — Text resource for the link’s localized title, which describes the contents of the menu.

- `image` — The name of the image resource to lookup.

- `content` — A group of menu items.

## See Also

### Creating a menu from content

- [init(_:content:)](<init(__content_).md>) — Creates a menu that generates its label from a localized string resource.
- [init(content:label:)](<init(content_label_).md>) — Creates a menu with a custom label.
- [init(_:systemImage:content:)](<init(__systemimage_content_).md>) — Creates a menu that generates its label from a localized string key and system image.
