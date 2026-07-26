---
title: 'rect(corners:isUniform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/rect(corners:isuniform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/rect(corners:isuniform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/rect%28corners%3Aisuniform%3A%29.json'
content_hash: 'sha256:7bdb9260b03934ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# rect(corners:isUniform:)

<sub>Type Method</sub>

Creates a rectangle with the same corner style set on four corners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func rect(corners: Edge.Corner.Style, isUniform: Bool = false) -> Self
```

## Parameters

- `corners` — The corner style for all four corners.

- `isUniform` — A Boolean value that indicates whether to apply the corner style on each corner individually or uniformly.

## Discussion

When you provide `false` for `isUniform`, the system may calculate a different radius for each corner. This can happen when the rectangle is not centered within the container shape, or the container shape’s corners have different radii. When you provide `true` for `isUniform`, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each corner to achieve the symmetric look.

## See Also

### Creating a rectangle with the same corner style

- [init(corners:isUniform:)](<../concentricrectangle/init(corners_isuniform_).md>) — Creates a rectangle with the same corner style set on four corners.
