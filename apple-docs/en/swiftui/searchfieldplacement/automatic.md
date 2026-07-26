---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/searchfieldplacement/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/searchfieldplacement/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchfieldplacement/automatic.json'
content_hash: 'sha256:ea27e4bf2518acee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SearchFieldPlacement](../searchfieldplacement.md)

# automatic

<sub>Type Property</sub>

SwiftUI places the search field automatically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: SearchFieldPlacement
```

## Discussion

Placement of the search field depends on the platform:

- In iOS, iPadOS, and macOS, the search field appears in the toolbar.
- In tvOS and watchOS, the search field appears inline with its content.

## See Also

### Getting a search field placement

- [navigationBarDrawer](navigationbardrawer.md) — The search field appears in the navigation bar.
- [navigationBarDrawer(displayMode:)](<navigationbardrawer(displaymode_).md>) — The search field appears in the navigation bar using the specified display mode.
- [sidebar](sidebar.md) — The search field appears in the sidebar of a navigation view.
- [toolbar](toolbar.md) — The search field appears in the toolbar.
