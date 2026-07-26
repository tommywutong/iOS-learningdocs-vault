---
title: 'init(uniformLeadingCorners:uniformTrailingCorners:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/concentricrectangle/init(uniformleadingcorners:uniformtrailingcorners:)'
source_url: 'https://developer.apple.com/documentation/swiftui/concentricrectangle/init(uniformleadingcorners:uniformtrailingcorners:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/concentricrectangle/init%28uniformleadingcorners%3Auniformtrailingcorners%3A%29.json'
content_hash: 'sha256:43193e8a9ebfa9c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ConcentricRectangle](../concentricrectangle.md)

# init(uniformLeadingCorners:uniformTrailingCorners:)

<sub>Initializer</sub>

Creates a rectangle with a corner style set on the leading two corners uniformly, and another style set on the trailing two corners uniformly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(uniformLeadingCorners: Edge.Corner.Style = .concentric, uniformTrailingCorners: Edge.Corner.Style = .concentric)
```

## Parameters

- `uniformLeadingCorners` — The corner style to apply to the leading two corners uniformly.

- `uniformTrailingCorners` — The corner style to apply to the trailing two corners uniformly.

## Discussion

For the two leading corners and two trailing corners, the system calculates the radius for each corner first. Then, it selects the largest leading radius and applies it to each leading corner, and it selects the largest trailing radius and applies it to each trailing corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform leading and trailing corners

- [rect(uniformLeadingCorners:uniformTrailingCorners:)](<../shape/rect(uniformleadingcorners_uniformtrailingcorners_).md>) — Creates a rectangle with a corner style uniformly set on the two leading corners, and another style uniformly set on the two trailing corners.
