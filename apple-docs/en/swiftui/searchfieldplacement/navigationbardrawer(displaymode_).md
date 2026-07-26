---
title: 'navigationBarDrawer(displayMode:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/searchfieldplacement/navigationbardrawer(displaymode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/searchfieldplacement/navigationbardrawer(displaymode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchfieldplacement/navigationbardrawer%28displaymode%3A%29.json'
content_hash: 'sha256:f51622160b19aea0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SearchFieldPlacement](../searchfieldplacement.md)

# navigationBarDrawer(displayMode:)

<sub>Type Method</sub>

The search field appears in the navigation bar using the specified display mode.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func navigationBarDrawer(displayMode: SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement
```

## Parameters

- `displayMode` — A control that indicates whether to hide the search field in response to scrolling.

## Discussion

The field appears below any navigation bar title. The system can hide the field in response to scrolling, depending on the `displayMode` that you set.

## See Also

### Getting a search field placement

- [automatic](automatic.md) — SwiftUI places the search field automatically.
- [navigationBarDrawer](navigationbardrawer.md) — The search field appears in the navigation bar.
- [sidebar](sidebar.md) — The search field appears in the sidebar of a navigation view.
- [toolbar](toolbar.md) — The search field appears in the toolbar.
