---
title: 'rect(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/rect(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/rect(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/rect%28uniformleadingcorners%3Atoptrailingcorner%3Abottomtrailingcorner%3A%29.json'
content_hash: 'sha256:108eecb3c3fb6c7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# rect(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)

<sub>Type Method</sub>

Creates a rectangle with a corner style uniformly set on the two leading corners, and two other styles for the two trailing corners respectively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func rect(uniformLeadingCorners: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self
```

## Parameters

- `uniformLeadingCorners` — The corner style to apply uniformly to the two leading corners.

- `topTrailingCorner` — The top trailing corner style.

- `bottomTrailingCorner` — The bottom trailing corner style.

## Discussion

For the two leading corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each leading corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform leading corners

- [init(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)](<../concentricrectangle/init(uniformleadingcorners_toptrailingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with a corner style set on the leading two corners uniformly, and two other styles for the trailing two corners respectively.
