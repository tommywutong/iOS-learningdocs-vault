---
title: 'init(_:systemImage:isInserted:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menubarextra/init(_:systemimage:isinserted:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menubarextra/init(_:systemimage:isinserted:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menubarextra/init%28_%3Asystemimage%3Aisinserted%3Acontent%3A%29.json'
content_hash: 'sha256:ea994ac97d300104'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuBarExtra](../menubarextra.md)

# init(_:systemImage:isInserted:content:)

<sub>Initializer</sub>

Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.

<sub>macOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource` — The localized string resource to use for the accessibility label of the item.

- `systemImage` — The name of a system image to use as the label.

- `isInserted` — Whether the item is inserted in the menu bar. The item may or may not be visible, depending on the number of items present.

- `content` — A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.

## See Also

### Creating a menu bar extra with an image

- [init(_:image:content:)](<init(__image_content_).md>) — Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:image:isInserted:content:)](<init(__image_isinserted_content_).md>) — Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:content:)](<init(__systemimage_content_).md>) — Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.
