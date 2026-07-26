---
title: 'init(sidebar:detail:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationsplitview/init(sidebar:detail:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationsplitview/init(sidebar:detail:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationsplitview/init%28sidebar%3Adetail%3A%29.json'
content_hash: 'sha256:c382c7a622505a3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationSplitView](../navigationsplitview.md)

# init(sidebar:detail:)

<sub>Initializer</sub>

Creates a two-column navigation split view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder sidebar: () -> Sidebar, @ContentBuilder detail: () -> Detail) where Content == EmptyView
```

## Parameters

- `sidebar` — The view to show in the leading column.

- `detail` — The view to show in the detail area.

## See Also

### Creating a navigation split view

- [init(sidebar:content:detail:)](<init(sidebar_content_detail_).md>) — Creates a three-column navigation split view.
