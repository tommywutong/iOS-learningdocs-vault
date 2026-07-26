---
title: topBarPinnedTrailing
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/topbarpinnedtrailing
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbarpinnedtrailing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/topbarpinnedtrailing.json'
content_hash: 'sha256:ae6838a28aaf4cfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# topBarPinnedTrailing

<sub>Type Property</sub>

A placement that pins the item to the trailing edge of the toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let topBarPinnedTrailing: ToolbarItemPlacement
```

## Discussion

Pinned items only move to the overflow menu when search is active and there isn’t enough room.

On iOS and visionOS, the top bar is the navigation bar.

## See Also

### Getting explicit placement

- [topBarLeading](topbarleading.md) — A placement for items in the leading edge of the top bar.
- [topBarTrailing](topbartrailing.md) — A placement for items in the trailing edge of the top bar.
- [bottomBar](bottombar.md) — A placement for items in the bottom toolbar.
- [bottomOrnament](bottomornament.md) — A placement for items in an ornament under the window.
- [keyboard](keyboard.md) — A placement for items in the keyboard section.
- [accessoryBar(id:)](<accessorybar(id_).md>) — Creates a unique accessory bar placement.
