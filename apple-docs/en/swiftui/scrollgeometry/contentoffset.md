---
title: contentOffset
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollgeometry/contentoffset
source_url: 'https://developer.apple.com/documentation/swiftui/scrollgeometry/contentoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollgeometry/contentoffset.json'
content_hash: 'sha256:d0e37b1abc5a14c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollGeometry](../scrollgeometry.md)

# contentOffset

<sub>Instance Property</sub>

The content offset of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var contentOffset: CGPoint { get set }
```

## Discussion

This is the position of the scroll view within its overall content size. This value may extend before zero or beyond the content size when the content insets of the scroll view are non-zero or when rubber banding.
