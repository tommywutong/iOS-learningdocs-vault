---
title: 'image(actions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsimagerenderer/image(actions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/image(actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerenderer/image%28actions%3A%29.json'
content_hash: 'sha256:e48ba1546dc28726'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md)

# image(actions:)

<sub>Instance Method</sub>

Creates an image from a set of drawing instructions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func image(actions: (UIGraphicsImageRendererContext) -> Void) -> UIImage
```

## Parameters

- `actions` — A [DrawingActions](drawingactions.md) block that, when invoked by the renderer, executes a set of drawing instructions to create the output image.

## Return Value

A [UIImage](../uiimage.md) object created by the supplied drawing actions.

## Discussion

You provide a set of drawing instructions as the block argument to this method, and the method will return the resultant [UIImage](../uiimage.md) object.

You can call this method repeatedly to create multiple images, each of which has identical dimensions and format.

## See Also

### Creating images

- [- JPEGDataWithCompressionQuality:actions:](<jpegdata(withcompressionquality_actions_).md>) — Creates a JPEG-encoded image from a set of drawing instructions.
- [- PNGDataWithActions:](<pngdata(actions_).md>) — Creates a PNG-encoded image from a set of drawing instructions.
- [DrawingActions](drawingactions.md) — A closure for drawing an image.
