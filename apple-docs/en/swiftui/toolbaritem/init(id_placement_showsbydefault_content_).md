---
title: 'init(id:placement:showsByDefault:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, tvOS 14.0+（27.0 起废弃）, visionOS 1.0+, watchOS 7.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/toolbaritem/init(id:placement:showsbydefault:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritem/init(id:placement:showsbydefault:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritem/init%28id%3Aplacement%3Ashowsbydefault%3Acontent%3A%29.json'
content_hash: 'sha256:97a893a47e76f0c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItem](../toolbaritem.md)

# init(id:placement:showsByDefault:content:)

<sub>Initializer</sub>

Creates a toolbar item with the specified placement and content, which allows for user customization.

> [!warning] Deprecated
> Use the CustomizableToolbarContent/defaultCustomization(_:options) modifier with a value of .hidden

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(id: String, placement: ToolbarItemPlacement = .automatic, showsByDefault: Bool, @ContentBuilder content: () -> Content)
```

## Parameters

- `id` — A unique identifier for this item.

- `placement` — Which section of the toolbar the item should be placed in.

- `showsByDefault` — Whether the item appears by default in the toolbar, or only shows if the user explicitly adds it via customization.

- `content` — The content of the item.

## See Also

### Creating a toolbar item

- [init(placement:content:)](<init(placement_content_).md>) — Creates a toolbar item with the specified placement and content.
- [init(id:placement:content:)](<init(id_placement_content_).md>) — Creates a toolbar item with the specified placement and content, which allows for user customization.
