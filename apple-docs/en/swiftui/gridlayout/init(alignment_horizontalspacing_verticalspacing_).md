---
title: 'init(alignment:horizontalSpacing:verticalSpacing:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gridlayout/init(alignment:horizontalspacing:verticalspacing:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gridlayout/init(alignment:horizontalspacing:verticalspacing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gridlayout/init%28alignment%3Ahorizontalspacing%3Averticalspacing%3A%29.json'
content_hash: 'sha256:1ea2ca5a5d66cfb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GridLayout](../gridlayout.md)

# init(alignment:horizontalSpacing:verticalSpacing:)

<sub>Initializer</sub>

Creates a grid with the specified spacing and alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(alignment: Alignment = .center, horizontalSpacing: CGFloat? = nil, verticalSpacing: CGFloat? = nil)
```

## Parameters

- `alignment` — The guide for aligning subviews within the space allocated for a given cell. The default is [center](../alignment/center.md).

- `horizontalSpacing` — The horizontal distance between each cell, given in points. The value is `nil` by default, which results in a default distance between cells that’s appropriate for the platform.

- `verticalSpacing` — The vertical distance between each cell, given in points. The value is `nil` by default, which results in a default distance between cells that’s appropriate for the platform.
