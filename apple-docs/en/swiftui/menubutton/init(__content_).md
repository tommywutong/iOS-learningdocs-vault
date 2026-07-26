---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/menubutton/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menubutton/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menubutton/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:3808dabc515bee1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuButton](../menubutton.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a menu button with the specified localized title and content.

> [!warning] Deprecated
> Use [Menu](../menu.md) instead.

<sub>macOS</sub>

```swift
nonisolated init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

## See Also

### Creating a menu button

- [init(label:content:)](<init(label_content_).md>) — Creates a menu button with the specified label and content. _(deprecated)_
