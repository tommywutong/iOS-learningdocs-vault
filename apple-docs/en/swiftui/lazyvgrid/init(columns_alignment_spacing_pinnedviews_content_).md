---
title: 'init(columns:alignment:spacing:pinnedViews:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/lazyvgrid/init(columns:alignment:spacing:pinnedviews:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/lazyvgrid/init(columns:alignment:spacing:pinnedviews:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/lazyvgrid/init%28columns%3Aalignment%3Aspacing%3Apinnedviews%3Acontent%3A%29.json'
content_hash: 'sha256:4c1e84193a57ef18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LazyVGrid](../lazyvgrid.md)

# init(columns:alignment:spacing:pinnedViews:content:)

<sub>Initializer</sub>

Creates a grid that grows vertically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(columns: [GridItem], alignment: HorizontalAlignment = .center, spacing: CGFloat? = nil, pinnedViews: PinnedScrollableViews = .init(), @ContentBuilder content: () -> Content)
```

## Parameters

- `columns` — An array of grid items to size and position each row of the grid.

- `alignment` — The alignment of the grid within its parent view.

- `spacing` — The spacing between the grid and the next item in its parent view.

- `pinnedViews` — Views to pin to the bounds of a parent scroll view.

- `content` — The content of the grid.
