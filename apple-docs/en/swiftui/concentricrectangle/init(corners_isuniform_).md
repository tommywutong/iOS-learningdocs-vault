---
title: 'init(corners:isUniform:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/concentricrectangle/init(corners:isuniform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/concentricrectangle/init(corners:isuniform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/concentricrectangle/init%28corners%3Aisuniform%3A%29.json'
content_hash: 'sha256:a6776f2a61bd3193'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ConcentricRectangle](../concentricrectangle.md)

# init(corners:isUniform:)

<sub>Initializer</sub>

Creates a rectangle with the same corner style set on four corners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(corners: Edge.Corner.Style, isUniform: Bool = false)
```

## Parameters

- `corners` — The corner style for all four corners.

- `isUniform` — A Boolean value that indicates whether to apply the corner style on each corner individually or uniformly.

## Discussion

When you provide `false` for `isUniform`, the system may calculate a different radius for each corner. This can happen when the rectangle is not centered within the container shape, or the container shape’s corners have different radii. When you provide `true` for `isUniform`, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each corner to achieve the symmetric look.

## See Also

### Creating a rectangle with the same corner style

- [rect(corners:isUniform:)](<../shape/rect(corners_isuniform_).md>) — Creates a rectangle with the same corner style set on four corners.
