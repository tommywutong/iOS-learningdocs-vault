---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menubarextra/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menubarextra/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menubarextra/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:4cb715f8f81e0f72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuBarExtra](../menubarextra.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a menu bar extra with a localized resource for a localized string to use as the label. The extra defines the primary scene of an `App`.

<sub>macOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource` — The title resource to use for the label of the item.

- `content` — A `View` to display when the user selects the item.

## Discussion

When this item is removed from the system menu bar by the user, the application will be automatically quit. As such, it should not be used in conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra

- [init(content:label:)](<init(content_label_).md>) — Creates a menu bar extra that will be displayed in the system menu bar, and defines the primary scene of an `App`.
- [init(_:isInserted:content:)](<init(__isinserted_content_).md>) — Creates a menu bar extra with a localized resource for a localized string to use as the label. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.
- [init(isInserted:content:label:)](<init(isinserted_content_label_).md>) — Creates a menu bar extra. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.
