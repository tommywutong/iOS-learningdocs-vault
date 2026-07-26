---
title: bottomBar
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 18.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/bottombar
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/bottombar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/bottombar.json'
content_hash: 'sha256:12415e4773c71e76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# bottomBar

<sub>Type Property</sub>

A placement for items in the bottom toolbar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let bottomBar: ToolbarItemPlacement
```

## Discussion

On tvOS, this applies only within the sidebar of a [NavigationSplitView](../navigationsplitview.md).  It has no effect if used elsewhere.

## See Also

### Getting explicit placement

- [topBarLeading](topbarleading.md) — A placement for items in the leading edge of the top bar.
- [topBarTrailing](topbartrailing.md) — A placement for items in the trailing edge of the top bar.
- [topBarPinnedTrailing](topbarpinnedtrailing.md) — A placement that pins the item to the trailing edge of the toolbar. _(beta)_
- [bottomOrnament](bottomornament.md) — A placement for items in an ornament under the window.
- [keyboard](keyboard.md) — A placement for items in the keyboard section.
- [accessoryBar(id:)](<accessorybar(id_).md>) — Creates a unique accessory bar placement.
