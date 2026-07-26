---
title: 'init(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/concentricrectangle/init(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:)'
source_url: 'https://developer.apple.com/documentation/swiftui/concentricrectangle/init(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/concentricrectangle/init%28uniformleadingcorners%3Atoptrailingcorner%3Abottomtrailingcorner%3A%29.json'
content_hash: 'sha256:90bd9d85583a1457'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ConcentricRectangle](../concentricrectangle.md)

# init(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)

<sub>Initializer</sub>

Creates a rectangle with a corner style set on the leading two corners uniformly, and two other styles for the trailing two corners respectively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(uniformLeadingCorners: Edge.Corner.Style = .concentric, topTrailingCorner: Edge.Corner.Style = .concentric, bottomTrailingCorner: Edge.Corner.Style = .concentric)
```

## Parameters

- `uniformLeadingCorners` — The corner style to apply to the leading two corners uniformly.

- `topTrailingCorner` — The corner style for the top trailing corner.

- `bottomTrailingCorner` — The corner style for the bottom trailing corner.

## Discussion

For the two leading corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each leading corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform leading corners

- [rect(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)](<../shape/rect(uniformleadingcorners_toptrailingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with a corner style uniformly set on the two leading corners, and two other styles for the two trailing corners respectively.
