---
title: 'rect(uniformLeadingCorners:uniformTrailingCorners:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/rect(uniformleadingcorners:uniformtrailingcorners:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/rect(uniformleadingcorners:uniformtrailingcorners:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/rect%28uniformleadingcorners%3Auniformtrailingcorners%3A%29.json'
content_hash: 'sha256:4328ee7806b2b318'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# rect(uniformLeadingCorners:uniformTrailingCorners:)

<sub>Type Method</sub>

Creates a rectangle with a corner style uniformly set on the two leading corners, and another style uniformly set on the two trailing corners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func rect(uniformLeadingCorners: Edge.Corner.Style, uniformTrailingCorners: Edge.Corner.Style) -> Self
```

## Parameters

- `uniformLeadingCorners` — The corner style to apply uniformly to the two leading corners.

- `uniformTrailingCorners` — The corner style to apply uniformly to the two trailing corners.

## Discussion

For the two leading corners and two trailing corners, the system calculates the radius for each corner first. Then, it selects the largest leading radius and applies it to each leading corner, and it selects the largest trailing radius and applies it to each trailing corner to achieve the symmetric look.

## See Also

### Creating a rectangle with uniform leading and trailing corners

- [init(uniformLeadingCorners:uniformTrailingCorners:)](<../concentricrectangle/init(uniformleadingcorners_uniformtrailingcorners_).md>) — Creates a rectangle with a corner style set on the leading two corners uniformly, and another style set on the trailing two corners uniformly.
