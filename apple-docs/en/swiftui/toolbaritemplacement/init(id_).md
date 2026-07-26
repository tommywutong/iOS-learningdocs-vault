---
title: 'init(id:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 13.0+（14.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/toolbaritemplacement/init(id:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/init(id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/init%28id%3A%29.json'
content_hash: 'sha256:1c41025e19bd7f44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# init(id:)

<sub>Initializer</sub>

Creates a custom accessory bar item placement.

> [!warning] Deprecated
> Use [accessoryBar(id:)](<accessorybar(id_).md>) instead.

<sub>macOS</sub>

```swift
init<ID>(id: ID) where ID : Hashable
```

## See Also

### Deprecated symbols

- [navigationBarLeading](navigationbarleading.md) — Places the item in the leading edge of the navigation bar. _(deprecated)_
- [navigationBarTrailing](navigationbartrailing.md) — Places the item in the trailing edge of the navigation bar. _(deprecated)_
