---
title: 'init(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/concentricrectangle/init(uniformbottomcorners:topleadingcorner:toptrailingcorner:)'
source_url: 'https://developer.apple.com/documentation/swiftui/concentricrectangle/init(uniformbottomcorners:topleadingcorner:toptrailingcorner:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/concentricrectangle/init%28uniformbottomcorners%3Atopleadingcorner%3Atoptrailingcorner%3A%29.json'
content_hash: 'sha256:093210334546ff61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ConcentricRectangle](../concentricrectangle.md)

# init(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)

<sub>Initializer</sub>

Creates a rectangle with a corner style set on the bottom two corners uniformly, and two other styles for the top two corners respectively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(uniformBottomCorners: Edge.Corner.Style = .concentric, topLeadingCorner: Edge.Corner.Style = .concentric, topTrailingCorner: Edge.Corner.Style = .concentric)
```

## Parameters

- `uniformBottomCorners` — The corner style to apply to the bottom two corners uniformly.

- `topLeadingCorner` — The corner style for the top leading corner.

- `topTrailingCorner` — The corner style for the top trailing corner.

## Discussion

For the two bottom corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each bottom corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform bottom corners

- [rect(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)](<../shape/rect(uniformbottomcorners_topleadingcorner_toptrailingcorner_).md>) — Creates a rectangle with a corner style set on the two bottom corners uniformly, and two other styles for the two top corners respectively.
