---
title: 'init(preferredCompactColumn:sidebar:content:detail:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationsplitview/init(preferredcompactcolumn:sidebar:content:detail:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationsplitview/init(preferredcompactcolumn:sidebar:content:detail:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationsplitview/init%28preferredcompactcolumn%3Asidebar%3Acontent%3Adetail%3A%29.json'
content_hash: 'sha256:9258291d9f7ad7e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationSplitView](../navigationsplitview.md)

# init(preferredCompactColumn:sidebar:content:detail:)

<sub>Initializer</sub>

Creates a three-column navigation split view that enables programmatic control over which column appears on top when the view collapses into a single column in narrow sizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, @ContentBuilder sidebar: () -> Sidebar, @ContentBuilder content: () -> Content, @ContentBuilder detail: () -> Detail)
```

## Parameters

- `preferredCompactColumn` — A [Binding](../binding.md) to state that controls which column appears on top when the view collapses.

- `sidebar` — The view to show in the leading column.

- `content` — The view to show in the middle column.

- `detail` — The view to show in the detail area.

## See Also

### Specifying a preferred compact column

- [init(preferredCompactColumn:sidebar:detail:)](<init(preferredcompactcolumn_sidebar_detail_).md>) — Creates a two-column navigation split view that enables programmatic control over which column appears on top when the view collapses into a single column in narrow sizes.
