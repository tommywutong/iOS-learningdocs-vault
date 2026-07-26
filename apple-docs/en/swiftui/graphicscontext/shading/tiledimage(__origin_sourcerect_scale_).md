---
title: 'tiledImage(_:origin:sourceRect:scale:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/shading/tiledimage(_:origin:sourcerect:scale:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading/tiledimage(_:origin:sourcerect:scale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading/tiledimage%28_%3Aorigin%3Asourcerect%3Ascale%3A%29.json'
content_hash: 'sha256:aec413de70901583'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Shading](../shading.md)

# tiledImage(_:origin:sourceRect:scale:)

<sub>Type Method</sub>

Returns a shading instance that tiles an image across the infinite plane.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func tiledImage(_ image: Image, origin: CGPoint = .zero, sourceRect: CGRect = CGRect(x: 0, y: 0, width: 1, height: 1), scale: CGFloat = 1) -> GraphicsContext.Shading
```

## Parameters

- `image` — An [Image](../../image.md) to use as fill.

- `origin` — The point in the current user space where SwiftUI places the bottom left corner of the part of the image defined by `sourceRect`. The image repeats as needed.

- `sourceRect` — A unit space subregion of the image. The default is a unit rectangle, which selects the whole image.

- `scale` — A factor that you can use to control the image size.

## Return Value

A shading instance filled with a tiled image.
