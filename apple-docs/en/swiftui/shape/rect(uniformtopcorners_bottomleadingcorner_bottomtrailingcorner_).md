---
title: 'rect(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/rect(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/rect(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/rect%28uniformtopcorners%3Abottomleadingcorner%3Abottomtrailingcorner%3A%29.json'
content_hash: 'sha256:3233b15b55d775a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# rect(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)

<sub>Type Method</sub>

Creates a rectangle with a corner style uniformly set on the two top corners, and two other styles for the bottom two corners respectively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func rect(uniformTopCorners: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self
```

## Parameters

- `uniformTopCorners` — The corner style to apply uniformly to the two top corners.

- `bottomLeadingCorner` — The bottom leading corner style.

- `bottomTrailingCorner` — The bottom trailing corner style.

## Discussion

For the two top corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each top corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform top corners

- [init(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)](<../concentricrectangle/init(uniformtopcorners_bottomleadingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with a corner style set on the top two corners uniformly, and two other styles for the bottom two corners respectively.
