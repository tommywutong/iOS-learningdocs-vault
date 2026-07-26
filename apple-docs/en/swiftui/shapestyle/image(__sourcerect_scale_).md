---
title: 'image(_:sourceRect:scale:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/image(_:sourcerect:scale:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/image(_:sourcerect:scale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/image%28_%3Asourcerect%3Ascale%3A%29.json'
content_hash: 'sha256:2736e1e2c39859f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# image(_:sourceRect:scale:)

<sub>Type Method</sub>

A shape style that fills a shape by repeating a region of an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func image(_ image: Image, sourceRect: CGRect = CGRect(x: 0, y: 0, width: 1, height: 1), scale: CGFloat = 1) -> ImagePaint
```

## Parameters

- `image` — The image to be drawn.

- `sourceRect` — A unit-space rectangle defining how much of the source image to draw. The results are undefined if `sourceRect` selects areas outside the `[0, 1]` range in either axis.

- `scale` — A scale factor applied to the image during rendering.

## Discussion

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).
