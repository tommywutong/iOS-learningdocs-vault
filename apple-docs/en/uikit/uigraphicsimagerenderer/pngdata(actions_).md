---
title: 'pngData(actions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsimagerenderer/pngdata(actions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/pngdata(actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerenderer/pngdata%28actions%3A%29.json'
content_hash: 'sha256:17ad5303a3b6d5d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md)

# pngData(actions:)

<sub>Instance Method</sub>

Creates a PNG-encoded image from a set of drawing instructions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pngData(actions: (UIGraphicsImageRendererContext) -> Void) -> Data
```

## Parameters

- `actions` — A [DrawingActions](drawingactions.md) block that, when invoked by the renderer, executes a set of drawing instructions to create the output image.

## Return Value

A [Data](../../foundation/data.md) object representing a PNG-encoded representation of the image created by the supplied drawing actions.

## Discussion

You provide a set of drawing instructions as the block argument to this method, and the method returns the resulting image as a PNG-encoded [Data](../../foundation/data.md) object.

You can call this method repeatedly to create multiple images, each of which has identical dimensions and format.

## See Also

### Creating images

- [- imageWithActions:](<image(actions_).md>) — Creates an image from a set of drawing instructions.
- [- JPEGDataWithCompressionQuality:actions:](<jpegdata(withcompressionquality_actions_).md>) — Creates a JPEG-encoded image from a set of drawing instructions.
- [DrawingActions](drawingactions.md) — A closure for drawing an image.
