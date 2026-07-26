---
title: bounds
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollgeometry/bounds
source_url: 'https://developer.apple.com/documentation/swiftui/scrollgeometry/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollgeometry/bounds.json'
content_hash: 'sha256:5fcc8518172d506f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollGeometry](../scrollgeometry.md)

# bounds

<sub>Instance Property</sub>

The bounds rect of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bounds: CGRect { get }
```

## Discussion

Unlike the visible rect, this value is within the content insets of the scroll view.
