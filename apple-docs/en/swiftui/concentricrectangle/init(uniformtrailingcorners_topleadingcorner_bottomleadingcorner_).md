---
title: 'init(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/concentricrectangle/init(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:)'
source_url: 'https://developer.apple.com/documentation/swiftui/concentricrectangle/init(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/concentricrectangle/init%28uniformtrailingcorners%3Atopleadingcorner%3Abottomleadingcorner%3A%29.json'
content_hash: 'sha256:9e149d3725a644c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ConcentricRectangle](../concentricrectangle.md)

# init(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)

<sub>Initializer</sub>

Creates a rectangle with a corner style set on the trailing two corners uniformly, and two other styles for the leading two corners respectively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(uniformTrailingCorners: Edge.Corner.Style = .concentric, topLeadingCorner: Edge.Corner.Style = .concentric, bottomLeadingCorner: Edge.Corner.Style = .concentric)
```

## Parameters

- `uniformTrailingCorners` — The corner style to apply to the trailing two corners uniformly.

- `topLeadingCorner` — The corner style for the top leading corner.

- `bottomLeadingCorner` — The corner style for the bottom leading corner.

## Discussion

For the two trailing corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each trailing corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform trailing corners

- [rect(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)](<../shape/rect(uniformtrailingcorners_topleadingcorner_bottomleadingcorner_).md>) — Creates a rectangle with a corner style uniformly set on the two trailing corners, and two other styles for the two leading corners respectively.
