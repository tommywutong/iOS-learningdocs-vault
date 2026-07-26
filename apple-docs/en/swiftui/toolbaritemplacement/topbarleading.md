---
title: topBarLeading
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/topbarleading
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbarleading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/topbarleading.json'
content_hash: 'sha256:3d2d528b4a71c4cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# topBarLeading

<sub>Type Property</sub>

A placement for items in the leading edge of the top bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 17.0, tvOS 17.0)
static var topBarLeading: ToolbarItemPlacement { get }
```

## Discussion

On watchOS, iOS, and tvOS, the top bar is the navigation bar.

## See Also

### Getting explicit placement

- [topBarTrailing](topbartrailing.md) — A placement for items in the trailing edge of the top bar.
- [topBarPinnedTrailing](topbarpinnedtrailing.md) — A placement that pins the item to the trailing edge of the toolbar. _(beta)_
- [bottomBar](bottombar.md) — A placement for items in the bottom toolbar.
- [bottomOrnament](bottomornament.md) — A placement for items in an ornament under the window.
- [keyboard](keyboard.md) — A placement for items in the keyboard section.
- [accessoryBar(id:)](<accessorybar(id_).md>) — Creates a unique accessory bar placement.
