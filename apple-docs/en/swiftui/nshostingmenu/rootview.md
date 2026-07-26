---
title: rootView
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 14.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingmenu/rootview
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingmenu/rootview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingmenu/rootview.json'
content_hash: 'sha256:9d887b105b785fb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingMenu](../nshostingmenu.md)

# rootView

<sub>Instance Property</sub>

The root view of the SwiftUI view hierarchy managed by this menu.

<sub>macOS</sub>

```swift
var rootView: Content { get set }
```

## Discussion

Updating this property will immediately update the `items` array, even if the menu is currently visible to the user.
