---
title: 'rect(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/rect(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/rect(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/rect%28uniformtrailingcorners%3Atopleadingcorner%3Abottomleadingcorner%3A%29.json'
content_hash: 'sha256:176c35b0c6193b61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# rect(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)

<sub>Type Method</sub>

Creates a rectangle with a corner style uniformly set on the two trailing corners, and two other styles for the two leading corners respectively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func rect(uniformTrailingCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style) -> Self
```

## Parameters

- `uniformTrailingCorners` — The corner style to apply uniformly to the two trailing corners.

- `topLeadingCorner` — The top leading corner style.

- `bottomLeadingCorner` — The bottom leading corner style.

## Discussion

For the two trailing corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each trailing corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform trailing corners

- [init(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)](<../concentricrectangle/init(uniformtrailingcorners_topleadingcorner_bottomleadingcorner_).md>) — Creates a rectangle with a corner style set on the trailing two corners uniformly, and two other styles for the leading two corners respectively.
