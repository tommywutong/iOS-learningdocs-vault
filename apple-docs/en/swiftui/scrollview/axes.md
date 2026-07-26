---
title: axes
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollview/axes
source_url: 'https://developer.apple.com/documentation/swiftui/scrollview/axes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollview/axes.json'
content_hash: 'sha256:6484966429d529ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollView](../scrollview.md)

# axes

<sub>Instance Property</sub>

The scrollable axes of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var axes: Axis.Set { get set }
```

## Discussion

The default value is [Axis.vertical](../axis/vertical.md).

## See Also

### Configuring a scroll view

- [content](content.md) — The scroll view’s content.
- [showsIndicators](showsindicators.md) — A value that indicates whether the scroll view displays the scrollable component of the content offset, in a way that’s suitable for the platform.
