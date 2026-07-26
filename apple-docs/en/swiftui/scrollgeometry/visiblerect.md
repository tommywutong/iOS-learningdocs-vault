---
title: visibleRect
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollgeometry/visiblerect
source_url: 'https://developer.apple.com/documentation/swiftui/scrollgeometry/visiblerect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollgeometry/visiblerect.json'
content_hash: 'sha256:2ff04111da10da67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollGeometry](../scrollgeometry.md)

# visibleRect

<sub>Instance Property</sub>

The visible rect of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var visibleRect: CGRect { get }
```

## Discussion

This value is computed from the scroll view’s content offset, content insets, and its container size.
