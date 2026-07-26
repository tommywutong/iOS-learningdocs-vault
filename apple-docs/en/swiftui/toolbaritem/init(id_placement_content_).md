---
title: 'init(id:placement:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toolbaritem/init(id:placement:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritem/init(id:placement:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritem/init%28id%3Aplacement%3Acontent%3A%29.json'
content_hash: 'sha256:aef4f1ba2d740144'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItem](../toolbaritem.md)

# init(id:placement:content:)

<sub>Initializer</sub>

Creates a toolbar item with the specified placement and content, which allows for user customization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(id: String, placement: ToolbarItemPlacement = .automatic, @ContentBuilder content: () -> Content)
```

## Parameters

- `id` — A unique identifier for this item.

- `placement` — Which section of the toolbar the item should be placed in.

- `content` — The content of the item.

## See Also

### Creating a toolbar item

- [init(placement:content:)](<init(placement_content_).md>) — Creates a toolbar item with the specified placement and content.
- [init(id:placement:showsByDefault:content:)](<init(id_placement_showsbydefault_content_).md>) — Creates a toolbar item with the specified placement and content, which allows for user customization. _(deprecated)_
