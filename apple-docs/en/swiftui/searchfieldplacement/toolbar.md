---
title: toolbar
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/searchfieldplacement/toolbar
source_url: 'https://developer.apple.com/documentation/swiftui/searchfieldplacement/toolbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchfieldplacement/toolbar.json'
content_hash: 'sha256:4bd105e67f9a9c27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SearchFieldPlacement](../searchfieldplacement.md)

# toolbar

<sub>Type Property</sub>

The search field appears in the toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static let toolbar: SearchFieldPlacement
```

## Discussion

The precise placement depends on the platform:

- In iOS and watchOS, the search field appears below the navigation bar and is revealed by scrolling.
- In iPadOS, the search field appears in the trailing navigation bar.
- In macOS, the search field appears in the trailing toolbar.

## See Also

### Getting a search field placement

- [automatic](automatic.md) — SwiftUI places the search field automatically.
- [navigationBarDrawer](navigationbardrawer.md) — The search field appears in the navigation bar.
- [navigationBarDrawer(displayMode:)](<navigationbardrawer(displaymode_).md>) — The search field appears in the navigation bar using the specified display mode.
- [sidebar](sidebar.md) — The search field appears in the sidebar of a navigation view.
