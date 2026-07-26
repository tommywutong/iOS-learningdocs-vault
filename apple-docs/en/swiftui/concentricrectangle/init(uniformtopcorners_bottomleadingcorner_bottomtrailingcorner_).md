---
title: 'init(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/concentricrectangle/init(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:)'
source_url: 'https://developer.apple.com/documentation/swiftui/concentricrectangle/init(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/concentricrectangle/init%28uniformtopcorners%3Abottomleadingcorner%3Abottomtrailingcorner%3A%29.json'
content_hash: 'sha256:2ab4992ef8755385'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ConcentricRectangle](../concentricrectangle.md)

# init(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)

<sub>Initializer</sub>

Creates a rectangle with a corner style set on the top two corners uniformly, and two other styles for the bottom two corners respectively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(uniformTopCorners: Edge.Corner.Style = .concentric, bottomLeadingCorner: Edge.Corner.Style = .concentric, bottomTrailingCorner: Edge.Corner.Style = .concentric)
```

## Parameters

- `uniformTopCorners` — The corner style to apply to the top two corners uniformly.

- `bottomLeadingCorner` — The corner style for the bottom leading corner.

- `bottomTrailingCorner` — The corner style for the bottom trailing corner.

## Discussion

For the two top corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each top corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform top corners

- [rect(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)](<../shape/rect(uniformtopcorners_bottomleadingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with a corner style uniformly set on the two top corners, and two other styles for the bottom two corners respectively.
