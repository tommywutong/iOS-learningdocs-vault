---
title: 'init(uniformTopCorners:uniformBottomCorners:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/concentricrectangle/init(uniformtopcorners:uniformbottomcorners:)'
source_url: 'https://developer.apple.com/documentation/swiftui/concentricrectangle/init(uniformtopcorners:uniformbottomcorners:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/concentricrectangle/init%28uniformtopcorners%3Auniformbottomcorners%3A%29.json'
content_hash: 'sha256:6ee58aa6fdd0075c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ConcentricRectangle](../concentricrectangle.md)

# init(uniformTopCorners:uniformBottomCorners:)

<sub>Initializer</sub>

Creates a rectangle with a corner style set on the top two corners uniformly, and another style set on the bottom two corners uniformly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(uniformTopCorners: Edge.Corner.Style = .concentric, uniformBottomCorners: Edge.Corner.Style = .concentric)
```

## Parameters

- `uniformTopCorners` — The corner style to apply to the top two corners uniformly.

- `uniformBottomCorners` — The corner style to apply to the bottom two corners uniformly.

## Discussion

For the two top corners and two bottom corners, the system calculates the radius for each corner first. Then, it selects the largest top radius and applies it to each top corner, and it selects the largest bottom radius and applies it to each bottom corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform top and uniform bottom corners

- [rect(uniformTopCorners:uniformBottomCorners:)](<../shape/rect(uniformtopcorners_uniformbottomcorners_).md>) — Creates a rectangle with a corner style uniformly set on the two top corners, and another style uniformly set on the two bottom corners.
