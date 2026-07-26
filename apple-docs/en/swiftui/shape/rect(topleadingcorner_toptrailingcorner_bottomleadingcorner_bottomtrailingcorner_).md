---
title: 'rect(topLeadingCorner:topTrailingCorner:bottomLeadingCorner:bottomTrailingCorner:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/rect(topleadingcorner:toptrailingcorner:bottomleadingcorner:bottomtrailingcorner:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/rect(topleadingcorner:toptrailingcorner:bottomleadingcorner:bottomtrailingcorner:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/rect%28topleadingcorner%3Atoptrailingcorner%3Abottomleadingcorner%3Abottomtrailingcorner%3A%29.json'
content_hash: 'sha256:4934ba6e0c74859c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# rect(topLeadingCorner:topTrailingCorner:bottomLeadingCorner:bottomTrailingCorner:)

<sub>Type Method</sub>

Creates a rectangle with individual styles for each corner.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func rect(topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self
```

## Parameters

- `topLeadingCorner` — The top leading corner style.

- `topTrailingCorner` — The top trailing corner style.

- `bottomLeadingCorner` — The bottom leading corner style.

- `bottomTrailingCorner` — The bottom trailing corner style.

## See Also

### Creating a rectangle with individual corner styles

- [init(topLeadingCorner:topTrailingCorner:bottomLeadingCorner:bottomTrailingCorner:)](<../concentricrectangle/init(topleadingcorner_toptrailingcorner_bottomleadingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with individual corner styles on all four corners.
