---
title: 'init(columnVisibility:sidebar:content:detail:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationsplitview/init(columnvisibility:sidebar:content:detail:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationsplitview/init(columnvisibility:sidebar:content:detail:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationsplitview/init%28columnvisibility%3Asidebar%3Acontent%3Adetail%3A%29.json'
content_hash: 'sha256:fd1f615384f2e789'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationSplitView](../navigationsplitview.md)

# init(columnVisibility:sidebar:content:detail:)

<sub>Initializer</sub>

Creates a three-column navigation split view that enables programmatic control of leading columns’ visibility.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(columnVisibility: Binding<NavigationSplitViewVisibility>, @ContentBuilder sidebar: () -> Sidebar, @ContentBuilder content: () -> Content, @ContentBuilder detail: () -> Detail)
```

## Parameters

- `columnVisibility` — A [Binding](../binding.md) to state that controls the visibility of the leading columns.

- `sidebar` — The view to show in the leading column.

- `content` — The view to show in the middle column.

- `detail` — The view to show in the detail area.

## See Also

### Hiding columns in a navigation split view

- [init(columnVisibility:sidebar:detail:)](<init(columnvisibility_sidebar_detail_).md>) — Creates a two-column navigation split view that enables programmatic control of the sidebar’s visibility.
