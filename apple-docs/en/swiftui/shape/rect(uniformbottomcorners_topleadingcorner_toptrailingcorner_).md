---
title: 'rect(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/rect(uniformbottomcorners:topleadingcorner:toptrailingcorner:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/rect(uniformbottomcorners:topleadingcorner:toptrailingcorner:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/rect%28uniformbottomcorners%3Atopleadingcorner%3Atoptrailingcorner%3A%29.json'
content_hash: 'sha256:da106f6de99ba4e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# rect(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)

<sub>Type Method</sub>

Creates a rectangle with a corner style set on the two bottom corners uniformly, and two other styles for the two top corners respectively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func rect(uniformBottomCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style) -> Self
```

## Parameters

- `uniformBottomCorners` — The corner style to apply uniformly to the two bottom corners.

- `topLeadingCorner` — The top leading corner style.

- `topTrailingCorner` — The top trailing corner style.

## Discussion

For the two bottom corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each bottom corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform bottom corners

- [init(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)](<../concentricrectangle/init(uniformbottomcorners_topleadingcorner_toptrailingcorner_).md>) — Creates a rectangle with a corner style set on the bottom two corners uniformly, and two other styles for the top two corners respectively.
