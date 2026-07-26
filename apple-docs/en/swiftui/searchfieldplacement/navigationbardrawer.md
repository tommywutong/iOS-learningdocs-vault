---
title: navigationBarDrawer
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/searchfieldplacement/navigationbardrawer
source_url: 'https://developer.apple.com/documentation/swiftui/searchfieldplacement/navigationbardrawer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchfieldplacement/navigationbardrawer.json'
content_hash: 'sha256:0cfc71496df7130c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SearchFieldPlacement](../searchfieldplacement.md)

# navigationBarDrawer

<sub>Type Property</sub>

The search field appears in the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
static let navigationBarDrawer: SearchFieldPlacement
```

## Discussion

The field appears below any navigation bar title and uses the [automatic](navigationbardrawerdisplaymode/automatic.md) display mode to configure when to hide the search field. To choose a different display mode, use [navigationBarDrawer(displayMode:)](<navigationbardrawer(displaymode_).md>) instead.

## See Also

### Getting a search field placement

- [automatic](automatic.md) — SwiftUI places the search field automatically.
- [navigationBarDrawer(displayMode:)](<navigationbardrawer(displaymode_).md>) — The search field appears in the navigation bar using the specified display mode.
- [sidebar](sidebar.md) — The search field appears in the sidebar of a navigation view.
- [toolbar](toolbar.md) — The search field appears in the toolbar.
