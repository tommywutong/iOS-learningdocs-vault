---
title: 'init(_:image:isInserted:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menubarextra/init(_:image:isinserted:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menubarextra/init(_:image:isinserted:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menubarextra/init%28_%3Aimage%3Aisinserted%3Acontent%3A%29.json'
content_hash: 'sha256:5e678333876a06e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuBarExtra](../menubarextra.md)

# init(_:image:isInserted:content:)

<sub>Initializer</sub>

Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.

<sub>macOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource` — The localized string resource to use for the accessibility label of the item.

- `image` — The image resource to use as the label.

- `isInserted` — Whether the item is inserted in the menu bar. The item may or may not be visible, depending on the number of items present.

- `content` — A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.

## See Also

### Creating a menu bar extra with an image

- [init(_:image:content:)](<init(__image_content_).md>) — Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:content:)](<init(__systemimage_content_).md>) — Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:isInserted:content:)](<init(__systemimage_isinserted_content_).md>) — Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.
