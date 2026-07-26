---
title: 'rect(uniformTopCorners:uniformBottomCorners:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/rect(uniformtopcorners:uniformbottomcorners:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/rect(uniformtopcorners:uniformbottomcorners:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/rect%28uniformtopcorners%3Auniformbottomcorners%3A%29.json'
content_hash: 'sha256:c49e621cc0ab986d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# rect(uniformTopCorners:uniformBottomCorners:)

<sub>Type Method</sub>

Creates a rectangle with a corner style uniformly set on the two top corners, and another style uniformly set on the two bottom corners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func rect(uniformTopCorners: Edge.Corner.Style, uniformBottomCorners: Edge.Corner.Style) -> Self
```

## Parameters

- `uniformTopCorners` — The corner style to apply uniformly to the two top corners.

- `uniformBottomCorners` — The corner style to apply uniformly to the two bottom corners.

## Discussion

For the two top corners and two bottom corners, the system calculates the radius for each corner first. Then, it selects the largest top radius and applies it to each top corner, and it selects the largest bottom radius and applies it to each bottom corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform top and uniform bottom corners

- [init(uniformTopCorners:uniformBottomCorners:)](<../concentricrectangle/init(uniformtopcorners_uniformbottomcorners_).md>) — Creates a rectangle with a corner style set on the top two corners uniformly, and another style set on the bottom two corners uniformly.
