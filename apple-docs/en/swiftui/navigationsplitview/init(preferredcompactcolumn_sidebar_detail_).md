---
title: 'init(preferredCompactColumn:sidebar:detail:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationsplitview/init(preferredcompactcolumn:sidebar:detail:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationsplitview/init(preferredcompactcolumn:sidebar:detail:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationsplitview/init%28preferredcompactcolumn%3Asidebar%3Adetail%3A%29.json'
content_hash: 'sha256:11af5336527f77ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationSplitView](../navigationsplitview.md)

# init(preferredCompactColumn:sidebar:detail:)

<sub>Initializer</sub>

Creates a two-column navigation split view that enables programmatic control over which column appears on top when the view collapses into a single column in narrow sizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, @ContentBuilder sidebar: () -> Sidebar, @ContentBuilder detail: () -> Detail) where Content == EmptyView
```

## Parameters

- `preferredCompactColumn` — A [Binding](../binding.md) to state that controls which column appears on top when the view collapses.

- `sidebar` — The view to show in the leading column.

- `detail` — The view to show in the detail area.

## See Also

### Specifying a preferred compact column

- [init(preferredCompactColumn:sidebar:content:detail:)](<init(preferredcompactcolumn_sidebar_content_detail_).md>) — Creates a three-column navigation split view that enables programmatic control over which column appears on top when the view collapses into a single column in narrow sizes.
