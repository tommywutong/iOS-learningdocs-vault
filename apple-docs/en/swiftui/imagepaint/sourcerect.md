---
title: sourceRect
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagepaint/sourcerect
source_url: 'https://developer.apple.com/documentation/swiftui/imagepaint/sourcerect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagepaint/sourcerect.json'
content_hash: 'sha256:19574132fefbc7ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImagePaint](../imagepaint.md)

# sourceRect

<sub>Instance Property</sub>

A unit-space rectangle defining how much of the source image to draw.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sourceRect: CGRect
```

## Discussion

The results are undefined if this rectangle selects areas outside the `[0, 1]` range in either axis.

## See Also

### Configuring the image paint style

- [image](image.md) — The image to be drawn.
- [scale](scale.md) — A scale factor applied to the image while being drawn.
