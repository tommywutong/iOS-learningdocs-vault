---
title: UIGraphicsImageRenderer.DrawingActions
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsimagerenderer/drawingactions
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/drawingactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerenderer/drawingactions.json'
content_hash: 'sha256:e2dae4012413e089'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md)

# UIGraphicsImageRenderer.DrawingActions

<sub>Type Alias</sub>

A closure for drawing an image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias DrawingActions = (UIGraphicsImageRendererContext) -> Void
```

## Discussion

`UIGraphicsImageDrawingActions` defines a block type that takes a [UIGraphicsImageRendererContext](../uigraphicsimagerenderercontext.md) object as an argument and has no return value.

You provide a block of this type as an argument to the image drawing methods on [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md). Your block should use the provided image renderer context to perform the drawing operations you want the renderer to execute.

See [Creating an image with an image renderer](../uigraphicsimagerenderer.md#Creating-an-image-with-an-image-renderer) for an example use of a `UIGraphicsImageDrawingActions` block.

## See Also

### Creating images

- [- imageWithActions:](<image(actions_).md>) — Creates an image from a set of drawing instructions.
- [- JPEGDataWithCompressionQuality:actions:](<jpegdata(withcompressionquality_actions_).md>) — Creates a JPEG-encoded image from a set of drawing instructions.
- [- PNGDataWithActions:](<pngdata(actions_).md>) — Creates a PNG-encoded image from a set of drawing instructions.
