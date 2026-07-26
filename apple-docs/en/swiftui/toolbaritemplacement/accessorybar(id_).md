---
title: 'accessoryBar(id:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toolbaritemplacement/accessorybar(id:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/accessorybar(id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/accessorybar%28id%3A%29.json'
content_hash: 'sha256:b5c1222d4717cc6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# accessoryBar(id:)

<sub>Type Method</sub>

Creates a unique accessory bar placement.

<sub>macOS</sub>

```swift
@backDeployed(before: macOS 14.0)
static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement where ID : Hashable
```

## Parameters

- `id` — A unique identifier for this placement.

## Discussion

On macOS, items with an accessory bar placement are placed in a section below the title bar and toolbar area of the window. Each separate identifier will correspond to a separate accessory bar that is added to this area.

```swift
extension ToolbarItemPlacement {
    static let favoritesBar = accessoryBar(id: "com.example.favorites")
}
...
BrowserView()
    .toolbar {
        ToolbarItem(placement: .favoritesBar) {
            FavoritesBar()
        }
    }
```

## See Also

### Getting explicit placement

- [topBarLeading](topbarleading.md) — A placement for items in the leading edge of the top bar.
- [topBarTrailing](topbartrailing.md) — A placement for items in the trailing edge of the top bar.
- [topBarPinnedTrailing](topbarpinnedtrailing.md) — A placement that pins the item to the trailing edge of the toolbar. _(beta)_
- [bottomBar](bottombar.md) — A placement for items in the bottom toolbar.
- [bottomOrnament](bottomornament.md) — A placement for items in an ornament under the window.
- [keyboard](keyboard.md) — A placement for items in the keyboard section.
