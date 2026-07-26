---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menu/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menu/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menu/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:760c39f37b6d0713'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Menu](../menu.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a menu that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content) where Label == Text
```

## Parameters

- `titleResource` — Text resource for the link’s localized title, which describes the contents of the menu.

- `content` — A group of menu items.

## See Also

### Creating a menu from content

- [init(content:label:)](<init(content_label_).md>) — Creates a menu with a custom label.
- [init(_:image:content:)](<init(__image_content_).md>) — Creates a menu that generates its label from a localized string resource and image resource.
- [init(_:systemImage:content:)](<init(__systemimage_content_).md>) — Creates a menu that generates its label from a localized string key and system image.
