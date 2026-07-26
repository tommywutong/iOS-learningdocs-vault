---
title: containerSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollgeometry/containersize
source_url: 'https://developer.apple.com/documentation/swiftui/scrollgeometry/containersize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollgeometry/containersize.json'
content_hash: 'sha256:728b2c7994e74c23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollGeometry](../scrollgeometry.md)

# containerSize

<sub>Instance Property</sub>

The size of the container of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var containerSize: CGSize { get set }
```

## Discussion

This is the overall size of the scroll view. Combining this and the content offset will give you the current visible rect of the scroll view.
