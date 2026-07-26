---
title: 'init(isInserted:content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menubarextra/init(isinserted:content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menubarextra/init(isinserted:content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menubarextra/init%28isinserted%3Acontent%3Alabel%3A%29.json'
content_hash: 'sha256:60968f5bd8300d07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuBarExtra](../menubarextra.md)

# init(isInserted:content:label:)

<sub>Initializer</sub>

Creates a menu bar extra. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.

<sub>macOS</sub>

```swift
nonisolated init(isInserted: Binding<Bool>, @ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `isInserted` — Whether the item is inserted in the menu bar. The item may or may not be visible, depending on the number of items present.

- `content` — A `View` to display when the user selects the item.

- `label` — A `View` to use as the label in the system menu bar.

## See Also

### Creating a menu bar extra

- [init(_:content:)](<init(__content_).md>) — Creates a menu bar extra with a localized resource for a localized string to use as the label. The extra defines the primary scene of an `App`.
- [init(content:label:)](<init(content_label_).md>) — Creates a menu bar extra that will be displayed in the system menu bar, and defines the primary scene of an `App`.
- [init(_:isInserted:content:)](<init(__isinserted_content_).md>) — Creates a menu bar extra with a localized resource for a localized string to use as the label. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.
