---
title: 'init(_:image:content:primaryAction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menu/init(_:image:content:primaryaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menu/init(_:image:content:primaryaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menu/init%28_%3Aimage%3Acontent%3Aprimaryaction%3A%29.json'
content_hash: 'sha256:297f7e06588d5a9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Menu](../menu.md)

# init(_:image:content:primaryAction:)

<sub>Initializer</sub>

Creates a menu with a custom primary action that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void)
```

## Parameters

- `titleResource` — Text resource for the link’s localized title, which describes the contents of the menu.

- `image` — The name of the image resource to lookup.

- `content` — A group of menu items.

- `primaryAction` — The action to perform on primary interaction with the menu.

## See Also

### Creating a menu with a primary action

- [init(_:content:primaryAction:)](<init(__content_primaryaction_).md>) — Creates a menu with a custom primary action that generates its label from a localized string resource.
- [init(content:label:primaryAction:)](<init(content_label_primaryaction_).md>) — Creates a menu with a custom primary action and custom label.
- [init(_:systemImage:content:primaryAction:)](<init(__systemimage_content_primaryaction_).md>) — Creates a menu with a custom primary action that generates its label from a localized string key and system image.
