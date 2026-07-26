---
title: 'init(alignment:spacing:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hstacklayout/init(alignment:spacing:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hstacklayout/init(alignment:spacing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hstacklayout/init%28alignment%3Aspacing%3A%29.json'
content_hash: 'sha256:577166f10fb3250c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HStackLayout](../hstacklayout.md)

# init(alignment:spacing:)

<sub>Initializer</sub>

Creates a horizontal stack with the specified spacing and vertical alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(alignment: VerticalAlignment = .center, spacing: CGFloat? = nil)
```

## Parameters

- `alignment` — The guide for aligning the subviews in this stack. It has the same vertical screen coordinate for all subviews.

- `spacing` — The distance between adjacent subviews. Set this value to `nil` to use default distances between subviews.
