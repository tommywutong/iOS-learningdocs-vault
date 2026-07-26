---
title: sidebar
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/searchfieldplacement/sidebar
source_url: 'https://developer.apple.com/documentation/swiftui/searchfieldplacement/sidebar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchfieldplacement/sidebar.json'
content_hash: 'sha256:3e867b72577f14eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SearchFieldPlacement](../searchfieldplacement.md)

# sidebar

<sub>Type Property</sub>

The search field appears in the sidebar of a navigation view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var sidebar: SearchFieldPlacement { get }
```

## Discussion

The precise placement depends on the platform:

- In iOS and iPadOS the search field appears in the section of the navigation bar associated with the sidebar.
- In macOS the search field appears as a sticky header in the sidebar, attached to the toolbar.

If a sidebar isn’t available, like when you apply the searchable modifier to a view other than a navigation split view, SwiftUI uses automatic placement instead.

> [!note] Note
> The search field appears inline with the sidebar’s content when building with Xcode 16 SDKs or earlier.

## See Also

### Getting a search field placement

- [automatic](automatic.md) — SwiftUI places the search field automatically.
- [navigationBarDrawer](navigationbardrawer.md) — The search field appears in the navigation bar.
- [navigationBarDrawer(displayMode:)](<navigationbardrawer(displaymode_).md>) — The search field appears in the navigation bar using the specified display mode.
- [toolbar](toolbar.md) — The search field appears in the toolbar.
