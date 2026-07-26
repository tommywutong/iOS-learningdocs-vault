---
title: 'init(alignment:spacing:pinnedViews:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/lazyhstack/init(alignment:spacing:pinnedviews:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/lazyhstack/init(alignment:spacing:pinnedviews:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/lazyhstack/init%28alignment%3Aspacing%3Apinnedviews%3Acontent%3A%29.json'
content_hash: 'sha256:aa99c9b6c7012228'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LazyHStack](../lazyhstack.md)

# init(alignment:spacing:pinnedViews:content:)

<sub>Initializer</sub>

Creates a lazy horizontal stack view with the given spacing, vertical alignment, pinning behavior, and content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, pinnedViews: PinnedScrollableViews = .init(), @ContentBuilder content: () -> Content)
```

## Parameters

- `alignment` — The guide for aligning the subviews in this stack. All child views have the same vertical screen coordinate.

- `spacing` — The distance between adjacent subviews, or `nil` if you want the stack to choose a default distance for each pair of subviews.

- `pinnedViews` — The kinds of child views that will be pinned.

- `content` — A content builder that creates the content of this stack.
